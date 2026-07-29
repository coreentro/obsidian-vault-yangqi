# Hermes Interface Troubleshooting

- Creation date: 2026-07-28
- Topic: Hermes interface and model-list loading failure
- Purpose: Diagnose why Hermes cannot open or fully load the interface shown in the supplied screenshot.

## Outcome

The Hermes window and local WebSocket gateway were reachable, but
`model.options` never returned. A clean process could build the same 13-provider
catalog normally, which isolated the failure to the desktop backend's shared RPC
worker state rather than the model configuration or upstream providers.

Restarting only the Hermes desktop application replaced the stuck backend
process. The same WebSocket probe then returned the catalog in 0.017 seconds,
and a UI check confirmed that the model menu rendered its provider and model
rows instead of loading skeletons. The independent messaging gateway, saved
sessions, configuration, and credentials were not changed.

## Evidence

- `hermes-after-restart.png` — desktop screenshot immediately after restart.
- `hermes-window-after-restart.png` — Hermes window after the replacement
  backend connected.
