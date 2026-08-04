---
title: "和Claude Code类似的工具"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/DirqweELAizKeskzwN4cDrbInDg
node_token: DirqweELAizKeskzwN4cDrbInDg
obj_token: FZ4Cd9391ouFT5xZciNchmNBnod
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "命令行智能体：一种全新的智能体交互方式"
  - "和Claude Code类似的工具"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 750
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 和Claude Code类似的工具

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 命令行智能体：一种全新的智能体交互方式

<callout emoji="✨">
如果你对Claude Code、Claude网页端、Claude Desktop、Cowork
ChatGPT网页端、CodeX CLI、CodeX App
这些名词眼花缭乱，没有在脑子里形成一个框架，**那么这个视频一定要看**
</callout>

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/BTUQbBYfjoC3MGxo8Uxc1hg5nfg) · `BTUQbBYfjoC3MGxo8Uxc1hg5nfg`

# 写在前面

在之前的教程里，我们已经详细讲过 Claude Code和Kimi Code

但这节课我想帮大家把视野打开：不只有 Claude Code、Kimi Code

还有 OpenAI 的 Codex 和 Google 的 Gemini CLI，它们都是同一类工具

# 一、各个名词概念的关系

在使用这类智能体工具的时候，你大概率会听到以下的名词

Claude 网页端、Claude Code、Claude Desktop、Cwork；

ChatGPT网页端、CodeX CLI、CodeX

这些名词会让你眼花缭乱，你搞不清楚它们之间的关系，这一小节我先让你脑子里面有个框架

理解这类工具，你只需要抓住一个核心范式。每家大厂做 AI 产品，基本就是三层**：**

**第一层：网页版聊天，**就是你在浏览器里跟模型对话，最基础的交互方式

> [!abstract]- 🖼 图片展示的是ChatGPT addCriterion图片展示的是Chat
> 图片展示的是ChatGPT addCriterion图片展示的是ChatGPT的网页端界面。左侧有“新聊天”“搜索聊天”“图片”“应用”“深度研究”“Codex”等选项，下方还有“探索GPT”“新项目”“个人IP打造思路”等板块。右侧上方显示“ChatGPT”，
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/NYVmbWRpUo8JHTxiF5PcJ39QnMe) · `NYVmbWRpUo8JHTxiF5PcJ39QnMe`

**第二层：智能体 APP，**有图形界面的桌面应用，能操作你的本地文件，帮你自动完成多步骤的复杂任务

> [!abstract]- 🖼 图片展示的是Codex的电脑客户端界面。左侧有“新线程”“自动化”“技能
> 图片展示的是Codex的电脑客户端界面。左侧有“新线程”“自动化”“技能”“线程”“Playground”等选项，当前选中“Playground”。右侧上方显示“新线程”，下方有“开始构建 Playground”字样，下方有“Build a classic Snake game in this repo.”“Create a one-page PDF that summarizes this app.”“Create a plan to...”三个任务选项，底部有“GPT - 5.4.4”“中”等信息。该图片与文档中介绍的AI产品形态相关，展示了CLI命令行的界面示例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/TNkobbyRmo1GO3xY8hAc8yivnzc) · `TNkobbyRmo1GO3xY8hAc8yivnzc`

**第三层：CLI 命令行工具，**在终端里运行的智能体，面向开发者，用来写代码、管理项目

> [!abstract]- 🖼 图片展示了Claude Code的命令行端界面。界面上方显示“Local
> 图片展示了Claude Code的命令行端界面。界面上方显示“Local Terminal”标签，下方有“Opus 4.6 (1M context)”和“内容OS git:(master)”等信息。画面中间有“Context 0%”字样。图片下方有红色文字标注“这是Claude Code的命令行端”。该图片与文档中介绍AI产品形态的内容相关，直观呈现了命令行工具这一产品形态，帮助读者更好地理解AI产品在第三层的实现形式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/J2p8bjonuoo4FNxy6Iwc9FSen7I) · `J2p8bjonuoo4FNxy6Iwc9FSen7I`

---

