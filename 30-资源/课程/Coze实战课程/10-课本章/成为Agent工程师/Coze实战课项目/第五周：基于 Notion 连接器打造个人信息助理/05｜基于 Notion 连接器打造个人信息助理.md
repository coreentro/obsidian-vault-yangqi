---
title: "05｜基于 Notion 连接器打造个人信息助理"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/UVYwws8o2iUfsqk6n5GczSmRnPe
node_token: UVYwws8o2iUfsqk6n5GczSmRnPe
obj_token: IgUZdmMf8oWBtJxZHeMcmA97nhe
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 3
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "第五周：基于 Notion 连接器打造个人信息助理"
  - "05｜基于 Notion 连接器打造个人信息助理"
obj_create_time: 1721228034
obj_edit_time: 1726922672
creator: ou_4f9742f370819a3c899baacbc140aed2
owner: ou_4f9742f370819a3c899baacbc140aed2
revision_id: 1056
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# 05｜基于 Notion 连接器打造个人信息助理

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 第五周：基于 Notion 连接器打造个人信息助理

# 05｜基于 Notion 连接器打造个人信息助理

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnmre5qy4r1lpb241e8ax2?from=ccm" type="iframe"></readonly-block>

## 案例及测试用例

Notion Copilot 体验地址：https://www.coze.cn/s/iMMVGwrp/

> [!abstract]- 🖼 图片展示了Coze平台的Bot Store界面。界面左侧有导航栏，可选择
> 图片展示了Coze平台的Bot Store界面。界面左侧有导航栏，可选择Explore、Bot Store等选项。右侧上方显示“Bot Store”，并有搜索框。中间部分突出显示“Your powerful Notion copilot”及“Try now”按钮，下方有多个Bot推荐，如Create Images with AI、Learn Anything - AI for Self等。右侧有一个名为“Harvest (Your Notion Copilot)”的Bot，其图标为黑色背景，带有金色装饰。该图片与文档中介绍Coze平台Bot Store的内容相关，展示了平台上的Bot资源。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/PDKKbUxIcolQzWx9HPUcQMTynhq) · `PDKKbUxIcolQzWx9HPUcQMTynhq`

保存页面测试用例：

- 长文深度解析 Coze 的多 Agent 模式的实现机制https://mp.weixin.qq.com/s/8_998tbRd6yuzZwnKR2crA
- 三万字深度对谈：为何 OpenAI 做不出革命性交互的产品？AI 是新的科技泡沫吗？https://mp.weixin.qq.com/s/ggLU3KmXDS01uA_iMPKLZA
- ChatGPT Is a Blurry JPEG of the Webhttps://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web

搜索测试用例：

与 RAG 有关的技术有哪些？

Reranker 对 RAG 的作用是什么？

## Part 1：Coze + Notion = 个人信息助理

#### Notion 作为个人信息库

- 数据库，我的信息库（Readings）
- 页面属性，页面内容，Block types
- [Notion AI Q&A](https://www.notion.so/blog/introducing-q-and-a)
- Notion 的免费功能已经足够强大！

#### Notion 连接器

- Notion API - https://developers.notion.com/reference/intro
- Notion 连接器（国内版）- https://www.coze.cn/store/plugin/7368111600210853899
- Notion 连接器（国际版）- https://www.coze.com/store/plugin/7368097062283640838
- Coze 官方的 Notion 插件 - https://www.coze.com/store/plugin/7329369142111322113（可以对比下）

####  将 Coze Bot 连接至 Notion 数据库

- 连接器 API：`connectToNotion`
- Bot 提示词
- 快捷指令

## Part 2：信息入库及索引（剪藏）

#### Bot 工作流：`save_page`

- 连接器 API：`saveToNotion`
- Bot 提示词

#### Bot 工作流：`save_page_with_properties`

- 连接器 API：`getPage`
- 连接器 API：`saveToNotion` 
- LLM：提取页面属性
- 快捷指令
- 实践中的可能需要优化的点

## Part 3：信息检索及问答（RAG）

#### RAG，[Dr. Know](https://www.coze.com/space/7370590980090642438/bot/7376552750731329542)

<callout emoji="⛱️">
RAG = Retrieval-Augmented Generation
</callout>

> [!abstract]- 🖼 图片展示了论文“FRESHLLMs: Refreshing Large 
> 图片展示了论文“FRESHLLMs: Refreshing Large Language Models with Search Engine Augmentation”的封面及部分内容，作者包括Tu Vu等。图片下方文字介绍了LLM（大型语言模型）的三个缺陷：无法实时获取最新信息，有“幻觉”问题，无法给出准确引用来源。这些缺陷表明LLM在获取和处理信息方面存在不足，而搜索引擎能提供更准确的信息，可作为LLM“推理”的依据。该图片与上下文关于LLM和搜索引擎在信息获取方面的对比分析紧密相关。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/NjOdbtim8oQFysxx7iHcl4LNn6c) · `NjOdbtim8oQFysxx7iHcl4LNn6c`

