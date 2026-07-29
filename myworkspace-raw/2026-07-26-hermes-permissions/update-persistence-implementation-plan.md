# Hermes Local Patch Persistence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 让 Hermes 的普通 CLI 更新和 Desktop 自更新在没有 LaunchAgent/守护进程的前提下，始终从仓库外的版本化 patch queue 恢复稳定签名与模型切换两组本地补丁；只要 stash、patch queue 或签名身份验证不完整，就在依赖刷新、Desktop 构建和应用替换之前失败关闭。

**Architecture:** `~/.hermes/local-patches` 是独立 Git 仓库和唯一补丁事实源，包含严格 manifest、两组补丁、无第三方依赖的 reconcile 工具和一个按需 CLI shim。仓库内 `cmd_update` 负责同步调用仓库外 reconcile；Git 忽略区内的 `venv/bin/hermes` shim 负责在仓库代码已被 reset 且上一次进程异常退出时先修复再导入 `hermes_cli.main`，解决“恢复器自身也被 reset”的鸡生蛋问题。macOS 的所有受支持打包入口复用同一签名策略与验证函数；发现已经建立稳定身份基线时，任何 ad-hoc fallback 都被拒绝。

**Tech Stack:** Python 3 标准库、Git patch/worktree、pytest、Bash、Node.js ESM、Electron Builder、macOS `codesign`/`xattr`。

## Global Constraints

- 本计划阶段只写本文档；不得修改 Hermes 代码、配置、权限、应用、Git 分支或 worktree。
- 实施时不得使用 LaunchAgent、定时任务或常驻守护进程；恢复只在 `hermes update`、Desktop 自更新、installer 和受支持的本地打包入口中同步发生。
- 主工作树 `/Users/yangqi/.hermes/hermes-agent` 当前有用户的未提交稳定签名补丁；实施前必须先做仓库外校验备份，未经明确迁移步骤不得 reset、checkout、clean、commit 或覆盖。
- 隔离 worktree `/Users/yangqi/.hermes/hermes-agent/.worktrees/live-model-switch` 的 `codex/live-model-switch` 分支承载两个模型切换提交；当前仅有的 `package-lock.json` 修改是运行时 churn，不进入补丁队列。
- patch queue 固定在 `${HERMES_HOME:-$HOME/.hermes}/local-patches`，本机默认即 `~/.hermes/local-patches`；不把补丁、恢复器或状态文件放进 `hermes-agent`。
- `cmd_update` 必须在 Python/Node 依赖刷新、web build、`desktop --build-only` 之前完成 stash 结果判定和同步 reconcile。
- stash 恢复冲突、用户跳过恢复、stash 丢失、manifest 不完整、patch 部分应用、补丁验证失败或 queue 不干净时均退出非零；不得继续构建或宣称更新成功。
- 已配置稳定签名身份或已有签名基线时，installer、CLI 和 npm 入口均不得退回 ad-hoc 签名。
- 不在源码、manifest、日志、测试夹具或本文档中保存或输出私钥、API key、令牌、证书私钥材料或环境变量值。补丁只可含公开源码；日志只记录相对路径、组 ID、patch ID、Git commit 和摘要哈希。
- 主仓库的本地定制最终保持为可被 updater stash/restore 的未提交工作树差异；不得再次把本地提交留在 `main` 上等待 updater 合并。

---

## 1. 已核对的当前事实与实施边界

1. `hermes_cli/main.py:_cmd_update_impl` 当前在 `git pull --ff-only` 失败时执行 `git reset --hard origin/{branch}`；本地提交不会进入 autostash。
2. `hermes_cli/main.py:_restore_stashed_changes` 当前冲突时保留 stash、把工作树 reset 回新 HEAD、返回 `False`，但调用者忽略返回值并继续依赖刷新与 Desktop build。
3. 成功路径的 stash restore 在依赖刷新和 Desktop build 前发生；缺的是失败关闭栅栏。
4. 当前稳定签名补丁已在主工作树及 `codex/hermes-stable-signing-2026-07-26` 分支的 6 个业务提交中保存：
   - `41efdcc10f` 到 `da13e34549`；
   - 不得把该分支祖先中的上游格式化提交 `953707103f` 当成本地补丁导出。
5. 模型切换实现位于 `codex/live-model-switch`：
   - `7421b009d4`：turn 运行期间排队模型切换；
   - `48cbe1a51d`：阻止 prompt 与正在应用的模型切换竞态。
6. 模型切换设计文档提交 `126223a61c` 当前对象仍可读，但没有分支/标签保护；必须在第一批 queue materialization 中导出。
7. `scripts/install.sh:install_desktop` 当前在 venv Python 不存在时仍会 ad-hoc 签名；即使已有稳定身份配置，也无法保证身份不降级。
8. `apps/desktop/package.json` 的 `pack`、`dist`、`dist:mac*` 直接调用 Electron Builder，绕过 Python 签名 helper。
9. Desktop updater 的可读 Rust 源码 `apps/bootstrap-installer/src-tauri/src/update.rs:resolve_hermes` 明确优先执行 `hermes-agent/venv/bin/hermes`。该路径在 Git 忽略区，适合作为按需、非守护的 reset 外恢复锚点，不需要修改 `/Applications/Hermes.app` 的 Bundle ID 或签名身份。

## 2. 最终文件与职责映射

### 仓库外独立 Git 仓库

- Create: `~/.hermes/local-patches/manifest.json`
  - 唯一的补丁顺序、校验和、目标路径、必需组和验证命令清单。
- Create: `~/.hermes/local-patches/bin/reconcile.py`
  - 仅使用 Python 标准库；验证 queue、在临时 worktree 计算期望树、识别 applied/missing/partial、原子应用和输出机器可读结果。
- Create: `~/.hermes/local-patches/bin/install-hermes-shim.py`
  - 原子安装/验证 `venv/bin/hermes` 按需 shim；不得改 Python 解释器或应用 bundle。
- Create: `~/.hermes/local-patches/bin/hermes-shim`
  - 对 `update` 先执行外部 preflight/recovery，再用同一 venv 的 Python 执行 `-m hermes_cli.main`；其他子命令直接透传。
