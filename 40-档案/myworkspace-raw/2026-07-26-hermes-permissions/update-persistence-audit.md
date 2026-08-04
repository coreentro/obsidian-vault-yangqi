# Hermes 更新与权限持久性审计

- 审计时间：2026-07-26T19:35:15+08:00
- 范围：`/Users/yangqi/.hermes/hermes-agent`、`/Applications/Hermes.app`、`/Applications/CuaDriver.app`、`/Users/yangqi/.hermes/config.yaml`，以及可只读访问的 TCC 元数据。
- 方法：只读检查 Git 状态/reflog/源码/更新器二进制字符串、`codesign`、`security`、TCC 数据库访问状态和日志。**没有执行更新、签名、TCC 写入、权限更改或删除操作。**
- 说明：本文不记录 API key、令牌或其他凭据；下列签名指纹是公开代码签名标识，不是密钥。

## 结论摘要

1. Hermes Desktop 当前配置了持久的本地证书签名身份，且它与 `/Applications/Hermes.app` 当前的 Designated Requirement（DR）完全匹配。若今后的本地重建路径始终使用该身份，Hermes 自身按签名身份绑定的 TCC 授权应保持稳定。
2. 本次“设计规格消失”不是普通远端快进造成的：reflog 显示本地提交 `126223a61c` 之后，主分支被 `reset` 到 `origin/main`。更新器对**未提交**变更会 stash/restore；对**本地提交**不会 stash，因此在分叉时 `reset --hard origin/main` 使提交从 `main` 可达历史消失。该对象目前仍可由 reflog 读取，但没有分支保护它。
3. 本地签名补丁尚未丢失：主工作树保留未提交变更，同时独立工作树/分支 `codex/hermes-stable-signing-2026-07-26` 持有 6 个提交。其保护强度高于只有 reflog 的设计规格，但它不会被主更新器自动合并回 `main`。
4. Desktop 的“计算机使用”界面明确说明：**辅助功能和屏幕录制授权属于 CuaDriver (`com.trycua.driver`)，不属于 Hermes**。当前 CuaDriver 使用 Apple Developer ID、固定 Team ID 和稳定 DR；这两项权限的稳定性主要取决于 CuaDriver 的身份，而不是 Hermes 的本地自签名证书。
5. 本机 TCC SQLite 数据库受 macOS 隐私保护，当前审计进程无法读取授权行（`authorization denied`）。因此不能把“身份稳定”误报为“已确认全部授权仍为允许”；实际授权状态需要在系统设置或应用自己的只读状态页复核。

## 1. 当前配置与更新策略

`/Users/yangqi/.hermes/config.yaml` 的相关有效值：

| 键 | 当前值 | 含义 |
| --- | --- | --- |
| `desktop.macos_signing_identity` | `3883384CCE1ED88EF4B41E1475BE63B768F2F65D` | 本地 macOS 重建应使用的证书 SHA-1 指纹；不是私钥。 |
| `updates.pre_update_backup` | `false` | 不生成更新前 Hermes 状态备份。此项不保护 Git 本地提交。 |
| `updates.backup_keep` | `5` | 全量备份保留数；因前项关闭，通常不生效。 |
| `updates.non_interactive_local_changes` | `stash` | 无交互更新时保留未提交的受跟踪和未跟踪文件；不是 `discard`。 |

未发现 `desktop.update_strategy` 配置项。当前 TypeScript 类型只定义桌面调用可传 `abort | stash | force` 的临时 dirty strategy（`apps/desktop/src/global.d.ts:332`），它不是此 `config.yaml` 中的持久设置。实际 CLI 默认策略由 `updates.non_interactive_local_changes: stash` 控制。

源代码的默认值也为 `updates.pre_update_backup: quick`、`backup_keep: 5`、`non_interactive_local_changes: stash`（`hermes_cli/config.py:3360-3381`）；本机显式把前者改为 `false`。

## 2. 更新器如何处理本地状态，以及本次提交为何消失

### 行为矩阵

