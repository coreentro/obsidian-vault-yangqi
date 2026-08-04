---
title: "Claude Code如何获取互联网上的信息"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/TYCGwjt6Mi0cmPkWNxbckna3nUh
node_token: TYCGwjt6Mi0cmPkWNxbckna3nUh
obj_token: QSthdsStUo7tUqxYkKwcDDrpnWH
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "命令行智能体：一种全新的智能体交互方式"
  - "Claude Code如何获取互联网上的信息"
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

# Claude Code如何获取互联网上的信息

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 命令行智能体：一种全新的智能体交互方式

# 写在前面

你好，我是大圣

当你装完Claude Code之后，很多人的第一件事是想联网获取信息

但你在Claude Code里面想使用搜索，并不如你想的那么简单

这节课我把所有的理论给你讲清楚，搞明白这个框架之后，你后面去选各种各样的工具，配搜索，心里就非常清楚了

# 一、获取互联网信息的两种情况

Claude Code 获取互联网上的信息，本质就两种情况：

> [!abstract]- 🖼 图片展示了Claude Code获取互联网信息的两种情况。上方标题为“C
> 图片展示了Claude Code获取互联网信息的两种情况。上方标题为“Claude Code怎么获取互联网信息？”，下方分为“搜索”和“抓取”两个部分。搜索部分对应“不知道链接，需要去找”，抓取部分对应“知道链接，想拿到内容”。该图与上下文紧密相关，是对文档中“Claude Code获取互联网上的信息，本质就两种情况”的直观呈现，帮助读者更清晰地理解获取互联网信息的两种方式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WkhpbKxRCootTcx0zJvcanyanff) · `WkhpbKxRCootTcx0zJvcanyanff`

**第一种：你不知道链接，需要去搜**

比如你问"最近两天，AI圈又发生什么大事件？"，你不知道答案在哪个网页上，需要 AI 帮你去搜索引擎里找

**第二种：你知道链接，想拿到内容**

比如你说"帮我获取一下这个网址的内容"，你已经有了具体的网址，只需要 AI 去把页面内容抓回来

# 二、Claude Code自带的联网能力

Claude Code 出厂就自带了两个联网工具，正好对应上面两种情况：

**WebSearch：**对应搜索，你输入关键词，它帮你去搜

**WebFetch：**对应抓取，你给它一个网址，它帮你把页面内容拿回来，返回一段摘要

> [!abstract]- 🖼 图片展示了Claude Code自带的两个联网工具。上方标题为“Clau
> 图片展示了Claude Code自带的两个联网工具。上方标题为“Claude Code自带的两个联网工具”，下方分为两个部分，左侧是WebSearch（搜索），输入关键词返回链接列表，对应“不知道链接”场景；右侧是WebFetch（抓取），输入网址返回页面摘要，对应“知道链接”场景。底部红色框内标注关键限制，即WebSearch走的是Anthropic官方后端，第三方API用不了。该图与上下文紧密相关，直观呈现了Claude Code的联网工具及其功能和适用场景。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JpWObCtaNohuWyxsYKIcBz82n3c) · `JpWObCtaNohuWyxsYKIcBz82n3c`

听起来很完美对不对？装完 Claude Code 就能搜索了？

**这里有个很多人踩的坑：**

**下面这张图是我用Claude Code分析Claude Code的源码，得出来的Web Search的机制**

> [!abstract]- 🖼 图片展示了Claude Code Web Search功能的机制，即通过
> 图片展示了Claude Code Web Search功能的机制，即通过Anthropic的Claude API里一个特殊“工具调用（tool use）”的Beta功能实现。具体包括工具定义与注册、Web Search的具体调用方式、请求构造、返回结果处理、特殊请求头部、对Anthropic API的依赖等内容。该图与上文提到的Claude Code Web Search机制分析相关，是对上文内容的详细说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MvulbwgJaoEh4kxogRBcuu9xnhc) · `MvulbwgJaoEh4kxogRBcuu9xnhc`

总结来看就是：

**WebSearch 搜索这个动作不是发生在你电脑上的，而是发生在你调用的API的服务器上**

所以如果你的请求走的是第三方中转商的服务器，人家服务器上根本没有搜索这个功能，请求到了那里就断了

> [!abstract]- 🖼 图片展示了Claude Code WebSearch搜索机制。你的电脑向
> 图片展示了Claude Code WebSearch搜索机制。你的电脑向API服务器发送请求，API服务器是官方还是第三方决定了搜索结果。若为Anthropic官方服务器，支持WebSearch Beta功能，请求会服务端去搜，返回结果，搜索成功；若为第三方API中转，不支持此功能，请求被忽略或报错，搜索失败。图片与上下文紧密相关，直观呈现了WebSearch搜索动作发生在服务器端而非电脑端，以及第三方中转商服务器无搜索功能导致搜索失败的情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Ef5ubwNOAoK4V9xwNskciyvcnSb) · `Ef5ubwNOAoK4V9xwNskciyvcnSb`

结论就是：