- Create: `~/.hermes/local-patches/patches/stable-signing/*.patch`
  - 稳定签名、更新恢复集成、installer fail-closed、npm 受控打包，以及 section 2 明列的 pytest 文件。
- Create: `~/.hermes/local-patches/patches/live-model-switch/*.patch`
  - 设计文档和两个模型切换实现提交。
- Create: `~/.hermes/local-patches/tests/test_reconcile.py`
  - 真实临时 Git 仓库上的 queue 单元/集成测试。
- Create: `~/.hermes/local-patches/tests/test_install_hermes_shim.py`
  - shim 原子安装、pip 覆盖后重装、pending marker 恢复测试。
- Create: `~/.hermes/local-patches/README.md`
  - 受支持入口、初装/更新/冲突恢复说明；不包含任何身份值或密钥。
- Runtime only, Git-ignore: `~/.hermes/local-patches/state/reconcile.lock`
  - `fcntl.flock` 的互斥锁。
- Runtime only, Git-ignore: `~/.hermes/local-patches/state/pending-update.json`
  - reset/异常退出恢复面包屑。
- Runtime only, Git-ignore: `~/.hermes/local-patches/state/signature-baseline.json`
  - 公开签名身份摘要；不含证书或私钥。
- Runtime only, Git-ignore: `~/.hermes/local-patches/logs/reconcile.jsonl`
  - 结构化、脱敏、追加日志。

### Hermes 主仓库

- Modify: `hermes_cli/main.py`
  - 在 `_stash_local_changes_if_needed` / `_restore_stashed_changes` 附近增加显式 stash 结果类型。
  - 在 `_cmd_update_impl` 中增加 preflight、pending marker、同步 reconcile、fail-closed 顺序栅栏。
  - 收紧 `_desktop_macos_local_signing_identity`、`_desktop_macos_relaunchable_fixup` 及 Desktop build 失败语义。
- Modify: `hermes_cli/config.py`
  - 保留现有 `desktop.macos_signing_identity` schema/default；不把 patch queue 路径放进这里，避免 queue 入口本身依赖会被 reset 的配置 schema。
- Modify: `scripts/install.sh:install_desktop`
  - 构建前 reconcile；签名前判定 stable baseline/config；helper 不可用时不允许在已配置机器上 ad-hoc。
- Modify: `apps/desktop/package.json`
  - 把公开 `pack`、`dist`、`dist:mac*` 路由到受控 wrapper；Electron Builder 原始命令改为明显的内部脚本名。
- Create: `apps/desktop/scripts/controlled-package.mjs`
  - 受控 npm 打包；在 macOS 上调用 Python 签名 helper并验证；不打印签名环境变量值。
- Modify: `website/docs/user-guide/desktop.md`
  - 说明稳定身份、受支持打包入口和 fail-closed 行为；不展示本机身份值。
- Modify: `tests/hermes_cli/test_update_autostash.py`
  - stash tri-state 与 `cmd_update` 顺序/失败关闭。
- Create: `tests/hermes_cli/test_local_patch_reconcile.py`
  - 主仓库到外部 reconcile subprocess 的契约测试。
- Modify: `tests/hermes_cli/test_gui_command.py`
  - 签名 identity/baseline 和 update build fatality。
- Modify: `tests/test_install_sh_macos_signing_fallback.py`
  - installer 的配置存在、baseline 存在、helper 缺失矩阵。
- Create: `tests/desktop/test_controlled_package_scripts.py`
  - 静态与 subprocess 测试所有 npm 打包入口都受控。
- Preserve: `tests/hermes_cli/test_macos_persistent_signing.py`
  - 继续作为真实签名的可选集成测试。
- Preserve/extend: `tests/test_tui_gateway_server.py`
  - 模型切换组自己的回归测试，不与持久化框架耦合。

## 3. Manifest v1 数据格式

`manifest.json` 使用 UTF-8、末尾换行、排序稳定的 JSON。严格拒绝未知字段和重复 ID；所有路径必须是 queue root 或目标仓库内的相对 POSIX 路径，不允许绝对路径、`..`、符号链接逃逸。

### 严格 schema

| 对象 | 必需字段与类型 | 约束 |
| --- | --- | --- |
| root | `schema_version: integer`、`queue_id: string`、`target: object`、`required_group_ids: string[]`、`groups: object[]` | `schema_version == 1`；`queue_id == "hermes-local-patches"`；不允许额外字段 |
| target | `repository_name: string`、`required_remote_urls: string[]`、`allowed_update_branches: string[]` | 名称固定 `hermes-agent`；remote 固定官方 HTTPS/SSH 两种 URL；本版 branch 只允许 `main` |
| group | `id: string`、`order: integer`、`required: boolean`、`patches: object[]`、`required_checks: string[]` | ID 仅 `[a-z0-9-]+`；order 唯一；不允许额外字段 |
| patch | `id: string`、`order: integer`、`file: string`、`format: string`、`sha256: string`、`source_commits: string[]`、`affected_paths: string[]` | `format == "git-format-patch"`；SHA-256 匹配 `[0-9a-f]{64}`；source commit 匹配 `[0-9a-f]{40}`；不允许额外字段 |

### 必须生成的实际条目

