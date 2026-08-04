---
title: "Coze知识库：工作流中使用知识库"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/OJdVwxvoAitiO3ke86IcXck1noc
node_token: OJdVwxvoAitiO3ke86IcXck1noc
obj_token: SmyXdcZJOoyclwxBRn4cpp8yngq
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体中级课程"
  - "第七章：Coze知识库与数据库功能讲解"
  - "Coze知识库：工作流中使用知识库"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 4
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# Coze知识库：工作流中使用知识库

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体中级课程 › 第七章：Coze知识库与数据库功能讲解

智能体地址：https://www.coze.cn/space/7362748064240877602/bot/7446623496387592226

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcn4x59kc79x48s2xg28v57?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，前面我们讲解了文本、表格和图片类型的知识库，我们的案例并没有使用到工作流

这节课我们将教大家如何在工作流中使用知识库

<callout emoji="💡"><p>在此之前我强烈建议你了解一下什么是RAG：[Coze知识库｜1.6万字RAG保姆级教程](https://axsppz4oyvj.feishu.cn/wiki/Gfn3wf0NVisB1zks1CUcE6s4nOb)</p><p></p><p>上述这篇文章1.6万字，还有对应的视频，花费两个小时了解下RAG对你使用Coze的知识库以及其能力边界都会有很大的帮助</p><p></p><p><b>学习Coze的知识库使用本身很简单，重点在于了解RAG这项技术的边界</b></p></callout>

PS：下文中我们不再对知识库的原理进行说明，而是直接讲解Coze的知识库创建和使用

# 创建知识库

**这一部分直接参考视频教学**

# Coze本身的总结提示词

```Plain Text
\n根据引用的内容回答问题: \n 1.如果引用的内容里面包含 <img src=\"\"> 的标签, 标签里的 src 字段表示图片地址, 需要在回答问题的时候展示出去, 输出格式为\"![图片名称](图片地址)\" 。 \n 2.如果引用的内容不包含 <img src=\"\"> 的标签, 你回答问题时不需要展示图片 。 \n 例如：\n 如果内容为<img src=\"https://example.com/image.jpg\">一只小猫，你的输出应为：![一只小猫](https://example.com/image.jpg)。\n 如果内容为<img src=\"https://example.com/image1.jpg\">一只小猫 和 <img src=\"https://example.com/image2.jpg\">一只小狗 和 <img src=\"https://example.com/image3.jpg\">一只小牛，你的输出应为：![一只小猫](https://example.com/image1.jpg) 和 ![一只小狗](https://example.com/image2.jpg) 和 ![一只小牛](https://example.com/image3.jpg)

The following is the content of the data set you can refer to: 
question is:
```

# 案例名称

Coze空间搜索：大圣教学｜知识库节点（工作流）
