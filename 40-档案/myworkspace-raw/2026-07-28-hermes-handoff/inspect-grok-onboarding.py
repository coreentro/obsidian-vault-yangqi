#!/usr/bin/env python3
"""Inspect Grok web onboarding with a stored xAI SSO session.

The SSO cookie is read from the protected registration output, never accepted
on the command line, and never printed. Output contains only page metadata,
storage/cookie names, and coarse text markers.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


DEFAULT_SESSIONS = Path(
    "/Users/yangqi/.grok-register/outputs/"
    "20260727-221156/SSO/auth-sessions.jsonl"
)
DEFAULT_SCREENSHOT = Path(
    "/Users/yangqi/Documents/Codex/MyWorkspace/"
    "2026-07-28-hermes-handoff/grok-account-inspect.png"
)
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/146.0.0.0 Safari/537.36"
)
MARKERS = (
    "sign in",
    "log in",
    "welcome",
    "terms",
    "privacy",
    "date of birth",
    "birthday",
    "age",
    "verify",
    "suspended",
    "blocked",
    "abusive",
    "upgrade",
    "subscribe",
    "free",
    "start chatting",
    "what do you want to know",
)
CAPTURE_PATHS = {
    "/api/auth/session",
    "/rest/products",
    "/rest/rate-limits",
}
SENSITIVE_KEY_PARTS = (
    "cookie",
    "email",
    "first_name",
    "last_name",
    "name",
    "secret",
    "token",
    "user_id",
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
    return " ".join(label.split())[:120]


def sanitize_json(value, key: str = "", depth: int = 0):
    key_lower = key.lower()
    if (
        key_lower == "id"
        or key_lower.endswith("_id")
        or any(part in key_lower for part in SENSITIVE_KEY_PARTS)
    ):
        return "[redacted]"
    if depth > 6:
        return "[max-depth]"
    if isinstance(value, dict):
        return {
            str(item_key): sanitize_json(
                item_value,
                str(item_key),
                depth + 1,
            )
            for item_key, item_value in list(value.items())[:80]
        }
    if isinstance(value, list):
        return [
            sanitize_json(item, key, depth + 1)
            for item in value[:40]
        ]
    if isinstance(value, str):
        value = safe_label(value)
        if value.startswith("eyJ") or len(value) > 120:
            return f"[string length={len(value)}]"
        return value
    return value


async def inspect(args: argparse.Namespace) -> dict:
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
    responses: list[dict] = []
    captured_payloads: list[dict] = []
    capture_tasks: list[asyncio.Task] = []

    async def capture_payload(response) -> None:
        if urlsplit(response.url).path not in CAPTURE_PATHS:
            return
        try:
            payload = await response.json()
        except Exception:
            payload = "[non-json]"
        captured_payloads.append(
            {
                "status": response.status,
                "url": safe_url(response.url),
                "body": sanitize_json(payload),
            }
        )

    def record_response(response) -> None:
        host = urlsplit(response.url).hostname or ""
        if host.endswith(("x.ai", "grok.com")):
            responses.append(
                {
                    "status": response.status,
                    "url": safe_url(response.url),
                }
            )
        if urlsplit(response.url).path in CAPTURE_PATHS:
            capture_tasks.append(asyncio.create_task(capture_payload(response)))

    page.on("response", record_response)
    main_response = await page.goto(
        args.url,
        wait_until="domcontentloaded",
        timeout=60_000,
    )
    await page.wait_for_timeout(args.wait_seconds * 1000)
    actions: list[str] = []
    if args.click_login:
        for label in ("登录", "Sign in", "Log in"):
            locator = page.get_by_text(label, exact=True)
            if await locator.count() and await locator.first.is_visible():
                await locator.first.click(timeout=5_000)
                actions.append(f"clicked:{label}")
                await page.wait_for_timeout(args.wait_seconds * 1000)
                break
    if capture_tasks:
        await asyncio.gather(*capture_tasks, return_exceptions=True)

    body_lower = (await page.locator("body").inner_text()).lower()
    buttons = []
    for locator in (
        page.locator("button"),
        page.locator("a"),
        page.locator('[role="button"]'),
    ):
        count = min(await locator.count(), 80)
        for index in range(count):
            try:
                item = locator.nth(index)
                if not await item.is_visible():
                    continue
                label = safe_label(await item.inner_text())
                if label and label not in buttons:
                    buttons.append(label)
            except Exception:
                continue

    storage = await page.evaluate(
        """() => ({
          local: Object.keys(localStorage).sort(),
          session: Object.keys(sessionStorage).sort()
        })"""
    )
    cookie_names = sorted(
        {
            f"{cookie['domain']}:{cookie['name']}"
            for cookie in await context.cookies()
        }
    )
    args.screenshot.parent.mkdir(parents=True, exist_ok=True)
    await page.screenshot(path=str(args.screenshot), full_page=True)
    os.chmod(args.screenshot, 0o600)

    result = {
        "main_status": main_response.status if main_response else None,
        "final_url": safe_url(page.url),
        "title": safe_label(await page.title()),
        "actions": actions,
        "markers": [marker for marker in MARKERS if marker in body_lower],
        "visible_controls": buttons[:40],
        "storage_keys": storage,
        "cookie_names": cookie_names,
        "responses": responses[-80:],
        "captured_payloads": captured_payloads[-12:],
        "screenshot": str(args.screenshot),
        "screenshot_mode": oct(args.screenshot.stat().st_mode & 0o777),
    }
    await context.close()
    await browser.close()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--session-index", type=int, default=1)
    parser.add_argument("--sessions", type=Path, default=DEFAULT_SESSIONS)
    parser.add_argument("--proxy", default="http://127.0.0.1:18082")
    parser.add_argument("--url", default="https://grok.com/")
    parser.add_argument("--wait-seconds", type=int, default=15)
    parser.add_argument("--click-login", action="store_true")
    parser.add_argument("--screenshot", type=Path, default=DEFAULT_SCREENSHOT)
    args = parser.parse_args()
    print(
        json.dumps(
            asyncio.run(inspect(args)),
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
