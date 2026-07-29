---
title: "【精选】Claude Code的使用技巧"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/GoKtwDdO6iyfqZkNG48clLVYned
node_token: GoKtwDdO6iyfqZkNG48clLVYned
obj_token: UTJjdxnquoyZNlxatQac1LWUnlg
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "让智能体真正能干活：自定义技能与工具协议"
  - "【精选】Claude Code的使用技巧"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 20
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 【精选】Claude Code的使用技巧

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 让智能体真正能干活：自定义技能与工具协议

<callout emoji="✨">
这节课是一场视频号的公开直播
下面是文字版，但如果有时间的话，我强烈建议你听一下视频版
里面有我的情绪，有我对这件事情的理解
这场分享质量非常高，一定要耐心听完，我把我对 Claude Code 的理解，以及如何用 Claude Code 去学习任何知识，全部分享在了里面
</callout>

<readonly-block href="https://axsppz4oyvj.feishu.cn/minutes/embed/obcnhd71a856w9spajn7d473?from=ccm" type="iframe"></readonly-block>

# 一、事情的背景

我最近在写小龙虾的教程，但是很痛苦，因为我发现到处都是 bug

这并不是说小龙虾没有价值，而是一个高速发展的软件，它几乎每一天一更新

而很多第三方厂商也在推出自己的各种各样的插件。**比方说飞书的官网插件**

[OpenClaw飞书官方插件上线｜一文讲清功能、安装更新教程与常见问题！ - 飞书官网](https://www.feishu.cn/content/article/7613711414611463386)

[OpenClaw 飞书官方插件使用指南（公开版） | OpenClaw Feishu Official Plugin User Guide (Public Version )](https://axsppz4oyvj.feishu.cn/docx/MFK7dDFLFoVlOGxWCv5cTXKmnMh)

---

而为了给各位做教程，我有现在市面上几乎所有主流的部署方式的小龙虾

**我有第三方厂商一键部署的小龙虾，飞书的妙搭和扣子**

飞书妙搭：https://miaoda.feishu.cn/app/app_4jpdt142y635u

扣子：https://code.coze.cn/p/7616650638742667315/preview

---

**我有使用云服务厂商部署的容器，腾讯云**

<grid>

> [!abstract]- 🖼 图片展示了腾讯云轻量应用服务器的多种配置及价格信息。其中，2核4G配置的
> 图片展示了腾讯云轻量应用服务器的多种配置及价格信息。其中，2核4G配置的60GBSSD盘1.5T，时长1年，日均价56.4元/月，售价199元；2核2G配置的60GBSSD盘1.5T，时长1年，日均价6.25元/月，售价99元；2核2G20M配置的60GBSSD盘1.5T，时长1月，日均价20.7元/月，售价20元；4核8G30M配置的60GBSSD盘1.5T，时长1月，日均价21.6元/月，售价88元。这些配置信息与文档中介绍的使用云服务厂商部署容器的腾讯云内容相关。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SIUlbRrZxoWpEcxcPP8cWNHvnnc) · `SIUlbRrZxoWpEcxcPP8cWNHvnnc`

> [!abstract]- 🖼 图片展示了OpenClaW Claude bot v1.50的界面。左侧
> 图片展示了OpenClaW Claude bot v1.50的界面。左侧是文件管理器，显示有“root”和“claude”文件夹。右侧是代码编辑区域，上方有“Claude Code v2.1.50”标题，欢迎语为“Welcome back!”，并提示使用“/init”创建CLAUE.md文件。下方显示“Opus 4.6 · API Usage Billing”及“~ /openclaw”信息，还有“/clear”指令及“L (no content)”提示。该图片与文档中介绍OpenClaW Claude bot v1.50的内容相关，直观呈现了其界面样式和部分功能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VnwnbtfbgoO79SxzAqvcs9ehnvd) · `VnwnbtfbgoO79SxzAqvcs9ehnvd`

</grid>

https://orcaterm.cloud.tencent.com/terminal?type=lighthouse&instanceId=lhins-b46son3p&region=na-siliconvalley&from=lh_console_login_btn

---

**我有使用我老婆的 MacBook Air 部署的项目**

> [!abstract]- 🖼 图片展示了一台MacBook Air笔记本电脑，放置在木质桌面上。电脑屏
> 图片展示了一台MacBook Air笔记本电脑，放置在木质桌面上。电脑屏幕上显示着代码界面，其中突出显示了“CLAUDE CODE”字样。屏幕下方是黑色的键盘，右侧有数字小键盘。电脑旁边有充电线等物品。这张图片与文档中介绍部署方式的内容相关，可能是用于展示使用我老婆的MacBook Air部署的项目时的场景，直观呈现了部署环境。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DKHmbC4iloA2NpxrXGkcwmiCnxd) · `DKHmbC4iloA2NpxrXGkcwmiCnxd`

