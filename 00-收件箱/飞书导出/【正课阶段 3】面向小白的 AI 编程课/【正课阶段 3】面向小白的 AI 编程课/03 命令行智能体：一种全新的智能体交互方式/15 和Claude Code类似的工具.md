---
title: "和Claude Code类似的工具"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/DirqweELAizKeskzwN4cDrbInDg"
node_token: "DirqweELAizKeskzwN4cDrbInDg"
obj_type: "docx"
document_id: "FZ4Cd9391ouFT5xZciNchmNBnod"
revision_id: "748"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/DirqweELAizKeskzwN4cDrbInDg>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>和Claude Code类似的工具</title>

<callout emoji="✨">
如果你对Claude Code、Claude网页端、Claude Desktop、Cowork
ChatGPT网页端、CodeX CLI、CodeX App
这些名词眼花缭乱，没有在脑子里形成一个框架，**那么这个视频一定要看**
</callout>



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="BTUQbBYfjoC3MGxo8Uxc1hg5nfg"/></figure>



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



![](https://feishu.cn/file/NYVmbWRpUo8JHTxiF5PcJ39QnMe)



**第二层：智能体 APP，**有图形界面的桌面应用，能操作你的本地文件，帮你自动完成多步骤的复杂任务



![](https://feishu.cn/file/TNkobbyRmo1GO3xY8hAc8yivnzc)



**第三层：CLI 命令行工具，**在终端里运行的智能体，面向开发者，用来写代码、管理项目



![](https://feishu.cn/file/J2p8bjonuoo4FNxy6Iwc9FSen7I)



---

![](https://feishu.cn/file/B8vKbfgBxomsWHxKObVco5RTnBh)



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



![](https://feishu.cn/file/BmnqbR4sDoO3scxJqv3cFowsn2c)



**第三，GPT-5.5 很适合写代码**



Codex 目前默认推荐的模型是 GPT-5.5，这个模型在编程方面的表现非常强



社群里有个伙伴讲：**Claude 是文科生，GPT-5.5 是理科生。**



Claude 的模型在内容创作、文案撰写、分析总结这些方面非常出色；



而 GPT-5.4 在代码生成、逻辑推理、工程实现上很强



![](https://feishu.cn/file/VVyKbRqYvohwgRxW9lqcTkVBnIb)



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



![](https://feishu.cn/file/Ww4xbnSYdo8coExIwf9c01tMnDe)



## 第一步：下载安装



Codex APP 是 OpenAI 官方推出的桌面应用，目前支持 macOS和Windows



https://openai.com/zh-Hans-CN/codex/



根据你打开的电脑系统，决定了它可以下载安装的版本



<grid>
<column width-ratio="0.449606">
![](https://feishu.cn/file/YosDblkeYoGEBgxP5VOcYldOnZb)
</column>
<column width-ratio="0.550394">
![](https://feishu.cn/file/AIaEb5h20oijKuxE3Z4cBFvNn7d)
</column>
</grid>





安装好之后打开 Codex APP，你会看到这样的选项，接下来进入第二步



![](https://feishu.cn/file/AshpbreOXo17YQxmp1UcdtINnxc)



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



<cite doc-id="GKHzw3DuZifd9EkZ3BZckUuvnbg" file-type="wiki" title="国内如何使用上CodeX" type="doc"></cite>



**方式二：接入API Key**



如果你手上有第三方的 API Key（比如在闲鱼上买的），可以直接输入



这个大家自行去闲鱼上或者找攻略



![](https://feishu.cn/file/LJ4qbIwpVoKOIJxfHgtcy7Kyn8b)



# 三、Codex CLI 上手指南



## 第一步：下载安装



你也可以选择命令行的方式来使用CodeX



这里我就不出详细的教程了。如果到现在为止你都没有办法自己去安装 CodeX 命令行工具，那你要回去温习一下 Claude Code 的安装过程



我给到大家直接的官网文档：https://developers.openai.com/codex/cli



![](https://feishu.cn/file/JU9XbC17Po63bTxL6b1ccBrUnew)



和 Claude Code 一样，Codex CLI 也可以使用 Trae 的插件，套上一个可视化的页面



## 第二步：接入模型



**这里仍然使用我们的老朋友，CC-Switch**



使用姿势和 Claude Code 接入外部 API 一模一样



![](https://feishu.cn/file/UdkwbqQa4oysZ7xNHkqcE1KAnoc)



# 四、CodeX的使用教程



这个教程在B站上有很多，我给大家找了一个，也可以在B站自行搜索



CodeX保姆级教程



https://www.bilibili.com/video/BV1Kk9kBAEJv/?spm_id_from=333.337.search-card.all.click&vd_source=e94f42ead4c2e95f4b13bec257d95670



# 五、谷歌的Gemini CLI



Google 的 Gemini CLI 也是同一类工具，我自己没有用过，但可以想象它也可以接第三方的 API，也可以使用谷歌的官方订阅



这是官方的安装教程：https://geminicli.com/



![](https://feishu.cn/file/XpFEbOD91oMoqxxJXFTcCiRkn7b)



# 六、开源的OpenCode



<callout emoji="✨">
这是一个开源的工具，对标的是 Claude Code
如有需要请自行用AI加联网搜索它们的区别，我自己并没有用 OpenCode
</callout>



## 第一步：下载与安装



下载地址：https://opencode.ai/download



它支持命令行方式，也支持Windows的客户端和Mac OS的客户端



![](https://feishu.cn/file/GRFdbV1MOoTcMAx8OBgcvAETnac)



## 第二步：接入外部大模型



**这里仍然使用我们的老朋友，CC-Switch**



使用姿势和 Claude Code 接入外部 API 一模一样



![](https://feishu.cn/file/HdPpbPPHNoeWnrxPaQPcg9SRnHf)



# 六、写在最后



这节课我希望大家记住一个框架：



**网页聊天 → 智能体 APP → CLI 命令行，**以后再出新的 AI 产品，大概率还是这个模式



**严格来讲，这也不是一篇使用和安装教程，更多的是一个信息差**



但我相信有了前面 Claude Code 给大家打下坚实的基础，安装 Code X 和 Gemini CLI应该是非常简单的



而教程相关的东西，你去网络上一搜一大堆



我希望你听完这节课，脑子里有一个完整的框架，不要再被这些所谓的新名词牵着走了



![](https://feishu.cn/file/U4lqbJ5grop5CVxT19ocqo50nDO)
