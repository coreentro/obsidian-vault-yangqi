# Status

## Done
- NewAPI channel 40: `f-anyrouter` → `f-zscc` (type 1 OpenAI, `https://api.zscc.in`)
- Abilities rebuilt for f shells
- Claude Desktop 3P configLibrary → `http://127.0.0.1:3001` with `[e]` + `[f]` labels
- Claude Code `~/.claude/settings.json` → NewAPI; default model shell `claude-opus-4-0` = `[f] claude-sonnet-4-6`
- Hermes `ZSCC_API_KEY` rotated to the new key

## Proved via NewAPI `/v1/messages`
- `[e] claude-opus-4-7` → grok-4.5 OK
- health `claude-haiku-4-5-20251001` → grok-4.5 OK
- `[f] claude-opus-4-0` / `claude-sonnet-4-0` → claude-sonnet-4-6 OK

## Use
1. Fully quit and reopen **Claude Desktop (3P)** so configLibrary reloads
2. Model picker: look for labels starting with **`[f]`**
3. Claude Code default is already `[f] claude-sonnet-4-6` shell