# 二、写教程的这几天我在做什么？

我想跟大家分享一下写OpenClaw教程的这几天我在做什么

## 1）我在找便宜的方案

第一，我在找便宜的方案。更确切地说，我在找能够一键部署的方案，因为我不想让大家在安装初期就耗费了心力

确实被我找到了，飞书的妙搭，还有扣子等等

然后我就开始启动了我们的教程

> [!abstract]- 🖼 图片展示了OpenClaw专区的相关内容。专区下有五个帖子标题，分别是“
> 图片展示了OpenClaw专区的相关内容。专区下有五个帖子标题，分别是“OpenClaw这么火，到底该怎么学？我的答案可能和你...”“开启龙虾学习前，我想对你说的话”“OpenClaw安装与部署的3种方式”“小白一键部署的几种方案”“为你的龙虾安装大脑”。这些帖子标题与文档中作者在学习和使用OpenClaw时思考的小白学习路径及分享养虾感悟的内容相呼应，体现了作者在学习OpenClaw过程中遇到的困惑及分享想法的初衷。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Aj6Abz2XZo1j4jx61k3c9AcgnyD) · `Aj6Abz2XZo1j4jx61k3c9AcgnyD`

## 2）我在学习和使用 OpenClaw

是的，你没有看错，我也在学习，我并不是OpenClaw专家，我自己也在养虾

我在这个过程中，一边思考一个小白到底应该按照怎样的路径去学习，也一边思考怎么把我在养虾过程中的感悟分享给大家

但是我这里面发现了一个很让我头疼的现象。养虾的过程中会出现各种稀奇古怪的 bug

> [!abstract]- 🖼 图片展示了养虾日常中遇到的Bug情况。上方标题为“养虾日常 Bug满天飞
> 图片展示了养虾日常中遇到的Bug情况。上方标题为“养虾日常 Bug满天飞的真实现场”，下方有三个分支，分别是“突然不回复 系统静默无响应”“版本更新 飞书通道突然失效”“装插件死机 整个系统崩溃”。最下方总结“全部靠Claude Code解决 哪怕资深程序员也未必能自己搞定”。该图与上下文紧密相关，直观呈现了作者在养虾过程中遇到的各类问题，为后续介绍使用Claude Code解决这些问题做铺垫。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Q7VmbcoowoiIrixRZqUck48Onfg) · `Q7VmbcoowoiIrixRZqUck48Onfg`

<callout emoji="✨">
比方说OpenClaw可能突然不回复你了；
再比如说有一天OpenClaw更新了新版本，你配的飞书通道不生效了；
再比如说，你看到一个好用的插件（飞书官方插件），你想把它装上去，结果你整个系统死机了；
</callout>

以上这些场景不是我臆想的，是我真实在养虾过程中发现的

我是怎么解决的？**我全部是靠 Claude Code 帮我去解决的**，哪怕今天我是资深的程序员，我都没有办法说一定能够自己去解决这些问题

> [!abstract]- 🖼 图片展示了Claude Code v2.1.71的界面，突出显示了其作为
> 图片展示了Claude Code v2.1.71的界面，突出显示了其作为OpenClaw助手的主要职责，包括学习引导、配置管理、故障排查、知识沉淀等。还说明其知识来源优先级为先查本地refs/文档，再查官网，查完后把有价值的内容沉淀到本地。理念是费量学习法，不需要读教程，直接对话就能学会OpenClaw，想了解什么直接问。该图片与上文提到的作者在养虾过程中遇到问题靠Claude Code解决相呼应，体现了其在养虾技能传授中的作用。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Anh5bXV3BoLctpxuZtvcjvVFnVh) · `Anh5bXV3BoLctpxuZtvcjvVFnVh`

然后我就开始思考，我到底该给大家一些什么样的内容，能让大家真正掌握养虾的技能，而不是说，你刚学完一个教程，半个月之后，它又变了

<callout emoji="✨">
我到底应该给社群里的2000多位伙伴提供什么样的教程，让大家能够真正学会AI？
我开始意识到一个问题，在AI时代，纯教程的内容已经不太适用了，大家更需要的是一些思维方法类的内容
</callout>

> [!abstract]- 🖼 图片展示了“AI编程必知必会的基础知识”板块内容，包含“服务器与操作系统
> 图片展示了“AI编程必知必会的基础知识”板块内容，包含“服务器与操作系统”和“程序中的API是什么”两个子项。该图片位于介绍Claude Code使用技巧的文档中，与上下文紧密相关，上下文提到作者在写教程时遇到问题需Claude Code解决，意识到纯教程内容已不太适用，社群伙伴更需思维方法类内容，此图片可能是在展示作者在AI编程方面需掌握的基础知识，为后续分享思维方法类内容做铺垫。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RKVSb0yHLogekmxqFpBcI6OfnUh) · `RKVSb0yHLogekmxqFpBcI6OfnUh`

