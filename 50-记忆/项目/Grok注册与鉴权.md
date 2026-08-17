---
created: 2026-08-17
updated: 2026-08-17
type: 项目记忆
status: 暂停
tags:
  - 记忆
  - 项目
---

# Grok 注册与鉴权

> Grok/xAI 的账号注册器与 OAuth 登录两条路。


## 📋 项目背景

需要稳定使用 Grok：一条是正规 OAuth 登录，一条是注册器批量拿账号。

## 🎯 长期偏好与约束

- 注册器目录与官方 CLI 目录**严格分开**，避免互相破坏。
- 不在知识库记录任何账号密码。

## 🧩 关键决策

- **`~/.grok` 属于官方 CLI，注册器一律用 `~/.grok-register` 与 `~/Grok-Register`** — 混用会破坏官方登录态。
- Hermes 侧用 `hermes auth add xai-oauth`；官方 CLI 用 `grok login --oauth`。

## ✅ 已完成

- 注册器 `grokreg` 就位（`~/.grok-register`、`~/Grok-Register`）。
- 两条鉴权路径明确：Hermes `hermes auth add xai-oauth`；官方 CLI `grok login --oauth`。
- Pi 侧可用模型：`nvidia` / `z-ai` / `glm-5.2`；Grok 走内置 `/login xai`。

## 📍 当前进度

可用。cf_temp（Cloudflare 临时邮箱/验证环节）细节见 skill `grok-register`。

## ❌ 失败方案

- 动 `~/.grok` 来配注册器 → 会影响官方 CLI 登录态。**禁止。**

## 🕳️ 踩坑

- 注册流程会遇 Cloudflare 验证，机房节点易失败 → 换干净节点。
- 详见 skill `grok-register` 与 [[50-记忆/03-踩坑与失败方案]]

## 🧪 技术方案

见 [[50-记忆/04-技术方案库]]「Grok / xAI」。另有 skill `xai-account-registration`。

## ⏭️ 下一步

1. 需要新账号时直接走 skill `grok-register`，不要临时手改目录。


---
返回：[[50-记忆/00-记忆索引]]
