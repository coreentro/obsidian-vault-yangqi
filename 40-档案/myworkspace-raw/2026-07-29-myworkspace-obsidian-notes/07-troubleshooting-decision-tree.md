---
title: 通用排障决策树
aliases: 排障方法论,故障诊断,模型不响应,打不开,连不上
tags:
  - 排障
  - 方法论
  - 决策树
  - 实操笔记
created: 2026-07-29
source-dirs:
  - 2026-07-16-hermes-claude-diagnosis
  - 2026-07-16-claude-keep-grok-only/hang-diagnosis-2026-07-16.md
  - 2026-07-16-chrome-wont-open
  - 2026-07-17-fix-v2ex-connection
  - 2026-07-15-browser-access-fix
  - 2026-07-16-antigravity-login-issue
  - 2026-07-26-slow-internet-diagnosis
related:
  - "[[01-model-provider-access]]"
  - "[[02-network-proxy-troubleshooting]]"
  - "[[03-hermes-fail-closed]]"
---

# 通用排障决策树

> 把 MyWorkspace 里七八次故障诊断抽出来的通用方法。无论换什么产品——Claude、Hermes、Chrome、某个网页打不开——排查顺序都是同一套。核心是**先定位层级，再动手修**。

## 零、一句话原则

**凡事先分清"本地 vs 上游"，再分清"进程 vs 配置 vs 网络"。**
不分层就动手，大概率在改一个根本不是根因的配置，越改越乱。

## 一、模型不响应 / 一直转圈不回答

这是最高频的故障。决策树（按顺序逐层判断）：

```
现象：桌面端发消息后长时间无回复
│
├─ 1. 进程在不在？
│   ├─ lsof -nP -iTCP:<端口> -sTCP:LISTEN  看本地代理端口有没有监听
│   ├─ 桌面端主进程、子进程在不在（Claude Code / hermes serve）
│   └─ 不在 → 启动；在 → 下一步
│
├─ 2. 本地能通，还是上游断？
│   ├─ curl http://127.0.0.1:<端口>/v1/models   ← 短请求
│   ├─ curl -X POST .../v1/messages -d '{"最短prompt"}'  ← 长请求
│   │   · /v1/models 200 但 /v1/messages 500/超时 = 本地正常，上游断
│   │   · 两个都 200 = 桌面端自己的会话状态有问题（见第 4 层）
│   └─ 两个都失败 = 本地配置或进程问题（回第 1 层）
│
├─ 3. 上游断的话，是代理还是真上游？
│   ├─ CPA 配置里 proxy-url 有没有设？
│   │   · 这是个反复出现的坑：系统代理 127.0.0.1:7897 本人能访问上游,
│   │     但 Homebrew launchd 启动的进程不继承系统代理环境变量,直连超时
│   ├─ 换代理出口节点再试（见 [[02-network-proxy-troubleshooting]]）
│   ├─ 确认上游服务器本身在不在（用别的线路/手机流量验）
│   └─ 都试过仍超时 → 是上游服务端问题，别再改本地配置
│
├─ 4. 本地和上游都通，但旧会话还卡 = 会话状态残留
│   ├─ 旧会话可能还带着已删除的模型 id、effort=max、超大上下文
│   ├─ 模型列表改过后，旧会话不会自动跟随默认模型切换
│   └─ 解法：Cmd+Q 全退 → 重开 → 新建空白会话 → 短消息测"只回复：收到"
│
└─ 5. 仍慢 = 推理强度太高
    ├─ 把 effort 从 max/xhigh/high 降到 medium
    ├─ 高 effort + 长上下文 resume 会长时间 thinking，UI 看着像卡死
    └─ 多个会话同时高 effort 会互相抢资源
```

### 实战案例印证（都落在同一棵树上）

- **Hermes 报 `Codex stream produced no bytes within 120s`** → 第 4 层：旧会话用 `gpt-5.6-luna` + high effort，默认虽切到 `sol` 但旧会话不跟随。改会话元数据为 `sol + medium`，重启，一次 7.81s 回 `收到`。
- **Claude `ConfigHealth unreachable`** → 第 3 层：CPA 端口 200、models 200，但 `/v1/messages` 500，错误是 CPA 调 `cli-chat-proxy.grok.com` i/o timeout。根因是 CPA（launchd 启动）没继承系统代理。改 `cliproxyapi.conf` 加 `proxy-url: "http://127.0.0.1:7897"`，重启服务，200。接着又 503 → 换 Clash `🧠 Claude` 组节点到 `US 02`，200。
- **Claude 右下角没模型 + 橙色 "needs a fix"** → 配置层：`inferenceModels[].name` 必须是 Anthropic id，写 `grok-4.5` 被拒。解法见 [[01-model-provider-access]] 第四节。

