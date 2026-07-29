# Claude 直连 CPA + 官方 Grok 模型名

## 结果
Claude 不再经 NewAPI `:3001`，改为直连 CLIProxyAPI：

- Base: `http://127.0.0.1:8317`
- Auth: CPA `api-keys`（`/opt/homebrew/etc/cliproxyapi.conf`）
- Provider profile name: `CPA → Grok official`
- 默认模型: `grok-4.5`
- 显示名 = 官方模型 id（无 `[e]` 前缀、无 claude 别名）

## 已接入的官方 Grok 模型（CPA `/v1/models` 中全部 grok-*，共 13）
1. grok-4.5
2. grok-4.3
3. grok-4.20-0309-reasoning
4. grok-4.20-0309-non-reasoning
5. grok-4.20-multi-agent-0309
6. grok-composer-2.5-fast
7. grok-build-0.1
8. grok-3-mini
9. grok-3-mini-fast
10. grok-imagine-image
11. grok-imagine-image-quality
12. grok-imagine-video
13. grok-imagine-video-1.5-preview

未纳入 Claude 列表的是 CPA 里的 GPT 模型（gpt-5.*），按“只留 Grok 官方”要求排除。

## 修改文件
- `~/Library/Application Support/Claude-3p/configLibrary/00000000-0000-4000-8000-000000003001.json`
- `~/Library/Application Support/Claude-3p/configLibrary/00000000-0000-4000-8000-000000157210.json`
- `~/Library/Application Support/Claude-3p/configLibrary/_meta.json`
- `~/.claude/settings.json`
- 会话 model 字段：`claude-code-sessions/.../local_*.json` 中 `claude-*` → `grok-4.5`

## 实测
- `POST /v1/messages model=grok-4.5` → 200，回复正常
- `grok-4.3` → 200
- `grok-3-mini-fast` → 200（响应 model 字段可能被上游标注成别的 grok 名）

## 使用方式
1. 完全退出 Claude：`Cmd+Q`
2. 重新打开
3. 优先新建会话
4. 模型菜单应出现官方名列表（默认 `grok-4.5`）

## 回滚
`backups/direct-cpa-*` 与 `backups/sessions-direct-cpa/`，以及 config 旁 `.bak-direct-cpa-*`

## 说明
- `grok-4.5` 请求有时响应标成 `grok-4.5-build`：Grok CLI/Build 路径的响应命名，不是又走了中转站。
- image/video 模型已列出，但 Claude 文本 Agent 场景未必能完整使用其多模态能力。
- NewAPI `:3001` 仍可服务 Codex/Hermes，只是 Claude 已不依赖它。