| 本地状态 | 代码路径 | 正常更新后的结果 | 关键限制 |
| --- | --- | --- | --- |
| 已跟踪但未提交的修改 | `git status --porcelain` 后 `git stash push --include-untracked`（`hermes_cli/main.py:7578-7675`） | 成功更新后 `git stash apply`，再尝试 drop stash（`7740-7857`） | 与上游冲突时更新器会把工作树 reset 回新 HEAD，并保留 stash 供人工恢复（`7794-7824`）。 |
| 未跟踪且非 ignored 文件 | 同上，`--include-untracked` | 与未提交修改一起 stash/restore | 如果同名文件或补丁上下文冲突，也可能不能自动恢复。 |
| ignored 文件（例如 `node_modules`、venv、构建产物） | `git stash --include-untracked` 不含 `--all` | 不会被 stash、restore 或通常更新路径删除 | 代码明确说明 ignored 路径不被此机制触碰（`7867-7874`）；它们也不构成补丁保护。 |
| 本地提交（在 `main` 上 ahead） | 不属于工作树脏状态，不会被 stash | 快进不可能时可能直接丢失 `main` 的可达性 | `git pull --ff-only` 失败后执行 `git reset --hard origin/<branch>`（`11703-11721`）。 |
| 无交互且显式配置为 `discard` | stash 后丢弃 stash | 本地未提交补丁被主动丢弃 | 本机当前不是该值；该路径见 `11782-11790`。 |

更新代码在成功后会 restore autostash（`11772-11798`）。这解释了为何当前主工作树内的签名补丁仍在，而已提交的设计文档不在：两者处在 Git 的不同状态层级。

### 本次事件的直接证据

- 19:04:44 创建本地提交：`126223a61c4fbf1738804c71646ab41c14778a08`，主题为 `docs: design deferred live model switching`，唯一文件是 `docs/superpowers/specs/2026-07-26-live-model-switch-design.md`。
- 19:26:28 reflog 记录：`reset: moving to origin/main`；当前 `main` 和 `origin/main` 都在 `eb52760564`，没有 ahead/behind。
- `126223a61c` 不被任何分支或标签包含；它不是 `origin/main` 的祖先。因此它目前只靠 reflog/未过期对象保留，**不可视为持久备份**。
- 当前存在一条更新 autostash：`stash@{0}`，说明更新器确实处理过工作树层的本地修改。

`/Users/yangqi/.hermes/hermes-setup` 是编译的 arm64 更新器，而非可审阅的 shell 脚本；它正在/曾以 `--update --branch main --target-app /Applications/Hermes.app` 运行。其嵌入字符串确认它委托 `hermes update`、等待 Hermes 退出并处理 quarantine；主仓库 reflog和 `hermes_cli/main.py` 则提供了本次 reset 的可核验证据。

## 3. 当前 Hermes.app 的签名、DR 与有效期

当前 `/Applications/Hermes.app`：

| 项目 | 观测值 | 审计判断 |
| --- | --- | --- |
| Bundle ID / 版本 | `com.nousresearch.hermes` / `0.17.0` | 稳定的应用标识。 |
| 签发者 | `Hermes Local Code Signing` | 本机自签名本地证书。 |
| 证书指纹 | SHA-1 `3883384CCE1ED88EF4B41E1475BE63B768F2F65D` | 与配置值逐字一致。 |
| DR | `identifier "com.nousresearch.hermes" and certificate leaf = H"3883384cce1ed88ef4b41e1475be63b768f2f65d"` | 只要 Bundle ID 与叶证书不变，DR 稳定。 |
| 有效期 | 2026-07-26 09:38:16 UTC 至 2046-07-21 09:38:16 UTC | 当前证书还有约 20 年；短期内到期不是重询问风险。 |
| 签名时间 / 校验 | 2026-07-26 18:11:16 本地时间；`codesign --verify --deep --strict` 通过 | 当前 bundle 与其 DR 一致、磁盘签名有效。 |
| Team ID / Gatekeeper | 无 Team ID；`spctl --assess` 为 `rejected` | 这是自签名应用的 Gatekeeper 分发风险，不等同于 TCC 拒绝；不要把它误解为“签名不稳定”。 |

稳定性的前提是：私钥与该证书仍在登录钥匙串内、`desktop.macos_signing_identity` 保持上述指纹、构建后确实执行了配置感知的重签名。若证书被重建、私钥丢失、Bundle ID 改变，或 `CSC_LINK`/`APPLE_SIGNING_IDENTITY` 使发布者签名路径接管，DR 可能改变，相关 TCC 授权可能再次询问。

## 4. TCC：已能确定的身份边界与仍不能保证的部分

### CuaDriver（屏幕录制、辅助功能）

仓库的桌面设置代码明确写明 macOS 的两项 TCC 授权“attach to cua-driver's own `com.trycua.driver` identity — not Hermes”（`apps/desktop/src/app/settings/computer-use-panel.tsx:53-58`）：

