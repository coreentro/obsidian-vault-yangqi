# Claude: keep only official Grok subscription model

## Intent
In Claude Desktop (3P gateway mode), leave only the official Grok subscription model and delete all other model entries from the picker.

## Material setup
Claude uses gateway mode through NewAPI:

- Base: `http://127.0.0.1:3001`
- Official Grok path label: `[e] grok-4.5`
- Claude-compatible request model ID: `claude-opus-4-7`
- Upstream is CPA / xAI Grok subscription (not SharedChat `[d]`, not denxio `[b]`, not anyrouter `[f]`)

## Changes
1. Rewrote both Claude-3p `configLibrary` active configs so `inferenceModels` has only:
   - `name`: `claude-opus-4-7`
   - `labelOverride`: `[e] grok-4.5`
   - `supports1m`: `false`
2. Files:
   - `/Users/yangqi/Library/Application Support/Claude-3p/configLibrary/00000000-0000-4000-8000-000000003001.json`
   - `/Users/yangqi/Library/Application Support/Claude-3p/configLibrary/00000000-0000-4000-8000-000000157210.json`
3. Pinned `~/.claude/settings.json` default model envs all to `claude-opus-4-7`.

## Removed from picker
All previous aliases were removed, including:

- other `[e]` Grok variants (`4.3`, `4.20-*`, `composer-*`)
- all `[b]` GPT entries
- all `[d]` SharedChat GPT entries
- all `[f]` Claude relay entries

## Backups
See `backups/` in this conversation directory, plus sibling `.bak-keep-grok-*` files next to originals.

## How to apply in UI
1. Fully quit Claude (`Cmd+Q`).
2. Reopen Claude.
3. Model menu should only show `[e] grok-4.5` (or that single remaining gateway model).
4. Prefer a new session if an old session still carries a deleted model id.

## Rollback
Restore the backed-up JSON files into `configLibrary/` and restore `settings.json` from `backups/`.
