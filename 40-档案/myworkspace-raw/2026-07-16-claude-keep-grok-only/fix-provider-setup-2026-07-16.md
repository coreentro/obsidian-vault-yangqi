# 修复：Your provider setup needs a fix / 右下角没模型

## 原因
Claude Desktop 的 custom 3P gateway **强制** `inferenceModels[].name` 必须是 Anthropic 模型目录里的名字，例如：

- `claude-opus-4-7`
- `claude-sonnet-4-6`
- `claude-haiku-4-5`

直接写 `grok-4.5` 会被拒绝：

```text
configured model "grok-4.5" is not an Anthropic model
failingField: inferenceModels
```

因此右下角模型选择器为空，并弹出橙色 “Your provider setup needs a fix”。

## 正确做法（已应用）
1. Claude 配置里：
   - `name` = Anthropic 壳模型 id（满足校验）
   - `labelOverride` = 官方 Grok 名（界面显示）
   - 网关直连 CPA：`http://127.0.0.1:8317`
2. CPA `oauth-model-alias.xai`：
   - 把 Anthropic 壳 id 映射到真实 Grok 上游
   - `fork: true` 保留官方 `grok-*` id 仍可被 Codex 等直接使用

## 当前映射
| 界面显示 (labelOverride) | Claude 请求 name | 上游 Grok |
|---|---|---|
| grok-4.5 | claude-opus-4-7 | grok-4.5 |
| grok-4.3 | claude-opus-4-6 | grok-4.3 |
| grok-4.20-0309-reasoning | claude-opus-4-1 | grok-4.20-0309-reasoning |
| grok-4.20-0309-non-reasoning | claude-opus-4-1-20250805 | grok-4.20-0309-non-reasoning |
| grok-4.20-multi-agent-0309 | claude-opus-4-20250514 | grok-4.20-multi-agent-0309 |
| grok-composer-2.5-fast | claude-sonnet-4-6 | grok-composer-2.5-fast |
| grok-build-0.1 | claude-sonnet-4-20250514 | grok-build-0.1 |
| grok-3-mini | claude-haiku-4-5-20251001 | grok-3-mini |
| grok-3-mini-fast | claude-haiku-4-5 | grok-3-mini-fast |
| grok-imagine-image | claude-sonnet-4-5 | grok-imagine-image |
| grok-imagine-image-quality | claude-sonnet-4-5-20250929 | grok-imagine-image-quality |
| grok-imagine-video | claude-opus-4-5 | grok-imagine-video |
| grok-imagine-video-1.5-preview | claude-opus-4-5-20251101 | grok-imagine-video-1.5-preview |

## 实测（修复后）
- `claude-opus-4-7` / `claude-opus-4-6` / `claude-sonnet-4-6` / `claude-haiku-4-5` 直打 CPA `/v1/messages` 均为 HTTP 200

## 你需要做
1. `Cmd+Q` 完全退出 Claude
2. 重新打开
3. 橙色报错应消失；右下角应能看到官方 Grok 名称（默认 grok-4.5）
4. 新建会话后发：`只回复：收到`

更新时间：2026-07-16T12:16:45
