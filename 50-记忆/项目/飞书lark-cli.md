---
created: 2026-08-17
updated: 2026-08-17
type: 项目记忆
status: 暂停
tags:
  - 记忆
  - 项目
---

# 飞书 lark-cli

> 本机 lark-cli 打通飞书文档、知识库、消息。


## 📋 项目背景

飞书是主要协作工具，需要用 CLI 读写文档、知识库、发消息，供 Agent 自动化。
相关笔记：[[20-领域/工具/飞书]]

## 🎯 长期偏好与约束

- 明确要求委托 Aily 时**直接发送，不再二次确认**（发送/放弃仍需明确确认的场景除外）。
- 不在知识库存 token。

## 🧩 关键决策

- CLI 安装在用户级 `~/.local/bin`（已在 PATH），不用 sudo 装系统目录。
- **发给自己时用 `--as bot`** — 否则会出现身份/权限问题。

## ✅ 已完成

- lark-cli 就位于 `~/.local/bin`。
- 知识库 profile 确定为 `cli_aade26ab1c781bcd`。
- 大量 lark-* 技能可用（doc / wiki / base / sheets / im / calendar / mail / minutes 等）。

## 📍 当前进度

可用。认证与切号细节见 skill `lark-cli-local-setup`。

## ❌ 失败方案

暂无明确证伪项（认证失败/切错账号的排查见下）。

## 🕳️ 踩坑

- 认证失败、账号切错、或 session 失效 → 按 skill `lark-cli-local-setup` 处理，不要手删配置。

## 🧪 技术方案

见 [[50-记忆/04-技术方案库]]「飞书 lark-cli」。技能：`lark-shared`（auth 相关）、`lark-doc`、`lark-wiki`、`lark-base` 等。

## ⏭️ 下一步

1. 需要飞书自动化时优先用对应 lark-* 技能，而不是裸调 API。


---
返回：[[50-记忆/00-记忆索引]]
