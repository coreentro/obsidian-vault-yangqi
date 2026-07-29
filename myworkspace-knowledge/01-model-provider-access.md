---
title: 模型 Provider 接入与鉴权
aliases: 模型接入,Grok 接入,Gemini 接入,Antigravity 接入,CPA 配置,OAuth 接入
tags:
  - 模型接入
  - OAuth
  - CPA
  - 排障
  - 实操笔记
created: 2026-07-29
source-dirs:
  - 2026-07-14-grok-login
  - 2026-07-14-grok-apple-login
  - 2026-07-16-claude-keep-grok-only
  - 2026-07-16-gemini-subscription
  - 2026-07-16-antigravity-login-issue
  - 2026-07-14-claude-cowork-full-access
  - 2026-07-14-codex-model-providers
  - 2026-07-14-cpa-usage
  - 2026-07-14-cpa-password
related:
  - "[[07-troubleshooting-decision-tree]]"
  - "[[03-hermes-fail-closed]]"
  - "[[02-network-proxy-troubleshooting]]"
---

# 模型 Provider 接入与鉴权

> 把 xAI Grok、Google Gemini、Antigravity 这几家的订阅，统一接到本地 CPA 代理，再分发给 Claude / Codex / Hermes 三个桌面端用。这一篇收的是实际趟出来的坑和可复用的配置模式。

## 一、整体链路：一条管子分三段

所有接入最终都落到这条链路，只是上游换成不同家：

```
桌面端 (Claude / Codex / Hermes)
  → 本地代理 NewAPI (:3001) 或直连 CPA (:8317)
  → 上游 OAuth 凭据 (xAI / Google / Antigravity)
  → 官方接口 (cli-chat-proxy.grok.com / aiplatform.googleapis.com)
```

**关键认知**：NewAPI 和 CPA 不是二选一，是两段。NewAPI 适合做模型聚合和给多端分发；CPA 适合直连，少一跳延迟。Claude 后期改成**直连 CPA 绕过 NewAPI**，因为 Claude 的 3P gateway 校验有自己的怪脾气（见下文）。Codex / Hermes 仍走 NewAPI，互不干扰。

## 二、Grok 官方订阅接入（已跑通）

**接入路径**（2026-07-14 跑通，2026-07-16 改为直连）：

1. Chrome 里用 Apple 账号走完 Grok OAuth 登录
2. CPA 本地暴露 Grok 文本模型（`http://127.0.0.1:8317`）
3. NewAPI channel 5 导入 Grok 模型列表 → 实测 `grok-4.5` 请求 200
4. Hermes 切到 `custom:newapi` 作默认 provider，一次性烟测通过
5. Claude 后改为直连 CPA（见第四节）

**CPA 里最终可用的官方 Grok 模型（13 个）**：

| 用途 | 模型 id |
|---|---|
| 主力文本 | `grok-4.5`、`grok-4.3` |
| 推理变体 | `grok-4.20-0309-reasoning`、`grok-4.20-0309-non-reasoning`、`grok-4.20-multi-agent-0309` |
| 轻量 | `grok-3-mini`、`grok-3-mini-fast` |
| 创作/构建 | `grok-composer-2.5-fast`、`grok-build-0.1` |
| 多模态 | `grok-imagine-image`、`grok-imagine-image-quality`、`grok-imagine-video`、`grok-imagine-video-1.5-preview` |

> `grok-4.5` 的响应有时标成 `grok-4.5-build`，这是 Grok CLI/Build 路径的内部命名，**不是又走了中转站**，别被吓到。

## 三、可复用教训：OAuth 接入的三个坑

### 坑 1 — 代理出口与目标绑定

xAI 对出口 IP 有反滥用策略。同一批临时邮箱注册的账号，换不同代理出口结果完全不同：

- **WARP 默认出口**：访问 `accounts.x.ai` 直接被拦 `Blocked due to abusive traffic patterns`（有无 Cookie 都拦）
- **AS906 DMIT 洛杉矶出口**：能进到 xAI consent 页，但 OAuth 仍返回 `invalid_grant: Access denied`
- **AS13335 Cloudflare 日本出口**：多个代理配置表面上是 A/B，实际都落到同一个出口，等于没做对照

> 详见 [[03-hermes-fail-closed]]。这里的可复用知识是：**做代理 A/B 之前先确认两个出口真的不是同一个 ASN**，否则你的"实验"根本没在变变量。

### 坑 2 — Antigravity 资格是服务端判的，本地点什么都没用

Antigravity 登录失败的现象是 `Sorry, this account is ineligible`。诊断要点：

1. **先确认失败发生在哪一层**：Google OAuth 成功返回 → Antigravity 自己又跳回 ineligible 页面 → 说明**不是登录问题，是 Antigravity 服务端资格校验**
2. **清缓存、重装、换设备都没用**：这些不改变账号在服务端的状态
3. **官方 FAQ 的资格条件**：只对获批地区的个人 Google 账号开放；中国大陆不在列表里；资格看的是 Google ToS 页显示的国家，不是设备网络位置
4. **三个账号同症**：`yangqihello`、`entrocore`、`liliyoungqi` 三个个人账号都 OAuth 成功但都被 Antigravity 拒——说明是区域/政策级阻断，不是单账号问题

