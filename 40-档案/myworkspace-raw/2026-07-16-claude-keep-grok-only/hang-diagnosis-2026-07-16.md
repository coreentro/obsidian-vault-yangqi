# Claude 一直不回答：诊断

## 结论（先说事实）
**不是 NewAPI/Grok 完全挂了。** 短请求实测正常：

- `GET /v1/models` → 200
- `POST /v1/messages` model=`claude-opus-4-7` → 200，约 1.5s，上游 `grok-4.5-build`
- stream 也能正常吐 thinking + text

所以矛盾不在“有没有线路”，而在 **Claude Desktop 的 Agent 会话状态**。

## 现象
日志显示消息已发出：

```
LocalSessions.sendMessage: sessionId=local_607d44ab-...
Sending message to session ...
```

但之后长时间没有：

```
Query completed / first_assistant / CycleHealth healthy
```

用户体感就是：**问了问题一直不回答。**

## 物质条件
1. 当前多个会话同时活着，且有会话把 **effort 拉到 max/xhigh**。
2. 多个 `claude-code` 子进程对 `127.0.0.1:3001` 占着大量 ESTABLISHED 连接。
3. Grok 官方订阅走 CPA，高 effort + 长上下文 resume 会长时间 thinking，UI 可能几乎不显示中间过程，像卡死。
4. 历史上还有 `claude-opus-4-7[1m]` 这种无效模型号（503 model_not_found）；当前这几个活动会话 model 字段已是 `claude-opus-4-7`，但旧会话/UI 状态仍可能叠加问题。

## 已做修复
1. 模型列表只保留官方 Grok：`[e] grok-4.5` ↔ `claude-opus-4-7`
2. 把会话配置里的 `effort: max/xhigh/high` 降到 `medium`，避免一上来就拉满推理
3. 备份在本目录 `backups/`

## 你现在要做的（关键）
1. **完全退出 Claude**：`Cmd+Q`（不要只关窗口）
2. 重新打开
3. **新建一个会话**（不要继续卡住的旧会话）
4. 确认右下角模型是 `[e] grok-4.5`
5. 先发一句短消息测试：“只回复：收到”
6. 若仍慢：在会话里把 effort/思考强度降到默认或 medium，不要 max

## 若还不行
- 检查 3001 隧道是否还在：`lsof -nP -iTCP:3001 -sTCP:LISTEN`
- 再测：`curl -sS http://127.0.0.1:3001/v1/models -H "Authorization: Bearer <token>"`