所以有了今天的分享。我想把我这几天是怎么学习OpenClaw，以及我总结出来的使用Claude Code学习任何新知识的方法论分享给大家

# 三、我是如何用Claude Code学习小龙虾的

> [!abstract]- 🖼 图片展示了学习OpenClaw的流程。从买一台服务器开始，接着安装Cla
> 图片展示了学习OpenClaw的流程。从买一台服务器开始，接着安装Claude Code，再建立《OpenClaw管理助手》文件夹，最后安装龙虾并学习、修复其bug。图片下方还标注了Cherry Studio和谷歌浏览器。该图与文档中介绍学习OpenClaw工具的内容相关，直观呈现了学习流程，辅助理解文档中提到的工具作用。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ZVIcb00T6offQ7xmJUGcZoqAnkh) · `ZVIcb00T6offQ7xmJUGcZoqAnkh`

上面这张图就是我学习 OpenClaw 的所有工具，也是我学习任何工具知识的工具

接下来我一个一个跟大家剖析，它们在我学习OpenClaw的过程中承担了哪些作用

## 1）买服务器

首先我需要买一台服务器，它可以是腾讯云这类云端服务商的产品，也可以是一台本地的MacBook Air。

核心的目的就是要让我能够安装龙虾

这部分不是我们今天的目的，详细的教程我会在后续的课程里面给大家讲解

## 2）安装Claude Code

[Claude Code 的安装](https://axsppz4oyvj.feishu.cn/wiki/Xov5w11iCim3sXk2nEjcRZVznsd)

> [!abstract]- 🖼 图片展示的是一个学习交流群的聊天记录。群内成员就安装Claude Cod
> 图片展示的是一个学习交流群的聊天记录。群内成员就安装Claude Code展开讨论，如孔繁玉提到安装过程不仅教会如何安装，还让其掌握有问题自己和AI一起解决的思路；程云详细介绍了安装步骤；mask询问是否关闭websearch也能联网搜索；王晓磊建议分Windows和Mac版本；王小云表示安装成功并感谢；陆爱萍按步骤操作后成功安装。该图片与文档中介绍Claude Code安装教程的内容相关，展示了学习群内成员对安装过程的反馈。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ROgubpcAUobePnxqhw9cGJcxnze) · `ROgubpcAUobePnxqhw9cGJcxnze`

我已经在咱们的课程里面写了一份非常详细的 Claude Code 的安装教程。当然，我无法保证100%的同学能安装成功，因为每个人的系统真的不一样

但只要你认真地看过这份教程，并且真正地去理解了它的逻辑，我相信给你一台新的 Linux 系统，或者给你一台苹果笔记本，你安装起来应该是顺风顺水的

<callout emoji="✨">
这里说一句对Windows系统不友好的话。
在AI时代，你安装的很多工具有bug，原罪都是因为它是Windows系统
</callout>

https://github.com/UfoMiao/zcf/blob/main/README_zh-CN.md

当你把我们上面那个教程一步一步看过，并且执行过一遍之后，在后续你在其他系统上重新安装 Claude Code 的时候，你可以使用我上面提到的这个 GitHub 的安装方式，叫 zcf

> [!abstract]- 🖼 图片展示的是ZCF - Zero-Config Code Flow的页面
> 图片展示的是ZCF - Zero-Config Code Flow的页面。页面上方有多个标签，如“downloads”“License”“Claude Code”等。页面中央突出显示“ZCF”，并有“Zero-Config Code Flow”字样。右侧有一个透明的蓝色方框，内有“ZCF”及“Zero-Config Code Flow”等信息。底部文字说明“零配置，一键搞定Claude Code & Codex环境设置 - 支持中英文双语配置、智能代理系统和个性化AI助手”。该图片与文档中介绍Claude Code学习小龙虾教程相关，展示了其安装方式之一的GitHub安装方式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SCUKb9LL2oicLCxNdTYc14hynlf) · `SCUKb9LL2oicLCxNdTYc14hynlf`

## 3）建立一个文件夹

这是最关键的一步，因为我们要建立一个项目，专门给 Claude Code 指导我们学习 OpenClaw

