---
created: 2026-08-17
updated: 2026-08-17
type: 项目记忆
status: 进行中
tags:
  - 记忆
  - 项目
---

# Codex Desktop

> 用官方 ChatGPT 账号，Grok 与 GPT 同菜单切换，且切换不丢聊天记录。


## 📋 项目背景

Codex Desktop 需要同时用到 GPT 与 Grok；早期切换供应商后侧边栏历史像"消失了"，引发对丢数据的担心。

## 🎯 长期偏好与约束

- 使用**官方 ChatGPT 账号**，默认开启 **Full Access**（含已有对话），无需逐次审批。
- 模型下拉里要能**直接切 Grok 与 GPT**（同一个菜单）。
- 切换模型/供应商**不能丢聊天记录**。

## 🧩 关键决策

- **供应商固定 `cliproxyapi`，只换 model 不换 provider** — 侧边栏按 `model_provider` 过滤，换 provider 会让历史看起来消失。
- **Grok 与 GPT 写进同一个 catalog json** — 实现同菜单切换。
- **CLI 独占供应商时用 `~/.codex-cli`，不动 `~/.codex`** — 避免污染桌面端配置。

## ✅ 已完成

- 官方账号接入 + Full Access 默认开启。
- Grok / GPT 进同一 catalog，下拉可直接切。
- 历史不全问题定位为**显示过滤 + 空 title**，非真实丢失。

## 📍 当前进度

可用。历史完整性用「四计数对账」验证：unique vscode rollout ≈ threads ≈ catalog ≈ thread/list。

## ❌ 失败方案

- 通过切 provider 来换模型 → 侧边栏历史被过滤掉，看起来像丢了。**不要这样做。**
- 试图清 Session / auth 来"修"历史 → 风险高且无必要，真因是过滤和空 title。

## 🕳️ 踩坑

- 空 `title` 的会话不是丢失，只是没标题。
- 修复顺序必须是：**备份 → 统一 provider → 重建 catalog → 补 title**。
- 详见 [[50-记忆/03-踩坑与失败方案]]

## 🧪 技术方案

见 [[50-记忆/04-技术方案库]]「Codex Desktop」。

## ⏭️ 下一步

1. 若再出现历史疑似缺失，先做四计数对账再动手，不要直接改文件。


---
返回：[[50-记忆/00-记忆索引]]
