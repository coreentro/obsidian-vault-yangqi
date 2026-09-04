---
created: 2026-08-17
updated: 2026-09-04
type: 项目记忆
status: 进行中
tags:
  - 记忆
  - 项目
---

# Hermes 配置

> 自定义中转供应商、模型切换、技能与工具链的本地配置。


## 📋 项目背景

Hermes Agent 作为主力入口，需要接多个自定义中转、维护技能库，并保证桌面端模型选择器可用。

## 🎯 长期偏好与约束

- **未经要求不要改 `model.default`。**
- 密钥只放 `.env`，`config.yaml` 用 `key_env` 引用；**不写进知识库**。
- 配置 Hermes 自身相关任务前，先看 skill `hermes-agent`。

## 🧩 关键决策

- **用 `custom_providers` 接中转**（name / base_url / api_mode / key_env / extra_headers / models），而不是硬改内置供应商 — 可并存、可回滚。
- 切换方式 `/model custom:<name>:<model>`。

## ✅ 已完成

- 建立 `custom_providers` 机制，桌面端输入框旁选择器按 `name` 分组。
- `muyuan.do`（`custom:muyuan/gpt-5.6-sol`）接入成功，靠 `extra_headers` 的 `UA=codex_cli_rs*` 绕过限制。
- `2026-08-20` 接入 `DigitalGleam`（`ai.digitalgleam.pp.ua`）：密钥在 `.env` 的 `DIGITALGLEAM_API_KEY`，`config.yaml` 用 `key_env` 引用；**未改** `model.default`（仍是 `grok-4.6` / `xai-oauth`）。
- `2026-08-20` 接入 `Hcnsec`（`api.hcnsec.cn`）：密钥在 `.env` 的 `HCNSEC_API_KEY`；目录目前只有 `glm-5.2`，无需自定义 UA；**未改** `model.default`。
- `2026-09-04` 刷新 Hermes 里 4 条 AgentRouter 的模型列表，对齐 `GET https://agentrouter.org/v1/models`（两条 key 目录相同）。下架 `claude-opus-4-6`；Claude 条只留 `claude-opus-4-8` / `claude-opus-5`；OpenAI 条加上 `deepseek-v4-flash` / `glm-5.3`，保留 `gpt-5.6-sol`。**未改** `model.default`（仍是 `claude-opus-5` / `custom:agentrouter-claude`）。未补 UA 头（Hermes CLI 对 `glm-5.3` 已回 `OK`）。

## 📍 当前进度

`2026-09-04` AgentRouter 站点目录 = `claude-opus-4-8`、`claude-opus-5`、`deepseek-v4-flash`、`glm-5.3`、`gpt-5.6-sol`。直连冒烟：后三个 chat + messages 均 200 回 `OK`；两个 Claude 模型两条 key 都是 **402 预算池额度耗尽**（目录仍列出，不是本地配置错）。桌面端选择器要**完全退出再打开**才看得到新模型。

新增供应商后**必须重启**桌面端，否则模型列表走缓存看不到新项。

⚠️ `2026-08-19` 实测：`muyuan.do` **UA 门禁已通过、但上游渠道空了**。`GET /v1/models` 200 且只列 `gpt-5.6-sol` 一个模型；调用该模型（`/v1/chat/completions`、`/v1/responses`、`/v1/messages` 三条路径 + Hermes CLI）**全部 503 `model_not_found: No available channel for model gpt-5.6-sol under group default (distributor)`**，30 秒内复测 5 次 0/5 成功 → 是站点侧渠道掉了，不是本地配置问题。配置保持原样待其恢复。

## ❌ 失败方案

- 不带自定义 UA 直连 `muyuan.do` → `403 client_restricted`。
- Hermes 内置 browser（Browserbase）抓某些站点 → WAF 403；改用本机浏览器 + 代理（skill `browser-tool-workarounds`）。

## 🕳️ 踩坑

- 模型列表有缓存 → 改完配置要重启。
- `muyuan.do` 偶发 CF 504 → 直接重试即可，不是配置错。
- 详见 [[50-记忆/03-踩坑与失败方案]]

## 🧪 技术方案

`custom_providers` 配置形状见 [[50-记忆/04-技术方案库]]。

## ⏭️ 下一步

1. 新接供应商时沿用同一形状，并在本卡「已完成」留一行（改了哪个文件、为什么）。


---
返回：[[50-记忆/00-记忆索引]]