<callout emoji="✨">
这里我说一下，很多伙伴对 Claude Code 的工作方式有很多困惑，我装了它之后，到底该怎么用？
首先，Claude Code 就是一个安装在你电脑上的通用智能体，你可以把它当成一个人
好，那在没有 Claude Code 之前，你是怎么工作的？
你要做一个项目，是不是要在你的电脑上新建一个文件夹，然后在里面新建文件、删除文件、修改文件，最后产出一个 PPT 或者 Word 文档，交给你的老板
或者说你要写代码，代码也是一个文件夹，你在这个文件下去写一篇又一篇的代码，最终打包成一个项目，把它部署起来
所以 Claude Code 的工作方式到底是什么？非常简单。
当你想要做一个任务的时候，你可以建一个文件夹，然后你在这个文件夹内启动你的 Claude Code
剩下的就是用自然语言指挥你的 Claude Code 在这个文件夹里面翻江倒海，想怎么折腾怎么折腾
</callout>

---

所以当我想要成立一个项目，叫做 OpenClaw 管理助手的时候，我就是新建一个文件夹，然后在这个文件夹内折腾

我给大家看一下我建立的这个文件夹的目录

> [!abstract]- 🖼 图片展示了在Finder中打开的“projects”文件夹内容。左侧路径
> 图片展示了在Finder中打开的“projects”文件夹内容。左侧路径栏显示为“Users > bonnie > projects”。右侧列表中，有两个文件夹，上方的“openclaw”文件夹被红色框突出显示，其创建时间为2026年3月15日1:45 AM，下方的“openclaw - digital - workforce”文件夹创建时间为2026年3月7日1:10 AM。该图片与文档中介绍建立文件夹的内容相关，直观呈现了作者在“projects”文件夹下建立的“openclaw”文件夹。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LZOQbDGZJox6agxY4N2cb0dGnhd) · `LZOQbDGZJox6agxY4N2cb0dGnhd`

> [!abstract]- 🖼 图片展示了OpenClaw文件夹内的目录结构。其中，红色框突出显示了“r
> 图片展示了OpenClaw文件夹内的目录结构。其中，红色框突出显示了“refs”文件夹和“CLAUDE.md”文档。该图片与文档中介绍建立文件夹的内容相关，用于直观呈现作者在OpenClaw项目中建立的文件夹及核心文档，即“refs”文件夹和“CLAUDE.md”文档，以帮助读者理解在Claude Code项目中文件组织方式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OlCZbzbbDowzkAxWL4rczWscnSe) · `OlCZbzbbDowzkAxWL4rczWscnSe`

这个文件夹的名字叫 OpenClaw，里面有一个文档叫 CLAUDE.md，还有一个文件夹是 refs

这里面的核心是这个 CLAUDE.md 文档。CLAUDE.md是什么？我在教程里给大家讲了

[[【启程必看】从这里开始/【正课阶段 3】上手智能体：桌面端与AI编程/让智能体真正能干活：自定义技能与工具协议/让它记住你的规矩：CLAUDE.md 配置指南|让它记住你的规矩：CLAUDE.md 配置指南]]

你可以认为是这个项目的一个说明书。当Claude Code在这个文件夹下启动的时候，它会优先去读这个CLAUDE.md的文档内容，这个文档内容是指导它做事情的关键

CLAUDE.md 不是必选，但它是一个最佳实践。

就像你作为一个人，每当你建立一个文件夹的时候，其实你对这个文件夹是有预期的，你要用它来干什么？

你打算在这个文件夹里做什么？你脑子里面都会有需求，CLAUDE.md就是这个需求说明

所以我这个文件夹里面最核心的都是CLAUDE.md的内容，你看懂了它，你就知道我要做什么

<callout emoji="✨">
我希望这个案例不仅给你一种如何学习龙虾的启发，更是你学习任何知识的启发
Claude Code 就是你最强的学习助手
下面这个CLAUDE.md里面最关键的是什么？
**我把OpenClaw的官网文档给到了它。这是它的知识来源，相当于我为它提供的上下文**
----
知识来源  
\- \`refs/\` 目录: 已沉淀的结构化参考文档（优先读取）  
\- 官方文档: https://docs.openclaw.ai/  
\- LLM 友好文档: https://docs.openclaw.ai/llms.txt（官网查询时优先用这个）
</callout>

**这个代码块不提供复制，大家可以自行截图，让你的AI帮你搞定**

```Markdown
# CLAUDE.md - OpenClaw 助手

## 教学理念

这个项目践行**费曼学习法**——用教来学。老师在学习 OpenClaw 的过程中，把经验沉淀为 Claude 可读的知识库，等于把"老师"封装进了工具里。

核心原则：
- `refs/` 里的文档不是给学员读的，是给 Claude 读的
- 学员不需要看教程，直接跟 Claude 对话就能学会
- Claude 基于知识库 + 学员的实际环境（配置、日志），提供个性化的引导和帮助

## 项目愿景

把这个目录打造成一个 **Claude Code Skill 插件**，让任何学员 clone 后即可获得一个全能 OpenClaw 助手，能够：

