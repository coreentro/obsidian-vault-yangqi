---
title: "Claude Code安装之跳过登陆验证和中转API配置"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/Gr7bw5h0xiDYpJkd0wFca6eZnVb
node_token: Gr7bw5h0xiDYpJkd0wFca6eZnVb
obj_token: JeLJdE47MoGlkox5rufclhO8npg
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "命令行智能体：一种全新的智能体交互方式"
  - "Claude Code安装之跳过登陆验证和中转API配置"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 10
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# Claude Code安装之跳过登陆验证和中转API配置

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 命令行智能体：一种全新的智能体交互方式

# 写在前面

你好，我是大圣

安装完Claude Code之后，并不能立马去打开使用，还要做一些配置

# 一、为什么要做配置

> [!abstract]- 🖼 图片展示了Claude Code的执行架构与AI大脑的关系。左侧为执行架
> 图片展示了Claude Code的执行架构与AI大脑的关系。左侧为执行架构（身体），包含终端交互、文件读写、代码执行、工具调用等模块；右侧为AI大脑（可替换），有Claude、GPT、Kimi、Gemini/DeepSeek等模型。中间有API调用箭头。底部文字说明“工具决定能做什么，大脑决定做得多好”。该图与上下文紧密相关，直观呈现了Claude Code执行任务时，执行架构与AI大脑的交互关系，强调了AI大脑在任务执行中的重要性。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WseTbV2BkoeAVHxqEwPcKw0SnSb) · `WseTbV2BkoeAVHxqEwPcKw0SnSb`

前面跟大家讲过，Claude Code它是一个执行架构，它要想干活，你必须给它配置大脑

所以这节课核心就是要给你的Claude Code去配置上AI模型

而这里面还有一个卡点，跟当初的Kimi Code一样，Kimi Code是Kimi Code的工具。

所以他当然希望你用它自家的模型  
  
于是我们在使用Kimi Code的时候，我们会登录Kimi的账号，然后就可以自动使用Kimi的官方订阅了

Claude Code也有这样的逻辑，但它最大的问题就是它的官方订阅太难了，需要解决各种问题，所以95%的人搞不定

但是它在启动的时候又有一个登录校验，所以我们要做的是两件事儿：

1. 跳过这个登录校验
2. 配置一个第三方的API

# 二、下载安装CC-Switch

我们上面要做的两件事儿，有一个工具专门帮我们做了

这个工具叫做CCswitch，从它的名字你也应该能够看出来，CC就是Claude Code，switch就是切换

这是一个开源项目，官方地址：https://github.com/farion1231/cc-switch/blob/main/README_ZH.md

下载地址：https://github.com/farion1231/cc-switch/releases

**上面的地址是github，国内网络是可以访问的，但可能会比较慢，偶尔也会抽风**

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/La1YbGRigoo6aIxZ7IOcttrSnld) · `La1YbGRigoo6aIxZ7IOcttrSnld`

# 三、配置中转API

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/IpAnbDRa5oM775xcWAvc1LZfn0g) · `IpAnbDRa5oM775xcWAvc1LZfn0g`

后面你会不断地接各种模型的 API，**这个在前面的课程里，我已经给大家详细地讲解过了**

接下来这个图你一定要理解，不管你接什么 API，你一般都需要三个要素：

1. API 地址

这个地址就是一个网址，它决定了你付费、要访问的模型是谁家的

1. 密钥

密钥就是你要带着的一把钥匙，通过它去访问，方便人家识别你的身份，给你计费

1. 模型 ID

你要告诉它你访问的是哪个模型

这里我一定要强调，大家一定要在这个教程里面去理解它本质的逻辑

因为没有任何一个教程可以告诉你全部的接入 API 的方式，但只要你理解了它的逻辑，未来不管你是接入 Kimi、OpenAI 还是 Gemini，只要去找这三个点就好了。找到了，你就能配置成功

> [!abstract]- 🖼 图片展示了访问一个API所需的三个要素。上方为“访问一个API”，下方有
> 图片展示了访问一个API所需的三个要素。上方为“访问一个API”，下方有三条箭头分别指向“API地址”“密钥”“模型ID”。其中“API地址”示例为https://claudecn.top，“密钥”未给出示例，“模型ID”示例为claude - opus - 4 - 6。该图与上下文紧密相关，上下文提到在接入API时，一般需这三点要素，且强调理解其本质逻辑，未来接入不同模型API时可按此逻辑配置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LhdqbuZ75oUtAwxSTxbcGgvOniY) · `LhdqbuZ75oUtAwxSTxbcGgvOniY`

我们接下来配置3个中转API

1. Kimi Code Plan：https://www.kimi.com/code/console

1. AIGOCode：https://aigocode.com/invite/WB3DJX6W

1. ClaudeCN：https://claudecn.top/register?aff=UyTK

# 写在最后

CC-Switch官方文档：https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/zh/1-getting-started/1.1-introduction.md