> [!abstract]- 🖼 图片展示了了claudeforcode.com网站上展示的AI产品形态框
> 图片展示了了claudeforcode.com网站上展示的AI产品形态框架。分为网页版聊天、智能体APP、CLI命令行三层。网页版聊天有Anthropic的Claude.ai、OpenAI的ChatGPT、Google的Gemini；智能体APP有Anthropic的Cowork、OpenAI的Codex APP；CLI命令行有Anthropic的Claude Code、OpenAI的Codex CLI、Google的Gemini CLI。该图与上下文紧密相关，直观呈现了文档中提到的每家大厂AI产品形态，帮助理解AI产品形态的层次及对应产品。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/B8vKbfgBxomsWHxKObVco5RTnBh) · `B8vKbfgBxomsWHxKObVco5RTnBh`

**以后不管哪家大厂再出新的 AI 产品，你用这个框架去套，大概率都能对上**

有了模型和 API 之后，产品形态无非就这几种：网页版聊天、带图形界面的智能体 APP、命令行工具

# 一、为什么要讲CodeX？

**不是因为 Codex 比 Claude Code 更好用。**

它们都是通用智能体，都是同一类工具，核心能力大同小异

推荐大家了解 Codex，有几个很实际的原因：

**第一，Codex 可以直接关联 ChatGPT 的官方订阅**

ChatGPT Plus 现在 20 美金一个月，这个价格不算贵。

而且相比其他平台，**ChatGPT 的封号策略宽松很多，不会动不动就把你号封了**

再加上 OpenAI 这边一直在重置额度，给的量还挺足的。所以用 ChatGPT 订阅来驱动 Codex，性价比很不错

<callout emoji="✨">
但需要注意，各家的策略都是随着时间而变化的
这个教程写于2026年的3月18号，也许在一个月后，GPT 也不会有那么的善良
</callout>

**第二，API 渠道价格便宜**

闲鱼上可以买到一些 Codex 的 API，价格特别便宜

<callout emoji="✨">
**提醒一句，便宜不能保证稳定和质量，但确实好用，适合练手和日常开发**
**这里不做任何推荐，不做任何背书，也不要问我哪家好**
</callout>

> [!abstract]- 🖼 图片展示的是闲鱼平台上的Codex月卡相关商品页面。页面上方搜索框显示“
> 图片展示的是闲鱼平台上的Codex月卡相关商品页面。页面上方搜索框显示“codex月卡”，下方有多个商品推荐，如“拒绝套路”“codex稳定中转”“business teams席位拼车”等，价格从2.88元/天到6.90元不等，部分商品显示已售罄或已售出。页面还设有筛选栏，可按价格、降价、新发、区域等条件筛选商品。该图片与文档中提到的闲鱼上可买到Codex API，价格便宜的内容相关，直观呈现了相关商品情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BmnqbR4sDoO3scxJqv3cFowsn2c) · `BmnqbR4sDoO3scxJqv3cFowsn2c`

**第三，GPT-5.5 很适合写代码**

Codex 目前默认推荐的模型是 GPT-5.5，这个模型在编程方面的表现非常强

社群里有个伙伴讲：**Claude 是文科生，GPT-5.5 是理科生。**

Claude 的模型在内容创作、文案撰写、分析总结这些方面非常出色；

而 GPT-5.4 在代码生成、逻辑推理、工程实现上很强

> [!abstract]- 🖼 图片展示了Codex + GPT addCriterionClaude 
> 图片展示了Codex + GPT addCriterionClaude Code + Claude的最佳实践。左侧为Codex + GPT - 5.44，被称 addCriterion“理科生”标识，包含代码生成、逻辑推理、工程实现等功能；右侧为Claude Code +
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VVyKbRqYvohwgRxW9lqcTkVBnIb) · `VVyKbRqYvohwgRxW9lqcTkVBnIb`

<callout emoji="✨">
**Claude 写代码也很强，不要问我说两者到底谁强哦**
</callout>

所以现在很多人的**最佳实践**是这样的：

**用 Codex 接上 ChatGPT 的订阅，专门用来写代码；用 Claude Code 接上 Claude 的模型，专门用来写内容**