| 应用 | 当前身份 | 与权限的关系 | 稳定性 |
| --- | --- | --- | --- |
| Hermes | `com.nousresearch.hermes` + 上述本地叶证书 DR | 可能请求自身的文件/自动化等权限；不承载 CuaDriver 的录屏和辅助功能 | 取决于本地证书/Bundle ID 不变。 |
| CuaDriver 0.12.6 | `com.trycua.driver`，Developer ID `Cua AI, Inc. (YCK386LBJ7)` | 屏幕录制和辅助功能的请求者 | DR 绑定 Apple Developer ID 链、Bundle ID 和 Team ID `YCK386LBJ7`；校验通过且有 stapled notarization，跨正常证书续期通常比本地自签名更稳定。 |

CuaDriver 的当前 DR 为 `identifier "com.trycua.driver" ... certificate leaf[subject.OU] = YCK386LBJ7`，`codesign --verify --deep --strict` 通过。代码同时明确权限弹窗会归属 CuaDriver（`computer-use-panel.tsx:102`、`174-175`），而不是 Hermes。

### TCC 数据库可见性与风险

用户级和系统级 TCC 数据库均存在，但对 SQLite 查询返回 `authorization denied`；原始只读字符串扫描也没有能可靠还原的 Hermes/CuaDriver 授权行。因此本审计**不能声明**当前具体的 `auth_value`、`csreq` 或“已经授予”的状态。

仍可能重复询问的情形：

1. Hermes 本地证书/私钥、Bundle ID 或实际请求权限的进程身份变化；特别是重回 ad-hoc 签名或切到不同发布者签名。
2. CuaDriver 更新时 Bundle ID、Team ID 或 DR 改变；当前版本稳定不保证未来供应商永不改变身份。
3. macOS TCC 重置、系统迁移/重装、MDM/配置描述文件改变、换用户账户，或授权被用户撤销。
4. 出现新的受保护服务或改由不同 helper/应用请求。例如 Hermes 的 Full Disk Access、Automation/AppleEvents 与 CuaDriver 的辅助功能、屏幕录制是不同授权主体；一个主体稳定不能替另一个主体背书。
5. 更新后局部补丁恢复冲突，导致重新构建走了与当前签名策略不同的路径。

建议在不触发授权弹窗的前提下，更新后从 Hermes 设置的 Computer Use 卡片复查 CuaDriver 的 Accessibility/Screen Recording 状态，并在“系统设置 → 隐私与安全性”核对 Hermes 的 Full Disk Access/Automation（如实际使用）与 CuaDriver 的两项权限。若要精确审计 TCC `csreq`，需要用户在有 Full Disk Access 的受信任终端中只读导出相关数据库行；本次未越过系统隐私边界。

## 5. 两个本地补丁的现状

| 补丁 | 当前位置 | 保护级别 | 结论 |
| --- | --- | --- | --- |
| 稳定签名补丁 | 主工作树的未提交修改；独立 worktree `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-26-hermes-permissions/hermes-stable-signing`；本地分支 `codex/hermes-stable-signing-2026-07-26` 的 6 个提交 | 高于 reflog：分支和 worktree 仍引用提交；另有 `hermes-stable-signing.patch` 备份 | 内容仍完整，但主 `main` 更新后不会自动把“已提交分支”合回。 |
| 模型切换设计规格 | 对象 `126223a61c`，仅 reflog 可达 | 低：未被分支/标签引用，reflog/垃圾回收后可能消失 | 应立即用独立分支或外部 patch/文档库固定；本审计未做恢复或写入。 |

`codex/live-model-switch` worktree 当前仅跟踪 `origin/main`，并有 `package-lock.json` 未提交修改；它没有包含 `126223a61c`，不能充当该设计规格的保护分支。

## 6. 最小可靠方案：让普通更新后自动恢复

这里的矛盾不是“要不要更新”，而是上游更新把 `main` 当作可完全重置的交付物，而本地定制同时被当作工作树状态和提交历史两种不同的生产资料。可靠方案必须把本地定制从可被重置的 `main` 历史中分离出来，并让每次更新后的恢复步骤有明确、可验证的入口。

### 推荐的最小方案（不在本次审计中执行）

