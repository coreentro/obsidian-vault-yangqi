---
title: Hermes 工程系统与 Fail-Closed 设计
aliases: Hermes 接管,fail-closed,grokreg,OAuth 授权失败处理,补丁架构
tags:
  - Hermes
  - 工程设计
  - OAuth
  - fail-closed
  - 实操笔记
created: 2026-07-29
source-dirs:
  - 2026-07-28-hermes-handoff
  - 2026-07-26-hermes-permissions
  - 2026-07-16-hermes-claude-diagnosis
  - 2026-07-16-hermes-model-change-failed
  - 2026-07-16-hermes-switch-ccswitch-d
  - 2026-07-15-hermes-permission-prompts
  - 2026-07-14-hermes-permission-prompt
  - 2026-07-17-hermes-model-provider-fix
related:
  - "[[01-model-provider-access]]"
  - "[[07-troubleshooting-decision-tree]]"
  - "[[02-network-proxy-troubleshooting]]"
---

# Hermes 工程系统与 Fail-Closed 设计

> 这一篇不只是"Hermes 怎么配"，而是从一次接管 xAI OAuth 工具的工作里提炼出的**失败处理哲学**。当外部服务端拒绝你时，本地程序该怎么反应才诚实、可靠、不反复空转。

## 一、接管背景一句话

接管 `/Users/yangqi/Grok-Register`（自建邮箱注册 xAI 账号、走 OAuth device flow 拿 CPA token 的工具）。目标：诊断为什么 OAuth 一直失败，加固失败语义，留可复现的交付。

## 二、诊断收敛：根因在 xAI 服务端，不在本地

七条证据把根因边界一步步收紧：

1. **修正一个假阳性**：SPA 壳 HTML 自带 "Device Authorized" 文案，不能据此判授权成功。必须看 token endpoint 返回。
2. **代理 A/B 无效**：`40080`/`1082`/"直连"三个配置实际同落 AS13335 Cloudflare 日本出口——等于没做对照（详见 [[02-network-proxy-troubleshooting]]）。
3. **真隔离测试**：从 Shadowrocket 节点生成临时 sing-box 配置，出口 AS906 DMIT 洛杉矶，不切系统代理。
4. **两个官方版本均复现**：Grok 0.2.106 和 0.2.111 在独立 `GROK_HOME`、同一美国出口、同一账号上，都到 `/oauth2/device/done`，但 token endpoint 仍 `invalid_grant: Access denied`。
5. **授权码 + PKCE 流也复现**：xAI consent 页直接显"生成认证代码失败 / Access denied"。**device flow 是否用 PKCE、客户端版本、轮询节奏都不是必要原因**。
6. **排除早期误判**：目标 SSO JWT 只含 `session_id`；Grok Web session 的 `userId` 为空，rate-limit 响应可能来自匿名回退——**现有 Web 响应不能证明账号有免费额度或已完成身份交接**。
7. **根因边界**：只能收敛到 xAI 服务端授权/风控策略，**不能从公开错误武断区分**账号资格、反滥用、实验门控、套餐限制或其他未公开政策。

> 辩证唯物主义的用法：证据只能否定假设、收紧边界，不能在证据之外脑补结论。把根因说成"账号被风控"是越界推断——公开错误只支持"某项服务端策略拒绝"，具体是哪一项没有证据。

## 三、Fail-Closed：七条加固规则

接管期间对本地代码做的核心改造——不是为了让 OAuth 成功（那是服务端的事），而是让**失败时程序诚实地报告失败**：

1. `/oauth2/device/done?denied=...` 或带 `error=...` **不再误判为授权成功**
2. malformed callback、verify 阶段拒绝、带 CSRF 的 approve 阶段拒绝 **都 fail-closed**；拒绝后不再重试 approve
3. verify 的 429 和其他非 200 状态 **不再落入 consent 成功路径**
4. `invalid_grant (Access denied)` **不再武断解释为"浏览器确认失败"**
5. 明确的 `Access denied` 视为稳定拒绝，**不再重复创建 3 个 device grant**（避免重试风暴）
6. `reoauth` 在零 CPA 产出时返回错误，使 CLI **以非零状态退出**（而非误导性的 `fail=0` 汇总）
7. OAuth 客户端配置无效时，**启动 worker 前直接返回真实错误**，不再显示 `fail=0`

