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

## 📍 当前进度

可用。sharedchat（d）挂 Cloudflare，需要代理配合才能稳定登录/调用。

## ❌ 失败方案

- 让 sharedchat / nodeloc / deepflood 走 `DIRECT` → Cloudflare 拦截，必须 `PROXY` + `force-remote-dns`。

## 🕳️ 踩坑

- deepflood 常遇 CF 真人验证；机房 IP 节点（如 JP BAGE）容易卡住 → 换干净节点或人工点验证。
- 详见 [[50-记忆/03-踩坑与失败方案]]

## 🧪 技术方案

- `d` 登录页：`https://new.sharedchat.cc/list/#/login`
- 完整前缀表与网关口径见 [[50-记忆/04-技术方案库]]

## ⏭️ 下一步

1. 定期跑 haiku 健康探测，剔除长期不可用的站点（仅停用，不删配置）。


---
返回：[[50-记忆/00-记忆索引]]
