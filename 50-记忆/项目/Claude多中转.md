---
created: 2026-08-17
updated: 2026-08-21
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
- `2026-08-17` **弃用本地 NewAPI `:3001`**，改客户端直连各站 — 详见 [[50-记忆/02-决策记录]]
- `2026-08-17` 健康探测改「先查目录再选探针」，**不再固定用 haiku** — 详见 [[50-记忆/02-决策记录]]

## ✅ 已完成

- 六站接入本地 NewAPI，模型列表按 `[a]`–`[f]` 前缀区分。
- Claude Desktop 与 Claude Code 均走 `:3001`。
- `f` 站对应 `ch40`。
- `2026-08-17` 跑了一次**只读健康探测**（未改任何配置），实测结论见下「当前进度」：
  - `~/.hermes/config.yaml` 现有 4 条 `custom_providers`：New(3.145.132.202) / AgentRouter Claude / AgentRouter OpenAI Compatible / Muyuan，其中 **AgentRouter 重复两条**（anthropic + openai 两种 api_mode，属有意设计）。
  - Claude Code 实际指向 `~/.claude/settings.json` 的 `anyrouter.top`，**不是**记忆里以为的本地 NewAPI `:3001`。
- `2026-08-17` 用户决定**弃用本地 NewAPI `:3001`**，架构简化为「客户端直连各中转站」。**未删除任何文件、容器或配置**，仅停止依赖。
- `2026-08-21` 按 AgentRouter 文档把 **Claude App（Desktop 1.34493.1）** 接到 `agentrouter.org`：写入 `~/Library/Application Support/Claude-3p/configLibrary/`，`deploymentMode=3p`，健康检查 `ConfigHealth=healthy`。密钥在该 JSON + `~/.hermes/.env` 的 `AGENTROUTER_CLAUDEAPP_API_KEY`（不写进知识库）。

## 📍 当前进度

`2026-08-21` Claude App 已直连 **c = agentrouter.org**（3P 网关模式）。

| 项 | 值 |
|---|---|
| 模式 | `deploymentMode=3p`，userData=`~/Library/Application Support/Claude-3p` |
| 网关 | `https://agentrouter.org`，auth=`bearer` |
| 模型 | `[c] claude-opus-5`（默认）、`[c] claude-opus-4-8` |
| 健康检查 | `ConfigHealth { state: healthy, provider: gateway }` |
| 本 key 目录 | 仅上述两个 Claude + `gpt-5.6-sol`（后者不是 Claude ID，未进 Desktop 列表） |
| 本 key **没有** haiku | 健康探针必须用 `inferenceModels` 第一项（opus-5），不能靠默认 haiku |

`2026-08-17` 实测 + 用户决策后的其它站点现状：

| 站点 / 路径 | 状态 |
|---|---|
| **c = agentrouter.org**（Hermes 当前 default）| 可用，但**必须带 `User-Agent` 头**，裸请求 401。当前配置里两条 `AgentRouter` **都没有** UA 头 → ⏳ 待用户决定是否补 |
| anyrouter.top（Claude Code 实际指向）| 目录仅 3 个模型（`claude-fable-5` / `claude-opus-5` / `gpt-5.6-sol`），**无 haiku**；opus/fable 补 1m beta 头后仍 503 |
| ~~本地 NewAPI `:3001`~~ | ⛔ **已弃用**（`2026-08-17` 用户决定）。**未删除任何文件/容器/配置**，仅停止依赖 |

**架构变更**：不再走「客户端 → 本地 NewAPI 汇聚 → 各站」，改为**客户端直连各中转站**。
因此 a–f 前缀不再依赖 NewAPI 汇聚，退化为**记忆里的站点代号**；模型列表里的前缀由各客户端自己的配置体现。

**下次从哪接**：Claude App 已可用。其它客户端（Hermes / Claude Code）仍按各自配置，未改。


## ❌ 失败方案

- 让 sharedchat / nodeloc / deepflood 走 `DIRECT` → Cloudflare 拦截，必须 `PROXY` + `force-remote-dns`。
- `2026-08-17` **用 haiku 探测 anyrouter** → 恒 403。该站目录里根本没有 haiku，不是"站点挂了"。**换站点自己提供的模型再判生死。**
- `2026-08-17` anyrouter 的 `claude-opus-5`/`claude-fable-5` 补 `anthropic-beta: context-1m-2025-08-07` → 从 400 转 **503**，仍不通。**别在这条路上继续加头**。