**正确动作**：走官方 country-association 申诉改国家关联；用 `@gmail.com` 个人号而非 Workspace 号；完成年龄验证（要 18+）；别依赖第三方工具绕，FAQ 明说会导致封号。

### 坑 3 — 别用"网页显示什么"判定授权成功

一个真实出现过的假阳性：Grok device flow 的 SPA 壳 HTML 自带 "Device Authorized" 文案，程序读到这串字就误判授权成功了。**必须看 token endpoint 的返回**，不能看中间页面文字。详见 [[03-hermes-fail-closed]]。

## 四、Claude Desktop 接 Grok 的特殊配置

Claude Desktop 的 3P gateway 有一个反直觉的硬校验：

> `inferenceModels[].name` **必须是 Anthropic 模型目录里的名字**，写 `grok-4.5` 会被直接拒：`configured model "grok-4.5" is not an Anthropic model`。

**绕过办法（已验证）**——用"壳名 + 标签覆盖 + CPA 别名"三段映射：

| 界面显示 (labelOverride) | Claude 请求的 name | CPA alias 映射到的上游 |
|---|---|---|
| grok-4.5 | `claude-opus-4-7` | `grok-4.5` |
| grok-4.3 | `claude-opus-4-6` | `grok-4.3` |
| grok-composer-2.5-fast | `claude-sonnet-4-6` | `grok-composer-2.5-fast` |
| grok-3-mini | `claude-haiku-4-5-20251001` | `grok-3-mini` |
| … | … | … |

- `name` 给 Claude 校验看（必须是 Anthropic id）
- `labelOverride` 给用户看（显示官方 Grok 名）
- CPA `oauth-model-alias.xai` 把壳名映射回真实 Grok 上游
- `fork: true` 保留官方 `grok-*` id 仍能被 Codex 直接用

**改完必须 `Cmd+Q` 完全退出再重开**，只关窗口不生效。新建会话测试，别用旧会话（旧会话可能还带着已删除的模型 id）。

## 五、Gemini / Antigravity 接入笔记

Gemini 这条线在 2026-07-16 走通了一半，核心节点：

1. 装官方 CPA Gemini CLI 插件，完成 `yangqihello@gmail.com` 的 Google OAuth + 年龄验证
2. Google 识别该账号为 `Gemini Code Assist in Google One AI Pro`
3. **上游已发迁移通知**：Gemini CLI 在 2026-06-18 后不再服务 Google One 和免费档——这是外部政策变化，不是本地配置问题
4. 关掉过时的 `gemini-cli` 插件路由，避免 429 和模型名碰撞
5. 把 Google Cloud 项目 `project-c785eaec-...` 链到_billing account、启用 `aiplatform.googleapis.com`、给账号 `Agent Platform User` 角色
6. **建了 0.10 美元/月的预算告警**（50%/90%/100% 三档）——接付费 API 第一件事就是设预算防暴账
7. Antigravity 桌面端最终用 Cloud fallback 路径工作，`Gemini 3.5 Flash (Medium)` 烟测通过

**一个反复出现的坑**：Hermes 请求 `gemini-3.1-pro-preview` 但 CPA 只暴露 `gemini-3.1-pro-low`，导致无限重试。**模型名必须两端一致**， CPA 暴露什么就请求什么，别用 preview id。

## 六、配置文件速查

| 用途 | 路径 |
|---|---|
| CPA 主配置 | `/opt/homebrew/etc/cliproxyapi.conf` |
| CPA 凭据目录 | `~/.cli-proxy-api/` |
| Claude 3P 配置库 | `~/Library/Application Support/Claude-3p/configLibrary/*.json` |
| Claude settings | `~/.claude/settings.json` |
| Hermes 配置 | `~/.hermes/config.yaml` |
| Hermes 状态库 | `~/.hermes/state.db`（改前必备份 + WAL/SHM） |
| Hermes 日志 | `~/.hermes/logs/agent.log` |
| 双路由器日志 | `~/.codex/hermes-dual-router/router.log` |

**回滚原则**：每次改配置前在同目录留 `.bak-<动作>-<时间戳>` 备份，改完出问题能一步退。所有对话目录里都有 `backups/` 子目录就是干这个的。

## 七、可复用 Checklist：接一个新 Provider

- [ ] 确认上游有有效凭据（OAuth 跑通、订阅生效），没有就先解决资格问题，别在本地配置上瞎试
- [ ] CPA 里加 provider 配置 + 凭据文件，`proxy-url` 指向本机代理（见 [[02-network-proxy-troubleshooting]]）
- [ ] `curl http://127.0.0.1:8317/v1/models` 验证 CPA 能列模型
- [ ] `curl POST /v1/messages` 用最短 prompt 烟测，确认上游回 200
- [ ] 桌面端配置：模型 name / labelOverride / alias 三段对齐
- [ ] `Cmd+Q` 全退重开，**新建会话**测试，不用旧会话
- [ ] effort/思考强度先降到 medium，跑通再拉高
- [ ] 改前留备份，改后验证，出问题一步回滚
