---
created: 2026-08-17
updated: 2026-08-17
type: 项目记忆
status: 进行中
tags:
  - 记忆
  - 项目
---

# Hermes 社区插件

> 用 GitHub 上成熟的第三方插件扩展 Hermes，而不是自制。

## 📋 项目背景

用户明确要求「找 GitHub 上成熟方案，别自己做」。社区总目录：`0xNyk/awesome-hermes-agent`（5.3k★，200+ 条目，含技能/插件/记忆后端/工具）。
另有社区地图站 `hermesatlas.com`。

## 🎯 长期偏好与约束

- **先找现成方案，不自制**（详见 [[50-记忆/01-长期偏好]]「解决问题的优先顺序」）。
- 装之前**必须审代码**：查外部网络、危险调用、是否改 Hermes 源码。
- **不装碰钱的**：涉及 USDC/钱包/助记词的一律跳过（`hermes-payguard`、`ClawRouter-Hermes`、`hermes-gondola-provider`）。
- 优先 `brew`（homebrew-core）而非 `curl | sh` 管道执行。
- 装到 **Hermes 自己的 venv**（`~/.hermes/hermes-agent/venv/bin/pip`），不污染系统 Python。

## 🧩 关键决策

- `2026-08-17` **装 `hermes-snow-search` + `rtk-hermes`，暂不装 `hermes-feishu-zh`** — 前两个不动 Hermes 源码；飞书那个会打补丁改 12+ 个核心文件（含 `run_agent.py`、`auxiliary_client.py`），升级易冲突，且仅 4★。用户选方案 A。
- `2026-08-17` **两个插件都不授予 `--allow-tool-override`** — 该权限可拦截所有经过内置工具的调用，保持最小权限。

## ✅ 已完成

- `2026-08-17` 审计三个候选（clone 后扫危险模式：`curl|sh`、`eval/exec`、`socket`、`wallet/BIP39`）：三者均 MIT、无钱包、无管道安装、无可疑外连。
- `2026-08-17` **装 `hermes-snow-search` 0.7.0**（pip → Hermes venv）+ `hermes plugins enable`。
  - 审计要点：仅 9 个文件；`SessionDB(read_only=True)` 只读；**零外部网络**；`pyproject` **无第三方依赖**。
  - 钩子行为已读源码确认：`on_pre_llm_call` 只做内存淘汰、明确 `No context injection needed`；`on_post_llm_call` 把 `snow_search` 的旧结果清空以省 token。
- `2026-08-17` **装 `rtk` 0.45.0（brew，homebrew-core，Apache-2.0，月装 2 万次）+ `rtk-hermes` 1.2.3**，启用为 `rtk-rewrite`。
  - 实测改写：`git status`→`rtk git status`、`cat X`→`rtk read X`（同义命令，不改语义）。
  - **实测省量**：`git status` 155→59 字符（省 62%）；`ls -la` 2081→753 字符（省 64%）。信息未丢（`ahead 3`、`clean` 均保留）。
  - 代码要点：`subprocess.run(["rtk","rewrite",cmd])` **不走 shell**（无注入）、有超时、退出码分类、失败回退原命令、默认仅 `local` 后端。
- `2026-08-17` 验证：`hermes plugins list` 两者均 `enabled`；entry-points 正确注册 2 个外部插件入口。

## 📍 当前进度

两个插件已装好、已启用、已实测生效。**注意：`hermes plugins enable` 提示「Takes effect on next session」——完整效果需新会话/重启 Hermes 后体现。**

`rtk` 有个提示：`No hook installed — run 'rtk init -g' for automatic token savings`。**未执行**（那是给 shell 全局装钩子的，超出当前需求范围，且会影响用户自己的终端）。Hermes 侧由 `rtk-rewrite` 插件负责改写，不需要全局钩子。

## ❌ 失败方案

- `hermes-feishu-zh` → **未装**（非失败，是主动否决）：会补丁改 Hermes 核心源码，升级风险高。它自带备份机制（`backups/hermes-feishu-zh-<时间戳>`），若将来要装可再评估。

## 🕳️ 踩坑

- `web_extract` 抓 GitHub 报 `Blocked: URL targets a private or internal network address` → fake-IP(198.18) 触发 SSRF 误拦。**改用 `curl` + GitHub API**。
- `grep` 关键词过滤插件列表时容易把目标行滤掉（表格有换行/截断）→ 直接 grep 插件名本身。
- `execute_code` 里 `terminal()` 返回可能没有 `output` 键（长命令超时），**取值要用 `.get()`**；brew 这类长任务直接用 `terminal` 工具并给足 timeout。

## 🧪 技术方案

```bash
# 装外部 pip 插件到 Hermes 自己的 venv（关键：不用系统 pip）
~/.hermes/hermes-agent/venv/bin/pip install <包名>
hermes plugins enable <插件名>          # 不加 --allow-tool-override
hermes plugins list | grep -iE "<插件名>"

# 查外部插件入口是否注册
~/.hermes/hermes-agent/venv/bin/python -c \
  "from importlib.metadata import entry_points; \
   print([e.name for e in entry_points().select(group='hermes_agent.plugins')])"

# 审计新插件（装前必做）
git clone -q --depth 1 <repo> && grep -rn --include="*.py" \
  -iE "curl .*\| *(ba)?sh|eval\(|exec\(|socket\.|BIP39|wallet|private_key" .
```

## ⏭️ 下一步

1. 用几天观察 `rtk` 是否有命令被改写后行为异常；若有，`hermes plugins disable rtk-rewrite` 即可回退。
2. 新会话里试 `snow_search` 工具，验证中文检索效果（它宣称 CJK 用 trigram 分词）。
3. 候选清单（暂不装，需要时再评估）：`DashClaw`（审批策略层，production）、`eagle-eye`（技能路由，你技能多）、`cronalytics`（定时任务成本，支持中文）、`Extracto`（本地正文提取，无需 key）。

---
返回：[[50-记忆/00-记忆索引]]
