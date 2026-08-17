---
created: 2026-08-17
updated: 2026-08-17
type: 项目记忆
status: 暂停
tags:
  - 记忆
  - 项目
---

# DeepSeek Harness

> 本地跑官方 dsh，像普通 App 一样双击打开。


## 📋 项目背景

想在本机用 DeepSeek 官方 harness（dsh）作为另一个 Agent 入口。

## 🎯 长期偏好与约束

- **必须像普通 App 双击打开**（`~/Applications/DeepSeek Harness.app`）。
- **不要做成开机常驻 launchd** — 用户明确拒绝。

## 🧩 关键决策

- 用官方包 `@deepseek-ai/dsh`（配置在 `~/.dsh`），而非第三方封装。
- 以 `.app` 包装启动脚本，保持"双击即用"。

## ✅ 已完成

- 官方 dsh 可用，Web 界面在 `http://localhost:3080`。
- 做成 `~/Applications/DeepSeek Harness.app`，双击启动。
- 明确启动命令为 `npx @deepseek-ai/dsh web`（PATH 里没有 `dsh` 可执行文件）。

## 📍 当前进度

可用但未常用。仅支持 `DEEPSEEK_API_KEY` 一种鉴权。

## ❌ 失败方案

- **想用 Grok OAuth 登录 dsh** → 走不通，官方只认 `DEEPSEEK_API_KEY`。**不要再试。**
- 直接敲 `dsh` → command not found，要用 `npx`。
- 做 launchd 常驻 → 用户明确否决。

## 🕳️ 踩坑

见 [[50-记忆/03-踩坑与失败方案]]。

## 🧪 技术方案

见 [[50-记忆/04-技术方案库]]「DeepSeek Harness」。相关：中转集成见 skill `dsh-relay-integration`。

## ⏭️ 下一步

1. 若要接本地中转，参考 skill `dsh-relay-integration` 而非改官方包。


---
返回：[[50-记忆/00-记忆索引]]
