---
title: "给Claude装上外部能力：MCP 配置指南"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/FW9fwEyFyi1JhIkNwFJcNgQnnWd
node_token: FW9fwEyFyi1JhIkNwFJcNgQnnWd
obj_token: AYGSdJGUZoj9fAxHukucHVqhng2
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "让智能体真正能干活：自定义技能与工具协议"
  - "给Claude装上外部能力：MCP 配置指南"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 620
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 给Claude装上外部能力：MCP 配置指南

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 让智能体真正能干活：自定义技能与工具协议

你好，我是大圣

这节课我们来解决一个你一定会遇到的问题：**Claude Code 接触不到外部信息**

# 一、Claude Code 是个瞎子

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/DKDebziyTopmMDxmC9ScEc5FnMg) · `DKDebziyTopmMDxmC9ScEc5FnMg`

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

<callout emoji="✨"><p>我有一篇专门讲 MCP 的理论文章，讲得非常详细：</p><p></p><p>[[【理论篇】小白了解 MCP，看这一篇就够了]]</p><p></p><p>但是这里大家先不要去看这篇文章，你跟着我的节奏走，先简单理解一下 MCP，然后我们直接进入到实操环节。<b>在这节课过后，大家可以去全方位了解一下 MCP的理论知识</b></p></callout>

这节课只做一件事：**动手给 Claude Code 装上高德地图，让它能查天气、查路线**

# 三、**准备工作：申请高德地图的 API Key**

> [!warning]- 🎬 视频（`video/quicktime`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/Vs20bsz9So3dkTx9sXJcBHnInlf) · `Vs20bsz9So3dkTx9sXJcBHnInlf`

在装工具之前，我们需要先拿到高德地图的 API Key

**什么是 API Key？**

API Key 就是一把钥匙。你要使用别人提供的服务（比如高德的地图能力），人家需要知道你是谁、怎么给你计费。这把钥匙就是你的身份凭证

这个概念非常重要。后面你在使用 AI 的过程中，会经常遇到 API Key

不管是接地图、接搜索还是接其他工具，逻辑都是一样的：**找到服务商 → 注册账号 → 拿到 Key**

**具体操作：**

1. 打开高德开放平台：[https://lbs.amap.com/](https://lbs.amap.com/)

1. 注册一个账号（用手机号就行）

1. 进入控制台，创建一个应用

> [!abstract]- 🖼 图片展示了高德开放平台首页，右上角有“控制台”标识，旁边有一个头像图标。
> 图片展示了高德开放平台首页，右上角有“控制台”标识，旁边有一个头像图标。下方文字为“高德地图MCP Server SSE解决方案”，并有“了解详情”按钮。图片与上下文的关系是，它直观呈现了文档中提到的“进入控制台，创建一个应用”步骤中，登录后点击进入控制台的操作位置，帮助用户更清晰地找到控制台入口。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/U5ahb0Dw5oZyXgxqinkcSWqhnpb) · `U5ahb0Dw5oZyXgxqinkcSWqhnpb`

控制台中创建我的应用地址：https://console.amap.com/dev/key/app

> [!abstract]- 🖼 图片展示的是高德开放平台控制台中“我的应用”页面。页面左侧有导航栏，右侧
> 图片展示的是高德开放平台控制台中“我的应用”页面。页面左侧有导航栏，右侧上方显示“我的应用”标题。页面中部显示“高德MCP Server 2025/7/31创建”的应用信息，包括Key名称、Key用途说明、安全密钥等。右上角有“创建新应用”按钮，页面右下角有“帮助中心”图标。图片中红色箭头指向“创建新应用”按钮，与上下文提到的“在应用里添加一个Key，服务类型选Web服务”操作步骤相关，提示用户在此处创建新应用以添加Key。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/EDvYbkYUso68rxxCUiacmbaRnqh) · `EDvYbkYUso68rxxCUiacmbaRnqh`

1. 在应用里添加一个 Key，服务类型选Web服务

1. 把生成的 Key 复制保存下来

> *高德的免费额度非常充足，日常使用完全不用担心费用问题。*

# **四、动手：给 Claude Code 装上高德地图**

拿到 Key 之后，接下来配置 MCP。我给你两种方式，选适合你的

## **方式一：手动配置**

> [!warning]- 🎬 视频（`video/quicktime`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/FLQ2b48ReogEIIxUto6cmdP8n0b) · `FLQ2b48ReogEIIxUto6cmdP8n0b`

进入你的项目文件夹，在**根目录**下创建一个文件，命名为 `.mcp.json`（注意开头有个点，这是隐藏文件）

让我们习惯用 Claude Code帮我做这件事情：

在终端定位到你的项目文件夹，然后启动 Claude，执行命令：

```Bash
touch .mcp.json
```

> [!abstract]- 🖼 图片展示的是在终端中操作Claude的界面。界面顶部显示Claude C
> 图片展示的是在终端中操作Claude的界面。界面顶部显示Claude Code版本为v2.1.44，并有“Welcome back!”的欢迎语。左侧有一个粉色小机器人图标，右侧提示运行/init指令可创建含Claude使用说明的CLAUDE.md文件，还显示了最近活动为空等信息。底部命令行显示当前路径为~/AI-Tour/projects/mcp-demo，输入了“touch .mcp.json”指令。此图片与上文在终端定位到项目文件夹后启动Claude并执行命令的内容相呼应，展示了具体操作示例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UQzpbgkx8oWQhrxgk5xcs7r1n5b) · `UQzpbgkx8oWQhrxgk5xcs7r1n5b`

然后在你的项目根目录下就会出现一个隐藏文件：

> [!abstract]- 🖼 图片展示了项目文件夹中的内容，其中左侧被红色框高亮的`.mcp.json
> 图片展示了项目文件夹中的内容，其中左侧被红色框高亮的`.mcp.json`文件是在项目根目录下创建的隐藏文件。右侧还有另外一个隐藏文件夹`.claude`。图片右侧有红色箭头指向`.mcp.json`文件，并标注“隐藏文件”。与上下文关系为：上下文提到在项目根目录下创建名为`.mcp.json`的隐藏文件，图片直观呈现了该隐藏文件在项目文件夹中的样子，帮助读者更清晰地了解创建后文件的显示形态。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/K9zubYl8goU0Ilxyky4cNp2En5c) · `K9zubYl8goU0Ilxyky4cNp2En5c`

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

> [!abstract]- 🖼 图片展示的是Claude Code查询北京明天天气的界面。上方显示“We
> 图片展示的是Claude Code查询北京明天天气的界面。上方显示“Welcome to Opus 4.6”，中间有命令“amap - maps_weather (MCP)(city: "北京")”，下方是查询结果，显示北京明天天气为白天晴、夜间晴，最高气温11℃、最低-3℃，风向南风、风力1 - 3级，还对天气情况进行了总结。该图片与上文介绍给Claude Code装上高德地图能力后，通过命令测试其是否生效的内容相关，直观呈现了查询结果。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FjNvb9Bwjo2y9Nx6uRjcfXCCnVf) · `FjNvb9Bwjo2y9Nx6uRjcfXCCnVf`

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

可以去看我的理论篇文章：[[【理论篇】小白了解 MCP，看这一篇就够了]]
