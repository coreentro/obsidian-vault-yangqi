# Codex Avatar Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Install and verify a durable Codex Dream Skin Studio theme using the user's avatar photo and the approved warm dark palette.

**Architecture:** Treat the supplied ZIP as the deployment engine. Run its static tests, install it into `~/.codex/codex-dream-skin-studio`, generate a user-level theme from the avatar through the supported customization script, then start/verify through the engine's loopback CDP injector. Preserve the official Codex application untouched and retain the restore command.

**Tech Stack:** macOS shell, bundled Codex Node.js runtime, Bash, Node.js, `sips`, CDP verifier, official Codex Desktop.

## Global Constraints

- Use the exact source image `/Users/yangqi/Desktop/微信图片_2026-07-16_152228_462.jpg`.
- Use theme name `橙色凝视`, tagline `在温暖的光里，把想法写成可运行的代码。`, and quote `STAY CURIOUS · KEEP BUILDING`.
- Use palette values recorded in the design spec.
- Do not modify official `.app`, `app.asar`, code signature, or system security settings.
- Restart only the official Codex app and the verified injector after approval.
- Do not claim success without real `tests`, `doctor`, and `verify` output.

### Task 1: Validate the extracted engine

**Files:**
- Read: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/archive/Codex 主题编辑器/.codex-dream-skin-studio/tests/run-tests.sh`
- Read: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/archive/Codex 主题编辑器/.codex-dream-skin-studio/references/qa-inventory.md`

- [ ] **Step 1: Run the supplied static test suite**

Run:
```bash
/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/archive/Codex\ 主题编辑器/.codex-dream-skin-studio/tests/run-tests.sh
```
Expected: exit code 0 with all checks passing.

- [ ] **Step 2: Inspect Codex installation and runtime identity**

Run:
```bash
mdfind 'kMDItemCFBundleIdentifier == "com.openai.codex"' | head -20
ps aux | grep -i '[C]odex'
```
Expected: official Codex app bundle is discoverable; if running, only its own process tree is considered for restart.

### Task 2: Install the engine

**Files:**
- Modify: `~/.codex/codex-dream-skin-studio/` (created by installer)
- Create: `~/Desktop/Codex Dream Skin.command`
- Create: `~/Desktop/Codex Dream Skin - Customize.command`
- Create: `~/Desktop/Codex Dream Skin - Verify.command`
- Create: `~/Desktop/Codex Dream Skin - Restore.command`

- [ ] **Step 1: Install without launching a second app instance**

Run:
```bash
/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/archive/Codex\ 主题编辑器/.codex-dream-skin-studio/scripts/install-dream-skin-macos.sh --no-launch
```
Expected: user-level installation completes and all four desktop entries exist.

- [ ] **Step 2: Confirm installation files**

Run:
```bash
find "$HOME/.codex/codex-dream-skin-studio" -maxdepth 2 -type f | sort
ls -l "$HOME/Desktop/Codex Dream Skin"*.command
```
Expected: engine scripts/assets exist and launcher files are executable.

### Task 3: Generate the avatar theme

**Files:**
- Read: `/Users/yangqi/Desktop/微信图片_2026-07-16_152228_462.jpg`
- Modify: `~/Library/Application Support/CodexDreamSkinStudio/theme/theme.json`
- Create: `~/Library/Application Support/CodexDreamSkinStudio/background-*.jpg`

- [ ] **Step 1: Run supported customization with exact source and palette**

Run:
```bash
"$HOME/.codex/codex-dream-skin-studio/scripts/customize-theme-macos.sh" \
  --image "/Users/yangqi/Desktop/微信图片_2026-07-16_152228_462.jpg" \
  --name "橙色凝视" \
  --tagline "在温暖的光里，把想法写成可运行的代码。" \
  --quote "STAY CURIOUS · KEEP BUILDING" \
  --accent "#ff9a52" \
  --secondary "#d7643e" \
  --highlight "#6c2e24" \
  --no-apply
```
Expected: `sips` creates a JPEG no larger than the engine's limit, and `theme.json` points to it.

- [ ] **Step 2: Validate persisted configuration**

Run:
```bash
python3 - <<'PY'
import json, pathlib
p = pathlib.Path.home() / 'Library/Application Support/CodexDreamSkinStudio/theme/theme.json'
data = json.loads(p.read_text())
assert data['name'] == '橙色凝视'
assert data['brandSubtitle'] == 'CODEX DREAM SKIN'
assert data['tagline'] == '在温暖的光里，把想法写成可运行的代码。'
assert data['quote'] == 'STAY CURIOUS · KEEP BUILDING'
assert data['colors']['accent'] == '#ff9a52'
assert data['colors']['secondary'] == '#d7643e'
assert data['colors']['highlight'] == '#6c2e24'
print(json.dumps(data, ensure_ascii=False, indent=2))
PY
```
Expected: assertions pass and the image file exists.

### Task 4: Start, verify, and capture evidence

**Files:**
- Create: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/home-verification-2026-07-16.png`
- Create: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/task-verification-2026-07-16.png`
- Create: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/verification-results-2026-07-16.json`

- [ ] **Step 1: Start/restart the official Codex through the supported launcher**

Run:
```bash
"$HOME/.codex/codex-dream-skin-studio/scripts/start-dream-skin-macos.sh" --port 9341 --prompt-restart
```
Expected: official Codex is running with the injector attached; no other app is stopped.

- [ ] **Step 2: Run live doctor**

Run:
```bash
"$HOME/.codex/codex-dream-skin-studio/scripts/doctor-macos.sh" --require-live
```
Expected: exit code 0 and live session checks pass.

- [ ] **Step 3: Run home-route verifier with screenshot**

Run:
```bash
"$HOME/.codex/codex-dream-skin-studio/scripts/verify-dream-skin-macos.sh" \
  --reload \
  --screenshot "/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/home-verification-2026-07-16.png" \
  | tee "/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/verification-results-2026-07-16.json"
```
Expected: JSON contains `pass: true`.

- [ ] **Step 4: Capture a task-route screenshot and inspect it**

Use the live Codex window to open a normal task route, then capture:
```bash
screencapture -x "/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/task-verification-2026-07-16.png"
```
Expected: background is atmospheric, while native sidebar, messages, composer, menus, and controls remain legible and interactive.

### Task 5: Confirm safety and recovery

**Files:**
- Create: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-16-codex-theme-editor/deployment-report-2026-07-16.md`

- [ ] **Step 1: Verify official Codex signature and payload timestamp**

Run:
```bash
APP="$(mdfind 'kMDItemCFBundleIdentifier == "com.openai.codex"' | head -1)"
codesign --verify --deep --strict "$APP"
stat -f '%Sm %N' -t '%Y-%m-%d %H:%M:%S' "$APP/Contents/Resources/app.asar" "$APP"
```
Expected: signature verification exits 0; app bundle and app.asar are not modified by the theme engine.

- [ ] **Step 2: Confirm restore entry is present**

Run:
```bash
ls -l "$HOME/Desktop/Codex Dream Skin - Restore.command"
```
Expected: restore launcher exists and is executable.

- [ ] **Step 3: Write the deployment report from real command output**

Record engine version, Codex version, theme/source, test/doctor/verify results, screenshot paths, install path, four launchers, restore path, signature result, and explicit statement that `.app` and `app.asar` were not modified.
