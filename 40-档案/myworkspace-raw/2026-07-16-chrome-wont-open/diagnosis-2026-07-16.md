# Chrome 无法打开 — 诊断记录（2026-07-16）

## 环境
- macOS Darwin 25.5.0 (arm64)
- Google Chrome 安装路径存在：`/Applications/Google Chrome.app`
- 版本：150.0.7871.115（签名/公证正常，Gatekeeper accepted）

## 检查结果
| 项 | 结果 |
|---|---|
| 安装包完整性 | 正常（Developer ID: Google LLC） |
| 用户配置目录 | `~/Library/Application Support/Google/Chrome` 存在 |
| Local State / Preferences | JSON 可解析，未见明显损坏 |
| 今日崩溃 dump | 无新的完整崩溃；7/15 有 diag 记录 |
| 后台进程 | 曾有 headless `agent-browser` Chrome 在跑（临时 user-data-dir） |

## 复现与修复尝试
1. 初始时：无用户态 Chrome 主进程，只有 crashpad + headless 实例。
2. 直接 `open -a "Google Chrome"` 一度未稳定出现用户窗口。
3. 使用 `open -na "Google Chrome" --args --new-window` 后：
   - 进程正常
   - AppleScript：`running=true windows=1`
   - 前台应用：Google Chrome
   - SingletonLock 已建立

## 结论（当时）
Chrome **本身未损坏**，更像是：
- 启动链路被后台/残留进程干扰，或
- 上一次异常退出后的瞬时启动失败，或
- 用户感知为“点了没反应”（进程起不来 / 窗口不置前）

## 若再次打不开：建议步骤
```bash
# 1) 结束所有 Chrome
pkill -x "Google Chrome" || true
killall "Google Chrome" 2>/dev/null || true

# 2) 清理残留单实例锁（仅在确认 Chrome 已全关时）
rm -f ~/Library/Application\ Support/Google/Chrome/SingletonLock \
      ~/Library/Application\ Support/Google/Chrome/SingletonCookie \
      ~/Library/Application\ Support/Google/Chrome/SingletonSocket

# 3) 重新打开
open -na "Google Chrome"
```

若仍失败，再试禁用扩展的安全模式：
```bash
open -na "Google Chrome" --args --disable-extensions
```

或临时新用户数据目录（不碰原配置）：
```bash
open -na "Google Chrome" --args --user-data-dir="/tmp/chrome-safe-profile"
```