每条都配套写 Go 测试，按红—绿循环验证：测试先失败 → 改代码 → 测试通过。

## 四、工程哲学：为什么要 Fail-Closed

**两个世界观的差别**：
- Fail-open：出了错尽量"宽容处理"，让流程继续跑。代价是**把真实问题藏起来**，表现为 CPA 文件数为 0 但显示成功，或反复重试同一个永久拒绝。
- Fail-closed：确认拒绝就停下来，明确报错，非零退出。代价是**流程更早中止**，但人能立刻看到"这是真的不行，不是暂时抽风"。

从实践观点看：**把失败如实呈现给实践者，比掩盖失败制造"在运行"的假象更符合劳动者的利益**。掩盖失败的程序让你在 xAI 一直拒绝时还以为是自己配置没弄对，反复无效劳动。

## 五、验收标准（每个改动都要落地的证据）

```text
go test -count=1 ./...                                  → 通过
go test -race -count=1 ./internal/oauth ./internal/reoauth → 通过
go vet ./...                                            → 通过
git diff --check                                         → 通过
go build ./cmd/grok                                      → 通过，重建 grokreg-e2e
独立代码审查                                              → 无 Critical 无 Important
隔离单账号 E2E                                            → ok=0 fail=1 退出码 1 CPA=0
                                                         （诚实报告外部阻断）
```

E2E 的 `ok=0 fail=1` 不是失败，是**正确地报告了失败**。在 xAI 开放授权前，本地无法合法生成凭据——这才是诚实的输出。

## 六、后续恢复：发现既有可用会话

接管诊断结束后的后续工作里，发现了一个**预存在的、用户自己授权过的**官方 Grok OAuth 会话（包含 refresh token，区别于临时邮箱注册号）。用 0.2.111 + 隔离 `GROK_HOME` + AS906 出口只执行一次 refresh：

- `/v1/settings` → 200，`allow_access=true`
- `/v1/user?include=subscription` → 200，`subscriptionTier=GrokPro`
- `/v1/billing?format=credits` → 200
- CPA 同款最小 `/v1/responses` → 200

结果写进 `verified-cpa/`（目录 `0700`、文件 `0600`）。**关键边界**：
- 这证明本地 CPA 格式和流程**对 xAI 授权的账号有效**，不证明那些临时邮箱账号变合法了
- 原 `~/.grok/auth.json` 没被覆盖；refresh 在隔离环境轮换了 token，要让官方 CLI 复用需用户单独授权同步

## 七、安全纪律（写下来供以后抄）

- 报告里不记 SSO、access token、refresh token、管理密钥、完整邮箱
- `/private/tmp` 里的 SSO/Cookie/邮件/验证码文件权限从 `0644` 收紧到 `0600`
- 不删也不撤销现有会话——删除/轮换需用户另行授权
- 官方测试全部用独立临时 `GROK_HOME`，不碰 `~/.grok/auth.json`

## 八、可复用教训

1. **外部服务拒绝时，先加固本地失败语义**，再去找外部解法——否则你在改不了的东西上浪费时间。
2. **假阳性是最大的坑**：看到"成功"字样就判成功，会让你以为问题在别处。判定成功的证据必须是**协议层的实际产出**（token、200 响应），不是中间页面的文字。
3. **代理实验先验 ASN**，否则你的对照实验是假的。详见 [[02-network-proxy-troubleshooting]]。
4. **稳定拒绝不要重试风暴**：永久拒绝重试 N 次还是拒绝，只会消耗资源和制造噪声。判别"暂时 vs 永久"是失败处理的关键分叉。
5. **非零退出比 `fail=0` 汇总和诚实**：脚本给 CI/上层一个"没成功"的真实信号，胜过掩盖失败的成功报文。