1. **把两个补丁都存为仓库外、版本控制的 patch queue。** 例如置于 `~/.hermes/local-patches/` 的独立 Git 仓库（不在 `hermes-agent` 内），每个补丁有固定来源 commit、目标文件清单和 SHA-256。保留现有 `hermes-stable-signing.patch`；将 `126223a61c` 的设计文档也导出/提交到该独立仓库。这样即使 `main`、reflog、stash 均被清理，补丁仍可恢复。
2. **主仓库只保留“可自动 stash/restore 的未提交应用态”，不要把本地定制提交到 `main`。** 当前 `updates.non_interactive_local_changes: stash` 已满足该前提，且本次签名补丁存活证明该链路实际工作。不要把它改成 `discard`。
3. **在仓库外安装一个更新后 reconciliation 包装器/任务，并让所有普通更新入口调用它。** 它应在 `hermes-setup --update` 或 `hermes update` 成功后：检查目标 HEAD、依次 `git apply --3way --index` 两个外部补丁、运行只读/测试验证；若任何补丁不能干净应用，保留 patch queue、退出非零并明确报告“未自动恢复”，绝不静默用 `reset --hard` 或 ad-hoc 签名替代。仅 Git `post-merge` hook 不足，因为当前风险路径包含 `reset --hard`，不会触发该 hook。
4. **签名补丁恢复后必须先验证再启动 Desktop。** 检查 `desktop.macos_signing_identity` 仍为现指纹、`codesign --verify --deep --strict /Applications/Hermes.app` 成功，并比较 DR 的 Bundle ID 和叶证书指纹。不要把“构建成功”当作“权限身份不变”。

为什么不是仅依赖一个本地分支：分支能保存提交，却不会被 `main` 的更新器自动合并；而直接把提交留在 `main` 恰会在 `--ff-only` 失败后的 hard reset 中失去可达性。为什么不是仅依赖 Git stash：stash 可以恢复普通工作树变化，但遇到上游冲突时设计上会保留 stash、复位工作树，不能保证无人工介入。外部 patch queue + 明确的更新后恢复入口同时覆盖了“可恢复性”和“自动执行”的需求。

### 验证清单（实施后，每次普通更新）

1. 更新前：确认 patch queue 有两个版本化条目、各自 SHA-256 和目标 base commit；确认 `git branch --contains` 能找到模型设计规格提交。
2. 更新前：`git status --short` 记录本地补丁状态；确认 `updates.non_interactive_local_changes` 仍是 `stash`。
3. 更新后：恢复器记录新 HEAD、两个 patch 的 `git apply --check`/应用结果；若有冲突则停止启动或明确降级，不丢弃 patch。
4. 更新后：`git diff --check`、签名补丁的相关测试，以及模型切换补丁的针对性测试/文档检查均通过。
5. 安装应用后：`codesign --verify --deep --strict /Applications/Hermes.app` 通过；DR 仍为 `com.nousresearch.hermes` + `3883384cce1ed88ef4b41e1475be63b768f2f65d`。
6. 在不点“授予权限”的情况下：设置页显示 CuaDriver 的 Accessibility 和 Screen Recording 都是已授权；系统设置中 Hermes/CuaDriver 对应授权仍存在。若出现新弹窗，先记录其显示的应用名和服务，再判断是身份变化还是新增权限。
7. 保留一次更新日志、reconciliation 日志和 patch queue 提交；这是判断后续提示是上游行为还是本地恢复失败的最小证据链。

## 风险评级

- **高：** 模型切换设计规格仅依赖 reflog，可能被 Git 垃圾回收清除。
- **中高：** 更新器在历史分叉时使用 `reset --hard origin/main`；任何再次提交到主 `main` 的本地工作都可能重演本次失联。
- **中：** TCC 数据库无法只读查询，因此实际授权状态未被独立验证；身份稳定不是授权状态的证明。
- **中：** Hermes 是本地自签名且 Gatekeeper assessment 被拒绝。它当前签名有效，但证书/私钥丢失、路径改走发布者签名或 ad-hoc fallback 时会改变稳定性假设。
- **低到中：** CuaDriver 当前是已公证的 Developer ID 应用，身份基础较稳定；未来供应商改 Bundle ID、Team ID 或权限服务时仍可能重新提示。

## 追加审计：更新时序、入口覆盖与无守护恢复方案

- 追加审计时间：2026-07-26（只读）。
- 结论先行：当前链路在“stash 恢复成功”时会先恢复源码、后重建 Desktop；但**不**在“stash 恢复冲突/失败”时 fail-closed。它会继续更新依赖和启动 Desktop 重建，存在把更新后的未补丁源码构建/替换为应用的风险。

