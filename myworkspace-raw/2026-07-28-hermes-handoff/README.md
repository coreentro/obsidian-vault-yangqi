# Hermes Handoff

- Creation date: 2026-07-28
- Conversation topic: Taking over Hermes's current work
- Purpose: Diagnose the unfinished xAI OAuth/CPA flow, harden its failure semantics, and preserve a reproducible handoff.

Current takeover notes: [takeover-notes.md](takeover-notes.md)

## Outcome

Official Grok 0.2.106 and 0.2.111 reproduced xAI's `Access denied` on both device-code and browser-PKCE OAuth paths. The remaining blocker is an xAI server-side authorization/risk-policy decision, not the local Hermes flow.

The local repository now fails closed on denied or malformed callbacks, avoids retry storms for permanent access denial, and exits nonzero when `reoauth` produces no CPA credentials. Fresh unit, race, vet, build, and isolated single-account E2E checks were completed.

## Recovered CPA

An independently authorized, pre-existing official Grok session was recovered through one isolated official refresh. Its resulting CPA credential passed the official access, subscription, billing, and minimal response checks. See [verification evidence](official-refresh-verification-2026-07-28.md). The temporary-mail accounts remain separately blocked by xAI.

## Local artifacts

- `build-shadowrocket-proxy.py` — builds an owner-readable temporary sing-box proxy config without printing node credentials.
- `official-device-confirm.py` — confirms an official device flow using a protected stored SSO session.
- `official-browser-confirm.py` — confirms and safely diagnoses the official browser-PKCE flow.
- `inspect-grok-onboarding.py` — inspects Grok Web session/product state with redacted output.
- `grok-browser-oauth.png` — xAI's visible `Access denied` page (mode `0600`).
- `grok-account-inspect.png` — protected Grok account inspection screenshot.
- `grokreg-e2e` — isolated verification build of the modified working tree.