- 引导新手从零安装、配置 OpenClaw
- 解答使用过程中的各种问题
- 代劳操作：改配置、排查故障
- 沉淀学习笔记

最终目标：发布为可安装的 Skill，学员装上就能用。知识层在日常使用中持续沉淀和优化。

## 当前阶段

我们正在边用边打磨，逐步积累：
1. 知识沉淀 — 把 OpenClaw 的安装、配置、使用经验整理成结构化文档
2. Skill 开发 — 时机成熟时，将知识库封装为 Claude Code Skill 插件

## 你的职责

- 帮我学习和使用 OpenClaw
- 修改配置文件（`~/.openclaw/openclaw.json`）
- 排查故障（查日志、健康检查、诊断问题）
- 通过浏览器操作 Web 界面（Playwright）
- 把学到的知识沉淀成 Markdown 文档
- 思考如何优化知识组织，为后续 Skill 化做准备

## 知识策略

**本地优先，官网补充**：
1. 先查 `refs/` 目录下的本地知识文档（快、省 token）
2. 本地找不到时再查官网，查完后将有价值的内容沉淀到 `refs/` 中
3. 每次从官网学到新知识，主动提议存到本地

### 知识来源
- `refs/` 目录: 已沉淀的结构化参考文档（优先读取）
- 官方文档: https://docs.openclaw.ai/
- LLM 友好文档: https://docs.openclaw.ai/llms.txt（官网查询时优先用这个）

### 文档同步策略

不追求实时同步，靠**版本标记 + 按需刷新**：
- 每份 `refs/` 文档必须标记：来源 URL、获取时间、对应的 OpenClaw 版本号
- 以下两种情况触发刷新：
  1. OpenClaw 升级了版本
  2. 实际使用中发现文档内容与实际行为不一致
- 刷新后更新文档中的版本标记

## 关键路径

- OpenClaw 安装目录: `~/.openclaw/`
- 主配置文件: `~/.openclaw/openclaw.json`

## 交互约定

- 回答 OpenClaw 相关问题时，优先参考官方文档和 `refs/` 下的资料
- 聊完一个主题后，询问是否需要沉淀成文档
- 确认沉淀后，更新到对应的学习笔记文件中

