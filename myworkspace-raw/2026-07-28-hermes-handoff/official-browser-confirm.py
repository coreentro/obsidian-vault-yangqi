#!/usr/bin/env python3
"""Complete an official Grok browser OAuth flow using a stored xAI SSO.

The SSO cookie is loaded from the protected registration output and never
accepted on the command line or printed. OAuth query parameters are also
removed from diagnostic output.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import time
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


DEFAULT_SESSIONS = Path(
    "/Users/yangqi/.grok-register/outputs/"
    "20260727-221156/SSO/auth-sessions.jsonl"
)
DEFAULT_SCREENSHOT = Path(
    "/Users/yangqi/Documents/Codex/MyWorkspace/"
    "2026-07-28-hermes-handoff/grok-browser-oauth.png"
)
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/146.0.0.0 Safari/537.36"
)


def load_sso(path: Path, session_index: int) -> str:
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if session_index < 1 or session_index > len(rows):
        raise ValueError(
            f"session index {session_index} outside 1..{len(rows)}"
        )
    for cookie in rows[session_index - 1].get("cookies", []):
        if cookie.get("name") == "sso" and cookie.get("value"):
            return str(cookie["value"])
    raise ValueError("selected session has no sso cookie")


def safe_url(raw_url: str) -> str:
    parts = urlsplit(raw_url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def safe_label(label: str) -> str:
    label = re.sub(
        r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "[email]",
        label,
        flags=re.IGNORECASE,
    )
    return " ".join(label.split())[:100]


async def complete(args: argparse.Namespace) -> dict:
    import cloakbrowser

    sso = load_sso(args.sessions, args.session_index)
    browser = await cloakbrowser.launch_async(
        headless=False,
        proxy=args.proxy or None,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-first-run",
            "--no-default-browser-check",
        ],
    )
    context = await browser.new_context(
        viewport={"width": 1280, "height": 800},
        user_agent=UA,
    )
    await context.add_cookies(
        [
            {
                "name": "sso",
                "value": sso,
                "domain": ".x.ai",
                "path": "/",
                "httpOnly": True,
                "secure": True,
            }
        ]
    )
    page = await context.new_page()
    callback_seen = asyncio.Event()
    logs: list[str] = []

    def watch_request(request) -> None:
        host = urlsplit(request.url).hostname or ""
        if host in {"127.0.0.1", "localhost"}:
            logs.append(f"callback:{safe_url(request.url)}")
            callback_seen.set()

    def watch_response(response) -> None:
        host = urlsplit(response.url).hostname or ""
        if host.endswith("x.ai"):
            logs.append(
                f"response:{response.status}:{safe_url(response.url)}"
            )

    page.on("request", watch_request)
    page.on("response", watch_response)
    await page.goto(
        args.authorization_url,
        wait_until="domcontentloaded",
        timeout=60_000,
    )
    await page.wait_for_timeout(1_500)

    candidates = (
        "button:has-text('Allow')",
        "button:has-text('Authorize')",
        "button:has-text('Continue')",
        "button:has-text('允许')",
        "button:has-text('授权')",
        "button:has-text('同意')",
        "button:has-text('继续')",
        "[type=submit]",
        "form button",
    )
    clicked: list[str] = []
    deadline = time.time() + args.timeout
    while time.time() < deadline and not callback_seen.is_set():
        for selector in candidates:
            try:
                locator = page.locator(selector).first
                if not await locator.count() or not await locator.is_visible():
                    continue
                label = " ".join((await locator.inner_text()).split())[:80]
                if any(
                    word in label.lower()
                    for word in ("deny", "cancel", "拒绝", "取消")
                ):
                    continue
                await locator.click(timeout=3_000)
                clicked.append(f"{selector}:{label}")
                await page.wait_for_timeout(1_500)
                break
            except Exception as exc:
                logs.append(f"click_error:{type(exc).__name__}")
        await page.wait_for_timeout(500)

    body_lower = (await page.locator("body").inner_text()).lower()
    controls = []
    for locator in (page.locator("button"), page.locator("a")):
        for index in range(min(await locator.count(), 60)):
            try:
                item = locator.nth(index)
                if await item.is_visible():
                    label = safe_label(await item.inner_text())
                    if label and label not in controls:
                        controls.append(label)
            except Exception:
                continue
    args.screenshot.parent.mkdir(parents=True, exist_ok=True)
    await page.screenshot(path=str(args.screenshot), full_page=True)
    os.chmod(args.screenshot, 0o600)
    result = {
        "ok": callback_seen.is_set(),
        "stage": "callback" if callback_seen.is_set() else "timeout",
        "final_url": safe_url(page.url),
        "clicked": clicked[-10:],
        "markers": [
            marker
            for marker in (
                "access denied",
                "error",
                "upgrade",
                "subscription",
                "unavailable",
                "invalid",
                "continue",
                "allow",
                "cancel",
                "consent",
                "authorized",
            )
            if marker in body_lower
        ],
        "visible_controls": controls[:30],
        "logs": logs[-40:],
        "screenshot": str(args.screenshot),
        "screenshot_mode": oct(args.screenshot.stat().st_mode & 0o777),
    }
    await context.close()
    await browser.close()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("authorization_url")
    parser.add_argument("--session-index", type=int, default=1)
    parser.add_argument("--sessions", type=Path, default=DEFAULT_SESSIONS)
    parser.add_argument("--proxy", default="http://127.0.0.1:18082")
    parser.add_argument("--timeout", type=float, default=90)
    parser.add_argument("--screenshot", type=Path, default=DEFAULT_SCREENSHOT)
    args = parser.parse_args()
    result = asyncio.run(complete(args))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