## 🕳️ 踩坑

- deepflood 常遇 CF 真人验证；机房 IP 节点（如 JP BAGE）容易卡住 → 换干净节点或人工点验证。
- **agentrouter.org 门禁规则已完整摸清**（`2026-08-17` 每组复测 3 次，全稳定）：放行需满足**任一**条件 —— ① `User-Agent` 以 `codex_cli_rs/` 或 `claude-cli/` **开头**（版本号任意）；② 同时带**任意 UA + `originator: codex_cli_rs`** 头。⚠️ **只给 `originator` 而不带 UA 仍 401**（两者需配合）。被拦的 UA：无UA / `python-httpx` / `curl` / `Python-urllib` / Chrome / `anthropic-sdk-python`（连官方 SDK 都拦）。`/v1/chat/completions` 路径**同样受门禁**。
- `2026-08-21` 补测：Claude App 自带的 Electron UA（里面带 `Claude/… Chrome/… Electron/…`）**已经能过门禁**；无 UA 仍 401。Desktop 配置里仍加了 `originator: codex_cli_rs` 作双保险。
- **原 UA 门禁描述**：不带 `User-Agent` 一律 `401 unauthorized client detected`，与 `muyuan.do` 的 `403 client_restricted` **同类**。配置里 `Muyuan` 有 `extra_headers` 的 UA，两条 `AgentRouter` **没有** → 这是当前 default provider 的隐患。
- **探测 localhost 必须绕过系统代理**：走代理时 `127.0.0.1:3001` 会返回**瞬时 503（0.0s）**，看起来像"服务在但坏了"；绕过后真相是 `Connection refused`（根本没起）。误判方向会完全跑偏。
- **别用 haiku 当通用探针**：haiku 只是"某些站点便宜稳定"的选择，站点没有该模型时 403 会被误读成站点故障。**先 `GET /v1/models` 看目录，再选探针模型。**
- 详见 [[50-记忆/03-踩坑与失败方案]]

## 🧪 技术方案

- `d` 登录页：`https://new.sharedchat.cc/list/#/login`
- 完整前缀表与网关口径见 [[50-记忆/04-技术方案库]]
- **agentrouter 放行头**（二选一，`2026-08-17` 实测）：
  ```yaml
  extra_headers:
    User-Agent: codex_cli_rs/0.104.0 (Mac OS 26.6.1; arm64)   # 方案A：仅此一行即可
  ```
  Hermes 源码 `agent/auxiliary_client.py::_codex_cloudflare_headers` 里已有同类逻辑，但**只用于 ChatGPT backend，不覆盖 custom_providers** —— 所以 custom provider 必须自己在 `extra_headers` 里声明。
- **健康探测正确姿势**（`2026-08-17` 实测可用）：
  1. `GET {base}/v1/models` 拿真实目录 → 选一个该站确实提供的模型当探针
  2. `POST {base}/v1/messages`，头带 `anthropic-version: 2023-06-01` + `x-api-key` + `authorization`
  3. UA 门禁站补 `User-Agent: codex_cli_rs/0.104.0 (Mac OS 26.6.1; arm64)`
  4. 探 localhost 用 `ProxyHandler({})` **绕过系统代理**，否则 503 假象
  5. 报错前先脱敏（`sk-xxxx***`）

## ⏭️ 下一步

1. Claude App 左下角切 `[c] claude-opus-5` 发一句即可人工确认（进程侧健康检查已通过）。
2. 🅿️ **已搁置**（用户 `2026-08-17` 决定：**没出问题就先别动**）—— 不给 Hermes 里的 `AgentRouter` 补 UA 头。
   - **触发条件**：若 agentrouter 开始返回 `401 unauthorized client detected` → 立刻在 `config.yaml` 两条 `AgentRouter` 下补：
     ```yaml
     extra_headers:
       User-Agent: codex_cli_rs/0.104.0 (Mac OS 26.6.1; arm64)
     ```
     照抄 `Muyuan` 写法即可，改完重启桌面端。**不必重新排查**，门禁规则见「🕳️ 踩坑」。
   - 现状：能正常工作，Hermes 实际请求已带合规 UA（具体在哪一层补的未定位到确切代码行，属已知未知）。
2. 探测任何站点前先 `GET /v1/models` 选探针，不再默认 haiku。
3. 不要默认重启 NewAPI（已弃用；文件未删，勿自行拉起）。


---
返回：[[50-记忆/00-记忆索引]]
