# Codex Model Providers

- Creation date: 2026-07-14
- Topic: Running different models and API relays in Codex
- Purpose: Record guidance on connecting Codex to supported model providers, local models, and OpenAI-compatible relay services.

## CPA setup

- Installed CLIProxyAPI with Homebrew.
- Restricted the proxy listener to `127.0.0.1:8317`.
- Added a `cliproxyapi` provider to the user-level Codex configuration.
- Added a separate `cpa` Codex profile so the existing default provider remains unchanged.
