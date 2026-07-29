# Grok 官方订阅接入路径（直连 CPA）

## 当前链路（2026-07-16 起）
Claude Desktop (3P gateway)
  → http://127.0.0.1:8317  (CLIProxyAPI)
  → xAI / SuperGrok OAuth (`~/.cli-proxy-api/xai-*.json`)
  → cli-chat-proxy.grok.com
  → 官方 Grok 订阅

## 模型名
请求与 UI 均使用官方 id，例如 `grok-4.5`、`grok-4.3`、`grok-composer-2.5-fast` 等。
默认：`grok-4.5`。

## 配置
- Claude configLibrary: gateway → 8317 + CPA key
- ~/.claude/settings.json: ANTHROPIC_BASE_URL=http://127.0.0.1:8317
- CPA conf: /opt/homebrew/etc/cliproxyapi.conf

## 与 NewAPI 关系
Claude 已绕过 NewAPI。NewAPI `:3001` 可继续给 Codex/Hermes 用，与 Claude 解耦。
