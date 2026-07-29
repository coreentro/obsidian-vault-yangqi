# Hermes Permissions

- Created: 2026-07-26
- Topic: Persistent macOS permissions for Hermes
- Purpose: Diagnose why Hermes repeatedly requests document, screen-recording, and privacy access, then configure persistent permissions.

## Outcome

- Root cause: local Hermes updates used ad-hoc signing, so every changed build produced a different macOS Designated Requirement and invalidated TCC permissions.
- Installed app: `/Applications/Hermes.app`
- Stable signing identity: `Hermes Local Code Signing`
- Certificate SHA-1: `3883384CCE1ED88EF4B41E1475BE63B768F2F65D`
- Certificate SHA-256: `4BEE25896E05A90081F1C303AE6C2642B946C4782BC53DA46B24107A2F1C9042`
- Certificate expiry: 2046-07-21
- Current Designated Requirement: bundle identifier `com.nousresearch.hermes` plus the certificate SHA-1 above; it does not depend on CDHash.
- Hermes Full Disk Access: enabled.
- CuaDriver Accessibility and Screen Recording: enabled; `hermes computer-use doctor --json` reports `overall: ok`.
- Hermes internal approval mode: `off`.
- Non-interactive update policy: `stash`, so the local source patch is restored after ordinary in-app updates.

Two real Hermes builds had different CDHashes (`058d6e…` and `bcd61a…`) but the same certificate-based Designated Requirement. Full Disk Access remained enabled after the replacement.

## Patch and recovery

- Isolated branch: `codex/hermes-stable-signing-2026-07-26`
- Final branch commit: `da13e34549`
- Patch: `hermes-stable-signing.patch`
- Patch SHA-256: `9f7b429073560e3b6cb6b2305470c4097eb63b45bc6d8f1d2cfadcc67e86b5bd`
- Original application backup: `hermes-app-backup/Hermes.app`
- First stable-signed build backup: `hermes-app-backup/stable-first-build.app`
- Verification: 175 relevant tests passed, including real codesign, entitlement, hardened-runtime, stable-requirement, and installer fallback tests.

The local signing private key must remain in the login keychain and must not be exported or shared. Deleting or replacing the certificate, resetting macOS privacy permissions, or reinstalling macOS can still require one new authorization.