## 二、应用打不开（以 Chrome 为例）

```
现象：点应用没反应 / 窗口不出来
│
├─ 1. 进程起没起？
│   ├─ ps / Activity Monitor 看主进程
│   ├─ 只有 crashpad / headless 残留进程 = 主进程没起来
│   └─ 有主进程但没窗口 = 窗口不前置或单实例锁残留
│
├─ 2. 安装包完整性？
│   ├─ codesign -dv 查签名 / Gatekeeper 状态
│   ├─ 版本号、安装路径存在性
│   └─ 配置目录 JSON 能不能解析（~/Library/Application Support/...）
│
├─ 3. 逐级恢复（从轻到重）
│   ├─ open -na "App" --args --new-window
│   ├─ 仍不行 → pkill -x → 清 SingletonLock/Cookie/Socket → 重开
│   ├─ 仍不行 → --disable-extensions 安全模式
│   ├─ 仍不行 → --user-data-dir="/tmp/xxx-safe-profile" 临时新目录（不碰原配置）
│   └─ 临时目录能开 = 原用户配置损坏，针对性迁移数据
```

> Chrome 那次诊断的结论不是"Chrome 坏了"，而是**后台残留的 headless Chrome 进程干扰了启动链路**。先排除残留进程，再怀疑损坏。

## 三、网页打不开 / 连接被关

```
现象：某网站 ERR_CONNECTION_CLOSED / Cloudflare 拦截页
│
├─ 1. 网站本身在不在？
│   ├─ 换条线路（手机流量、别的代理节点）访问同一个 URL
│   ├   · 别的线路能开 = 问题在你当前出口
│   └─   · 都开不了 = 网站或 DNS 问题
│
├─ 2. 是不是代理出口被针对？
│   ├─ 当前出口节点对该域名被 reset/refused
│   ├─ 换出口节点或临时关代理再试
│   └─ V2EX 案例：原节点 Abco1 对 v2ex.com 的隧道被关，换个节点 v2ex 就活了
│
├─ 3. 是不是 Cloudflare 按 IP 拦？
│   ├─ 看拦截页有没有 Cloudflare Ray ID
│   ├─ 该 IP 被该站 Cloudflare 规则拒绝 = 换出口 IP
│   └─ codex.openai.chatgpt.site 案例：换 Shadowrocket 节点后活动页就开了
│
└─ 4. DNS / 系统代理路径
    ├─ scutil --dns 看解析路径
    └─ 确认系统级代理（1082 / 7897）是不是真的在转发
```

**可复用知识**：出口 IP 和目标域名之间存在**绑定关系**。同一个出口对 A 网站通，对 B 网站可能就被 reset，不要假设"网通了就什么都通"。详见 [[02-network-proxy-troubleshooting]]。

## 四、"感觉网慢"但连接看起来正常

这种症状最容易被误诊。诊断纪律：

1. **先确认是不是真慢**：带宽测试、延迟测试，别只凭体感
2. **分清是全站慢还是特定目标慢**：特定目标慢大概率是出口路由问题，不是本地网络
3. **代理节点切换后再测**：很多"网慢"其实是当前出口节点拥塞或路由绕远
4. 别把存储扫描当网络诊断用——两件事

## 五、排障的元原则

1. **物质先于意识**：先看进程、端口、日志、curl 返回码这些客观证据，不要先脑补"是不是配置错了"。
2. **矛盾分层**：一个故障可能有多个矛盾叠加（旧会话 + effort 拉满 + 上游超时），但**主要矛盾只有一个**。先找主要矛盾，解决了次要矛盾往往自己消失。
3. **主要矛盾的主要方面**：本地 vs 上游，先判断哪一边。本地能改，上游改不了——改不了的那边要确认清楚，否则你会在改不了的地方反复瞎试。
4. **实践是检验标准**：每改一项都验证，不要连续改三项再测——连改三项还是坏，你不知道是哪一项作的妖。
