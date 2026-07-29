# Grok Login

- Creation date: 2026-07-14
- Conversation topic: Log in to Grok with the selected Apple account
- Purpose: Complete the browser login flow and connect the resulting CPA OpenAI-compatible Grok endpoint to the local NewAPI gateway.

## Result

- OAuth login completed successfully.
- CLIProxyAPI exposes the Grok text models locally.
- NewAPI channel 5 now includes the Grok text model list.
- A real `grok-4.5` request through NewAPI returned successfully.
- Hermes now uses `custom:newapi` as its default provider.
- A real Hermes one-shot request through the persisted NewAPI credential returned successfully.