### 7. `hermes update` / Desktop 更新的真实时序

Desktop 自更新链在源码与测试注释中被定义为：`Desktop → hermes-setup --update → hermes update → hermes desktop --build-only → relaunch`（`tests/hermes_cli/test_desktop_exe_integrity.py:3-4`、`hermes_cli/main.py:5534-5547`）。`hermes-setup` 本体是编译的 arm64 Mach-O，当前未找到对应 Rust 源码；其内嵌字符串也表明它调用 `hermes update` 并处理目标应用退出/替换。因此以下时序对 `hermes update` 是源码可证实的，对 Desktop 更新链是由该调用契约支持的结论；最后一次“复制到 `/Applications/Hermes.app`”的 Rust 实现细节无法仅凭当前可读源确认。

| 阶段 | `hermes update` 行为 | 对补丁/应用的影响 |
| --- | --- | --- |
| 1 | 脏工作树先执行 `git stash push --include-untracked`（`hermes_cli/main.py:7578-7675`） | 未提交补丁进入 autostash；本地提交不进入 stash。 |
| 2 | `git pull --ff-only`；若历史分叉则 `git reset --hard origin/<branch>`（`11703-11721`） | 分叉会清空主工作树到上游。 |
| 3 | `finally` 中在 `update_succeeded` 后执行 `_restore_stashed_changes`（`11772-11798`） | **正常成功时，stash 恢复先于依赖刷新和 Desktop 构建。** |
| 4 | Python/Node 依赖刷新、web build（`11815` 起，`11903-11904`） | 仅在阶段 3 已返回后发生。 |
| 5 | 若已有 Desktop，子进程执行 `python -m hermes_cli.main desktop --build-only`（`11906-11944`） | 该构建发生在正常 stash restore 之后。`cmd_gui` 在 `6581-6596` 进行签名 fixup；Desktop 更新器随后负责重启/替换。 |

因此，对问题 1 的精确答案是：

- **成功路径：是。** 已成功的 `stash apply` 在 `hermes update` 内完成后才进入 Desktop 构建，所以签名补丁处于工作树时，`desktop --build-only` 能读取该补丁中的 `_desktop_macos_relaunchable_fixup`。
- **冲突/失败路径：否。** `_restore_stashed_changes` 在 `git stash apply` 冲突后保留 stash，再执行 `git reset --hard HEAD`（`7794-7820`），但刻意“不 `sys.exit`”（`7821-7824`）。调用者也不检查其 `False` 返回值，而是继续到 `11903-11944`。故当前更新可以以新 HEAD 的未补丁源码进入 Desktop 构建。这个构建即使失败也被 `cmd_update` 标为 non-fatal（`11934-11942`），随后仍打印 `Code updated`。
- 这不是只停留在理论上的小差异：Desktop 更新器通过 `hermes update` 驱动 build，且当前编译的 `hermes-setup` 源码不可得，不能证明它会把该“non-fatal build failure”重新提升为失败或拒绝替换 `/Applications/Hermes.app`。应按**没有 end-to-end fail-closed 保证**处理。

### 8. 当前未提交签名补丁的入口覆盖矩阵

