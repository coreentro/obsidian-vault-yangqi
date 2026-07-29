---
title: "OpenClaw的命令和插件配置"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/A654wmnTgi8kjfkooAvc63Z7ntc
node_token: A654wmnTgi8kjfkooAvc63Z7ntc
obj_token: AjzkdnsJvoL8NTxbcakciMEknGd
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "OpenClaw专区"
  - "OpenClaw的命令和插件配置"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 210
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# OpenClaw的命令和插件配置

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › OpenClaw专区

<callout emoji="✨">
当我们部署完龙虾之后，有一些最初始的命令和插件需要大家了解一下。这涉及到一些最佳实践
</callout>

# 一、OpenClaw的版本

OpenClaw 的版本更新非常快，所以我们要学会查看它的版本，并且做出更新

```Bash
openclaw -v
```

> [!abstract]- 🖼 图片展示了OpenClaw的版本信息。上方显示“大圣的助手”机器人标识，
> 图片展示了OpenClaw的版本信息。上方显示“大圣的助手”机器人标识，右侧有“09:15”时间。下方有用户发送的“/openclaw -v”指令，机器人回复“OpenClaw 版本仍是 2026.3.11 (commit: 29dc654)”并附有绿色对勾。该图片与文档中介绍OpenClaw版本相关内容对应，直观呈现了OpenClaw当前版本及更新情况，帮助用户了解其版本信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OLGLbw0Fwodcjsx3yKtc2pMHnOh) · `OLGLbw0Fwodcjsx3yKtc2pMHnOh`

<callout emoji="✨">
像扣子上购买的，这个 OpenClaw 还会提醒你需要升级版本
</callout>

![图片展示了OpenClaw实时浏览器界面。界面上方显示版本为2026.3.11，健康状况正常。中间区域有“Update available: v2026.3.13 \[running v2026.3.11\]”提示，右侧有“Update now”按钮。下方是聊天区域，用于快速干预的直接网关聊天会话。该图片与文档中OpenClaw版本更新内容相关，直观呈现了OpenClaw版本信息及更新提示，帮助用户了解其版本情况。](https://feishu.cn/file/T41Sbikomop79vxsqgJcbhxtnFd)

---

现在OpenClaw的版本升级非常快，有时候一天一个版本。我们可以自行选择是否更新

<callout emoji="✨">
这里最重要的是大家要注意，版本更新可能会导致bug，大家要有这个预期
我讲这个并不是不让大家去更新，一个新生软件，它的每一次更新可能都会带来非常好用的能力
</callout>

```Bash
openclaw update
```

我们可以直接使用龙虾的管理助手帮我们去更新

> [!abstract]- 🖼 图片展示了使用龙虾管理助手更新OpenClaw的操作界面。对话窗口显示用
> 图片展示了使用龙虾管理助手更新OpenClaw的操作界面。对话窗口显示用户指令“帮我把OpenClaw更新到最新版本”，助手回复正在检查配置和更新设置等。右侧控制台区域显示当前版本为2026.3.8，有新版本2026.3.13可用，点击“开始更新”可进行操作，但因安装方式限制，自动更新被跳过，需通过包管理器手动更新。图片与上下文紧密相关，直观呈现了使用龙虾管理助手更新OpenClaw的过程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ZGCtbJPlToQ0wPxLj0HcCE2En9c) · `ZGCtbJPlToQ0wPxLj0HcCE2En9c`

但是你会发现飞书妙搭不让你更新，这个也非常容易理解。

云端必须统一管理，用户如果可以随意更新的话，那很可能就会把系统更新崩

> [!abstract]- 🖼 图片展示了OpenClaw的控制台界面。左侧显示“大圣的飞书专属Claw
> 图片展示了OpenClaw的控制台界面。左侧显示“大圣的飞书专属Claw”及调用2次工具，下方有当前状态信息，如全局OpenClaw CLI版本为2026.3.8，项目本地依赖已是最新。右侧是控制台主界面，有“聊天”“概述”“实例”“会话”“使用情况”“定时任务”“代理”等选项卡，当前选中“聊天”，下方有“用于快速干预的直接网关聊天会话”等信息。图片与上下文关系为，直观呈现了OpenClaw的控制台操作界面，辅助说明其功能和状态。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/IOwWbxWekoxJ7ZxLwe5ccLUnnQe) · `IOwWbxWekoxJ7ZxLwe5ccLUnnQe`

---

<callout emoji="✨">
扣子是可以做OpenClaw更新的，但更新之后有一个小插曲，飞书用不了了
所以我让龙虾管理助手帮我修复了飞书的问题，它也成功修复了
这个案例是想告诉伙伴们，龙虾就是这么的不稳定
</callout>

> [!abstract]- 🖼 图片展示了OpenClaw助手更新成功的界面。左侧显示当前版本为282 
> 图片展示了OpenClaw助手更新成功的界面。左侧显示当前版本为282 6.3.13（stable），并更新了3个插件，分别是feishu - openclaw - plugin、openclaw - cozeelop - trace、wecom - openclaw - plugin。右侧是OpenClaw聊天界面，有“Help me configure a channel”等指令。图片与上下文关系紧密，直观呈现了上文提到的扣子更新成功后，OpenClaw助手修复飞书问题的场景，展示了更新后的状态。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RLYubBsnToSXzvxzJXIcCVxxnVg) · `RLYubBsnToSXzvxzJXIcCVxxnVg`