<readonly-block href="https://player.bilibili.com/player.html?bvid=1Bx4y1n7cB&amp;spm_id_from=333.999.list.card_archive.click" type="iframe"></readonly-block>

#### [Re2G: Retrieve, Rerank, Generate](https://arxiv.org/abs/2207.06300)

<callout emoji="💥">
经过一段时间沉淀，有用的 Agent 技术（暂时）留下了：**工作流**和 **RAG**。
</callout>

> [!abstract]- 🖼 图片展示了Jina Reranker v2的架构。从文档开始，经分块阅读
> 图片展示了Jina Reranker v2的架构。从文档开始，经分块阅读（Chunking）后，进入Embedding model生成Embeddings，再存入VectorDB。Query通过Embedding model生成Embeddings，与VectorDB中的Embeddings进行Embedding similarity查询，获取Query results，筛选出Relevant chunks。这些Relevant chunks通过Prompt template与prompts结合，生成独立回答，再由LLM总结并生成最终答案。右侧有Search、Recommender、Copilot、Conversational AI图标，分别对应搜索、推荐、助手、对话功能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OHQDbQ8kHonnIHxoGhucZ4KUnMh) · `OHQDbQ8kHonnIHxoGhucZ4KUnMh`

> [!abstract]- 🖼 图片展示了RAG（Retrieval-Augmented Generat
> 图片展示了RAG（Retrieval-Augmented Generation）和Re2G两种架构。RAG架构中，Query经Query Encoder后，通过ANN Index获取Top-K Passages，再由Add Query、Generator生成输出，Marginalization得到最终结果。Re2G架构在RAG基础上，将ANN Index改为BM25 Index，引入Reranker，其余环节与RAG类似。该图与上下文紧密相关，直观呈现了两种架构的组成及差异，为理解RAG工作原理提供可视化参考。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FafobU3jxoaJxOx0mUCcTnIynXd) · `FafobU3jxoaJxOx0mUCcTnIynXd`

###### 以 Jina Reranker v2 为例

```Bash
curl -X 'POST' \
  'https://api.jina.ai/v1/rerank' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <YOUR JINA AI TOKEN HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "jina-reranker-v2-base-multilingual",
  "query": "I am planning a road trip from Berlin to Munich in my Volkswagen VII. Can you calculate the carbon footprint of this trip?",
  "documents": [
    "{'\''Name'\'': '\''getWeather'\'', '\''Specification'\'': '\''Provides current weather information for a specified city'\'', '\''spec'\'': '\''https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'\'', '\''example'\'': '\''https://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=YOUR_API_KEY'\''}",
    "{'\''Name'\'': '\''calculateDistance'\'', '\''Specification'\'': '\''Calculates the driving distance and time between multiple locations'\'', '\''spec'\'': '\''https://maps.googleapis.com/maps/api/distancematrix/json?origins={startCity}&destinations={endCity}&key={API_KEY}'\'', '\''example'\'': '\''https://maps.googleapis.com/maps/api/distancematrix/json?origins=Berlin&destinations=Munich&key=YOUR_API_KEY'\''}",
    "{'\''Name'\'': '\''calculateCarbonFootprint'\'', '\''Specification'\'': '\''Estimates the carbon footprint for various activities, including transportation'\'', '\''spec'\'': '\''https://www.carboninterface.com/api/v1/estimates'\'', '\''example'\'': '\''{type: vehicle, distance: distance, vehicle_model_id: car}'\''}"
  ]
}'
```