两个工具各司其职，发挥各自模型的长处

# 二、Codex APP 上手指南

CodeX有两种形态：电脑客户端和命令行，这里我们先讲电脑客户端

使用 Codex APP 分两步走：**第一步是下载安装，第二步是接入模型。** 

这两步是分开的，你装的是工具，接的是大脑

<callout emoji="✨">
下面这张图几乎适用于所有的情况
</callout>

> [!abstract]- 🖼 图片展示了Codex APP上手指南中下载安装和接入模型的步骤。第一步是
> 图片展示了Codex APP上手指南中下载安装和接入模型的步骤。第一步是下载安装，分为macOS客户端和Windows客户端两个选项；箭头指向第二步接入模型。接入模型有ChatGPT官方订阅和第三方API Key两种方式，前者推荐，需$20/月，登录即用无需额外付费；后者灵活便宜，稳定性自行甄别。该图与上下文紧密相关，直观呈现了上手操作的流程和选择。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Ww4xbnSYdo8coExIwf9c01tMnDe) · `Ww4xbnSYdo8coExIwf9c01tMnDe`

## 第一步：下载安装

Codex APP 是 OpenAI 官方推出的桌面应用，目前支持 macOS和Windows

https://openai.com/zh-Hans-CN/codex/

根据你打开的电脑系统，决定了它可以下载安装的版本

<grid>

> [!abstract]- 🖼 图片展示了Codex APP的界面。上方有Codex的标志及“通过免费套
> 图片展示了Codex APP的界面。上方有Codex的标志及“通过免费套餐和Go套餐试用；其他套餐用户可限时享受双倍速率额度”的文字，下方有“下载适用于macOS的版本”按钮。界面左侧有“Threads”“Skills”“Automations”等选项，右侧显示了“Create Codex app CTA”等任务，以及“src/hero.txt”文件的代码内容。该图片与文档中“第一步：下载安装”部分对应，直观呈现了安装好Codex APP后的界面情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YosDblkeYoGEBgxP5VOcYldOnZb) · `YosDblkeYoGEBgxP5VOcYldOnZb`

> [!abstract]- 🖼 图片展示了OpenAI官网Codex页面。页面上方有导航栏，中间是Cod
> 图片展示了OpenAI官网Codex页面。页面上方有导航栏，中间是Codex标志及名称，下方文字介绍通过免费套餐和Go套餐试用，其他套餐用户可同时享受双倍速度额度。下方有“下载Windows版”按钮。页面右侧是Codex APP界面，显示“Create Codex app CTA”等操作选项，下方有代码编辑区域，显示了部分代码内容及文件更改情况。该图片与文档中下载安装Codex APP的内容相关，直观呈现了下载后的界面样式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AIaEb5h20oijKuxE3Z4cBFvNn7d) · `AIaEb5h20oijKuxE3Z4cBFvNn7d`

</grid>

安装好之后打开 Codex APP，你会看到这样的选项，接下来进入第二步

> [!abstract]- 🖼 图片展示了Codex APP的登录界面。界面上方显示“Codex”，中间
> 图片展示了Codex APP的登录界面。界面上方显示“Codex”，中间有一个带有“1”和“-”的云朵图案，下方文字为“欢迎使用 Codex 与代理协同构建的最优方式”。下方有两个按钮，黑色按钮上写“继续使用 ChatGPT 登录”，白色按钮上写“输入 API 密钥”。该图片对应文档中“第一步：下载安装”之后的“第二步：接入模型”部分，说明安装好Codex APP后，接下来要进行的登录操作，可选择使用ChatGPT登录或输入API密钥登录。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AshpbreOXo17YQxmp1UcdtINnxc) · `AshpbreOXo17YQxmp1UcdtINnxc`

## 第二步：接入模型

装好了工具，接下来要给它接上大脑。你有两种选择：

**方式一：接入 ChatGPT 官方订阅**

打开 Codex 后选择继续使用ChatGPT登陆，用浏览器登录你的 ChatGPT 账号。