| group / patch | order | file | source commits | affected paths / checks |
| --- | ---: | --- | --- | --- |
| `stable-signing/stable-signing-core` | 10 / 10 | `patches/stable-signing/0001-stable-signing-core.patch` | `41efdcc10ff7dc15e7201fbbd0c82e803bd7a338`、`284f3eeeb601c22aac2bc1940b1680ae7920b424`、`ee4fa0be574d076cd021532ee5aa1c74262f868d`、`c16c7622f263d9dcc209c7943a5a890f241ed5e4`、`61140d568c64df621d358590072271846b4e60e4`、`da13e3454935abd7b0936460980bd2b246597bc7` | `hermes_cli/config.py`、`hermes_cli/main.py`、`scripts/install.sh`、`tests/hermes_cli/test_gui_command.py`、`tests/hermes_cli/test_macos_persistent_signing.py`、`tests/hermes_cli/test_set_config_value.py`、`tests/test_install_sh_macos_signing_fallback.py`、`website/docs/user-guide/desktop.md` |
| `stable-signing/update-persistence-integration` | 10 / 20 | `patches/stable-signing/0002-update-persistence-integration.patch` | Task 3–5 的隔离实施 worktree 必须先产生一个经测试的 commit；导出工具读取该 commit 的完整 40 位 object ID 并立即写 manifest | package.json、controlled wrapper、update/reconcile/installer 测试以及 `main.py`、`install.sh`；checks 为 `python-syntax`、`update-fail-closed`、`signing-policy`、`npm-entrypoints` |
| `live-model-switch/live-model-switch-design` | 20 / 10 | `patches/live-model-switch/0001-live-model-switch-design.patch` | `126223a61c4fbf1738804c71646ab41c14778a08` | `docs/superpowers/specs/2026-07-26-live-model-switch-design.md` |
| `live-model-switch/live-model-switch-runtime` | 20 / 20 | `patches/live-model-switch/0002-live-model-switch-runtime.patch` | `7421b009d4a7fd400b1cba520e753bb33cfb2182`、`48cbe1a51db8347bb8474d1e6218c1ce767b8eee` | `tui_gateway/server.py`、`tests/test_tui_gateway_server.py`；checks 为 `model-switch-queue`、`model-switch-prompt-race` |

最终 manifest 的 `required_group_ids` 必须逐字为 `["stable-signing", "live-model-switch"]`。每个 patch 的 `sha256` 由导出后文件内容计算并写入；生成器若拿不到真实 64 位摘要或完整 40 位 source commit，必须拒绝写 manifest。其余不变量：

- `required_group_ids` 必须与 `groups[].required == true` 的 ID 集合完全相等。
- `order` 在同一层级唯一且严格递增。
- 每个 patch 的实际变更路径集合必须与 `affected_paths` 完全相等；多一个或少一个都拒绝。
- queue Git worktree 和 index 必须 clean，`HEAD` 必须存在；运行时 `state/`、`logs/` 由 `.gitignore` 排除。
- 每个 patch 文件 SHA-256 必须匹配 manifest。
- patch 内容若涉及 `.env`、`config.yaml`、`auth.json`、`*.p12`、`*.key`、`*.pem`、Keychain 导出或其他 credential 路径，验证直接失败。
- queue 只保存源码补丁和公开元数据，不保存当前应用证书、私钥或环境快照。

## 4. Reconcile 的幂等、事务与失败算法

### 公共命令边界

`bin/reconcile.py` 暴露以下稳定 CLI：

```text
python ~/.hermes/local-patches/bin/reconcile.py validate --repo ~/.hermes/hermes-agent --manifest ~/.hermes/local-patches/manifest.json --json
python ~/.hermes/local-patches/bin/reconcile.py apply --repo ~/.hermes/hermes-agent --manifest ~/.hermes/local-patches/manifest.json --operation-id 550e8400-e29b-41d4-a716-446655440000 --json
python ~/.hermes/local-patches/bin/reconcile.py verify --repo ~/.hermes/hermes-agent --manifest ~/.hermes/local-patches/manifest.json --json
python ~/.hermes/local-patches/bin/reconcile.py mark --stage prepared --operation-id 550e8400-e29b-41d4-a716-446655440000 --json
python ~/.hermes/local-patches/bin/reconcile.py recover --repo ~/.hermes/hermes-agent --manifest ~/.hermes/local-patches/manifest.json --json
```

退出码固定：

- `0`：完整、已应用且验证通过。
- `40`：queue/manifest 缺失、不干净、schema 非法或 checksum/路径集合不符。
- `41`：上游 stash restore 未完成；由 `cmd_update` 使用，reconcile 本身不吞掉。
- `42`：目标处于 partial/conflicted 状态，或 patch 无法在新 HEAD 上构造期望树。
- `43`：补丁已应用但 required checks 失败。
- `44`：稳定签名策略或签名身份验证失败。
- `45`：另一个 reconcile/update 持有锁；不等待超过 10 秒。

### 幂等计算

每次 `apply` 都执行同样的确定性步骤：

1. 用 `fcntl.flock` 独占 `state/reconcile.lock`；锁超时退出 `45`。
2. 验证 queue Git repo clean、manifest schema、required groups、文件哈希、路径 containment 和目标 remote/branch。
3. 记录目标 `HEAD`、queue `HEAD`、operation ID；不读取或记录环境变量值。
4. 用 `tempfile.mkdtemp()` 创建显式临时目录，并以参数数组执行 `git worktree add --detach TEMP_DIR TARGET_HEAD`；不得经 shell 拼接。
5. 在临时 worktree 按 `(group.order, patch.order)` 顺序以参数数组执行 `git apply --3way --index PATCH_FILE`；每完成一个 group 就记录该 group 开始/结束 tree 之间的 binary diff 和期望 blob/mode。
6. 任一 patch 失败即删除临时 worktree并退出 `42`；真实目标工作树尚未被写入。
7. 从临时 worktree计算：
   - 每个 group 的 `git diff --binary --full-index GROUP_START_TREE GROUP_END_TREE`；
   - queue 全部 group 的实际变更路径；
   - 每个 group 受管路径的期望 mode、blob SHA 和存在/删除状态。
8. 实际路径集合与 manifest 中所有 `affected_paths` 的并集不完全相等时退出 `40`。
9. Manifest 校验同时拒绝不同 group 共享同一个 `affected_path`。随后按 group 对真实目标的受管路径同时比较 index 与 worktree：
   - 该 group 全部路径等于临时期望树：状态为 `applied`；
   - 该 group 全部路径等于 `HEAD`：状态为 `missing`；
   - 其他任意组合：状态为 `partial`，退出 `42`，真实目标尚未被写入。
