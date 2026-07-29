# Hermes 与 Claude 运行故障诊断

- 诊断日期：2026-07-16
- 诊断范围：本机进程、监听端口、配置、历史日志、只读 API 烟测

## 结论

两者不是桌面程序没有启动，而是启动后在模型请求层阻塞/失败：

- Hermes：当前活动会话实际使用 `gpt-5.6-luna`，日志连续三次出现 Codex 流首字节超时（120 秒），最终会话报错。默认配置虽然是 `gpt-5.6-sol`，但旧会话没有跟随默认模型切换。
- Claude：桌面端和本地 CPA (`127.0.0.1:8317`) 都在运行；模型列表接口返回 200，但实际 `/v1/messages` 请求被 CPA 转到 `cli-chat-proxy.grok.com` 后出现 500 / TCP 超时，之前还出现过 connection reset。根因在 Grok 上游链路，不是 Claude 配置校验或桌面端未启动。

## 证据

### Hermes

- `hermes status`：Gateway running，OpenAI Codex 已登录。
- `~/.hermes/config.yaml`：默认 `gpt-5.6-sol`，provider `openai-codex`。
- `~/.hermes/logs/agent.log`：会话 `20260716_144533_271770` 使用 `gpt-5.6-luna`，三次 `Codex stream produced no bytes within TTFB cutoff (120s)`，随后 `API call failed after 3 retries`。
- `~/.codex/hermes-dual-router/router.log`：路由器在 `127.0.0.1:8320` 正常工作，部分请求返回 200；另有上游连接关闭、EOF、broken pipe。说明本地应用与路由器活着，但官方 Codex 流不稳定/无首字节。
- Hermes Gateway 的 Feishu/Weixin 报错是独立问题：Weixin session expired；部分时间代理 `127.0.0.1:1082` 不可用。它会影响消息平台，不是桌面模型请求的主根因。

### Claude

- Claude 主进程、Claude Code 子进程均存在。
- `127.0.0.1:8317` 由 `cliproxyapi` 监听；认证 `GET /v1/models` 返回 HTTP 200。
- 实际文本请求返回 HTTP 500，响应信息为：CPA 调用 `https://cli-chat-proxy.grok.com/v1/responses` 时 TCP dial timeout。
- Claude 日志在 14:48 记录：上游 `cli-chat-proxy.grok.com` connection reset by peer，单个循环耗时约 399 秒后 unhealthy。
- 两个活动 Claude Code 进程都带 `--effort max`；日志反复提示 memory pressure。它们会放大等待时间和资源占用，但不是最初的上游超时根因。
- Claude 的 sqlite project detection error、git ls-files fallback、title-gen failed 属于项目扫描/标题生成的次要问题。

## 建议顺序

1. 先完全退出 Claude 和 Hermes，清掉卡住的旧会话进程，再各自新建空白会话。
2. Hermes 先用新会话/较轻模型测试，不要继续 `gpt-5.6-luna` 的旧会话；可先用 `gpt-5.6-sol` 或 `grok-4.5`。
3. Claude 把 effort 降到 medium/default，先发短消息；若 CPA 的直接 `/v1/messages` 仍返回 500/timeout，就不要继续改 Claude 配置，应先恢复/检查 Grok 上游或网络代理。
4. 如果关注的是 Hermes 的飞书/微信机器人：重新登录 Weixin，并修复/启动 `127.0.0.1:1082` 对应代理；Feishu 连接也需检查 7897 代理稳定性。

本次只做了读取和烟测，没有改写配置或删除会话。

## 用户截图补充证据

截图显示 Hermes 当前会话底部明确为 `GPT-5.6-luna · High`，错误为：

`API call failed after 3 retries: Codex stream produced no bytes within 120s (TTFB threshold: 120s)`

