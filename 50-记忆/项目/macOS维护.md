---
created: 2026-08-17
updated: 2026-08-17
type: 项目记忆
status: 进行中
tags:
  - 记忆
  - 项目
---

# macOS 维护

> 整机体检、权限弹窗、Finder 与工具链异常的处置口径。


## 📋 项目背景

macOS 26.6.1 上反复出现授权弹窗、截图失败、Finder 插件异常等问题，需要固定处置口径避免重复排查。

## 🎯 长期偏好与约束

- **不要主动提议或执行删除**（备份、旧文件、缓存都算）。
- 排障只动授权范围内的对象。

## 🧩 关键决策

- **禁止使用 `screencapture`，看屏幕统一走 cua-driver** — Hermes.app 是本地签名，TCC（隐私权限）记录永不匹配，每次都会弹录屏授权框。
- 弹窗类问题**先查真因再动权限设置**。

## ✅ 已完成

- 定位「授权弹窗反复冒 + computer_use 截图全 `0x0`」真因 = **微信 Sparkle 自动更新循环**，沉淀为 skill `wechat-sparkle-updater-loop`。
- 定位「一截图就弹录屏框」真因 = Hermes.app 本地签名 TCC 不匹配 → 改用 cua-driver。
- Claude Code URL Handler.app 反复重建 → 沉淀为 skill `claude-code-url-handler-removal`。
- 固化 Finder 插件处置：`pluginkit` ignore + `killall Finder`；清废纸篓用 `trashItem`。

## 📍 当前进度

常见问题均有对应技能可直接套用。

## ❌ 失败方案

- **只改 `defaults` 压制微信更新弹窗** → 无效，必须用只读文件占位。
- 把弹窗当权限问题反复重设 TCC → 无效，真因在应用侧循环。

## 🕳️ 踩坑

- 见 [[50-记忆/03-踩坑与失败方案]]「macOS」段。

## 🧪 技术方案

- 整机体检：skill `macos-system-health-check`
- 网络/代理诊断：skill `macos-proxy-network-diagnostics`
- 桌面操作：skill `macos-computer-use`（背景操作，不抢焦点）

## ⏭️ 下一步

1. 新出现的系统级怪象，先判断是否已有对应 skill，再决定是否新建。


---
返回：[[50-记忆/00-记忆索引]]
