---
title: "Coze对话流｜创建对话流"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/GeRywRLgniFDOvkGvIccmXQdnoh
node_token: GeRywRLgniFDOvkGvIccmXQdnoh
obj_token: UCiLdRAaDo1bsvxlY8nc9rdenHe
obj_type: docx
space_id: 7334260678754041858
space_name: "付费星球/AI零基础"
depth: 3
breadcrumb:
  - "AI零基础到智能体高手"
  - "Coze智能体从入门到进阶"
  - "第六章｜对话流与会话"
  - "Coze对话流｜创建对话流"
obj_create_time: 1734133952
obj_edit_time: 1736953643
creator: ou_4f9742f370819a3c899baacbc140aed2
owner: ou_4f9742f370819a3c899baacbc140aed2
revision_id: 329
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - AI零基础到智能体高手
---

# Coze对话流｜创建对话流

> [!info] 位置
> AI零基础到智能体高手 › Coze智能体从入门到进阶 › 第六章｜对话流与会话

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcn5m3o7r1sia33qv2493vg?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，今天这节课我们来给大家讲解对话流的概念。

这里我们要先了解下对话流的前世今生，在Coze刚出来的时候，只有工作流，并没有对话流的概念。

后来因为在工作流中没有办法让大模型感知上下文，因此推出了对话流的概念。

对话流通过增加了一个会话的概念，每次和对话流的对话都会被存储在会话中。

然后每次在对话流中使用大模型相关节点的的时候，就可以把之前所有的对话从会话中取出来，构成上下文给到大模型，从而让对话流中的大模型节点拥有了感知这个对话的能力

这也是为什么叫对话流的原因，因为需要感知上下文的场景基本都是对话类场景，比如智能客服，虚拟陪伴等，所以这个对话流含义很贴切

# 初识对话流

我们直接通过案例进行学习

案例名称：大圣教学｜对话流

# 几点注意

1. 对话流的开始节点，直接使用USER_INPUT即可，一般不会加其他参数
2. 对话流经常配合Coze的单Agent（对话流模式）使用