10. 把所有 `missing` group 的 binary diff 按 group order 拼成一个输入，对它先执行 `git apply --check --3way --index`，通过后只执行一次 `git apply --3way --index`；任一 group 无法预检时全部 missing groups 都不写入。
11. 再次逐路径核对 blob/mode。成功后仅对这些已知受管路径以参数数组执行 `git reset -- PATH_1 PATH_2`（参数列表按实际受管路径扩展），把本地补丁恢复为未提交、未暂存状态，便于下一次 autostash；queue 外的 staged/unstaged 文件不动。
12. 执行 `git diff --check`、Python syntax 和 manifest 中 required checks。检查失败时不 reset/clean 用户文件，保留已应用补丁与日志，退出 `43`，从而阻止构建。
13. 输出单行 JSON：`operation_id`、target/queue HEAD、每组 `applied|already_applied`、检查结果和退出码；人类日志仅打印 ID 与摘要。

这个算法的关键是先在临时 worktree 构造“新上游 HEAD + 完整 patch series”的期望树，再把所有缺失 group 合为一次真实写入。它避免“第一个 patch 已写入、第二个 patch 才发现冲突”的半应用状态，也能在 stash 已成功恢复全部补丁时稳定识别 `already_applied`。

### Pending marker

`state/pending-update.json` 的严格字段为：

| 字段 | 类型与约束 |
| --- | --- |
| `schema_version` | integer，必须为 `1` |
| `operation_id` | canonical UUID string |
| `stage` | `prepared`、`head-updated`、`reconciled`、`verified`、`complete` 之一 |
| `started_at` | UTC ISO-8601 string |
| `target_repo` | string，本机必须规范化为 `~/.hermes/hermes-agent` |
| `target_head_before` | 40 位小写 Git object ID |
| `target_head_after` | `null` 或 40 位小写 Git object ID |
| `queue_head` | 40 位小写 Git object ID |
| `stash_ref` | `null` 或 40 位小写 Git object ID |
| `required_group_ids` | 必须逐字为 `["stable-signing", "live-model-switch"]` |

- 使用同目录临时文件 + `os.replace` 原子更新。
- `prepared` 在任何 stash/pull/reset 之前写入。
- pull/reset 成功后改为 `head-updated`。
- reconcile 完成后改为 `reconciled`。
- required checks 完成后改为 `verified`。
- 全部 update 成功并重装 shim 后改为 `complete`，随后原子移动到脱敏日志归档；不能在中途静默删除。
- `stash_ref` 只记录 Git 对象 ID，不记录 stash 内容。

## 5. `cmd_update` 的精确控制流改造

### 接口

在 `hermes_cli/main.py` 的 stash helpers 附近定义：

```python
class StashRestoreStatus(str, Enum):
    RESTORED = "restored"
    SKIPPED = "skipped"
    CONFLICT = "conflict"
    FAILED = "failed"

@dataclass(frozen=True)
class StashRestoreResult:
    status: StashRestoreStatus
    stash_ref: str
    conflicted_paths: tuple[str, ...] = ()

@dataclass(frozen=True)
class LocalPatchReconcileResult:
    returncode: int
    operation_id: str
    target_head: str
    queue_head: str
    group_states: Mapping[str, str]
```

`_local_patch_queue_root() -> Path` 必须只返回 `get_hermes_home() / "local-patches"`。`_run_local_patch_reconcile(repo: Path, *, mode: Literal["validate", "apply", "verify", "recover"], operation_id: str) -> LocalPatchReconcileResult` 必须用参数数组执行外部工具、要求单行 JSON，并把非 JSON、超时或 schema 不符映射为 returncode `40`。

`_restore_stashed_changes` 改为返回 `StashRestoreResult`，不再用 `False` 混淆“用户跳过”和“冲突”。现有冲突时 reset 回 clean `HEAD`、保留 stash 的安全行为继续保留。

### 更新顺序

`_cmd_update_impl` 的新顺序必须固定为：

1. 现有 managed/docker/nix、并发进程和 venv holder guard。
2. 外部 queue `validate`；失败退出 `40`，尚未改 Git。
3. 写 `pending-update.json: prepared`。
4. 现有 pre-update backup。
5. 现有 lockfile churn 处理、fetch、branch 解析。
6. stash 当前工作树并把 stash ref 写入 pending marker。
7. pull 或 divergent history 的 reset；成功后 marker=`head-updated`。
8. 尝试 restore stash，并保存显式 `StashRestoreResult`。
9. **无论 stash restore 是成功、跳过还是冲突，都同步运行外部 `apply`**：
   - 成功 restore：通常返回 `already_applied`；
   - 冲突后 clean HEAD：从 queue 重建两组受管补丁；
   - 这样 updater 集成补丁会先回到磁盘。
10. reconcile 失败：退出其 `40/42/43`；不得执行 bytecode 清理、依赖刷新、web build 或 Desktop build。
11. reconcile 成功但 stash result 不是 `RESTORED`：退出 `41`；受管补丁已恢复，queue 外改动仍在原 stash 中，绝不继续构建。
12. marker=`reconciled`，运行快速 required checks；失败退出 `43`。
13. marker=`verified`，才允许现有 Python/Node dependency refresh、web build 和 Desktop build。
14. 如果稳定签名 baseline/config 表示 strict 模式，`desktop --build-only` 的最终失败从当前 non-fatal 提升为 `44`；不能打印“Code updated!”后让 installer 使用旧或错误身份产物。
15. 所有后续 sync/migration 完成后，重新原子安装并验证 `venv/bin/hermes` shim；这是必要步骤，因为 pip editable install 可能重写 console script。
16. marker=`complete`，最后打印成功。

### “Already up to date”路径

当前 `commit_count == 0` 分支也必须执行同一 restore → reconcile → stash 状态判定：

- 不能因为没有上游 commit 就跳过补丁完整性；
- queue 缺组或目标 partial 时仍失败；
- reconcile 与 stash 完整后才允许 venv repair；
- 这条路径是 crash 后第二次运行自动自愈的关键。

### `updates.non_interactive_local_changes=discard`

- queue 是独立、显式必需的本地策略，不能被 `discard` 丢弃。
- `discard` 仍可丢弃 queue 外的临时本地改动，但随后必须从 queue 应用两个 required groups。
- stash drop 失败必须退出非零；不能在“用户要求 discard 但实际 stash 仍未知”时构建。
- 文档明确：该配置不关闭 local patch queue。

