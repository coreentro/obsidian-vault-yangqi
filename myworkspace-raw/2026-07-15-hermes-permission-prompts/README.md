# Hermes Permission Prompts

- Creation date: 2026-07-15
- Conversation topic: Hermes repeatedly requests permissions
- Purpose: Record the diagnosis and troubleshooting notes for repeated permission prompts.

## Diagnosis and fix

- Hermes uses `/Users/yangqi/.hermes/hermes-agent` and the local gateway service.
- `~/.hermes/config.yaml` now contains `approvals.mode: 'off'`.
- Historical logs showed the literal value `"'\"off\"'"`, which Hermes treated as an unknown mode and downgraded to `manual`.
- Rewrote the setting with `hermes config set approvals.mode off`.
- Restarted the Hermes gateway and desktop client.
- Verified runtime state: `approval_mode=off`, `bypass_active=True`.
