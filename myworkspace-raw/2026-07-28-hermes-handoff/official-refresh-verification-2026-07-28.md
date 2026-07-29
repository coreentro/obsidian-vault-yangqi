# Official OAuth Refresh Verification

- Date: 2026-07-28
- Scope: One pre-existing, owner-controlled official Grok OAuth session; no temporary-mail account was retried.
- Client: Official Grok 0.2.111 in an isolated `GROK_HOME`.
- Network: Isolated US AS906 egress. System proxy and Shadowrocket selection were not changed.

## Verified result

1. The official client refreshed the existing session successfully and rotated its refresh authority inside the isolated home.
2. `GET /v1/settings` returned HTTP 200 with `allow_access=true`.
3. `GET /v1/user?include=subscription` returned HTTP 200 with `subscriptionTier=GrokPro`.
4. `GET /v1/billing?format=credits` returned HTTP 200.
5. A CPA-header-compatible minimal `POST /v1/responses` returned HTTP 200.
6. A CPA JSON document was written under `verified-cpa/` with directory mode `0700` and file mode `0600`.

## Boundaries

- The newly registered temporary-mail accounts remain separately rejected by xAI with `invalid_grant: Access denied`; this recovery proves that the local CPA format and flow work for an xAI-authorized account, not that those accounts became eligible.
- The source `~/.grok/auth.json` was not overwritten. Because the successful refresh rotated the token in the isolated home, syncing it back to the user's official Grok home requires a separate explicit decision.
- No token, cookie, email address, user identifier, or raw API response is recorded in this report.