## 6. 鸡生蛋问题的双锚点解法

仅在 `main.py` 中实现 reconcile 仍有一个崩溃窗口：Git reset 已完成，但 Python 进程在调用 reconcile 前被杀死；下一次从磁盘导入的是未打补丁的上游 `main.py`。

本方案用两个互补锚点封闭该窗口：

1. **当前进程锚点：** `cmd_update` 在 reset 前已经加载自己的函数对象，reset 不会改正在运行的 Python frame；正常进程会继续调用仓库外 `reconcile.py`。
2. **下次启动锚点：** 把 `venv/bin/hermes` 安装为极薄的外部 shim。Desktop updater 的 `resolve_hermes` 已固定优先调用该文件；Git reset 不会触及 ignored venv。shim 在任何 `update` 前都执行：

```text
validate queue
if pending marker is non-complete OR target is not fully applied:
    reconcile.py recover/apply
if recovery succeeds:
    exec venv/bin/python -m hermes_cli.main update --yes --gateway --force --branch main
else:
    exit nonzero without importing reset 后的 main.py
```

shim 不常驻、不轮询、不修改应用、不请求 macOS 权限。即使 pip 在依赖刷新阶段重写 shim，此时仓库补丁已经完成 reconcile；成功路径末尾再安装 shim。由此得到完整窗口覆盖：

| 异常点 | 下次恢复依据 |
| --- | --- |
| reset 前 | 原工作树/原 shim/queue 均在 |
| reset 后、reconcile 前 | ignored venv shim + pending marker + 外部 queue |
| reconcile 后、依赖刷新前 | 仓库补丁已恢复 + shim |
| pip 重写 shim 后 | 仓库内 patched `cmd_update` 已恢复 |
| 成功结束 | 仓库补丁 + 重新安装的 shim + complete marker |

shim 安装必须：

- 先验证目标确实是规范化后的 `~/.hermes/hermes-agent/venv/bin/hermes`，拒绝符号链接逃逸；
- 写同目录临时文件、`fsync`、`chmod 0755`、`os.replace`；
- 在文件内嵌 queue tool SHA-256 和 schema version，`verify` 时比对；
- 不依赖原 console script 备份，直接使用同 venv 的 Python `-m hermes_cli.main`，避免递归；
- 保留 `argv` 和进程退出码，不输出环境值；
- 提供 `HERMES_LOCAL_PATCH_SHIM_BYPASS=1` 仅供测试/人工诊断，普通 updater 不设置。

## 7. 稳定签名策略与 installer fail-closed

### 签名策略接口

把 `hermes_cli/main.py` 的签名逻辑收敛为：

```python
@dataclass(frozen=True)
class MacOSSigningPolicy:
    mode: Literal["publisher", "stable-local", "adhoc-first-install"]
    identity: str | None
    baseline_required: bool

```

`_desktop_macos_signing_policy() -> MacOSSigningPolicy` 按本节优先级返回不可变策略或抛出明确配置错误。`_verify_desktop_macos_identity(app: Path, policy: MacOSSigningPolicy) -> bool` 必须完成 strict signature、Bundle ID、叶证书 fingerprint 和 DR 摘要四项验证后才返回 `True`。

规则按优先级：

1. `CSC_LINK` 或 `APPLE_SIGNING_IDENTITY` 的**存在性**表示 publisher 路径；只传布尔决策，不记录/打印值。
2. `state/signature-baseline.json` 存在时必须是 `stable-local`；config 中 identity 缺失、不唯一或不可用均失败，不得 ad-hoc。
3. config 有非空 `desktop.macos_signing_identity` 时是 `stable-local`。
4. 只有 baseline 不存在、config 文件不存在或明确 identity 为空的真正首次安装，才允许 `adhoc-first-install`。
5. config 读取错误不是“空配置”，必须失败。

`signature-baseline.json` 只保存公开身份摘要，严格字段为：

| 字段 | 类型与约束 |
| --- | --- |
| `schema_version` | integer，必须为 `1` |
| `bundle_id` | string，必须为 `com.nousresearch.hermes` |
| `certificate_sha1` | 40 位大写十六进制公开证书 fingerprint |
| `designated_requirement_sha256` | 64 位小写十六进制，来自规范化 DR 文本 |
| `created_at` | UTC ISO-8601 string |

- 首次建立 stable-local 签名后写一次；后续更新只能验证，不能自动改写。
- 如需更换证书，必须使用单独、显式的 re-enroll 流程；不属于 update。
- 任何日志只写“configured identity matched/mismatched”，不回显 identity。

### `_desktop_macos_relaunchable_fixup`

- stable-local 签名前解析 identity，若名称匹配多个 Keychain identity 则拒绝；推荐并测试 40 位 fingerprint。
- 用参数数组调用 `codesign --force --deep --sign RESOLVED_IDENTITY --timestamp=none --preserve-metadata=entitlements,flags,runtime APP_PATH`；命令日志不得包含 `RESOLVED_IDENTITY`。
- 随后必须：
  - `codesign --verify --deep --strict`；
  - 验证 Bundle ID；
  - 提取叶证书到临时目录并用 Python `hashlib.sha1` 比对配置/baseline；
  - 规范化 `codesign -dr -` 输出并比对 DR SHA-256。
- 任一步失败返回 `False`；不得再试 `--sign -`。

### `scripts/install.sh:install_desktop`

在 pack 前先调用 queue `verify/apply`。签名 fallback 改为精确矩阵：

| 条件 | 行为 |
| --- | --- |
| publisher env 存在 | 沿用 publisher 流程，不回显值 |
| venv Python/helper 可用 | 调统一 signing policy/fixup；失败即 installer 非零 |
| helper 不可用且 baseline 存在 | 非零；禁止 ad-hoc |
| helper 不可用且 `config.yaml` 存在 | 保守非零；无法证明 identity 为空，禁止 ad-hoc |
| helper 不可用、baseline/config 都不存在 | 仅首次安装允许现有 ad-hoc + strict verify |