ChatGPT Plus（20 美金/月）、Pro、Business、Enterprise 等付费计划都包含 Codex 的使用权限，不需要额外付费

关于 ChatGPT 的订阅，核心要解决两个问题：

1. 网络的问题
2. 付款的问题

关于网络的问题，大家自行解决。而且 ChatGPT 对于网络的要求不高

**至于如何解决付款和账号的问题，请看下一节课**

[[国内如何使用上CodeX]]

**方式二：接入API Key**

如果你手上有第三方的 API Key（比如在闲鱼上买的），可以直接输入

这个大家自行去闲鱼上或者找攻略

> [!abstract]- 🖼 图片展示的是闲鱼平台中关于“codex月卡”的搜索结果页面。页面上方有搜
> 图片展示的是闲鱼平台中关于“codex月卡”的搜索结果页面。页面上方有搜索框，显示“codex月卡”。下方有多个商品推荐，如“拒绝套路”“codex稳定中转”“business teams席位拼车”等，每个商品下方有价格、评价人数、卖家信息等信息。其中，“拒绝套路”商品价格为2.88元/天，每天100刀额度；“codex稳定中转”商品价格为1.10元，已售100+；“business teams席位拼车”商品价格为6.90元，549人想要。该图片与文档中介绍接入API Key的方式相关，展示了在闲鱼上搜索codex月卡的情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LJ4qbIwpVoKOIJxfHgtcy7Kyn8b) · `LJ4qbIwpVoKOIJxfHgtcy7Kyn8b`

# 三、Codex CLI 上手指南

## 第一步：下载安装

你也可以选择命令行的方式来使用CodeX

这里我就不出详细的教程了。如果到现在为止你都没有办法自己去安装 CodeX 命令行工具，那你要回去温习一下 Claude Code 的安装过程

我给到大家直接的官网文档：https://developers.openai.com/codex/cli

> [!abstract]- 🖼 图片展示了Codex CLI的设置步骤，分为安装、运行和升级三部分。安装
> 图片展示了Codex CLI的设置步骤，分为安装、运行和升级三部分。安装步骤显示使用npm安装Codex CLI的命令“npm i -g @openai/codex”；运行步骤提示在终端运行“codex”，首次运行需登录认证；升级步骤给出与安装相同的命令用于升级。图片底部突出显示“如果是Codex新手，请阅读最佳实践指南”。该图片对应文档中“Codex CLI上手指南”的“下载安装”部分，为用户提供了直观的安装、使用及升级操作指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JU9XbC17Po63bTxL6b1ccBrUnew) · `JU9XbC17Po63bTxL6b1ccBrUnew`

和 Claude Code 一样，Codex CLI 也可以使用 Trae 的插件，套上一个可视化的页面

## 第二步：接入模型

**这里仍然使用我们的老朋友，CC-Switch**

使用姿势和 Claude Code 接入外部 API 一模一样

> [!abstract]- 🖼 图片中问中“CC Switch上接入CodeX”对应的内容。图中展示了C
> 图片中问中“CC Switch上接入CodeX”对应的内容。图中展示了CC Switch界面，上方有Claude、Codex、Gemini等图标，Codex图标被红色框突出显示。下方有一个输入框，显示网址“https://aixj.vip”，并有“使用中”标识。图片下方配有红色箭头，指向Codex图标，旁边标注“CC Switch上接入CodeX”，直观呈现了在CC Switch上接入CodeX的操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UdkwbqQa4oysZ7xNHkqcE1KAnoc) · `UdkwbqQa4oysZ7xNHkqcE1KAnoc`

# 四、CodeX的使用教程

这个教程在B站上有很多，我给大家找了一个，也可以在B站自行搜索

CodeX保姆级教程

https://www.bilibili.com/video/BV1Kk9kBAEJv/?spm_id_from=333.337.search-card.all.click&vd_source=e94f42ead4c2e95f4b13bec257d95670

# 五、谷歌的Gemini CLI

Google 的 Gemini CLI 也是同一类工具，我自己没有用过，但可以想象它也可以接第三方的 API，也可以使用谷歌的官方订阅

