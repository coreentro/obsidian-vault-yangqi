---
title: "Claude Code如何获取互联网上的信息"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/TYCGwjt6Mi0cmPkWNxbckna3nUh"
node_token: "TYCGwjt6Mi0cmPkWNxbckna3nUh"
obj_type: "docx"
document_id: "QSthdsStUo7tUqxYkKwcDDrpnWH"
revision_id: "4"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/TYCGwjt6Mi0cmPkWNxbckna3nUh>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>Claude Code如何获取互联网上的信息</title>

# 写在前面



你好，我是大圣



当你装完Claude Code之后，很多人的第一件事是想联网获取信息



但你在Claude Code里面想使用搜索，并不如你想的那么简单



这节课我把所有的理论给你讲清楚，搞明白这个框架之后，你后面去选各种各样的工具，配搜索，心里就非常清楚了



# 一、获取互联网信息的两种情况



Claude Code 获取互联网上的信息，本质就两种情况：



![](https://feishu.cn/file/WkhpbKxRCootTcx0zJvcanyanff)



**第一种：你不知道链接，需要去搜**



比如你问"最近两天，AI圈又发生什么大事件？"，你不知道答案在哪个网页上，需要 AI 帮你去搜索引擎里找



**第二种：你知道链接，想拿到内容**



比如你说"帮我获取一下这个网址的内容"，你已经有了具体的网址，只需要 AI 去把页面内容抓回来



# 二、Claude Code自带的联网能力



Claude Code 出厂就自带了两个联网工具，正好对应上面两种情况：



**WebSearch：**对应搜索，你输入关键词，它帮你去搜



**WebFetch：**对应抓取，你给它一个网址，它帮你把页面内容拿回来，返回一段摘要



![](https://feishu.cn/file/JpWObCtaNohuWyxsYKIcBz82n3c)



听起来很完美对不对？装完 Claude Code 就能搜索了？



**这里有个很多人踩的坑：**



**下面这张图是我用Claude Code分析Claude Code的源码，得出来的Web Search的机制**



![](https://feishu.cn/file/MvulbwgJaoEh4kxogRBcuu9xnhc)



总结来看就是：



**WebSearch 搜索这个动作不是发生在你电脑上的，而是发生在你调用的API的服务器上**



所以如果你的请求走的是第三方中转商的服务器，人家服务器上根本没有搜索这个功能，请求到了那里就断了



![](https://feishu.cn/file/Ef5ubwNOAoK4V9xwNskciyvcnSb)



结论就是：



1. 如果你是官方订阅，可以无痛使用
2. 如果你的中转API是云雾，可以使用
3. 如果你的中转AP是Claude Code不可以使用



我录制一个视频，教大家怎么测试



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="F7FQbSGEJorB8NxBSW9cnBPhnkh"/></figure>



# 三、自带的用不了，有哪些替代方案？



所以如果Claude Code自带的搜索工具，你用不了，或者说感觉功能不够



那我们就要自己去配置



这里仍然是搜索和抓取两条线，分别有替代方案



![](https://feishu.cn/file/GoWJbTmuao7GTLxFJQNcZPE6nKh)



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



![](https://feishu.cn/file/K8SWbNsydoq6ZoxkuCccMK75nDb)



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