这比“尝试用 shell 解析 YAML”更可靠：helper 缺失时宁可停止，也不把解析不确定性转成身份降级。

## 8. 直接 npm 打包旁路的最小受控处理

`apps/desktop/package.json`：

- 公开 `pack`、`dist`、`dist:mac`、`dist:mac:dmg`、`dist:mac:zip` 分别调用 `node scripts/controlled-package.mjs dir`、`all`、`mac`、`mac-dmg`、`mac-zip`。
- 原 Electron Builder 命令移到 `builder:internal`；名字和文档注明只允许 wrapper/CLI 设置随机 operation token 后调用。
- `cmd_gui` 不再执行公开 `npm run pack`，而调用 `controlled-package.mjs dir --caller hermes-cli`，避免递归。

`controlled-package.mjs`：

1. 先构建前端。
2. macOS 且没有 publisher env 时设置 `CSC_IDENTITY_AUTO_DISCOVERY=false`，只检查 env key，不打印值。
3. 调内部 builder。
4. 构建成功后定位 repo venv Python，调用统一 Python signing policy/fixup。
5. helper 缺失且 baseline 或 config 存在时退出 `44`；不 ad-hoc。
6. helper 返回成功后再验证 app 存在和 strict signature。
7. 非 macOS 保持现有 builder 行为。

无法阻止用户手工执行 `npx electron-builder`，但要做到：

- 所有仓库声明的 npm 打包脚本均被 wrapper 覆盖；
- `builder:internal` 缺少 wrapper 生成的短生命周期环境 token 时直接拒绝；
- 文档明确裸 `npx electron-builder` 是不受支持入口；
- 静态测试枚举 `package.json` 中所有含 `electron-builder`/`builder` 的脚本，保证只有内部脚本可直接触达；
- `npm run pack` 的 subprocess 测试证明 helper 失败时不产生成功退出。

这满足“明确阻断/包装 + 可自动验证”的最小范围，而不试图拦截用户在仓库外任意执行二进制。

## 9. 测试矩阵

### Queue/manifest

| 场景 | 期望 |
| --- | --- |
| queue repo clean、两组齐全、哈希正确 | validate 0 |
| 缺 `live-model-switch` | 40，目标零写入 |
| queue 有未提交 manifest/patch 改动 | 40 |
| patch SHA-256 不符 | 40 |
| patch 路径包含 `..`/绝对路径/符号链接逃逸 | 40 |
| patch 触及 credential denylist | 40 |
| manifest 声明路径与 patch 实际路径不同 | 40 |
| 两组均已应用 | apply 0，目标 diff 前后字节一致 |
| 两组均缺失 | apply 0，组合补丁一次写入 |
| 一组已应用、一组缺失 | 允许按完整组状态补齐缺组；最终两组完整 |
| 单个组内部分应用/受管文件被额外编辑 | 42，不覆盖 |
| 新上游导致 three-way 冲突 | 42，真实目标零写入 |
| required check 失败 | 43，不进入 build |
| 并发 reconcile | 第二个 45 |

为支持“一组已应用、一组缺失”，临时期望树仍按完整 series 生成，但真实目标按 group 的受管路径分别判定；同一路径不得跨 group。Manifest 校验必须拒绝两个 group 共享 `affected_paths`，从而保持组级原子性。稳定签名组内部两个 patch 可共享路径，因此它作为一个原子 group 一起 applied/missing 判定。

### Stash/update 顺序

| stash 状态 | reconcile | 期望 |
| --- | --- | --- |
| 无 stash | 成功 | 继续依赖刷新 |
| restore 成功 | already applied | 继续 |
| restore 冲突 | queue apply 成功 | 受管补丁恢复，但 cmd_update 退出 41；依赖/web/Desktop 均未调用 |
| 用户选择不 restore | queue apply 成功 | 退出 41，stash 保留 |
| stash ref 无法解析/drop 失败 | 任意 | 非零，不构建 |
| restore 成功 | queue 缺组/哈希错 | 40，不构建 |
| restore 成功 | patch 冲突 | 42，不构建 |
| `commit_count == 0` 且目标 missing | queue 补齐，再允许 venv repair |
| divergent `reset --hard` | queue 补齐后才继续 |
| updater 在 reset 后被 kill | 下一次 shim 读 pending marker 并 recover |
| pip 重写 shim | 更新末尾原子重装；校验通过后 complete |

断言方式：mock `_install_python_dependencies_with_optional_fallback`、`_update_node_dependencies`、`_build_web_ui`、`_run_logged_subprocess`，在所有 40–45 失败场景下 `assert_not_called()`。

### 稳定签名

| 场景 | 期望 |
| --- | --- |
| configured fingerprint 可用 | certificate/DR/bundle ID 验证通过 |
| config 读取失败 | 44，不调用 `codesign --sign -` |
| stable baseline 存在但 config identity 为空 | 44 |
| identity 名称匹配多个证书 | 44 |
| `codesign` stable identity 失败 | 44，无 ad-hoc retry |
| strict verify 失败 | 44 |
| 叶证书 fingerprint 与 baseline 不同 | 44 |
| DR hash 与 baseline 不同 | 44 |
| publisher env 存在 | 不触碰 publisher 签名，不打印 env 值 |
| 真正首次安装且无 config/baseline/helper | 可 ad-hoc，但 strict verify 失败仍非零 |
| installer helper 缺失且 config 存在 | 非零，codesign 未调用 |
| Desktop build 在 strict 模式失败 | `cmd_update` 非零，installer 不替换应用 |

真实 macOS 集成测试只接受 `HERMES_TEST_CODESIGN_IDENTITY` 作为进程环境输入，不打印值，不写 fixture；测试结束删除临时 app/certificate extraction。

### npm 与模型切换

