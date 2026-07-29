#!/usr/bin/env python3
"""Confirm an official Grok device flow with a locally stored xAI SSO session.

The SSO value is read from the protected JSONL file and is never accepted on
the command line or printed. Output is limited to non-secret flow metadata.
"""

from __future__ import annotations

import argparse
import asyncio
import importlib.util
import json
from pathlib import Path


DEFAULT_SESSIONS = Path(
    "/Users/yangqi/.grok-register/outputs/"
    "20260727-221156/SSO/auth-sessions.jsonl"
)
DEVICE_BROWSER = Path(
    "/Users/yangqi/Grok-Register/scripts/device_oauth_browser.py"
)


def load_browser_module():
    spec = importlib.util.spec_from_file_location(
        "device_oauth_browser", DEVICE_BROWSER
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {DEVICE_BROWSER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
    cookies = rows[session_index - 1].get("cookies", [])
    for cookie in cookies:
        if cookie.get("name") == "sso" and cookie.get("value"):
            return str(cookie["value"])
    raise ValueError("selected session has no sso cookie")


def safe_result(result: dict) -> dict:
    return {
        "ok": bool(result.get("ok")),
        "stage": result.get("stage"),
        "url": result.get("url"),
        "denied": result.get("denied"),
        "clicked": result.get("clicked"),
        "logs": [
            line
            for line in result.get("logs", [])
            if "cookie" not in line.lower()
        ][-30:],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("verification_url")
    parser.add_argument("--session-index", type=int, default=1)
    parser.add_argument("--sessions", type=Path, default=DEFAULT_SESSIONS)
    parser.add_argument("--proxy", default="http://127.0.0.1:40080")
    parser.add_argument("--timeout", type=float, default=90)
    args = parser.parse_args()

    sso = load_sso(args.sessions, args.session_index)
    browser = load_browser_module()
    result = asyncio.run(
        browser.browser_confirm(
            sso,
            args.verification_url,
            args.proxy,
            timeout=args.timeout,
        )
    )
    print(json.dumps(safe_result(result), ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