```JSON
{
  "model": "jina-reranker-v2-base-multilingual",
  "usage": {
    "total_tokens": 383,
    "prompt_tokens": 383
  },
  "results": [
    {
      "index": 2,
      "document": {
        "text": "{'Name': 'calculateCarbonFootprint', 'Specification': 'Estimates the carbon footprint for various activities, including transportation', 'spec': 'https://www.carboninterface.com/api/v1/estimates', 'example': '{type: vehicle, distance: distance, vehicle_model_id: car}'}"
      },
      "relevance_score": 0.5422876477241516
    },
    {
      "index": 1,
      "document": {
        "text": "{'Name': 'calculateDistance', 'Specification': 'Calculates the driving distance and time between multiple locations', 'spec': 'https://maps.googleapis.com/maps/api/distancematrix/json?origins={startCity}&destinations={endCity}&key={API_KEY}', 'example': 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Berlin&destinations=Munich&key=YOUR_API_KEY'}"
      },
      "relevance_score": 0.23283305764198303
    },
    {
      "index": 0,
      "document": {
        "text": "{'Name': 'getWeather', 'Specification': 'Provides current weather information for a specified city', 'spec': 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}', 'example': 'https://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=YOUR_API_KEY'}"
      },
      "relevance_score": 0.05033063143491745
    }
  ]
}
```

###### Qwen-Agent：分块阅读

<callout emoji="💥">
最好的语义相关度计算算法是 LLM 本身😎
</callout>

> [!abstract]- 🖼 图片展示了Level-2 Agent（并行读取所有片段）的工作流程。用户
> 图片展示了Level-2 Agent（并行读取所有片段）的工作流程。用户查询“用英语回复并告诉我自行车是什么时候发明的”，LLM对512个token的片段进行相关性判断，如Chunk 1、Chunk 2等，其中Chunk 2、Chunk 3被判定为相关片段，包含“19世纪”“自行车”等信息。最终，LLM基于4k短相关片段语境生成“自行车是在19世纪发明的”回复。该图与上下文介绍的LLM评估搜索结果等内容相关，直观呈现了流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LE6JbPjKHoWK4bxQ4F5c7jJvnPf) · `LE6JbPjKHoWK4bxQ4F5c7jJvnPf`

#### Bot 工作流：`search_notion`

- 连接器 API：`searchNotion`
- LLM：生成查询关键词
- LLM：评估搜索结果

#### 搜索之后，三种使用搜索结果的方式

1. 基于摘要回答用户问题
2. 获取完整页面内容，基于页面内容回答用户问题
3. 获取完整页面内容，先基于单个页面回答，然后总结

#### Bot 工作流：`search_and_answer`

- Bot 工作流：`search_notion`
- 连接器 API：`getPage`
- LLM：生成独立回答
- LLM：总结并生成最终回答
- Bot 提示词
- 快捷指令

## 拓展阅读

- 【公众号文章】[我用Coze手搓了一个极简版Perplexity（基本可以替代Google搜索)](https://mp.weixin.qq.com/s/ASwN2aD0huS2u2UmAIkdhA)
- 【公众号文章】[如何用Coze制作一个信息检索Bot（含Workflow的基础用法）](https://mp.weixin.qq.com/s/Ory8iVXXjjN3zSTcupPm6Q)
- 【B 站视频教程】[一步一步带你手搓一个Coze Bot——Dr. Know（极简版 Perplexity）](https://www.bilibili.com/video/BV1Bx4y1n7cB)
- 【公众号文章】[Coze机器人 + Notion数据库 = 个人知识助理](https://mp.weixin.qq.com/s/CZxBH1L34C9hJe8ByO4HPw)
- 【公众号文章】[这是Coze平台上最完善、最强大的Notion连接器](https://mp.weixin.qq.com/s/3gzSEjWxnxB0dRKFZvOx4g)
- 【论文】[Re2G: Retrieve, Rerank, Generate](https://arxiv.org/abs/2207.06300)
- 【研究】[使用Qwen-Agent将上下文记忆扩展到百万量级](https://qwenlm.github.io/zh/blog/qwen-agent-2405/)
- 【公众号文章】[Jina Reranker v2：多语言支持、函数调用、代码搜索，超快推理！](https://mp.weixin.qq.com/s/YCraYU0Jg2O_WBUxMxrZ9g)
- 【公众号文章】[RAGFlow开源Star量破万，是时候思考下RAG的未来是什么了](https://mp.weixin.qq.com/s/wk3nlPU0rKAcHCiELUCr1A)
