---
created: 2026-08-17
updated: 2026-08-17
type: 项目记忆
status: 进行中
tags:
  - 记忆
  - 项目
---

# Hermes 桌面端界面

> 让桌面端聊天区「我说的」和「AI 说的」一眼分清；以及其他 UI 观感调整。

## 📋 项目背景

用户反馈：桌面端聊天里**自己发的文字和 AI 回复混在一块儿、分不清**。
Hermes 桌面端是 Electron（用 Web 技术做的桌面程序）应用，聊天区样式由打包在 `app.asar` 里的 CSS 控制。

## 🎯 长期偏好与约束

- 不改 Hermes 应用本体（升级会被覆盖）→ 用 `~/.hermes/desktop-plugins/` 插件注入。
- 插件里**不硬编码颜色**，只用主题变量（`var(--ui-accent)` 等），换皮肤自动跟随。
- **禁止屏幕捕获**排查 UI（会弹录屏框且拿不到画面）→ 改读源码。

## 🧩 关键决策

- `2026-08-17` **用桌面插件注入 CSS，而不是改 asar 或换皮肤** — 皮肤只能改颜色值，改不了「有没有边框/标签」这类结构；改 asar 会被升级覆盖。插件可热重载、可随时关。
- `2026-08-17` **只强化用户消息，助手消息仅加淡左边界** — 助手消息含大量 Markdown（表格/代码块），重度改样式易破版。

## ✅ 已完成

- `2026-08-17` 解包 `/Applications/Hermes.app/Contents/Resources/app.asar` 读渲染层 CSS，定位根因（见「当前进度」）。
- `2026-08-17` 新建插件 `~/.hermes/desktop-plugins/chat-role-contrast/plugin.js`：
  - 用户消息：左侧 3px 强调色条 + 10% 淡底 + 38% 可见边框 + 圆角 + 左上角「你」标签
  - 助手消息：2px 淡左边界 + 「HERMES」小标签
  - 监听 `host.onEvent('*')` 幂等重注入，防主题切换后样式丢失
- `2026-08-17` 验证：node 可加载 ESM；4 个 `data-slot` 选择器在当前版本真实存在（9/1/3/7 处）；4 个主题变量均有定义。

## 📍 当前进度

**根因已定位**（读打包 CSS 得出）：

| 变量 | 实际值 | 后果 |
|---|---|---|
| `--theme-mix-bubble` | **浅色模式 `0%`** / 深色 `.dark` 为 `46%` | 用户气泡底色被**完全混掉**，等于没有背景色 |
| `--ui-stroke-tertiary`（气泡边框）| `--ui-accent` 仅混约 **5%** 不透明度 | 边框几乎不可见 |

即：**深色模式下本来能看出气泡，浅色模式下用户消息几乎没有任何视觉边界** → 两边糊成一片。

插件已落盘并通过静态验证，**等用户在 ⌘K 里执行「Reload desktop plugins」后确认观感**。

## ❌ 失败方案

- `computer_use(action='capture')` 看界面 → 弹录屏授权框且返回 `0x0`，**纯负收益**，已列入红线。
- 靠换内置皮肤解决 → 皮肤只改颜色，改不了结构（边框/标签/间距），且 `mix-bubble: 0%` 的问题依旧。

## 🕳️ 踩坑

- **打包版桌面端 CDP 调试口是关闭的**（`apps/desktop/electron/dev-cdp.ts`：packaged build 一律关，无环境变量可覆盖）→ skill `inspecting-hermes-desktop-dom` 的方法**对打包版不适用**，只能解 asar 读静态 CSS。
- `grep -oE` 里写 `(0, 300)` 这类大区间会报 `maximum repetition exceeds 255` → 改用 Python 正则。
- 在 `/tmp` 子目录里 `rm -rf` 自己所在目录会导致后续命令报 `getcwd` 失败 → 删之前先 `cd` 出去，或给命令加 `workdir`。

## 🧪 技术方案

```bash
# 读打包后的渲染层 CSS（不看屏幕也能诊断 UI）
npx --yes @electron/asar extract \
  /Applications/Hermes.app/Contents/Resources/app.asar /tmp/out
grep -o -- "--ui-chat-bubble-background:[^;]*;" /tmp/out/dist/assets/index-*.css
```

- 插件目录：`~/.hermes/desktop-plugins/<id>/plugin.js`（`<id>` 必须等于文件夹名）
- 生效方式：文件落盘后几秒自动热加载；不生效则 ⌘K →「Reload desktop plugins」
- 关闭方式：Settings → Plugins 里关掉；或移走该文件夹
- 稳定选择器：`aui_user-message-root` · `aui_user-message-text` · `aui_assistant-message-root`

## ⏭️ 下一步

1. 让用户 ⌘K →「Reload desktop plugins」，确认区分度是否够；不够就调 `--ui-accent` 混色比例（10%/38%）或加大间距。
2. 若用户想要更强区分，可考虑把用户消息改为右对齐（需确认不影响长文本与代码块）。

---
返回：[[50-记忆/00-记忆索引]]
