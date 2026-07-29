# 自动发推

把一篇 Markdown 长文落地成可检查、可复用、可发布的 X 线程资产包。

这个项目默认采用 safe publishing：没有显式 `--live --yes` 时，只生成本地 outbox，不碰你的 X 账号。

## 能做什么

- 读取一篇 Markdown 长文
- 识别正文里的图片标记 `![alt](path)`
- 自动拆成不超过 280 字符的 X thread
- 校验图片路径、图片大小和可选尺寸
- 生成可复制发布的 `thread.txt`
- 生成机器可读的 `thread.json`
- 在配置好 X 凭据后，一键按回复链发布

## 快速开始

```bash
python3 publish.py init-sample
python3 publish.py plan posts/example-codex-x-assets.md
```

生成结果会放在 `outbox/<稿件名>/<时间戳>/`。

## 从自己的素材创建稿件

```bash
python3 publish.py new --title "Codex 不只是写代码" --slug codex-assets --from material.txt
python3 publish.py plan posts/codex-assets.md
```

## Markdown 写法

```markdown
---
title: Codex 不只是写代码
status: ready
expect_image_size: 2000x800
---

![封面图](assets/cover.png)

很多人用 Codex，只把它当成写代码工具。

但这其实低估了它。
```

图片标记会绑定到它后面的第一条推文。比如封面图放在正文开头，就会随第一条推文一起发布。

## 真实发布到 X

先安装依赖：

```bash
python3 -m pip install -r requirements.txt
```

复制环境变量模板：

```bash
cp .env.example .env
```

然后填入 X Developer Portal 里的 OAuth 1.0a user-context 凭据。

```bash
python3 publish.py publish posts/example-codex-x-assets.md --live --yes
```

脚本会自动读取项目根目录里的 `.env`。当前实现使用 X 官方推荐的新发帖接口 `POST /2/tweets`。带图片时会通过 Tweepy 先上传媒体，再把 `media_id` 挂到对应推文上。

## 命令

```bash
python3 publish.py init-sample
python3 publish.py new --title "标题" --slug my-thread --from material.txt
python3 publish.py plan posts/my-thread.md
python3 publish.py publish posts/my-thread.md
python3 publish.py publish posts/my-thread.md --live --yes
python3 publish.py run-ready
python3 publish.py run-ready --live --yes
```

`run-ready` 会扫描 `posts/*.md`，只处理 `status: ready` 且没有记录在 `state/published.json` 里的稿件。它适合放进 cron、launchd 或其他自动化调度器。

一个最小定时任务可以这样写：

```bash
*/30 * * * * cd /Users/yangqi/Documents/自动发推 && python3 publish.py run-ready --live --yes >> logs/auto-x.log 2>&1
```

正式启用前，先连续跑几次不带 `--live` 的 `run-ready`，确认 outbox 和检查清单都符合预期。

## 发布前检查

`plan` 和 `publish` 都会检查：

- 每条推文是否超过 280 字符
- 图片路径是否存在
- 图片文件是否超过 5 MB
- 如果安装了 Pillow，图片尺寸是否等于 `expect_image_size`
- 每条推文是否超过 4 张图片

## 安全边界

内容生产的核心矛盾，是效率和风险的矛盾。自动化越强，误发的代价越高。

所以这个项目把流程拆成三层：

- 资产层：Markdown、图片、路径、标题
- outbox 层：可复制、可审查、可归档的线程包
- live 层：只有你显式确认后才调用 X API

这样既能提高生产力，又不会把发布关系交给一个不可检查的黑箱。