1. 如果你是官方订阅，可以无痛使用
2. 如果你的中转API是云雾，可以使用
3. 如果你的中转AP是Claude Code不可以使用

我录制一个视频，教大家怎么测试

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/F7FQbSGEJorB8NxBSW9cnBPhnkh) · `F7FQbSGEJorB8NxBSW9cnBPhnkh`

# 三、自带的用不了，有哪些替代方案？

所以如果Claude Code自带的搜索工具，你用不了，或者说感觉功能不够

那我们就要自己去配置

这里仍然是搜索和抓取两条线，分别有替代方案

> [!abstract]- 🖼 图片展示了Claude Code获取互联网信息的两条替代方案流程。搜索方
> 图片展示了Claude Code获取互联网信息的两条替代方案流程。搜索方面，可接第三方搜索API（如Brave、Tavily等，通过MCP挂载），也可用CDP控制本地浏览器（不花钱，用自己Chrome去搜）。抓取方面，有第三方抓取工具（如Firecrawl等，拿到完整原始内容）。底部文字强调本质都是接API（要注册、要Key、后续要付费），CDP是唯一不花钱的路（直接控制电脑Chrome，不接任何API）。该图与上下文紧密相关，直观呈现了获取信息的替代方案及核心要点。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/GoWJbTmuao7GTLxFJQNcZPE6nKh) · `GoWJbTmuao7GTLxFJQNcZPE6nKh`

这节课给大家讲的仍然是框架，我会推荐一些实操教程

我想给大家分享的是未来很长一段时间，寻找优质的信息源，是你经常要做的事情

# 四、接入第三方搜索API

本质就是你自己去一个搜索服务商那里，注册账号，拿到一个 API Key，然后把这个 Key 配置到 Claude Code 里

比如 Brave Search、Tavily、Exa 这些

至于怎么挂到 Claude Code 上，最常见的方式是通过 MCP（Model Context Protocol）/ Skills来挂载

MCP和skills是我们后面要讲的概念，这里不展开

**但不管是 MCP 还是别的什么方式，本质都一样：都是在调别人家的搜索 API**

既然是调别人家的API就没有免费的，最多是刚注册的时候给一些额度

比如 Brave 每月免费 2000 次，Tavily 每月免费 1000 次。但本质上后续都是要付费的

再比如智谱的AI搜索：https://docs.bigmodel.cn/cn/guide/tools/web-search

> [!abstract]- 🖼 图片展示了智谱AI搜索引擎的说明，包含搜索引擎编码、特性及价格。特性方面
> 图片展示了智谱AI搜索引擎的说明，包含搜索引擎编码、特性及价格。特性方面，search_std为基础版，满足日常查询需求，性价比高；search_pro为高级版，多引擎协作显著降低空结果率，召回率和准确率大幅提升；search_pro_sogou覆盖腾讯生态等内容，search_pro_quark精准触达垂直内容。价格均为0.01元/次，其中search_pro_sogou和search_pro_quark为0.05元/次。该图与文档中介绍智谱AI搜索的内容相关，为用户了解不同搜索引擎特性及价格提供参考。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/K8SWbNsydoq6ZoxkuCccMK75nDb) · `K8SWbNsydoq6ZoxkuCccMK75nDb`

# 五、CDP控制本地浏览器

这是一条不花钱的路

CDP 全称是 Chrome DevTools Protocol，你不用记这个名字，只需要知道它干了什么：

**让 Claude Code 直接控制你电脑上的 Chrome 浏览器**

就像有个人坐在你电脑前，帮你打开 Chrome，输入关键词，点搜索，然后把搜索结果读回来

你用的是自己的浏览器，走的是自己的网络，不需要注册任何 API，不需要花一分钱

# 六、抓取的替代方案

如果你觉得 Claude Code 自带的 WebFetch 返回的摘要不够用

你想拿到完整的原始网页内容，可以接第三方的抓取工具

比如 Firecrawl，它可以帮你把网页的完整内容抓下来，包括原始的 HTML 和 Markdown

这个本质上也是接 API，也需要注册、拿 Key、后续付费

# 总结一下

Claude Code 联网搜索，就这么一个框架：

**获取互联网信息 = 搜索 + 抓取**

搜索有三条路：

- Claude Code 自带的 WebSearch（但第三方 API 可能用不了）
- 接第三方搜索 API（Brave、Tavily 等，通过 MCP 挂载）
- CDP 控制本地 Chrome 浏览器（不花钱）

抓取有两条路：

- Claude Code 自带的 WebFetch
- 接第三方抓取工具（如 Firecrawl，返回完整内容）

**本质只有两种：要么接 API（花钱），要么控制本地浏览器（不花钱）**

这节课只讲框架，让你心里有个全局的认知，具体每种方案怎么配置、用什么工具，我们后面展开来讲

# 附录：延伸阅读

1. 一泽的Web-Access Skill：https://mp.weixin.qq.com/s/rps5YVB6TchT9npAaIWKCw

这是一个开源的skill，号称搜索强度拉满，大家可以试用一下是否符合自己的需求
