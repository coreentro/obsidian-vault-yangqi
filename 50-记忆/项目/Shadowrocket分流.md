---
created: 2026-08-17
updated: 2026-08-20
type: 项目记忆
status: 暂停
tags:
  - 记忆
  - 项目
---

# Shadowrocket 分流

> 规则分流 + 保证 Cloudflare / 特定站点可达。


## 📋 项目背景

多个中转站与工具依赖代理；需要精细分流（国内直连、目标站走代理），并解决部分站点 TLS 断连与 CF 验证问题。
相关笔记：[[20-领域/工具/网络订阅]]

## 🎯 长期偏好与约束

- 排障**严格限定在授权范围**：不要把代理配置当无关组件随意改动。
- 不主动删除既有配置文件。
- **禁止关闭 VPN** / `killall MacPacketTunnel`（`2026-08-20`）。

## 🧩 关键决策

- **`Hermes` 配置 = `FINAL,PROXY` + CN 直连**；`Basic*` = `FINAL,DIRECT` — 两套口径分开，避免互相污染。
- **CF 站点必须 `PROXY` + `force-remote-dns`** — 防 DNS 泄漏导致验证失败。

## ✅ 已完成

- 建立 utun + fake-IP（`198.18.x.x`）+ 本地代理 `127.0.0.1:1082`。
- 路由分组：`Proxy | Config | Direct | Scene`。
- 定位「改了配置没生效」的真因：生效项看 plist 的 `CurrentRuleFileName`。
- `2026-08-20`：`Basic.db` 增加 `DOMAIN-SUFFIX,justwoker.icu,PROXY,force-remote-dns`，`api.justwoker.icu/wallet` 恢复 200（New API）。未改 FINAL、未切配置。
- `2026-08-20`：同法再加 `htai91.com` / `gorouter.app` / `tabitoken.com`（均 CF+New API），全部 200。`jianzhile.vip` 本来就通，无需规则。
- 流程已做成 skill `chrome-err-tunnel-fix`（Chrome ERR_TUNNEL 单站：权威 NS → 加例外 → 禁关 VPN）。

## 🔑 规则生效链（`2026-08-20` 挖清）

三层，顺序不能反：

| 层 | 文件/进程 | 谁写 | 触发 |
|---|---|---|---|
| 源规则 | `Databases/Basic.db` | `sqlite3` INSERT | 立即 |
| 编译规则 | `Group Containers/…/Basic.db.rule` | **主程序冷启动** | `quit` + `open`（已在跑时 `open` 无效） |
| 内存规则 | MacPacketTunnel | 隧道启动时读一次 | 重启隧道（=断一下网，需用户同意） |

门禁：`Basic.db.rule` mtime 必须晚于 `Basic.db`，否则重启隧道是白做。

## 📍 当前进度

基本可用。`justwoker.icu` 已进 Basic 代理例外。遗留：部分成人站 TLS 断连（节点侧）；deepflood 等 CF 站偶发真人验证。

## ❌ 失败方案

- **靠改分流规则解决 TLS 断连** → 无效。真因是节点 SNI / 机房 IP 被拉黑，只能换节点。
- CF 站点走 `DIRECT` → 必被拦。

## 🕳️ 踩坑

- 覆盖了 conf 但生效的仍是 `Basic.db`：改完看三键，**不要**杀隧道。
- Chrome `ERR_TUNNEL_CONNECTION_FAILED` 在 fake-IP + `FINAL,DIRECT` 下常常只是「这域名不在名单里」，不是 VPN 坏了。
- 机房 IP 节点（如 JP BAGE）在 CF 真人验证上极易卡住。
- 详见 [[50-记忆/03-踩坑与失败方案]]

## 🧪 技术方案

见 [[50-记忆/05-环境地图]]「网络」段。

## ⏭️ 下一步

1. 需要访问受限站点时，优先换干净（非机房）节点，而不是继续调规则。


---
返回：[[50-记忆/00-记忆索引]]