这是官方的安装教程：https://geminicli.com/

> [!abstract]- 🖼 图片展示了谷歌的Gemini CLI相关内容。上方文字为“Build >
> 图片展示了谷歌的Gemini CLI相关内容。上方文字为“Build > debug & deploy with AI”，下方介绍可从终端使用Gemini 3进行查询、编辑大代码库、从图像或PDF生成应用程序及自动化复杂工作流程等。中间有安装命令“$ npm install -g @google/gemini-cli”，还有“More install options”选项。底部展示了“> GEMINI”字样及使用提示，如询问问题、编辑文件、运行命令等。此图位于介绍谷歌Gemini CLI官方安装教程处，是对其功能及安装的直观呈现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XpFEbOD91oMoqxxJXFTcCiRkn7b) · `XpFEbOD91oMoqxxJXFTcCiRkn7b`

# 六、开源的OpenCode

<callout emoji="✨">
这是一个开源的工具，对标的是 Claude Code
如有需要请自行用AI加联网搜索它们的区别，我自己并没有用 OpenCode
</callout>

## 第一步：下载与安装

下载地址：https://opencode.ai/download

它支持命令行方式，也支持Windows的客户端和Mac OS的客户端

![图片展示了OpenCode的下载安装页面。上方有OpenCode图标及“下载OpenCode适用于macOS、Windows和Linux的Beta版”字样。下方分为两部分，\[1\]为OpenCode终端安装命令，包括curl、npm、bun、brew等指令；\[2\]为OpenCode桌面版（Beta）下载，有macOS（Apple Silicon）、macOS（Intel）、Windows（x64））等选项，其中Windows（x64）选项被红色框突出显示。该图片与文档中OpenCode下载与安装的内容相关，直观呈现了下载安装步骤及桌面版下载选项。](https://feishu.cn/file/GRFdbV1MOoTcMAx8OBgcvAETnac)

## 第二步：接入外部大模型

**这里仍然使用我们的老朋友，CC-Switch**

使用姿势和 Claude Code 接入外部 API 一模一样

> [!abstract]- 🖼 图片展示了OpenCode接入外部大模型时的界面。界面上方有多个图标，其
> 图片展示了OpenCode接入外部大模型时的界面。界面上方有多个图标，其中“OpenCode”图标被红色箭头指向。下方提示“还没有添加任何供应商”，并有“导入当前配置”和“添加供应商”两个按钮。该图片与文档中介绍OpenCode接入外部大模型的内容相关，说明在使用OpenCode时，可通过添加供应商来接入外部大模型，使用姿势与Claude Code接入外部API相同。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HdPpbPPHNoeWnrxPaQPcg9SRnHf) · `HdPpbPPHNoeWnrxPaQPcg9SRnHf`

# 六、写在最后

这节课我希望大家记住一个框架：

**网页聊天 → 智能体 APP → CLI 命令行，**以后再出新的 AI 产品，大概率还是这个模式

**严格来讲，这也不是一篇使用和安装教程，更多的是一个信息差**

但我相信有了前面 Claude Code 给大家打下坚实的基础，安装 Code X 和 Gemini CLI应该是非常简单的

而教程相关的东西，你去网络上一搜一大堆

我希望你听完这节课，脑子里有一个完整的框架，不要再被这些所谓的新名词牵着走了

> [!abstract]- 🖼 图片展示了Code X的安装与接入模型流程。第一步是下载安装，分为mac
> 图片展示了Code X的安装与接入模型流程。第一步是下载安装，分为macOS客户端和箭头指向左侧框和Windows客户端。第二步是接入模型，推荐使用ChatGPT官方订阅，$20/月，登录即用，无需额外付费；也可选择第三方API Key，灵活便宜，稳定性自行甄别。该图与上下文紧密相关，是对Code X安装及接入模型操作步骤的直观呈现，帮助用户清晰了解操作流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/U4lqbJ5grop5CVxT19ocqo50nDO) · `U4lqbJ5grop5CVxT19ocqo50nDO`
