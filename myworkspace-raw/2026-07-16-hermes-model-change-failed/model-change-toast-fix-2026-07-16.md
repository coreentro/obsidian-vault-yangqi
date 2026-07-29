# Claude Desktop: Model change couldn't be applied

## What the toast is
Right-upper yellow toast text comes from **Claude.app** (Code/Cowork 3P mode), not Hermes:

- i18n: `Model change couldn’t be applied. You can try again.`
- source: `epitaxy_set_model` in Claude Desktop renderer

## Root cause (material conditions)
Claude Desktop is running in **custom 3P / gateway** mode:

- base: `http://127.0.0.1:3001` (SSH tunnel to NewAPI)
- model picker labels like `[e] grok-4.5` are **labelOverride only**
- actual request model IDs are Claude-compatible aliases, e.g. `claude-opus-4-7`

config had `supports1m: true` on all mapped models. Claude UI then stores/switches models as:

```text
claude-opus-4-7[1m]
```

Gateway NewAPI only knows:

```text
claude-opus-4-7
```

so `config.set` / model switch fails → toast **Model change couldn't be applied**.

Verified:

| Request model | Result |
|---|---|
| `claude-opus-4-7` | 200 → grok-4.5-build |
| `claude-opus-4-7[1m]` | 503 model_not_found |
| `claude-haiku-4-5-20251001` | 200 |
| `claude-haiku-4-5-20251001[1m]` | 503 model_not_found |

Secondary issues (still true, separate from this toast):

- `[d] ...` mapped IDs hit SharedChat and return **no Codex subscription / 403**
- some `[b]/[f]` mapped IDs currently have **no available channel**

## Fix applied
1. Disabled `supports1m` in both Claude-3p configLibrary entries:
   - `00000000-0000-4000-8000-000000003001.json`
   - `00000000-0000-4000-8000-000000157210.json`
2. Stripped `[1m]` from persisted session model fields under Claude-3p sessions.
3. Backups stored in `backups/`.

## What you should do now
1. Fully quit Claude Desktop (`Cmd+Q`).
2. Reopen Claude.
3. Open session, model menu: pick `[e] grok-4.5` (or another `[e]` item).
4. Toast should disappear / switch should apply.
5. Prefer **new session** when changing provider letter groups (`[e]` vs `[d]` vs `[b]`), because old sessions may still carry stale provider-bound state.

## If still failing
- Confirm bottom-right still shows an `[e] ...` model, not a broken `[d]/[b]` entry.
- Confirm tunnel `127.0.0.1:3001` is up (`ssh` process listening).
- For `[d]` models: SharedChat needs Codex subscription/claim; config switch alone cannot invent entitlement.
