# Hermes → CC Switch [d] sharedchat

## Done
Hermes 默认大模型线路已切到 CC Switch 的 **[d] sharedchat**。

| 项 | 值 |
|---|---|
| Provider | `d-sharedchat` |
| Model | `gpt-5.5` |
| Base URL | `https://new.sharedchat.cc/v1` |
| API mode | `codex_responses`（与 CC Switch 站点 d 一致） |
| CC Switch Hermes current | `d-sharedchat` (`is_current=1`) |
| Key | `~/.hermes/.env` 的 `SHAREDCHAT_API_KEY`，并已同步进 CC Switch DB |

## Connectivity reality check (2026-07-16)
用当前 SharedChat key 实测：

1. `GET /v1/models` → **200**（模型列表正常）
2. `POST /v1/chat/completions` → **200 但业务关闭**：`该接口未接入公益站独立网关，旧转发链路已关闭`
3. `POST /v1/responses`（Codex）→ **403**：`您当前没有可用的 Codex 订阅，请到网页端领取或开通后再试`

因此：**切换配置已经完成**，但 **[d] 线路当前账号/订阅权限不足或中继策略变化**，实际对话仍可能失败。这不是 Hermes 没切过去，而是上游 d 站权限问题。

## UI 若仍显示旧模型
1. 完全退出 Hermes.app（Cmd+Q）
2. 再打开
3. 或终端确认：`hermes status` 应显示 `Provider: d-sharedchat` / `Model: gpt-5.5`

## Rollback
- `~/.hermes/config.yaml.bak-switch-d-*`
- `~/.hermes/.env.bak-switch-d-*`
- `~/.cc-switch/backups/cc-switch.db.bak-switch-d-*`
