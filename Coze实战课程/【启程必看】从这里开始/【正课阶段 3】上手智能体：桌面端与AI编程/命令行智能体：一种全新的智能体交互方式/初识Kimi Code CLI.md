---
title: "初识Kimi Code CLI"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/XBi2w6RzniX7sEk0pOWcVbL7nvb
node_token: XBi2w6RzniX7sEk0pOWcVbL7nvb
obj_token: T1c5dJ5Dco4QbqxjDjXc5VE7nNg
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "命令行智能体：一种全新的智能体交互方式"
  - "初识Kimi Code CLI"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 3
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 初识Kimi Code CLI

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 命令行智能体：一种全新的智能体交互方式

# 写在前面

你好，我是大圣

虽然Claude Code是命令行智能体的鼻祖，也是最强大的通用智能体，但它有一些使用门槛。

所以我们从国内的Kimi Code CLI的进行学习，它们的产品形态及功能基本是一样的

Kimi Code CLI最适合中国宝宝体质使用，虽然它需要付一些费用（最低 49/月）

<callout emoji="✨">
我强烈建议大家装一下Kimi Code因为它是你后面装各种环境的强大助手
</callout>

写安装教程最复杂的根本不是使用教程，而是每个学员不同的电脑环境，导致在安装过程中问题百出

而这个时候，如果你已经成功安装Kimi Code，你就可以用Kimi Code去帮你：

我的Git怎么安装？我的Python版本对不对？我的Node.js是不是冲突了？

这类以前只有程序员能够解决的问题，现在依靠AI的普通人也很容易解决

# 一、Kimi Code的下载与安装

地址：https://www.kimi.com/code

> [!abstract]- 🖼 图片展示了Kimi Code的安装页面。页面上方有“Kimi Code 
> 图片展示了Kimi Code的安装页面。页面上方有“Kimi Code 3倍额度计划已常驻！去查看”提示。中间大标题为“Kimi Code”，介绍其会员计划面向代码开发的权益。下方有“安装Kimi Code”按钮，右侧有复制命令的区域，分别有“On Mac/Linux”和“On Windows”选项，当前选中“On Mac/Linux”。页面底部展示了VS Code和Kimi Code Cursor的相关信息。图片右侧有红色箭头指向复制命令区域，旁边文字提示“根据系统来复制右边的命令”，与上下文介绍Kimi Code安装步骤的内容相呼应。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YuHdbFjJKoV7mqxt8KWcJxD3nfd) · `YuHdbFjJKoV7mqxt8KWcJxD3nfd`

我已经问过Kimi Code了，他说他的安

额外的依赖

> [!abstract]- 🖼 图片展示了Windows电脑上安装Kimi Code时的命令操作界面。关
> 图片展示了Windows电脑上安装Kimi Code时的命令操作界面。关键信息有：1. Windows电脑可安装，但同样不推荐安装Python；2. 用“irm https://code.kimi.com/install.ps1 | iex”命令安装，此命令在Windows上是天然小白可用；3. 该命令其实是Invoke -RestMethod https://code.kimi.com/install.ps1 | Invoke -Expression的缩写形式；4. 小白可直接在PowerShell里重贴运行即可，不需额外安装Python、git或Node.js，脚本会自动把uv和Python 3.13都搞定。此图与上下文介绍Kimi Code下载与安装的内容相关，直观呈现了安装步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/B1T7bvOIWoNiAWxLhhUcPfL9nOf) · `B1T7bvOIWoNiAWxLhhUcPfL9nOf`

> [!abstract]- 🖼 图片展示的是Kimi Code CLI安装相关说明。其中，绿色框突出显示
> 图片展示的是Kimi Code CLI安装相关说明。其中，绿色框突出显示“是的，Python也会自动安装”，并强调用户可放心告诉小白用户只需运行特定命令，无需提前准备。下方还列出了安装脚本自动完成的三件事：自动安装uv、uv自动下载并安装Python 3.13（若电脑无此版本）、自动安装Kimi Code CLI。此图片与文档中Kimi Code CLI下载与安装部分内容相关，为用户安装该工具提供指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/N59nbBAc6o1iPoxvCauclyJYnfg) · `N59nbBAc6o1iPoxvCauclyJYnfg`

---

关于下载和安装，请看下方视频

<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1664.000000" token="JxanbZ5MYorCKWxHGFjc03gbnkf"/></figure>

# 二、学会看Kimi Code的官方文档

官方文档地址：https://moonshotai.github.io/kimi-cli/zh/guides/getting-started.html

> [!abstract]- 🖼 图片展示了Kimi Code CLI文档页面。页面顶部有搜索栏，右侧有“
> 图片展示了Kimi Code CLI文档页面。页面顶部有搜索栏，右侧有“指南”“定制化”“配置”等导航选项。页面中部标题为“开始使用”，介绍Kimi Code CLI是运行在终端的AI Agent，可完成软件开发任务等。下方列出其支持的使用方式，包括交互式命令行和浏览器界面。页面右侧有“On this page”栏，列出文档相关章节。图片中红色箭头指向“指南”选项，提示可来回切换学习，与上下文介绍学会看Kimi Code官方文档的内容相呼应。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YN0FbSaL5oFkLUxPT8dcdH9Tnrf) · `YN0FbSaL5oFkLUxPT8dcdH9Tnrf`
