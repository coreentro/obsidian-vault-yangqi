---
title: "用CodeX自动生成朋友圈到飞书群"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/CYwpwXWcliHk9pk1PCfcSOmjnyh
node_token: CYwpwXWcliHk9pk1PCfcSOmjnyh
obj_token: Qs3bdVAlmo0ao0xDQaGc5h6Qnwd
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "第十一章：CodeX实战案例"
  - "用CodeX自动生成朋友圈到飞书群"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 3
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 用CodeX自动生成朋友圈到飞书群

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 第十一章：CodeX实战案例

# 写在前面

你好，我是大圣

前两天我做了一件事情：让 AI 每天扫描我的内容 OS 里面我自己的录音、灵感等数据，帮我自动生成 3 到 5 条朋友圈，经过我的审核之后，自动推到飞书

这个例子非常适合拿来学习：

1. 它是一个真正的实战案例
2. 它把AI对知识的整理、CodeX 的自动化、skill 的打磨，以及和飞书的联动全部贯穿了起来

这节课我就带着大家完整去复现这个案例

<grid>
<column width-ratio="0.611284">
> [!abstract]- 🖼 图片展示了大圣关于朋友圈日供的实践内容。三个月前，他依托Claude C
> 图片展示了大圣关于朋友圈日供的实践内容。三个月前，他依托Claude Code + Codex + Obsidian + 飞书，打造了内容OS，将每天思考、阅读沉淀其中。但产出端利用少，原始素材沉睡。他让Codex写朋友圈日供skill，每天早上8:30扫描昨天内容，生成5条朋友圈，自己改动并定稿。Codex需对比初稿和改动，优化朋友圈写作，再定时推送到飞书，提醒发朋友圈时间。此实践让大圣复盘、记录自己，让外界看见变化。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/EOUzbOpd1ob1WKxNBgYcQXo0nWb) · `EOUzbOpd1ob1WKxNBgYcQXo0nWb`
</column>
<column width-ratio="0.388716">
> [!abstract]- 🖼 图片展示的是飞书CLI智能体“朋友圈助手”发送的一条朋友圈日供消息。消息
> 图片展示的是飞书CLI智能体“朋友圈助手”发送的一条朋友圈日供消息。消息显示时间为09:30，来源为20260706朋友圈日供，配有链接图片。内容提到作者下定决心实践将80%朋友圈改成由内容OS“日供”；三个月前依托Claude Code + Codex + Obsidian + 飞书打造内容OS，已沉淀思考、阅读素材；因产出端利用少，素材闲置；想打造完美启动链路，但需打磨；昨天让Codex帮写朋友圈日供skill，逻辑是每天早上8:30扫描昨天内容，产出5条朋友圈，作者会改动并定稿。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/W0MObpIqzoOLq2xOfLWcacT5ntc) · `W0MObpIqzoOLq2xOfLWcacT5ntc`
</column>
</grid>

---

<callout emoji="✨">
我一直跟大家分享，我不懂你的业务，所以我没有办法去深入到你的业务里面
我也不想给大家分享一些我没有做过的例子，因为那样我绝对讲不出底层逻辑来
所以我把我做过的例子以及这其中的思考完整地分享给大家
我相信，在 AI 的帮助下，你一定能够举一反三，进而去赋能你的业务
我希望大家在咱们的社群里，可以真正地打磨出自己的 skill，打磨出自己的业务线，而不是到处去找别人去要
**所以这节课，不管你做不做朋友圈，你是不是内容创作者，我相信对你都会有启发**
</callout>

# 一、前置学习

**在学习这节课之前，强烈建议你把前面的课程都看一遍（每一步都算数，有些学习过程你省不了）**

这节课它依赖的知识点有：

1. 如何借助 CodeX 去打造自己的系统：<cite doc-id="Ghr2wvUXkiVcRukGgThcEWZEnsd" file-type="wiki" title="一个贯穿始终的学习案例" type="doc"></cite>
2. Skill 是什么？<cite doc-id="V9pbweJb0iZVFjk5jskcVJPMnQd" file-type="wiki" title="【必看理论篇】面向小白的Skills保姆级教程" type="doc"></cite>
3. 飞书 CLI 是什么？<cite doc-id="NFRwwaLKDiM6J7k8KGecqNg2nle" file-type="wiki" title="智能体跟外部打交道的第三种方式" type="doc"></cite>
4. Codex 的自动化能力是什么？<cite doc-id="U4b1wgWi1iwJ9pk6fxTcXtRFnXc" file-type="wiki" title="CodeX的自动化能力" type="doc"></cite>

