#!/bin/zsh

set -euo pipefail

cleanup_analysis_file="/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-26-slow-internet-diagnosis/storage-analysis.json"
cleanup_expected_hash="d5c98b9f0b66305cd2a24ef5a884b84ab682abd71fed50787dca907d6c447d9d"

cleanup_actual_hash=$(/usr/bin/shasum -a 256 "$cleanup_analysis_file" | /usr/bin/awk '{print $1}')
if [[ "$cleanup_actual_hash" != "$cleanup_expected_hash" ]]; then
  print -u2 "停止：清理报告在脚本生成后发生了变化。"
  exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
  print -u2 "停止：未找到 jq，无法读取已审核的清理白名单。"
  exit 1
fi

cleanup_active_processes=$(
  /bin/ps -axo comm= |
    /usr/bin/grep -E \
      '/Applications/(Claude|WorkBuddy|Quark|Lark|Doubao|ChatGPT)\.app|Claude Helper|WorkBuddy|Quark Helper|Lark Helper|Doubao Browser Helper|Codex' ||
    true
)

if [[ -n "$cleanup_active_processes" ]]; then
  print -u2 "停止：以下相关应用仍在运行。请保存工作并完全退出后重试："
  print -u2 "$cleanup_active_processes"
  exit 2
fi

typeset -a cleanup_report_targets
while IFS= read -r cleanup_report_target; do
  cleanup_report_targets+=("$cleanup_report_target")
done < <(/usr/bin/jq -r '.green[].trash_paths[]' "$cleanup_analysis_file")

typeset -a cleanup_additional_targets=(
  "/Applications/Claude.app"
  "/Users/yangqi/Library/Application Support/Claude"
  "/Users/yangqi/Library/Application Support/Claude-3p"
  "/Users/yangqi/Library/Caches/claude-cli-nodejs"
  "/Users/yangqi/Library/Caches/com.anthropic.claudefordesktop"
  "/Users/yangqi/Library/Caches/com.anthropic.claudefordesktop.ShipIt"
  "/Users/yangqi/Library/Preferences/com.anthropic.claudefordesktop.plist"
  "/Users/yangqi/Library/Logs/Claude"
  "/Users/yangqi/Library/Logs/Claude-3p"
  "/Users/yangqi/Library/HTTPStorages/com.anthropic.claudefordesktop"
  "/Users/yangqi/.claude"
  "/Users/yangqi/.claude.json"
  "/Users/yangqi/.claude.json.backup"
  "/Users/yangqi/Library/Application Support/Quark/Quark/Cache/videoCache"
  "/Users/yangqi/Library/Application Support/LarkShell/aha/users/b080780fbd59945cfb60b70a985c7a1b/profile_explorer/Service Worker/CacheStorage"
  "/Users/yangqi/Library/Application Support/LarkShell/aha/users/87a9a1b70ea38d00a587d085fd7a6666/profile_explorer/Service Worker/CacheStorage"
  "/Users/yangqi/Library/Application Support/LarkShell/aha/users/85882130fca470c1b3fa89949e291e69/profile_explorer/Service Worker/CacheStorage"
  "/Users/yangqi/Library/Application Support/LarkShell/aha/users/c1d2a125bd1776757dc153538e3fe993/profile_explorer/Service Worker/CacheStorage"
  "/Users/yangqi/Library/Application Support/Doubao/Profile 1/Service Worker/CacheStorage"
  "/Users/yangqi/.cache/codex-runtimes"
  "/Users/yangqi/Library/Caches/com.workbuddy.workbuddy.BundleMigration"
)

typeset -a cleanup_targets
cleanup_targets=("${cleanup_report_targets[@]}" "${cleanup_additional_targets[@]}")

typeset -A cleanup_seen_targets
for cleanup_target in "${cleanup_targets[@]}"; do
  if [[ -n "${cleanup_seen_targets[$cleanup_target]-}" ]]; then
    continue
  fi
  cleanup_seen_targets[$cleanup_target]=1

  case "$cleanup_target" in
    *"/Google/Chrome"*|*"/Caches/Google"*|*"/GoogleUpdater"*)
      print -u2 "停止：白名单意外包含 Chrome 路径：$cleanup_target"
      exit 3
      ;;
  esac

  case "$cleanup_target" in
    /Users/yangqi/*|/Applications/Claude.app)
      ;;
    *)
      print -u2 "停止：目标超出已批准范围：$cleanup_target"
      exit 4
      ;;
  esac
done

print "将把已确认项目移到废纸篓，不会清空废纸篓。"
print "范围包括：Claude 应用及全部本地数据、WorkBuddy 升级数据、非 Chrome 绿色缓存、夸克/飞书/豆包离线缓存和 Codex 可重下载运行时。"
print "明确保留：Chrome、微信、Colima、Codex 会话与备份、项目文件及其他应用。"
print
print -n "请输入 DELETE APPROVED ITEMS 继续："
IFS= read -r cleanup_confirmation

if [[ "$cleanup_confirmation" != "DELETE APPROVED ITEMS" ]]; then
  print "已取消，没有移动任何内容。"
  exit 0
fi

cleanup_moved_count=0
for cleanup_target in "${cleanup_targets[@]}"; do
  if [[ ! -e "$cleanup_target" && ! -L "$cleanup_target" ]]; then
    continue
  fi

  print "移到废纸篓：$cleanup_target"
  /usr/bin/osascript - "$cleanup_target" <<'APPLESCRIPT'
on run argv
  set targetPath to item 1 of argv
  tell application "Finder"
    delete POSIX file targetPath
  end tell
end run
APPLESCRIPT
  cleanup_moved_count=$((cleanup_moved_count + 1))
done

print
print "已移动 $cleanup_moved_count 个目标到废纸篓。"
print "请先确认应用和重要功能正常；只有手动清空废纸篓后，空间才会真正释放。"
