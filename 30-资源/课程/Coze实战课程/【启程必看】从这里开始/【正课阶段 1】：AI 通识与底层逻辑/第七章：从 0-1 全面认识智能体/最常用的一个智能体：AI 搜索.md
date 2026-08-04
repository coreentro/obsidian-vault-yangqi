---
title: "最常用的一个智能体：AI 搜索"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/FWizwRHHciS9w4kjRVxcqFUcnmg
node_token: FWizwRHHciS9w4kjRVxcqFUcnmg
obj_token: BtMmdPlWBoljBXx1VCjcTi0GnKe
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 1】：AI 通识与底层逻辑"
  - "第七章：从 0-1 全面认识智能体"
  - "最常用的一个智能体：AI 搜索"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 2
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 最常用的一个智能体：AI 搜索

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 1】：AI 通识与底层逻辑 › 第七章：从 0-1 全面认识智能体

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnwtk9h7ol56497isb2sb4?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，这节课我带着大家了解一个非常成熟的AI Agent产品：AI搜索

AI搜索可以说是AI Agent第一个落地并且大规模应用的产品

通过这节课，我希望你不仅对智能体有了一个更加具象的了解，而且养成AI搜索的好习惯

从以前的遇事不决问百度变成遇事不决问AI搜索

# AI搜索的原理

我们知道大模型的一个核心缺陷就是没有办法获取最新的实时数据，所以AI本身并不能当作搜索引擎

比如你问一个大模型，最近3天发生的AI圈重要事件，大模型是不知道的，因为他的训练日期是很早之前的

而传统的搜索引擎，每当我们搜索的时候出来的是一堆的列表，然后需要我们一个个鉴别阅读，很浪费时间

而AI搜索就是利用搜索引擎获取最新的数据，然后利用大模型对搜索的内容进行总结，输出更好的答案给到用户。

他的简单架构如下：

<whiteboard token="L6ZLw9MxnhwPRBbHBtzc1laHn6f"></whiteboard>

**PS：其实AI搜索也可以认为是一个RAG系统，他的知识库就是整个互联网的数据**

# 为什么AI搜索是AI Agent？

<callout emoji="💡">
**AI Agent（智能体） = LLM（大模型）+ Planning（规划）+ Memory（记忆）+ Tools（工具）**
</callout>

AI搜索正是LLM + Tools（搜索引擎）的结合体

所以AI搜索就是一个智能体

# AI搜索工具

市面上的AI搜索工具太多了

首先几乎每家的大模型产品都配置了联网搜索的能力，比如Kimi、豆包、DeepSeek等等

当然也有专门的AI搜索产品，例如：

1. 国内的秘塔搜索：https://metaso.cn/
2. 360的纳米AI搜索：https://www.n.cn/
3. 海外的Perplexity（需要魔法）:https://perplexity.ai/

我个人会比较喜欢国内的秘塔搜索，每天100次的免费搜索次数足够使用了

演示一个例子：帮我总结最近3天AI圈发生的大事件

# 写在最后

这节课我不仅想给你介绍AI搜索这个概念，我还想给你传达一个理念。

过去，学会搜索是一项非常重要的能力，所以我们经常遇事不决问百度

同样现在学会AI搜索更是一项非常重要的能力，我们要养成遇事不决问AI的习惯
