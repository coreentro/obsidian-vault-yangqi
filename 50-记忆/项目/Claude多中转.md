---
created: 2026-08-17
updated: 2026-08-17
type: 项目记忆
status: 进行中
tags:
  - 记忆
  - 项目
---

# Claude 多中转

> 六个中转站（a–f）统一进模型列表，用前缀一眼看出走哪家。


## 📋 项目背景

同时有多个第三方中转站，模型名重复、看不出走哪家，切换容易出错。目标：本地 NewAPI 汇聚 + 前缀标识。

## 🎯 长期偏好与约束

- 模型列表里**必须用前缀区分站点**：`[b] gpt-5.5`、`[e] grok-4.5`、`[f] claude-…`。
- 切换时要一眼看出走哪个中转。
- **不写真实密钥进知识库**。

## 🧩 关键决策

- **前缀映射固定**：`a=jianzhile` `b=denxio` `c=agentrouter` `d=sharedchat` `e=CPA` `f=zscc`。
- **Claude Desktop / Claude Code 统一指向本地 NewAPI `:3001`**，不直连各站，便于集中切换。
- **健康探测固定用 haiku，优先 `e-cpa`** — 便宜且稳定。

## ✅ 已完成

- 六站接入本地 NewAPI，模型列表按 `[a]`–`[f]` 前缀区分。
- Claude Desktop 与 Claude Code 均走 `:3001`。
- `f` 站对应 `ch40`。
- `2026-08-17` 跑了一次**只读健康探测**（未改任何配置），实测结论见下「当前进度」：
  - `~/.hermes/config.yaml` 现有 4 条 `custom_providers`：New(3.145.132.202) / AgentRouter Claude / AgentRouter OpenAI Compatible / Muyuan，其中 **AgentRouter 重复两条**（anthropic + openai 两种 api_mode，属有意设计）。
  - Claude Code 实际指向 `~/.claude/settings.json` 的 `anyrouter.top`，**不是**记忆里以为的本地 NewAPI `:3001`。

## 📍 当前进度

`2026-08-17` 实测（只读，未改配置）——**记忆与现状已漂移，需要择期对齐**：

| 站点 / 路径 | 实测结果 |
|---|---|
| **c = agentrouter.org**（Hermes 当前 default）| 裸请求 **401 `unauthorized client detected`**；**补 `User-Agent: codex_cli_rs/…` 后 200，回 `OK`** ✅ |
| anyrouter.top（Claude Code 实际指向）| 站点活着但 **目录里只有 3 个模型**：`claude-fable-5` / `claude-opus-5` / `gpt-5.6-sol`；**没有任何 haiku**。haiku 探测必然 403「该令牌无权访问」。opus/fable 报「需启用 1m 上下文」，补 beta 头后转 503 |
| **本地 NewAPI `:3001`** | ❌ **没在跑**（绕过代理后 `Connection refused`；colima 未启动，无 newapi 进程）。`:3080` 是 DeepSeek Harness，不是 NewAPI |

**下次从哪接**：`50-记忆/04-技术方案库` 里「Claude Desktop/Code → 本地 NewAPI :3001」与「健康探测固定 haiku」两条已**不再反映现状**，已在该页标注实测状态。要恢复 a–f 六站前缀体系，得先把 NewAPI 起回来。


## ❌ 失败方案

- 让 sharedchat / nodeloc / deepflood 走 `DIRECT` → Cloudflare 拦截，必须 `PROXY` + `force-remote-dns`。
- `2026-08-17` **用 haiku 探测 anyrouter** → 恒 403。该站目录里根本没有 haiku，不是"站点挂了"。**换站点自己提供的模型再判生死。**
- `2026-08-17` anyrouter 的 `claude-opus-5`/`claude-fable-5` 补 `anthropic-beta: context-1m-2025-08-07` → 从 400 转 **503**，仍不通。**别在这条路上继续加头**。

## 🕳️ 踩坑

- deepflood 常遇 CF 真人验证；机房 IP 节点（如 JP BAGE）容易卡住 → 换干净节点或人工点验证。
- **`agentrouter.org` 是 UA 门禁站**：不带 `User-Agent` 一律 `401 unauthorized client detected`，与 `muyuan.do` 的 `403 client_restricted` **同类**。配置里 `Muyuan` 有 `extra_headers` 的 UA，两条 `AgentRouter` **没有** → 这是当前 default provider 的隐患。
- **探测 localhost 必须绕过系统代理**：走代理时 `127.0.0.1:3001` 会返回**瞬时 503（0.0s）**，看起来像"服务在但坏了"；绕过后真相是 `Connection refused`（根本没起）。误判方向会完全跑偏。
- **别用 haiku 当通用探针**：haiku 只是"某些站点便宜稳定"的选择，站点没有该模型时 403 会被误读成站点故障。**先 `GET /v1/models` 看目录，再选探针模型。**
- 详见 [[50-记忆/03-踩坑与失败方案]]

## 🧪 技术方案

- `d` 登录页：`https://new.sharedchat.cc/list/#/login`
- 完整前缀表与网关口径见 [[50-记忆/04-技术方案库]]
- **健康探测正确姿势**（`2026-08-17` 实测可用）：
  1. `GET {base}/v1/models` 拿真实目录 → 选一个该站确实提供的模型当探针
  2. `POST {base}/v1/messages`，头带 `anthropic-version: 2023-06-01` + `x-api-key` + `authorization`
  3. UA 门禁站补 `User-Agent: codex_cli_rs/0.104.0 (Mac OS 26.6.1; arm64)`
  4. 探 localhost 用 `ProxyHandler({})` **绕过系统代理**，否则 503 假象
  5. 报错前先脱敏（`sk-xxxx***`）

## ⏭️ 下一步

1. 定期跑 haiku 健康探测，剔除长期不可用的站点（仅停用，不删配置）。


---
返回：[[50-记忆/00-记忆索引]]