这与 `agent.log` 中的三次 120 秒 TTFB 超时完全一致，并进一步确认当前卡住的是旧的 `gpt-5.6-luna` 高推理强度会话，而不是 Hermes 桌面程序未启动。

## Claude 截图与复测补充

15:00 左右截图显示 Claude 的 ConfigHealth 为 `unreachable`，探测 `http://127.0.0.1:8317/v1/messages` 时超时，探测模型为 `claude-haiku-4-5`。

15:01 本机复测结果：

- `127.0.0.1:8317/`：HTTP 200，说明 CPA 进程和本地 TCP 端口正常。
- 带认证请求 `127.0.0.1:8317/v1/models`：HTTP 200，约 1ms，说明认证和模型列表路径正常。
- 带认证请求 `127.0.0.1:8317/v1/messages`：HTTP 500，约 30s，错误为 CPA 调用 `cli-chat-proxy.grok.com/v1/responses` 时 `i/o timeout`。

因此截图中的“Can't reach 127.0.0.1:8317”是 Claude 对“完整 provider health check 超时”的用户界面归因；不是 TCP 端口真的不存在，而是本地 CPA 能接收请求，却无法在超时时间内从 Grok 上游完成一次消息请求。

## 已修复：CPA 出站代理

### 根因
系统代理 `127.0.0.1:7897` 可正常访问 `cli-chat-proxy.grok.com`，但 Homebrew launchd 启动的 CPA 进程没有继承系统代理环境变量；CPA 全局 `proxy-url` 原来为空，因此直连 Grok 上游并超时。

### 修改
- 备份：`/opt/homebrew/etc/cliproxyapi.conf.bak-cpa-outbound-proxy-20260716-150544`
- 将 `/opt/homebrew/etc/cliproxyapi.conf` 的全局配置改为：
  `proxy-url: "http://127.0.0.1:7897"`
- 重启 Homebrew 服务 `cliproxyapi`

### 验证
- CPA 重新监听 `127.0.0.1:8317`
- 带认证 `/v1/models`：HTTP 200
- 带认证 `/v1/messages`，模型 `claude-haiku-4-5`：HTTP 200，3.48 秒，返回 `收到`

## 第二次修复：切换 Clash Claude 路由节点

### 新现象
截图中的错误变为 HTTP 503：

`upstream connect error ... delayed connect error: Connection refused`

### 根因
Clash 的 `🧠 Claude` 选择组原来使用 `🚀 默认节点`，而默认节点当时落到 `🇺🇸 美国 | SS | US 01`。该节点对 Grok 上游连接被拒绝。

### 处理
未关闭代理进程，仅通过 mihomo Unix 控制接口把 `🧠 Claude` 组切换到：

`🇺🇸 美国 | SS | US 02`

### 验证
切换后，CPA `/v1/messages` 使用 `claude-haiku-4-5` 实测：HTTP 200，1.66 秒，返回 `收到`。

## Hermes 最终修复与验证

### 根因
当前活动会话不是默认配置，而是历史/界面残留的高负载会话：

- `20260716_152613_3cf352`：`gpt-5.6-terra`，effort `high`
- `20260716_145955_d0585e`：`grok-4.5`，xAI 非流式请求，约 21,597 token 上下文
- 旧 `gpt-5.6-luna` 会话也曾连续 TTFB 超时

### 处理
- 不删除历史消息；备份 `~/.hermes/state.db` 及 WAL/SHM 文件
- 将当前卡住会话 `20260716_152613_3cf352` 的元数据改为 `gpt-5.6-sol + medium`
- 重启 Hermes 客户端及其本地 serve 后端
- `🤖 ChatGPT` Clash 组保持在 `🇺🇸 美国 | SS | US 02`

### 最终验证
全新 Hermes one-shot 请求：

- 模型：`gpt-5.6-sol`
- provider：`openai-codex`
- 输入：`只回复：收到`
- 耗时：7.81 秒
- 返回：`收到`
- `completed: true`，`failed: false`
