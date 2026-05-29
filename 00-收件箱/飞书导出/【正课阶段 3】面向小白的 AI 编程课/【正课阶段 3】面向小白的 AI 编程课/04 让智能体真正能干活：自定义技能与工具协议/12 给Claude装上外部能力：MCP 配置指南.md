---
title: "给Claude装上外部能力：MCP 配置指南"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/FW9fwEyFyi1JhIkNwFJcNgQnnWd"
node_token: "FW9fwEyFyi1JhIkNwFJcNgQnnWd"
obj_type: "docx"
document_id: "AYGSdJGUZoj9fAxHukucHVqhng2"
revision_id: "620"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/FW9fwEyFyi1JhIkNwFJcNgQnnWd>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>给Claude装上外部能力：MCP 配置指南</title>

你好，我是大圣



这节课我们来解决一个你一定会遇到的问题：**Claude Code 接触不到外部信息**



# 一、Claude Code 是个瞎子



<figure view-type="Preview"><source mime="video/mp4" origin-height="1964.000000" origin-width="3024.000000" token="DKDebziyTopmMDxmC9ScEc5FnMg"/></figure>



假设你跟 Claude Code 说：



```Bash
帮我查一下北京明天的天气怎么样
```



它不会去查。它会告诉你"抱歉，我无法获取实时天气信息"。



**因为 Claude Code 默认只能操作你电脑上的文件。** 读文件、写文件、改代码、跑命令，这些它都行。



但出了你电脑这个范围，它就是个瞎子



搜不了网页，查不了天气，规划不了路线，连不上任何外部服务



**你得给它装上外部工具，这就是 MCP干的事情**



# **二、MCP 是什么**



MCP 的全称是 Model Context Protocol，中文叫模型上下文协议。



**用一句话来说：MCP 是一个标准接口，让 Claude Code 能连接各种外部工具**



你可以把它想象成一个扩展坞：



> *你的笔记本电脑接口有限，没法连接所有外设。*
> 
> *但如果你外接一个扩展坞，就能通过标准化的接口连上显示器、键盘、硬盘等各种设备*



MCP 就是 Claude Code 的扩展坞。



通过它，你可以给 Claude Code 接上搜索引擎、地图、数据库等各种外部能力。



每一个外部工具，在 MCP 的世界里叫做一个 **MCP 服务器**（MCP Server）



<callout emoji="✨"><p>我有一篇专门讲 MCP 的理论文章，讲得非常详细：</p><p></p><p><cite doc-id="OHtQwPfvuiiXrbkRSHicdwMXnje" file-type="wiki" title="12｜【理论篇】小白了解 MCP，看这一篇就够了" type="doc"></cite></p><p></p><p>但是这里大家先不要去看这篇文章，你跟着我的节奏走，先简单理解一下 MCP，然后我们直接进入到实操环节。<b>在这节课过后，大家可以去全方位了解一下 MCP的理论知识</b></p></callout>



这节课只做一件事：**动手给 Claude Code 装上高德地图，让它能查天气、查路线**



# 三、**准备工作：申请高德地图的 API Key**



<figure view-type="Preview"><source mime="video/quicktime" origin-height="2160.000000" origin-width="3840.000000" token="Vs20bsz9So3dkTx9sXJcBHnInlf"/></figure>



在装工具之前，我们需要先拿到高德地图的 API Key



**什么是 API Key？**



API Key 就是一把钥匙。你要使用别人提供的服务（比如高德的地图能力），人家需要知道你是谁、怎么给你计费。这把钥匙就是你的身份凭证



这个概念非常重要。后面你在使用 AI 的过程中，会经常遇到 API Key



不管是接地图、接搜索还是接其他工具，逻辑都是一样的：**找到服务商 → 注册账号 → 拿到 Key**



**具体操作：**