```

## 4）为你的Claude Code提供初始和额外的上下文

<callout emoji="✨">
不要指望你的 Claude Code 什么都懂
比如你跟它讲小龙虾，它可能都不知道小龙虾是什么，它得自己去搜索。那万一它搜索出来是那种吃的小龙虾，你怎么办？
AI 通识就会发挥作用。AI 到底懂什么？不懂什么？
</callout>

所以这里面你就需要两步。

第一步是为你的 Claude Code 提供初始的上下文。那初始的上下文从哪里来？官网

<callout emoji="✨">
阅读官网原版文档会是 AI 时代最重要的技能之一
人负责找到官网文档，而 AI 负责阅读
而未来的产品，它一定要能提供适合 Agent 阅读的文档，否则这个产品就是不合格的
</callout>

我们以 OpenClaw 的官方文档为例。首先，我给你看两个链接

- **给人阅读的**：https://docs.openclaw.ai

- **给Agent阅读的**：https://docs.openclaw.ai/llms.txt

这里面关键的就是给 Agent 阅读的这个文档，

大家可以仔细看一下，你站在AI的角度可以思考一下，它为什么这么设计？

当你提供了这个初始文档给到你的 Claude Code 的时候，那你们俩的认知就对齐了。他会知道什么是 OpenClaw，他会知道什么是小龙虾，他也会知道什么是 Agent、Getaway 通道这些

---

第二种上下文是你在学习过程中需要额外提供的

举个例子，**飞书官网出了他们的官方插件**，你安装这个插件之后，你的OpenClaw 可以很好的集成飞书

而且飞书的官方插件可以帮你快速配置多Agent，快速接入飞书，快速申请机器人权限

那我怎么装？

当然是用 Claude Code 帮我们装。但 Claude Code 不知道这个信息，**那我就发挥了作用，我要为它去找上下文**

是我找到了这两篇文档

[OpenClaw飞书官方插件上线｜一文讲清功能、安装更新教程与常见问题！ - 飞书官网](https://www.feishu.cn/content/article/7613711414611463386)

[OpenClaw 飞书官方插件使用指南（公开版） | OpenClaw Feishu Official Plugin User Guide (Public Version )](https://axsppz4oyvj.feishu.cn/docx/MFK7dDFLFoVlOGxWCv5cTXKmnMh)

这两篇文档我可以直接把链接给到他，也可以用 Chrome 插件把它下载成 Markdown 的方式给到他，都可以

当我有了这两篇文档，我就能让 Claude Code 帮我去装飞书官网的插件，出现问题之后它也能帮我修复

**它不仅能还能阅读文档，安装插件，下载下来之后还能阅读代码，这是它最强大的能力**

<callout emoji="✨">
我讲到这里的时候，你应该能感受到 Claude Code 是智能体了，它是能做事情的
</callout>

## 5）Cherry Studio和谷歌浏览器做什么？

> [!abstract]- 🖼 图片展示了使用Claude Code学习小龙虾的流程。从买一台服务器开始
> 图片展示了使用Claude Code学习小龙虾的流程。从买一台服务器开始，接着装Claude Code，再建立《OpenClaw管理助手》文件夹，同时装龙虾学习小龙虾并修复bug。此外，还提到Cherry Studio和谷歌浏览器两个辅助工具，Cherry Studio用于解释概念，谷歌浏览器用于查找互联网数据。该图与文档中介绍使用Claude Code学习小龙虾的步骤内容相呼应，直观呈现了操作流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LMFubPRsYovKTdxsduKczyZLnq7) · `LMFubPRsYovKTdxsduKczyZLnq7`

再看这张图，我们还有两个工具，Cherry Studio 和谷歌浏览器

谷歌浏览器就是用来帮我查找互联网上的数据。比方说我想找飞书插件的官方文档，我想找小龙虾的官方文档，我当然要通过浏览器去找。

那当我发现 Claude Code 给我吐了一堆新名词之后，我不懂一些概念的时候，我就会用 Cherry Studio 帮我去解释

你可能会问，为什么不问Claude Code？费token，我们要尽量少的去污染你的Claude Code的上下文

## 6）总结一下

> [!abstract]- 🖼 图片展示了AI时代学习任何知识的工具链。初始上下文由官方文档提供，额外上
> 图片展示了AI时代学习任何知识的工具链。初始上下文由官方文档提供，额外上下文通过互联网搜索获取，插件/指南等第三方教程提供知识来源。这些上下文共同指向CLAUDE.md，其包含项目说明书和知识来源。Claude Code作为通用智能体，负责思考、执行和沉淀，其下有安装配置、排查故障和沉淀知识三个步骤。该图与文档中总结Claude Code学习小龙虾内容相关，直观呈现其工作流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LkNBbCB2Eo31QoxxVoWcVoO0nfh) · `LkNBbCB2Eo31QoxxVoWcVoO0nfh`

OK，以上就是我用 Claude Code 去学习龙虾的所有的东西。那这里我们可以总结出几个点

<callout emoji="✨">
第一点：Claude Code 是通用智能体，它不仅能思考，而且能真正的在你电脑上执行。
这是我为什么一直推荐它的原因
第二点：Cherry Studio 是一个对话软件，它的优势在于 token 消耗的少
所以当有一些概念我不了解的时候，我就跟 Cherry Studio 去聊天，帮助我学习
第三点，互联网帮我获取最新的信息，比方说 OpenClaw 的官方地址，比方说飞书官方插件的教程
上述三者从来都不是对立的，而是互相补充的。
**你怎样才能把它们用好？这里面就是你必须极致地知道 AI 到底擅长什么，不擅长什么**
</callout>

<callout emoji="✨">
第一点，**时刻思考为你的 Agent 提供充足的上下文（尤其是官方文档）**
第二点，这个方法论不仅适用于Claude Code，ChatGPT的CodeX、Gemini的Gemini CLI，OpenCode都可以用
</callout>

> [!abstract]- 🖼 图片展示的是Cherry Studio的界面。左侧为导航栏，有“新线程”
> 图片展示的是Cherry Studio的界面。左侧为导航栏，有“新线程”“自动化”“技能”“线程”“Playground”等选项，当前选中“新线程”。右侧是新线程界面，上方有“新线程”标题，下方有“开始构建Playground”提示，下方输入框提示“向 Codex 任意提问，@ 添加文件，/ 调出命令”，下方还有GPT - 5.4、中等大小等选项。该图与上下文介绍的Cherry Studio是一个对话软件，其优势在于token消耗少，可帮助学习新概念等内容相关。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DbUib7BrToyU83xVcl4cv1JTn5d) · `DbUib7BrToyU83xVcl4cv1JTn5d`

# 四、AI时代学习任何知识的元能力

上面这个案例，我想总结一个点，就是AI时代学习任何知识的元能力

你会发现我们学习的方式完全变了。

有了 Claude Code 我们能够完完全全地在实践中进行学习，而不是以前单纯地看知识，看概念

**这里面大家可以再思考一下，你该怎么学 Claude Code？你完全可以用 Claude Code 去学 Claude Code**

所以大家觉得下面我红线标出来的这些教程价值还大吗？

真的不大了。为什么？因为你完全可以让 Claude Code 帮你现场举例子、现场实操、现场感受

> [!abstract]- 🖼 图片展示了Claude Code学习资源目录，其中“为你的Claude 
> 图片展示了Claude Code学习资源目录，其中“为你的Claude Code披上外衣”部分被红色框突出显示。该部分包含5个子目录，分别是“让它记住你的规矩：CLAUDE.md配置指南”“让重复的事情自动化：Commands、Hooks、Skills的...”“Commands实战：把常用指令存成快捷方式”“Hooks实战：让规矩自动执行，不靠AI记忆”“给Claude装上外部能力：MCP配置指南”。这些内容与上下文提到的AI时代学习任何知识的元能力相呼应，强调通过Agent结合优质上下文学习知识，列举了Claude Code学习相关资源。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/L8NJbj5Okoo1JDxDC2Tc9QxRnrg) · `L8NJbj5Okoo1JDxDC2Tc9QxRnrg`

<callout emoji="✨">
这就是我今天特别想给大家分享的 AI 时代的元能力
用 Agent 结合优质的上下文去学习任何你想学的知识
</callout>

那什么样的知识可能有价值？这思维方式，就像我们今天的这节直播、这节教程

当然还有像 Claude Code 的安装，还有像 Skill 的整体框架，这些东西是有价值的。但具体的一个细节的实操，价值感已经越来越弱了

---

至此，我已经完全论证了我那句话：**学不会 Claude Code 不要学小龙虾**。

Claude Code 一定要掌握，掌握的不是这个工具，是这个工具背后所代表的 AI 时代的新沟通方式

# 五、另外一个重要技能：沉淀你的Skill

上面一个话题我们告一段落，下面我们进入到另一个话题，沉淀你的 skill

我会认为，**当你学会用 Claude Code 学习任何知识的时候，当你又学会用 Claude Code 沉淀你的业务工作流的时候，你在 AI 时代就立于不败之地了**

<callout emoji="✨">
剩下的只是去找更多的事情去做，以及把事情做到极致的态度
</callout>

> [!abstract]- 🖼 图片展示了微信朋友圈写作、转换小绿书、发布草稿箱的业务工作流。左侧人物口
> 图片展示了微信朋友圈写作、转换小绿书、发布草稿箱的业务工作流。左侧人物口喷观点，指向“朋友圈写作”；“朋友圈写作”指向“转换小绿书”；“转换小绿书”指向“发布草稿箱”。下方有三个文件夹图标，分别对应“wechat-pyq-writer”“wechat-newspic-writer”“wechat-newspic-publisher”，与上文提到的技能相关，体现了技能在业务工作流中的应用。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SgkjbQFyGoVeUoxkDG6cL7awnDe) · `SgkjbQFyGoVeUoxkDG6cL7awnDe`

## 1）找到你完全可以使用的Skill

[[【启程必看】从这里开始/【正课阶段 3】上手智能体：桌面端与AI编程/让智能体真正能干活：自定义技能与工具协议/Claude Skills 实操指南：如何安装、如何寻找Skills|Claude Skills 实操指南：如何安装、如何寻找Skills]]

https://github.com/JimLiu/baoyu-skills

## 2）在别人的基础上优化出你的Skill

<callout emoji="✨">
我想做一键发布到公众号的 Skill，我会怎么做？
</callout>

有一种方式，我可以直接从0-1打磨属于自己的 skill，我只要找到公众号的那个开发者文档，丢给我的 Claude Code，我想它能做出来。

但还有一种更简单的方式，**就是你找到这样一个开源的 skill**

然后你用 Claude Code 去读懂它的逻辑。

在读懂它的框架和逻辑之后，看看哪些是符合你需求的，哪些是不符合的。

在此基础上去改，这时候会快很多

https://github.com/artshooter/wechat-publisher

---

当我找到这篇文档的时候，我让 Claude Code 帮我分析，我就立马知道了它基本的架构。然后我说我想打造一个发布到小绿书的，你帮我看一下接口有没有

他就帮我去搜了，他说有，然后帮我改造了一下。我的小绿书一键发布的 Skill 就有了

## 3）完全从0-1打磨属于自己的Skill

打磨提示词，打磨流程，找到合适的API

这个的话就是你自己对 AI 的理解，完全打磨属于自己的 skill，比方说我的朋友圈写作

这个也是有流程的，我想分享给大家

首先就是你一定要能用文字描述出来。如果你的文字都没有办法描述你的SOP的话，那AI更不理解

你像我的朋友圈写作skill它本质并没有什么复杂的技术问题，核心是我让它符合我的风格

那我这个时候就只能我自己先多写。

当我写了100条朋友圈之后，我对朋友圈有感觉了，然后我也找了一些方法论，最终我把自己写朋友圈的内容做成了一篇SOP

这个 SOP 既是给我自己看，也是给我的 AI 看的。然后我把它直接丢给我的 Claude Code 让它帮我做一个 skill，10分钟完全搞定

## 4）组合多个 Skill

组合多个 Skill 形成你自己的一套工作流。

那这个也很好讲，这里面核心的观点就是软件系统里面经常讲的拆分，就是边界

你像我，我上面是三个 Skill 组成一个工作流。那我也可以直接用一个 Skill 完成这三件事。

那对我来讲，我觉得朋友圈写作、小绿书转换，还有小绿书发布，它应该是三个独立的 Skill，这样的话我好维护

当你开始思考这些问题的时候，你本质就是在管理一家 Agent 组成的公司。所以你的能力绝对不仅仅是 AI 了，是各个方面的能力

你是否了解你的 Agent 的能力边界？你怎么把一个复杂的任务拆成多个细分的任务？

等等

## 5）人和AI的正向飞轮

<callout emoji="✨">
这里我必须说一个我看到的现象。
首先，只有人强，AI才能强。**但我见到太多人，他只想让 AI 强**
这样你会陷入到很深的焦虑之中。
原因很简单，你发现别人用AI为什么那么强？大家都是用Claude的模型，都是用Claude Code，为什么别人用得好，我用不好？是不是我AI技能掌握得不够？
**不是你AI技能掌握得不够。是你的综合能力的问题**
</callout>

> [!abstract]- 🖼 图片展示了人和AI的正向飞轮关系。左侧“我越强”代表综合能力+领域知识，
> 图片展示了人和AI的正向飞轮关系。左侧“我越强”代表综合能力+领域知识，右侧“AI越强”代表更精准的上下文+执行，两者通过“提供更好的上下文”和“产出更好的结果，反哺学习”相互促进。下方有两组对比，左侧“只想让AI强”焦虑，永远追不上变化；右侧“每件事都让自己变强”正向飞轮，立于不败之地。底部核心观点为“不是AI技能不够，是综合能力的问题”。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Lmd5bAqYqoTo2lxc6tqcIbC5nsb) · `Lmd5bAqYqoTo2lxc6tqcIbC5nsb`

<callout emoji="✨">
上面这段话可能有点扎心，但我觉得这就是事实。但同时它是有解的
我自己的解决方案就是：我在用AI的第一性原理就是：**做任何一件事情，都要考虑如何让我自己变强**
比如我用AI写作，我从来不搞什么一键爆款自动化工作流。我必须有我的观点，我必须要把关，必须要做最后的润色。核心的原因就是我要提高自己的写作能力，而不是让AI代替我
----
所以在社群里面有一些伙伴问的问题，我一看就知道你纯粹是为了完成一个任务。
就像 Claude Code 的安装。
我一再强调，安装不是目的，我们要在这个过程中学到一些你以前没有学到过的东西。
但我仍然见到一些伙伴，遇到问题贴群里问，遇到问题贴群里问，好像最终的目标就是把 Claude Code 安装完就可以了，发个朋友圈。
不应该是这样子的，这样子的话你永远用不好AI，你的成长速度永远跟不上AI的成长速度
-----
**我越强，AI越强，AI越强，我越强，这就是我的正向飞轮**
**我们的课程是你这个正向飞轮的起点，但很多人希望把它当成终点，这是有问题的**
</callout>

# 六、后面课程的计划

基于上面的理念，我后面的课程计划会做一些调整

我会重点讲一些你必须知道的知识。也就是说，你问AI都不知道怎么问的东西

比如服务器是什么意思？

比如 API 是什么意思？

比如 JSON 是什么意思？

再比如，如何从腾讯云或百度云这种云服务器厂商购买云服务器，并且让大家对云服务器的基本操作有一个框架性的认识

我相信，当你可以买一个远端的云服务器，并且装上 Claude Code 之后，那再叠加我今天这晚的教程，你在安装小龙虾的时候，不会遇到太多的卡点

# 写在最后

大圣AI超级个体

我特别希望大家对于 AI 的付费止于此。虽然我的课程价格只有649，

但我希望这是你为 单纯的AI 学习付的最后一笔费用

所以我特别希望能帮助大家规划一条正确的路径，并且把学习AI的底层逻辑教给大家，

让大家能够举一反三。未来不管出现任何的工具，任何的知识，你都可以轻松应对。

更重要的是，在这个过程中，**不仅 AI 越来越强，你也越来越强**

但这些仅仅是我自己的努力是不够的，需要大家的配合

你是否愿意真正地践行 AI First？

你愿不愿意花时间去真正地跟 AI 沟通，而不是急功近利地拿到你的答案？

你是否愿意遇到问题之后先自己解决？通过互联网、AI 加 Claude Code 尝试解决，当解决不了的时候，你再向社群里提问，并且愿意花时间描述清楚你的问题？

以上，共勉
