---
title: 网络代理与出口排障
aliases: 代理排障,出口节点,Shadowrocket,Clash,sing-box,ASN 隔离
tags:
  - 网络
  - 代理
  - 排障
  - 实操笔记
created: 2026-07-29
source-dirs:
  - 2026-07-17-fix-v2ex-connection
  - 2026-07-15-browser-access-fix
  - 2026-07-28-hermes-handoff
  - 2026-07-16-hermes-claude-diagnosis
  - 2026-07-16-google-account-region
  - 2026-07-16-ip-geolocation-difference
  - 2026-07-23-anyrouter-access
  - 2026-07-28-any-router-403
related:
  - "[[07-troubleshooting-decision-tree]]"
  - "[[01-model-provider-access]]"
  - "[[03-hermes-fail-closed]]"
---

# 网络代理与出口排障

> 国内环境接海外 AI 服务，代理不是"能通就行"。每次故障里至少一半的根因都落在出口节点上。这篇收的是反复出现的代理坑，以及一套判断出口是不是真问题的方法。

## 一、核心认知：出口 IP 与目标是"一对多绑定"

很多人把"代理通了"理解成全局开关——网通了就什么都通。实际上：

- **同一个出口 IP** 对网站 A 通，对网站 B 可能就被 reset/refused/Cloudflare 拦
- **同一个代理软件**切不同节点，对同一网站的可达性会完全不同
- 代理软件的多个"出口"可能实际落在**同一个 ASN**（同一家云厂商），等于没切

> 从实践观点看：网络可达是具体的、有条件的，不是抽象的、全局的。判断"网通不通"必须落到"某个出口对某个目标通不通"这个具体矛盾上。

## 二、一次 A/B 实验无效的典型案例

这是 MyWorkspace 里最有价值的一条教训：

**现象**：在 Grok OAuth 接入时，切换了几个代理配置以为做了 A/B，但 xAI 一直返回 `Access denied`。

**真相**：`40080`、`1082` 和所谓"直连"三个配置，实际出口都落在 **同一个 AS13335 Cloudflare 日本节点**。表面上切了三次代理，实际上变量根本没变——这不是 A/B 实验，是同一个实验做了三遍。

**正确做法**：做代理对照实验前，**先验证两个出口的 ASN 真的不一样**：
- 用 IP 地理信息服务查出口 IP 和 ASN
- ASN 相同就是同一个出口，不管配置名差多远
- 要真正隔离，用不同云厂商的出口（如 AS906 DMIT vs AS13335 Cloudflare）

那次实验最后用 Shadowrocket 节点生成了一个临时 sing-box 配置，出口走 AS906 洛杉矶，才算做出有效对照——结果还是被 xAI 拒，但至少把根因收敛到了"xAI 服务端策略"，而不是纠结本地代理配错。详见 [[03-hermes-fail-closed]]。

## 三、本地代理软件的三层结构

这张图在排障时反复有用：

```
应用层 (Claude / Hermes / Chrome)
   │
   ├─ 系统代理环境变量 (HTTP_PROXY/HTTPS_PROXY)
   │   · 只对读环境变量的进程生效
   │   · launchd 启动的 Homebrew 服务通常不继承！  ← 反复出现的坑
   │
   ├─ 应用内代理设置
   │   · Claude-3p / Hermes 各自的配置文件里 proxy-url 字段
   │   · CPA: /opt/homebrew/etc/cliproxyapi.conf 的 proxy-url
   │   · 不设 = 直连上游
   │
   └─ 系统级代理 (Shadowrocket 1082 / Clash 7897)
       · 真正转发流量的那一层
       · 出口节点决定 IP 和 ASN
```

### 那个反复出现的坑：launchd 不继承系统代理

CPA 由 Homebrew 装成 launchd 服务，启动时**不继承**你 shell 里的 `HTTP_PROXY`，也不会自动用系统代理。结果：你本人能访问上游，但 CPA 直连上游超时。

**解法**：在 CPA 配置文件里显式写 `proxy-url: "http://127.0.0.1:7897"`，然后重启服务。这是 2026-07-16 那次 Claude `ConfigHealth unreachable` 的根因。

> 一句话：**服务进程的代理要在服务自己的配置里设，别指望它继承你的系统代理。**

## 四、出口节点与具体目标的绑定清单

从几次故障里抽出来的"哪个出口对哪个目标通"的经验清单：

| 出口 / 节点 | 对 xAI `accounts.x.ai` | 对 v2ex.com | 对 Grok 上游 `cli-chat-proxy.grok.com` | 对 Cloudflare 拦截站 |
|---|---|---|---|---|
| WARP 默认 | 被拦 abusive traffic | - | - | - |
| `Abco1-youngqi-20270717` | - | 隧道关闭 | - | - |
| `vm-argo-dedirock-*` | - | 通 | - | - |
| Clash `🚀 默认节点` → `US 01` | - | - | refused | - |
| Clash `🧠 Claude` → `US 02` | - | - | 200 | - |
| AS906 DMIT 洛杉矶 | 能进 consent 但 OAuth 仍拒 | - | - | - |
| 切换 Shadowrocket 节点 | - | - | - | codex 活动页通了 |

**读法**：这不是一份"照着配就行"的表，而是证明**出口对目标的可达性是具体的、要实测的**。你的节点和我的不一样，别抄这张表，自己用 curl 测。

## 五、Cloudflare 拦截的识别

- 拦截页通常带 `Cloudflare Ray ID: xxxxxxx`
- 被拦说明该出口 IP 触发了该站的 Cloudflare 规则
- **不是网站宕机**，换出口 IP 通常能解决
- codex.openai.chatgpt.site 那次：两个浏览器都收到同一 Ray ID 的拦截页，换 Shadowrocket 节点后活动页就开了

## 六、IP 地理位置与账号资格的耦合

这个坑在 Antigravity 登录里最明显：

- Antigravity 资格看的是 **Google ToS 页显示的国家**，不是设备网络位置
- 一个未登录的 Google ToS 页显示 `国家/地区版本：中国`——但这不证明账号本身的国家关联，因为那个浏览器没登录
- 公网出口按目标分流：一个 IP 地理服务看到 LA 出口，另一个看到河南电信出口——**不能凭一次地理查询就断定账号关联的国家**

> 矛盾分析法：这里"设备网络位置""账号关联国家""服务端资格判定"是三个不同的东西，别混为一谈。服务端判资格，你改本地网络没用。

## 七、代理排障 Checklist

- [ ] 确认系统代理端口在监听（`lsof -nP -iTCP:1082 -sTCP:LISTEN`）
- [ ] 应用进程是否走了你要的代理？（launchd 服务要单独配）
- [ ] 当前出口 IP 和 ASN 是什么？（别假设，查）
- [ ] 换出口节点后目标是否可达？
- [ ] 换 ASN 不同的出口再测一次（真 A/B）
- [ ] 手机关代理 / 换网络能不能复现？（排除本地路由问题）
- [ ] 看 Cloudflare 拦截页有没有 Ray ID
- [ ] 网站本身的资格/区域判定 vs 网络可达性——分清这两件事