| 入口 | 当前是否走配置签名补丁 | 证据与限制 |
| --- | --- | --- |
| `hermes desktop --force-build`（也包括正常 `hermes desktop` 需重建时） | 是，且签名失败时停止该命令 | `cmd_gui` 强制重建于 `6481-6483`；pack 后调用 `_desktop_macos_relaunchable_fixup`，失败即 `sys.exit(1)`（`6580-6596`）。 |
| `hermes update` 的内置 Desktop rebuild | 是，但上游 restore 失败时可用未补丁源码构建 | `11906-11944` 子进程调用 `desktop --build-only`，最终进入上述 `cmd_gui` fixup。**遗漏的是更新恢复失败的 fail-closed 栅栏，不是 fixup call site。** |
| Desktop → `hermes-setup --update` | 间接覆盖，非可完全证明的端到端保证 | 链路注释/测试明确委托 `hermes update`；其之后走 `desktop --build-only`。但 `hermes-setup` 为无可读源码的二进制，且因上一节冲突路径为 non-fatal，不能保证它拒绝复制旧/未补丁产物。 |
| `scripts/install.sh --include-desktop` / `--stage desktop` | 常规 venv 可用时是 | `install_desktop` 在 `scripts/install.sh:2912-2934` 调 Python helper，传 `publisher_signing_configured=False`；helper 返回失败即 installer 返回非零，明确拒绝 ad-hoc downgrade。 |
| `scripts/install.sh` 的 venv Python 不可执行的历史 fallback | **否，稳定身份可能丢失** | `scripts/install.sh:2935-2943` 直接 `codesign --sign -`，只做 strict verification，不读取 `desktop.macos_signing_identity`、不比较 DR。即使证书配置存在，此恢复/新装边缘路径也会 ad-hoc 签名。 |
| 手动 `cd apps/desktop && npm run pack`、`npm run dist*`、直接 electron-builder | 否 | `apps/desktop/package.json:31-38` 直接调用 builder；未经过 `cmd_gui` 或 shell installer，因而不读取 `desktop.macos_signing_identity`。使用者必须随后运行受控 fixup，或此入口本身接入同一 signing helper。 |
| `hermes desktop --skip-build` | 不重建，不适用 | `cmd_gui:6456-6475` 只是启动既有产物；它不会修复此前由旁路构建造成的签名。 |
| `hermes desktop --source` | 不适用 `.app` TCC 身份 | source mode 只构建/启动开发 Electron，不生成待安装的 packaged `.app`。 |

还需注意 build 前 `_force_adhoc_macos_signing` 会把 electron-builder 固定到 ad-hoc（`hermes_cli/main.py:6261-6286`），再由后置 fixup 改为配置证书。这在受控 CLI 路径可行，但意味着任何绕过后置 fixup 的入口都会停在 ad-hoc 身份上。

### 9. 无 LaunchAgent/守护进程的最小可行恢复设计

可以做到，前提是把 reconciliation 放到**当前同步的 `cmd_update` 流程内部**，而不是依赖 Git `post-merge`。`post-merge` 不覆盖现有的 `reset --hard` 分叉路径。

最小生产性改动建议如下（本审计未实施）：

1. 在 `hermes_cli/main.py` 新增一个受控的 `_reconcile_local_patch_queue()`：读取仓库外、版本控制的 patch manifest（例如 `$HERMES_HOME/local-patches/manifest.json`），对每个补丁先检查“已应用”或执行 `git apply --3way --index`，写入明确日志；任何补丁无法应用即返回失败，不进入构建。
2. 改造 `cmd_update` 的 `11772-11798` 恢复处理：捕获 `_restore_stashed_changes()` 的布尔结果；若恢复冲突，保留原 stash、保持当前代码的 clean new HEAD，然后立即以外部 patch queue 做权威恢复。若 queue 未完整恢复，`sys.exit(nonzero)`，使后续 `11903-11944`、Desktop relaunch/替换均不会发生。若 stash 已成功恢复，queue 通过反向检查识别“已应用”而不重复打补丁。
3. 在同一 `cmd_update` 内，将 reconciliation 放在依赖刷新和 `desktop --build-only` **之前**。这样 Desktop updater 无需新增守护进程；它已经同步调用 `hermes update`，非零退出即可阻止成功路径。可加一项持久配置/清晰默认值时，最少再改 `hermes_cli/config.py` 的 schema/default；若路径固定在 `$HERMES_HOME/local-patches`，运行时本身只需改 `main.py`。
4. 为使 `scripts/install.sh --include-desktop` 同样安全，修改 `scripts/install.sh:2912-2944`：调用同一 Python reconciliation helper 后才 pack/install；当 `desktop.macos_signing_identity` 已配置但 Python helper 不可用时，应失败而非走 `--sign -` fallback。否则“普通修复/新装”仍是身份降级旁路。
5. 增加针对 `tests/hermes_cli/test_cmd_update.py` 的顺序/失败测试、针对 `tests/hermes_cli/test_gui_command.py` 的“reconcile 后才 build”测试，以及针对 `tests/test_install_sh_macos_signing_fallback.py` 的“已配置身份时 helper 不可用必须失败”测试。现有测试只验证签名 fixup 自身，不验证 update 的 stash-conflict-to-build 禁止关系。

该方案的边界也应明确：它能自动恢复在 patch queue 中声明的签名补丁和模型切换补丁；它不会也不应静默吞掉 queue 外的任意本地改动。queue 与 stash 都失败时，正确结果是更新非零并保留恢复证据，而不是构建一个看似成功但丢失本地权限策略的应用。