> [!abstract]- 🖼 图片展示了OpenClaw助手与OpenClaw聊天界面。左侧是助手界面
> 图片展示了OpenClaw助手与OpenClaw聊天界面。左侧是助手界面，显示“OpenClaw助手”标题，有“回到该版本”“查看修改记录”等选项，中间有“为什么我发现你更新之后，飞书用不了了？帮我排查一下问题。”的提问。右侧是OpenClaw聊天界面，显示“main - 大圣”“auto”等信息。该图片与上下文关系紧密，是助手帮助排查飞书用不了问题的场景呈现，直观展示了问题提出及助手响应的对话界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/C0k3bOPa0osAx2xZnhOc34Z7nWb) · `C0k3bOPa0osAx2xZnhOc34Z7nWb`

> [!abstract]- 🖼 图片展示了OpenClaw助手的修复飞书问题过程。左侧红框内说明飞书问题
> 图片展示了OpenClaw助手的修复飞书问题过程。左侧红框内说明飞书问题已修复，原因是OpenClaw后飞书插件出现ID不匹配错误，修复步骤包括查看错误日志、修改openclaw.json配置等。右侧是OpenClaw聊天界面，显示了与助手的对话，助手回复了修复情况及后续操作，还展示了飞书插件状态。该图片与文档中龙虾管理助手修复飞书问题的案例相关，直观呈现了修复过程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/EOG4b3XtXoLQj0xzka0ctlGlngT) · `EOG4b3XtXoLQj0xzka0ctlGlngT`

# 二、飞书官方插件

插件你可以认为是对于 OpenClaw 能力的一个扩展

比方说，我想要 OpenClaw 和飞书深度集成。如果单单 OpenClaw 去开发这个功能的话，会非常麻烦。但如果飞书官方下场，他们可以开发一个叫插件的功能，就可以方便地把 OpenClaw 和飞书集成起来

下方两个文档就是飞书官方插件的说明和使用教程

[OpenClaw飞书官方插件上线｜一文讲清功能、安装更新教程与常见问题！ - 飞书官网](https://www.feishu.cn/content/article/7613711414611463386)

[OpenClaw 飞书官方插件使用指南（公开版） | OpenClaw Feishu Official Plugin User Guide (Public Version )](https://axsppz4oyvj.feishu.cn/docx/MFK7dDFLFoVlOGxWCv5cTXKmnMh)

## 1）安装并开启飞书官方插件

在我做教程的当下，飞书妙搭天然支持飞书插件，用如下方式测试即可

> [!abstract]- 🖼 图片展示了OpenClaw飞书官方插件的常见诊断命令与问题修复内容。在与
> 图片展示了OpenClaw飞书官方插件的常见诊断命令与问题修复内容。在与AI的对话中，可发送命令确认安装情况、检查配置、批量完成用户授权等。其中，/feishu start用于确认是否安装成功，/feishu doctor可检查配置是否正常，/feishu auth可批量完成用户授权。此外，插件还内置了常见问题解决方案，遇到问题可先询问小龙虾。该图片与上文介绍飞书官方插件安装开启等内容相呼应，为使用插件提供操作指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Ce9EbLoCZoUrgdxzdpFci5LTnlc) · `Ce9EbLoCZoUrgdxzdpFci5LTnlc`

> [!abstract]- 🖼 图片展示了OpenClaw飞书官方插件的使用情况。大圣发送“/feish
> 图片展示了OpenClaw飞书官方插件的使用情况。大圣发送“/feishu start”指令后，系统回复飞书OpenClaw插件已启动。接着，大圣询问当前安装的飞书OpenClaw插件，系统回复是飞书OpenClaw插件（而非飞书官方功能），并列出其核心插件（feishu - openclaw - plugin）及位置。该图片与上下文紧密相关，直观呈现了飞书官方插件的安装与开启状态，以及其核心插件信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SH96bi1yEoPMUpxFQqzczvlRnHe) · `SH96bi1yEoPMUpxFQqzczvlRnHe`

---

但是扣子，它默认使用的是 OpenClaw 内置的飞书插件

> [!abstract]- 🖼 图片展示了OpenClaw飞书官方插件的安装与使用情况。左侧为OpenC
> 图片展示了OpenClaw飞书官方插件的安装与使用情况。左侧为OpenClaw助手界面，显示已安装2个飞书插件，分别是OpenClaw内置插件（stock版本）和飞书官方npm插件。右侧是飞书聊天界面，显示OpenClaw当前使用的是code/auto模型，可与助手交流。该图片与上下文紧密相关，直观呈现了飞书官方插件的安装状态及使用情况，辅助说明飞书官方插件的安装与使用方法。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OCYgbhOcJog68rx2nrBcVKwfnbd) · `OCYgbhOcJog68rx2nrBcVKwfnbd`