# 二、这个案例解决什么问题

我是一名内容创作者，日常工作包括：**发朋友圈、发短视频、发公众号、做直播、做课**

而这些内容，就是我一人公司的几条业务线

对于我一人公司的 AI 落地来讲，就是把这几条业务线全部打磨成 100% 自动化（**当然这是一个非常长期的事情**）

**这个案例就是解决的就是我朋友圈业务线的问题**

---

下面这张框架就是我朋友圈的生产逻辑

我每天会输入很多的素材，我会把它收集到内容 OS 里面，进入到我的素材库

那我的朋友圈就依赖于每天进账的内容生成

<callout emoji="✨">
**我这里不是那种根据鸡汤和观点生成大而空的朋友圈**
**他一定是基于我今天发生的事情、我今天的思考**
这里面的 AI 起的作用是，它把我零散的思考汇聚起来，本质是一个信息整理的作用
</callout>

> [!abstract]- 🖼 图片展示了内容创作者生成朋友圈的生产逻辑框架。上方有四块内容来源，分别为
> 图片展示了内容创作者生成朋友圈的生产逻辑框架。上方有四块内容来源，分别为“我今天阅读的文章”“我今天迸发的灵感”“我今天社群的音频记录”“我今天跟别人对话的录音”，均指向“内容OS”。内容OS再指向“03素材库”，素材库有两条输出，一条是“每天3 - 5条朋友圈”，另一条是“调用朋友圈写作Skill”，最后“每天3 - 5条朋友圈”会定时推送到飞书。该图与上下文紧密相关，直观呈现了朋友圈生成的逻辑流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CiglbSniXoQVNLxkMFWcaLXKnHd) · `CiglbSniXoQVNLxkMFWcaLXKnHd`

生成朋友圈之后，我还想让它自动帮我发到飞书上

发到飞书的原因有两个：

**第一，我要在手机上发朋友圈**

**第二，我想让飞书也起到一个提醒我的作用，因为我的朋友圈每隔 3 个小时发一条**

# 三、第一步：生成朋友圈的逻辑

我通过视频来给大家讲解一下我生成朋友圈的逻辑，以及它使用的 skill

<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="PAnYbWAzRoAH56xmhtPcHJ2Wn3f"/></figure>

> [!abstract]- 🖼 该图是文档中生成朋友圈的逻辑框架图，对应文档中“第一步：生成朋友圈的逻辑
> 该图是文档中生成朋友圈的逻辑框架图，对应文档中“第一步：生成朋友圈的逻辑”相关内容。图中展示了朋友圈日供内容的全流程：首先由朋友圈日供定时任务每天8点半执行产出日供文档，且每1小时执行一次；之后系统扫描前一天的素材，分别对应技能1“ds-moments-supply”和技能2“ds-moments-writer”；两个技能处理后生成每日一份的日供文档，再经人工编辑成朋友圈终稿，最后对比AI初稿与人编终稿的差异，以此优化技能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BPESberyfo46ujxcD8qcMSXRnZb) · `BPESberyfo46ujxcD8qcMSXRnZb`

# 四、第二步：对接飞书机器人

在第三步里面，我们生成了朋友圈。接下来，我把朋友圈发送到飞书上

请注意，飞书跟你的 CodeX 的联动其实分两种：

1. 第一种是 CodeX 生成的内容发送到飞书上
2. 第二种是用你的飞书去控制 CodeX 的任务执行

**我们这节课讲的其实是第一种，不要搞混了**

这部分能力靠的是飞书 CLI：<cite doc-id="NFRwwaLKDiM6J7k8KGecqNg2nle" file-type="wiki" title="智能体跟外部打交道的第三种方式" type="doc"></cite>

我们继续看视频

<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="PvFJbpir7oyMImxJzFicp2rnnff"/></figure>

# 写在最后

我一直跟大家分享，我不懂你的业务，所以我没有办法去深入到你的业务里面

我也不想给大家分享一些我没有做过的例子，因为那样我绝对讲不出底层逻辑来。

所以我把我做过的例子以及这其中的思考完整地分享给你们。我相信，在 AI 的帮助下，你一定能够举一反三

我希望大家在我们的社群里，可以真正地打磨出自己的 skill，打磨出自己的业务线，而不是到处去找别人去要

以上，希望对大家有帮助