- 静态枚举 `pack`、`dist*` 全部经过 `controlled-package.mjs`。
- `builder:internal` 无 token 失败，有 token 才执行 fake builder。
- macOS helper/baseline/config 失败矩阵与 installer 相同。
- 模型组必须运行以下行为测试：
  - active turn 中 `/model` 只更新 `pending_model_switch`，不修改 live agent；
  - 多次选择 latest-wins；
  - idle model switch 应用期间 prompt 进入 queue；
  - model switch finally 清除 `model_switch_applying` 并 drain queued prompt；
  - notification/goal follow-up 在 switch 期间不抢占。

## 10. 初次安装/迁移流程

这是唯一允许把现有分散状态收敛为 queue 的流程，必须在用户确认维护窗口后执行：

1. 只读记录主工作树、两个 worktree、相关分支、stash 和源 commit 的状态。
2. 先在仓库外建立 queue Git repo 与 reconcile 测试；此时不碰主仓库。
3. 从精确 source commits 导出：
   - stable-signing：只取 `41efdcc10f..da13e34549` 的 6 个业务提交，不含 `953707103f`；
   - live-model-switch design：`126223a61c`；
   - live-model-switch runtime：`7421b009d4`、`48cbe1a51d`；
   - 明确排除 worktree 的 `package-lock.json` churn。
4. 在新的 clean、detached 临时 worktree（基于当时 `origin/main`）应用两组，再实现 update-persistence integration；运行完整测试，导出最终组 patch。
5. 生成真实 manifest 哈希/路径集合，运行 queue 自测，提交 queue Git repo。
6. 在 queue 内再保存一份主工作树当前 diff 的带时间戳 rescue patch，只用于迁移审计，不加入 manifest；校验 SHA-256 并提交。
7. 为主工作树创建显式命名 safety stash，确认其对象可解析。因为下一步会清理受管路径，这是实施中唯一需要用户明确批准的破坏性边界。
8. 把主工作树恢复到 clean `origin/main`，但不清理 ignored `venv`、node_modules 或应用。
9. 运行外部 reconcile 一次性应用两个 group；验证结果与临时期望树完全一致。
10. 原子安装 `venv/bin/hermes` shim，验证：
    - `hermes --version` 能透传；
    - `hermes update --check` 不改仓库；
    - fake pending marker 会先触发 recover。
11. 读取当前 `/Applications/Hermes.app` 的公开 Bundle ID、叶证书 fingerprint 和规范化 DR，建立 `signature-baseline.json`；不得导出证书私钥。
12. 运行受控 Desktop rebuild，验证 release app 的 fingerprint/DR 与 baseline 一致后，才允许替换/启动应用。
13. safety stash 保留到至少一次完整后续更新演练成功；清理必须另行明确批准。

若第 7 步的 safety stash 无法创建，或第 9 步发现 partial 状态，立即停止；不得用 reset/clean 猜测恢复。

## 11. 后续普通更新流程

### 终端 `hermes update`

1. ignored venv shim 先 validate/recover queue。
2. patched `cmd_update` 再做 queue validate，写 pending marker。
3. stash → pull/reset → restore。
4. 外部同步 reconcile 两组。
5. stash 非完整或 queue 非完整则 40–43 退出。
6. checks 通过后刷新依赖、web 和 Desktop。
7. stable identity 验证通过后重装 shim、complete marker、成功退出。

### Desktop Update

1. `/Users/yangqi/.hermes/hermes-setup` 按现有 `resolve_hermes` 调 `venv/bin/hermes`；不需要修改或重签 Hermes.app。
2. shim 先 recover，再透传 updater 给出的 `hermes update --yes --gateway --force --branch main`；如果 updater 指定另一个分支，manifest 的 `allowed_update_branches` 会先拒绝。
3. 非零退出被现有 updater 当作 update stage 失败，不进入独立 `desktop --build-only` 和应用替换。
4. update 成功后 updater 再调用 `hermes desktop --build-only`；同一 signing policy 再验证 release app。
5. 复制应用后保留签名；建议在 updater 后续增强中增加对 target app 的同一只读 identity 验证，但不能把该增强当成 queue/build 前 fail-closed 的替代。

### Installer repair / `--include-desktop`

1. queue 存在时先 validate/reconcile。
2. build 使用受控 npm 入口。
3. stable config/baseline 存在时 helper 不可用即失败。
4. 只有真正首次安装才允许 ad-hoc fallback。
5. 严格验证成功后才安装 app。

## 12. 实施任务拆分

### Task 1: Materialize and validate the external queue

**Files:**
- Create all `~/.hermes/local-patches` source, patch, test and documentation files listed in section 2.

**Interfaces:**
- Produces: manifest v1; `reconcile.py validate/apply/verify/recover`; exit codes 0/40/42/43/45.

- [ ] 写 manifest/reconcile 的失败测试，覆盖 schema、hash、path、required groups、partial 和 conflict。
- [ ] 在临时 Git 仓库运行测试，确认尚无实现时失败。
- [ ] 实现严格 manifest loader、queue clean check、临时 worktree expected-tree 算法和结构化日志。
- [ ] 运行 queue 测试并确认全部通过。
- [ ] 从精确 source commits 生成两组 patch，生成真实哈希和路径集合，不包含 lockfile churn 或 credential 文件。
- [ ] 在 clean `origin/main` 临时 worktree验证两组可顺序应用。
- [ ] 提交独立 queue Git repo；不提交主仓库。

### Task 2: Add the reset-proof on-demand shim

**Files:**
- Create: `~/.hermes/local-patches/bin/install-hermes-shim.py`
- Create: `~/.hermes/local-patches/bin/hermes-shim`
- Test: `~/.hermes/local-patches/tests/test_install_hermes_shim.py`

**Interfaces:**
- Consumes: `reconcile.py recover`.
- Produces: reset 外 `venv/bin/hermes` 恢复入口。

- [ ] 写失败测试：reset 后 pending marker、queue conflict、argv/exit code 透传、pip 覆盖后重装。
- [ ] 验证测试先失败。
- [ ] 实现原子 shim 安装、SHA/schema 自校验和 `python -m hermes_cli.main` exec。
- [ ] 运行测试，确认 reset→kill→next update 的真实临时 repo 演练通过。
- [ ] 提交 queue repo 的 shim 变更。

### Task 3: Make `cmd_update` explicitly fail closed

