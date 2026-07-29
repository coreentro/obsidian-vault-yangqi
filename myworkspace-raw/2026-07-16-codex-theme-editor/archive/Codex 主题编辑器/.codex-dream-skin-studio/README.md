# Codex Dream Skin Studio

把一张自己喜欢的图片变成 macOS Codex 主题：主页显示独立横幅，普通任务页显示低干扰背景和磨砂内容层，同时保留 Codex 原生侧栏、卡片、项目选择器、任务内容和输入框。

项目通过本机回环 CDP 动态注入，不修改官方 `.app`、`app.asar` 或代码签名。刷新、切换任务和 Codex 重启后可持续重新应用，并提供一键恢复。

![Codex Dream Skin Studio 主页实机效果](docs/screenshots/home-live.png)

## 最简单的使用方式

1. 解压整个项目文件夹，不要只复制 CSS 或图片。
2. 双击 `Install Codex Dream Skin.command`。首次安装会复制到 `~/.codex/codex-dream-skin-studio` 并在桌面创建四个入口。
3. 双击桌面的 `Codex Dream Skin - Customize.command`。
4. 在 Finder 选择图片，输入主题名。图片会自动转成最长边不超过 3200 px 的 JPEG。
5. Codex 会在得到确认后重启一次；以后从桌面的 `Codex Dream Skin.command` 启动。

桌面入口：

- `Codex Dream Skin.command`：启动或重新应用主题；
- `Codex Dream Skin - Customize.command`：重新选图并应用；
- `Codex Dream Skin - Verify.command`：执行真实 CDP 自检并保存截图；
- `Codex Dream Skin - Restore.command`：移除主题、恢复原始基础配色并正常启动 Codex。

## 素材要求

- 支持 macOS 可读取的 PNG、JPEG、HEIC、TIFF 和 WebP；
- 原文件不超过 50 MB；处理后的文件不超过 16 MB；
- 横向图片效果最好，建议宽度 2000 px 以上；
- 左侧保留较安静的区域，会更适合叠加主页原生标题；
- 图片只作为横幅和背景，不会作为整张界面截图覆盖原生控件。

主题名和三种强调色也可以通过命令行设置：

```bash
~/.codex/codex-dream-skin-studio/scripts/customize-theme-macos.sh \
  --image "/path/to/image.png" \
  --name "我的主题" \
  --accent "#7cff46" \
  --secondary "#36d7e8" \
  --highlight "#642a8c"
```

恢复随包附带的传送门示例：

```bash
~/.codex/codex-dream-skin-studio/scripts/customize-theme-macos.sh --reset-demo
```

## 自检

静态、配置往返和官方签名检查：

```bash
./tests/run-tests.sh
```

检查已启动的真实主题：

```bash
~/.codex/codex-dream-skin-studio/scripts/doctor-macos.sh --require-live
~/.codex/codex-dream-skin-studio/scripts/verify-dream-skin-macos.sh \
  --reload --screenshot "$HOME/Desktop/Codex Dream Skin Verification.png"
```

验证器不会只检查“脚本是否运行”。它会检查原生侧栏、输入框、主页横幅、原生建议卡、项目选择器、横向溢出，以及装饰层是否拦截点击。

## 工作原理与安全边界

- 动态发现 Bundle ID 为 `com.openai.codex` 的官方应用；
- 验证应用及其 Node.js 的代码签名、OpenAI Team ID、CPU 架构和 Node.js 版本；
- 通过用户级 `launchd` 启动官方可执行文件，并只在 `127.0.0.1` 开启 CDP；
- 只接受由 Codex 主进程或合法子进程持有的监听端口；
- 只向包含预期 Codex 原生结构的 `app://` 页面注入；
- 使用常驻注入器处理刷新、路由切换和渲染器重建；
- 恢复时核对 PID、启动时间、Node 路径和注入器路径，避免误停其他进程。

CDP 端口是仅限本机但未认证的调试接口。主题运行期间不要执行来源不明的本地程序；使用 Restore 入口可关闭主题会话和调试端口。

## 文件位置

- 安装目录：`~/.codex/codex-dream-skin-studio`
- 状态、日志和用户图片：`~/Library/Application Support/CodexDreamSkinStudio`
- Codex 基础主题备份：上述状态目录内的 `theme-backup.json`

项目不会备份或修改 `app.asar`，因为它从不写入官方应用包。

## 故障排查

- 找不到配置：先正常启动一次 Codex，再重新安装。
- Codex 签名无效：恢复或重新安装官方 Codex；项目会拒绝继续。
- Codex 更新后界面没有主题：从桌面重新运行 `Codex Dream Skin.command`，再执行 Verify。
- 验证失败：查看 `~/Library/Application Support/CodexDreamSkinStudio/injector-error.log` 和 `start-error.log`。
- 端口 9341 被占用：启动器会在 9341–9441 中选择空闲端口并写入状态文件。

## 支持范围

首个正式版面向 macOS Codex Desktop。项目不依赖全局 Node.js，也不包含超过 100 MB 的运行时二进制。Codex 升级若移除内部签名 Node 或改变关键原生结构，项目会失败关闭并要求更新适配，而不会盲目修改应用。

代码采用 MIT License。示例人物视觉不随 MIT 软件许可证授予角色、商标或商业分发权，详见 `NOTICE.md` 与 `references/asset-provenance.md`。

主页和任务页截图均由运行中的 Codex 渲染器通过 CDP 实际截取，不是静态 HTML 预览。完整结果见 `references/acceptance-report-2026-07-15.md`。
