---
title: "AI每日早报【智能体】"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/Wxg3wN3JKi3qPokFggycyYhDn4b
node_token: Wxg3wN3JKi3qPokFggycyYhDn4b
obj_token: JkIVdOWEeoJiPCxoSBOc0UixnTb
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体中级课程"
  - "第十章：Coze中阶实战案例解析"
  - "AI每日早报【智能体】"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 5
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# AI每日早报【智能体】

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体中级课程 › 第十章：Coze中阶实战案例解析

智能体地址：https://www.coze.cn/space/7362748064240877602/bot/7471196385732362294

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnki48a3zzj68q62l378pu?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，这节课带着大家手把手搓一个AI每日早报

注意，这个AI日报本质还是一个Demo，关于异常等我们都没有处理，这里给大家展示一个思路

# 需求分析

我们经常会在一些社群里收到一些AI日报，这个案例我们就来简单的实现一个AI日报的需求

第一步：我们要找到一个信息源，可以选择：https://www.aibase.com/zh/news

> [!abstract]- 🖼 图片展示了AI日报案例中从信息源获取的新闻资讯内容。上方显示类型为“新闻
> 图片展示了AI日报案例中从信息源获取的新闻资讯内容。上方显示类型为“新闻资讯”，有“热门视频”按钮。下方有三篇新闻，每篇新闻包含标题、发布平台及时间。第一篇是启明星辰整合DeepSeek大模型的新闻，发布于33分钟前；第二篇是斯坦福&华大推出AI训练新方法S1的新闻，发布于1小时前；第三篇是OpenAI联合创始人短暂任职Anthropic后再次离职的新闻，发布于1小时前。图片与上下文紧密相关，直观呈现了AI日报所需信息源的内容。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HOtzbbFk5oM2qkxLCWkcMWsCnfb) · `HOtzbbFk5oM2qkxLCWkcMWsCnfb`

第二步：我们要通过插件的方式将页面涉及的链接获取下来

第三步：由于这里有很多的链接，我们找到文章的链接，然后提取前6个

第四步：根据每个文章的链接获取文章内容，并且进行总结

第五步：最后使用画板的方式生成图片，进行输出

**我们直接看案例：大圣教学｜中级案例｜AI日报长图**