1. 打开高德开放平台：[https://lbs.amap.com/](https://lbs.amap.com/)



1. 注册一个账号（用手机号就行）



1. 进入控制台，创建一个应用



![](https://feishu.cn/file/U5ahb0Dw5oZyXgxqinkcSWqhnpb)



控制台中创建我的应用地址：https://console.amap.com/dev/key/app



![](https://feishu.cn/file/EDvYbkYUso68rxxCUiacmbaRnqh)



1. 在应用里添加一个 Key，服务类型选Web服务



1. 把生成的 Key 复制保存下来



> *高德的免费额度非常充足，日常使用完全不用担心费用问题。*



# **四、动手：给 Claude Code 装上高德地图**



拿到 Key 之后，接下来配置 MCP。我给你两种方式，选适合你的



## **方式一：手动配置**



<figure view-type="Preview"><source mime="video/quicktime" origin-height="2160.000000" origin-width="3840.000000" token="FLQ2b48ReogEIIxUto6cmdP8n0b"/></figure>



进入你的项目文件夹，在**根目录**下创建一个文件，命名为 `.mcp.json`（注意开头有个点，这是隐藏文件）



让我们习惯用 Claude Code帮我做这件事情：



在终端定位到你的项目文件夹，然后启动 Claude，执行命令：



```Bash
touch .mcp.json
```



![](https://feishu.cn/file/UQzpbgkx8oWQhrxgk5xcs7r1n5b)



然后在你的项目根目录下就会出现一个隐藏文件：



![](https://feishu.cn/file/K9zubYl8goU0Ilxyky4cNp2En5c)



使用记事本打开文件，然后贴入下面的命令



**PS：把 `你的Key` 替换成你刚才申请的高德 API Key**



```JSON
{
  "mcpServers": {
    "amap": {
      "command": "npx",
      "args": ["-y", "@amap/amap-maps-mcp-server"],
      "env": {
        "AMAP_MAPS_API_KEY": "你的Key"
      }
    }
  }
}
```



保存文件就可以了



## 方式二：让 Claude Code帮你配置



<callout emoji="✨">
这个视频踩了一些坑，所以时间达到了 16 分钟。
但我故意没有剪辑，因为我发现这个踩坑的过程特别有价值。**感兴趣的可以看一下，你可以二倍速观看**
</callout>



<readonly-block href="https://axsppz4oyvj.feishu.cn/minutes/embed/obcnxk61238264z4c5te7c11?from=ccm" type="iframe"></readonly-block>



如果你觉得手动创建文件太麻烦，你完全可以让 Claude Code 帮你做这件事



启动 Claude Code，直接跟它说：



```JSON
帮我配置高德地图的 MCP 服务器
```



Claude Code 会自动帮你创建配置文件，内容跟方式一完全一样



**这就是 Claude Code 的好处：很多操作你不需要自己手动做，直接用中文告诉它就行**



配置完之后需要退出 Claude Code 再重新启动，让它重新读取配置文件



# 五、验证它完全生效了



重新启动 Claude Code，然后直接使用命令进行测试



```JSON
帮我查一下北京明天的天气
```



这一次，Claude Code 真的去查了。它会调用高德地图的接口获取实时天气数据，然后把结果告诉你



![](https://feishu.cn/file/FjNvb9Bwjo2y9Nx6uRjcfXCCnVf)



# 六、**两个作用域：项目级和用户级**



<readonly-block href="https://axsppz4oyvj.feishu.cn/minutes/embed/obcnxl1aj6jy836lom66ojxe?from=ccm" type="iframe"></readonly-block>



这个概念大家应该不陌生了。



我们在 CLAUDE.md 里面，以及在后面的 skill 里面，都会有这样一个概念：项目级和用户级



我们刚才创建的 `.mcp.json` 放在项目根目录下。



这意味着：**只有在这个项目里启动 Claude Code，高德地图才可用**



换一个项目文件夹打开 Claude Code，它又是个瞎子了



这是**项目级**的配置



但你可能觉得：高德地图这种工具，我在哪个项目里都想用啊



这时候你可以用**用户级**的配置：让一个工具对你所有的项目都生效



方法很简单，我们直接问 Claude Code



<callout emoji="✨">
我会在课程里不断地给大家强调：当你不知道要怎么具体用哪个命令做一件事的时候，你就用自然语言去问 Claude Code，它大概率都是知道的
这就是我一直强调的AI 套娃的作用：你不知道怎么用 AI，你就去问 AI；
你不知道怎么用 Claude Code，你也可以去问 Claude Code。
大家一定要理解这里面的精髓，这是 AI 编程最底层的逻辑
</callout>



# 七、**举一反三**



高德地图只是众多 MCP 服务器中的一个



通过同样的方式，你还可以给 Claude Code 接上各种外部能力。方法都是一样的



1. 找到你需要的 MCP 服务器
2. 如果需要 API Key，去对应平台申请
3. 在 `.mcp.json` 里添加配置
4. 重启 Claude Code



想装多个工具，就在 `mcpServers` 里面加多个就行：



```JSON
{
  "mcpServers": {
    "amap": {
      "command": "npx",
      "args": ["-y", "@amap/amap-maps-mcp-server"],
      "env": {
        "AMAP_MAPS_API_KEY": "你的Key"
      }
    },
    "另一个工具": {
      "command": "npx",
      "args": ["-y", "另一个工具的包名"],
      "env": {}
    }
  }
}
```



具体一个工具到底怎么配它的 .mcp.json 格式，接下来我专门去讲该用何种方式去找到它



# 八、具备寻找 MCP的能力



<readonly-block href="https://axsppz4oyvj.feishu.cn/minutes/embed/obcnxl5r3sm671gy86jeb955?from=ccm" type="iframe"></readonly-block>



我们的课程理念一直是授人以鱼，且授人以渔



关于 MCP，我不可能帮你穷举所有的 MCP，所以你要具备自己去寻找 MCP 的能力



这里我想跟你分享的是，对于这种非常标准化的工具，一定有大量的网站和大量的社区支持你去自由地搜索 MCP



我先给你推荐几个：



- https://github.com/yzfly/Awesome-MCP-ZH【一个推荐 MCP的 github仓库】
- https://www.modelscope.cn/mcp【国内魔搭社区的 MCP广场】
- https://smithery.ai/servers【一个国外的 MCP 社区】
- https://mcp.so/server/mcp-advisor【一个帮你推荐MCP的 mcp】
- https://mcp.so



在写这篇文章的时候，我还没有特别大量地使用 MCP，所以没有办法给大家分享我自己的实践案例



但是我可以告诉你，我是怎么找到这些网站的。非常简单，就是利用谷歌的 AI 加搜索的能力



# 九、**写在最后**



这一课做了一件事：**给 Claude Code 装上了外部能力**



在此之前，它只能操作你电脑上的文件。现在，它能查天气、查路线，能感知真实世界的信息了



而高德地图只是一个开始。通过 MCP 这个扩展坞，你可以给 Claude Code 接上几乎任何外部服务



如果你想深入了解 MCP 的底层原理：



它为什么要这样设计、跟 Function Calling 有什么渊源、三个核心角色分别是什么？



可以去看我的理论篇文章：<cite doc-id="OHtQwPfvuiiXrbkRSHicdwMXnje" file-type="wiki" title="12｜【理论篇】小白了解 MCP，看这一篇就够了" type="doc"></cite>
