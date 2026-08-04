# Acceptance report — 2026-07-15

## Result

Codex Dream Skin Studio `1.0.0` passed its macOS release checks on the live Codex desktop app.

- macOS architecture: `arm64`
- Codex version: `26.707.72221`
- Codex signing Team ID: `2DC432GLL2`
- Codex bundled Node.js: `v24.14.0`
- CDP endpoint: loopback port `9341`
- Official app deep signature after installation: valid
- `app.asar` modification: none

## Automated result

`tests/run-tests.sh` passed syntax, default and custom payload, exact TOML theme-setting round trip, missing-`HOME` recovery, signed runtime, and doctor checks.

Live doctor returned `pass: true`, `officialAppSignatureValid: true`, `modifiesAppAsar: false`, and `live: true`.

Live renderer verification returned `pass: true` after `Page.reload`:

- injected version `1.0.0`;
- style and decorative chrome present;
- decorative chrome `pointer-events: none`;
- native sidebar and composer visible;
- no horizontal document overflow;
- home banner `1227 × 252` and visible;
- four native suggestion cards visible;
- native project selector visible.

## Evidence

- Home screenshot: `docs/screenshots/home-live.png`
- Home screenshot SHA-256: `fcc535ede268e108ec6ecfca76ac6020864c79e1ee8f2a7ca0e9067d727b2a40`
- Task screenshot: `docs/screenshots/task-live.png`
- Task screenshot SHA-256: `92696762b89542b3b5f8daf1eb16a84c1751813487989064c2cb055c692f030d`

The screenshots are real CDP captures from the running Codex renderer, not static HTML previews.
