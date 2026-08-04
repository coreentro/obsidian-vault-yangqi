---
title: "手把手演示如何用AI完成一个代码案例"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/CPtSwJTgLiquYwk0POEclpzUnKh
node_token: CPtSwJTgLiquYwk0POEclpzUnKh
obj_token: H2rIdEwNQopUeix3lH8c8hDqndf
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体高级课程"
  - "第十二章：代码节点与AI编程入门技术讲解"
  - "手把手演示如何用AI完成一个代码案例"
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

# 手把手演示如何用AI完成一个代码案例

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体高级课程 › 第十二章：代码节点与AI编程入门技术讲解

智能体地址：https://www.coze.cn/space/7362748064240877602/bot/7486862233411026959

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnjz5n9b52l2m1r6nrd79w?from=ccm" type="iframe"></readonly-block>

# 写在前

大家好，我是大圣，这节课手把手带大家演示下我是如何用AI完成一个代码案例的

这节课，我们仍然是采用输入和输出的思想 + 那个代码提示词

# 需求分析

当输入和输出比较复杂的时候，在开始跟大模型对话之前，你需要先静下心来，整理你的输入和期望的输出

这一步很重要，最好是将输入和输出的结构纸质化

我们直接看案例

## 定义输出

```JSON
{
    "news": [
        {
            "title": "标题",
            "summary": "摘要",
            "url": "文章地址",
            "source": "搜狐/头条"
        }
    ]
}
```

这是一个非常典型的转换代码（胶水代码）

这段代码我们完全可以让大模型帮我们写

# 代码节点

# 让大模型写代码

**这里面有个问题就是大模型怎么知道你输出的字段从哪里获取呢？这里有两个点**

1. JSON的key本身是英文，是有语义的，如果语义清楚，大模型就可以自动识别
2. 就算大模型识别错了也没关系，**你再多几轮对话告诉他正确的字段即可**