**Files:**
- Modify: `hermes_cli/main.py`
- Modify: `tests/hermes_cli/test_update_autostash.py`
- Create: `tests/hermes_cli/test_local_patch_reconcile.py`

**Interfaces:**
- Consumes: external reconcile CLI and manifest v1.
- Produces: stash tri-state、pending marker stages、build 前同步栅栏。

- [ ] 写 stash `RESTORED/SKIPPED/CONFLICT/FAILED` 单元测试。
- [ ] 写 `cmd_update` 调用顺序与 40–43 时 dependency/web/Desktop `assert_not_called` 测试。
- [ ] 写 `commit_count == 0` 和 divergent reset 的恢复测试。
- [ ] 运行测试确认失败。
- [ ] 实现最小 result types、subprocess adapter 和顺序改造。
- [ ] 运行目标测试，再运行现有 `test_cmd_update.py`、`test_update_yes_flag.py`、gateway update tests。
- [ ] 在隔离实现 worktree提交，导出到 stable-signing group 的 persistence patch。

### Task 4: Seal signing and installer fallbacks

**Files:**
- Modify: `hermes_cli/main.py`
- Modify: `scripts/install.sh`
- Modify: `tests/hermes_cli/test_gui_command.py`
- Modify: `tests/hermes_cli/test_macos_persistent_signing.py`
- Modify: `tests/test_install_sh_macos_signing_fallback.py`

**Interfaces:**
- Produces: `MacOSSigningPolicy`、baseline verification、installer strict matrix、exit 44。

- [ ] 写 baseline/config/helper/publisher 的完整失败测试。
- [ ] 写 certificate fingerprint、Bundle ID、DR hash mismatch 测试。
- [ ] 运行测试确认当前 fallback 场景失败。
- [ ] 实现统一 policy/fixup，不回显 identity/env 值。
- [ ] 把 strict 模式 Desktop build failure 提升为 fatal。
- [ ] 运行 mock tests 和可选真实 macOS codesign test。
- [ ] 更新 stable-signing group patch 与 SHA/路径集合。

### Task 5: Wrap all npm packaging entrypoints

**Files:**
- Modify: `apps/desktop/package.json`
- Create: `apps/desktop/scripts/controlled-package.mjs`
- Create: `tests/desktop/test_controlled_package_scripts.py`

**Interfaces:**
- Consumes: venv Python signing policy/fixup。
- Produces: 公开 npm pack/dist 的受控入口和内部 token gate。

- [ ] 写 package.json 静态枚举和 fake builder/helper subprocess 测试。
- [ ] 运行测试确认直接入口尚未受控。
- [ ] 实现 wrapper、内部 token 和 cmd_gui 调用调整。
- [ ] 运行 Node/pytest 目标测试。
- [ ] 更新 patch manifest checksum。

### Task 6: End-to-end migration rehearsal

**Files:**
- No new production files; update queue README/manifest only if rehearsal reveals contract mismatch.

**Interfaces:**
- Validates: two anchors、two groups、stash failure semantics、stable identity。

- [ ] 在 disposable clone 演练 clean fast-forward。
- [ ] 演练 divergent reset。
- [ ] 演练 stash conflict，确认 queue 恢复但更新退出 41 且 build 未运行。
- [ ] 在 reset 后、reconcile 前 kill，确认 shim 下一次自动 recover。
- [ ] 模拟 pip 覆盖 shim，确认成功结尾重装。
- [ ] 在 macOS disposable app 上连续两次不同二进制 rebuild，确认 CDHash 可变但 DR/fingerprint/bundle ID 不变。
- [ ] 执行完整目标测试矩阵并保存脱敏结果。
- [ ] 只有全部通过后，按第 10 节迁移真实主工作树；不提交主仓库。

## 13. 完成门槛

只有同时满足以下条件才可声明实施完成：

- queue 独立 Git repo clean 且有两个 required groups；
- 设计提交、模型两个实现提交和稳定签名实现都有 queue 内可校验 patch；
- 主工作树上的最终受管 diff 与临时期望树逐 blob/mode 一致；
- stash conflict、queue 缺失/冲突、签名失败均在依赖/web/Desktop 之前非零；
- Desktop updater 通过 `venv/bin/hermes` shim 覆盖 reset 后崩溃窗口；
- installer 和所有声明的 npm pack/dist 入口在 stable 模式下没有 ad-hoc fallback；
- 两次真实 rebuild 的 DR/fingerprint/bundle ID 稳定；
- `package-lock.json` churn 不在 queue；
- 没有任何密钥、token、私钥材料或环境值进入 manifest、patch、日志或测试输出；
- 主仓库未提交本地定制到 `main`，也未删除迁移 safety stash。

## 14. 未决风险

1. 裸 `npx electron-builder` 无法在操作系统层面禁止；本计划封住仓库声明的 npm 脚本并把裸调用定义为不受支持。若要求绝对禁止，需要额外的执行环境/文件权限策略，超出本方案范围。
2. `venv/bin/hermes` 不是上游承诺的扩展点，pip 可能重写；双锚点和更新末尾重装覆盖已知窗口，但上游若改变 Desktop updater 的 `resolve_hermes` 路径，需要同步更新 shim 策略。
3. 上游若同时修改稳定签名或 gateway model-switch 的受管路径，reconcile 会按设计失败关闭，需要人工 rebase queue；这是保护机制，不应改成静默覆盖。
4. 当前 TCC 数据库仍不可只读核实，签名身份稳定只能证明 DR/证书/Bundle ID 没变，不能证明 macOS 中每一项授权当前都是 allow。
5. 最终 `/Applications/Hermes.app` 的复制后验证目前应作为 updater 增强；在此之前依赖 release app 签名验证和保签名复制。若要求最强端到端保证，应在可读的 bootstrap updater Rust 源码中增加复制后同一 identity verifier，并重新构建外部 updater。
6. 首次把现有 dirty 主工作树迁移为完整 queue 需要一次显式、可回滚的 clean-base 切换；计划已经要求 rescue patch、safety stash 和用户批准，实施时不得省略。
