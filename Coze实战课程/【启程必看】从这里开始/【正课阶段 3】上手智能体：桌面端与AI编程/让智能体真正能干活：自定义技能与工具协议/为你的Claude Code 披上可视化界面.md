---
title: "为你的Claude Code 披上可视化界面"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/DiRgwyalJiF9Y1ke9NacyswCnud
node_token: DiRgwyalJiF9Y1ke9NacyswCnud
obj_token: YoptdolSZogXC5xGD2ecoq1inFd
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "让智能体真正能干活：自定义技能与工具协议"
  - "为你的Claude Code 披上可视化界面"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 442
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 为你的Claude Code 披上可视化界面

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 让智能体真正能干活：自定义技能与工具协议

# 写在前面

当我们装完 Claude Code 之后，有一些小伙伴还是不习惯命令行的模式

所以我们会为它披上一个壳，这个壳可以让我们用可视化的方式去使用 Claude Code

可视化的方式可以让我们做到左边聊天，右边实时看文件变化，再也不用直接面对命令行

底层干活的还是 Claude Code，只是交互方式变了 

<callout emoji="✨">
这节课我们的核心是一个叫Trae的工具。
但是我在附录里面会给大家提供两个开源作者的软件，大家感兴趣可以尝试
</callout>

# 一、为什么Trae可以当做Claude Code的壳

在动手之前，花两分钟理解一下原理。不理解原理，后面遇到问题你会慌

Trae 是字节跳动出品的代码编辑器，他是一个编程的IDE。

它有两个关键特性让它能成为 Claude Code 的外壳：

**第一，Trae 内置了终端。**

Claude Code 本质上就是一个跑在终端里的程序。Trae 自带终端，意味着 Claude Code 可以直接在 Trae 里面运行，效果和你在系统终端里用完全一样

**第二，Trae 提供了 Claude Code 插件** 

这个插件做的事情很简单，把你和 Claude Code 之间的命令行交互，变成一个聊天界面。

你在聊天框里打字，插件帮你把消息传给 Claude Code，Claude Code 的回复再显示在聊天框里

所以整个链条是这样的：

<callout emoji="✨">
**1）你在 Trae 的聊天框打字**
**2）Trae 的 Claude Code 插件接收**
**3）调用你本地已安装的 Claude Code**
**4）Claude Code 操作你的项目文件**
**5）你在 Trae 的文件面板里直接看到变化**
</callout>

> [!abstract]- 🖼 图片展示了Claude Code在Trae中的工作流程。你先在聊天框里打
> 图片展示了Claude Code在Trae中的工作流程。你先在聊天框里打字，Claude Code插件接收后调用本地已安装的Claude Code，后者操作项目文件，文件变化会在文件面板实时显示。图片以流程图形式呈现，突出Claude Code插件、文件面板、Claude Code底层引擎等关键部分，直观说明了Claude Code在Trae中的操作链条，与上下文对工作流程的描述相契合。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QbggbNq0rodFyfxH5Hacy7CSnJb) · `QbggbNq0rodFyfxH5Hacy7CSnJb`

你已经装好的 Claude Code 还是那个 Claude Code，Trae 只是给它提供了一个更友好的操作界面

# 二、Trae + Claude Code的操作全流程

## 1）下载并安装Trae

1. 打开 Trae 官网：https://www.tra e.cn/ide/download

> [!abstract]- 🖼 图片展示的是Trae官网下载页面。页面上方有“选择适合你的系统”字样，下
> 图片展示的是Trae官网下载页面。页面上方有“选择适合你的系统”字样，下方有三个系统选项，分别是Mac（macOS 12.0+）、Windows（Windows 10, 11）和Linux。每个选项下方都有对应的下载按钮，Mac选项的下载按钮为绿色，显示“下载 .dmg(Apple Silicon)”，Windows选项的下载按钮为绿色，显示“下载 Windows (x64) 版本”，Linux选项的下载按钮为绿色，显示“加入候补名单”。该图片与文档中“下载并安装Trae”部分内容相关，用于指导用户选择适合自己系统的下载版本。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BuDTbzXh2of0n5x7yFnc4lnsn7g) · `BuDTbzXh2of0n5x7yFnc4lnsn7g`

<callout emoji="✨">
注意，由于苹果系统和 Windows 系统没有本质的区别，所以我们这里不再区分版本写教程
本教程使用的是苹果系统
</callout>

1. 下载并且安装

<callout emoji="✨">
这里给大家说一个小插曲：
为了给大家演示从零安装的整个过程，我让 Claude Code 把我的 trae 给深度清删除
</callout>

> [!abstract]- 🖼 图片展示的是Claude Code与Trae配合使用时，关于Trae卸载
> 图片展示的是Claude Code与Trae配合使用时，关于Trae卸载的界面内容。上方红框突出显示“我的电脑上安装了Trae这个软件，我想把它卸载干净，因为我想重新下载，我要给我的学员写教程，我需要从头来一遍”，表明用户需求。下方是终端命令执行结果，列出Trae相关文件路径，如应用程序、配置和数据文件等，还提示在彻底删除前需确认Trae是否运行及是否备份配置或项目文件。该图片与文档中Trae+Claude Code操作全流程中卸载Trae的内容相关，用于辅助说明卸载操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XoJ7bJDWroEAjUxpprPcVlbqnxv) · `XoJ7bJDWroEAjUxpprPcVlbqnxv`

---

我下载了苹果版本的 Trae，然后安装成功之后点击打开

<grid>

> [!abstract]- 🖼 图片展示的是Trae软件的启动界面。背景为深色，中央有一个绿色和白色相间
> 图片展示的是Trae软件的启动界面。背景为深色，中央有一个绿色和白色相间的图标，下方文字为“欢迎使用 TRAE”，下方有一个灰色的“开始”按钮。该图片位于介绍Trae+Claude Code操作全流程的文档中，是在下载并安装Trae后，打开软件时所见的界面，是安装成功后的第一步操作展示，与上下文介绍的Trae安装及后续操作流程紧密相关。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YHahbrESIodjasxYrsAciEVPnmd) · `YHahbrESIodjasxYrsAciEVPnmd`

> [!abstract]- 🖼 图片展示的是Claude Code在安装完成后打开时的界面。界面上方显示
> 图片展示的是Claude Code在安装完成后打开时的界面。界面上方显示“选择您的主题”，并说明可通过菜单或设置随时更改主题。下方有三个主题选项，分别是“暗色”“亮色”“深蓝”，其中“暗色”主题被选中。界面底部有“选择语言”选项，当前语言为“Chinese (Simplified) 简体中文”，下方有一个“继续”按钮。该图片与文档中“安装Claude Code插件”步骤后的操作流程相关，展示了安装完成后进入的初始界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ELKEbVJQoo04mCxK9wbc8iG0nCb) · `ELKEbVJQoo04mCxK9wbc8iG0nCb`

</grid>

<grid>

> [!abstract]- 🖼 图片展示的是Trae软件的偏好设置界面。界面中有“暂不导入”和“使用VS
> 图片展示的是Trae软件的偏好设置界面。界面中有“暂不导入”和“使用VS Code快捷键风格”两个下拉框，下方有“继续”和“跳过”两个按钮。其中，“跳过”按钮被红色框突出显示。该图片对应文档中“安装Claude Code插件”步骤里，安装完成后点击右上角图标打开Claude Code后的操作说明，对于小白而言，这里不需要操作，可直接跳过。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/D9v8bBTq9ok4j4xCuVscl3T7nFh) · `D9v8bBTq9ok4j4xCuVscl3T7nFh`

> [!abstract]- 🖼 图片展示的是安装Claude Code插件时的界面。画面中央有一个带有绿
> 图片展示的是安装Claude Code插件时的界面。画面中央有一个带有绿色边框的图标，下方提示“添加命令行，在Terminal中使用命令'trae-cn'启动”。下方有两个按钮，分别是“安装'trae-cn'命令”和“跳过”，其中“跳过”按钮被红色框突出显示。该图片对应文档中“安装Claude Code插件”步骤里，安装完成后点击右上角图标打开Claude Code后的操作界面，提示可跳过安装命令行部分，减少不必要的动作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/J2vNbsjsEomcK3xNcIjczrqYn0b) · `J2vNbsjsEomcK3xNcIjczrqYn0b`

</grid>

> [!abstract]- 🖼 图片展示了Trae软件的登录注册界面。界面上方有红色箭头指向“选择个人用
> 图片展示了Trae软件的登录注册界面。界面上方有红色箭头指向“选择个人用户登录注册”文字，中间显示“一切就绪，开始体验”，并说明为提供更好服务需登录以使用AI功能。下方有三个选项，分别是“个人用户”（以红色框突出显示）、“企业用户”和“跳过”，其中“个人用户”被红色框重点标识。该图片与文档中“安装Claude Code插件”步骤相关，是安装完成后打开Claude Code时的登录注册界面示例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/EurLbJf0TonNFwxXpsrc44E7nah) · `EurLbJf0TonNFwxXpsrc44E7nah`

> [!abstract]- 🖼 图片展示的是Trae软件界面中Claude Code插件的弹窗提示。弹窗
> 图片展示的是Trae软件界面中Claude Code插件的弹窗提示。弹窗标题为“欢迎使用全新SOLO模式！”，内容介绍SOLO模式集成多种工具，只需表达需求，它会主动推进开发流程。下方有“取消”和“立即体验”两个按钮，其中“立即体验”按钮被红色框突出显示。图片右上角有“与Builder协作”的标识。图片与上下文关系为：在介绍Trae+Claude Code操作流程时，用于说明安装Claude Code插件后打开的界面情况，提示不要体验其solo模式，可自行了解。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Hvb1bR7JVoQ89oxb2M1cotHznWh) · `Hvb1bR7JVoQ89oxb2M1cotHznWh`

## 2）安装Claude Code插件

<callout emoji="✨">
请注意，我们这里不是Trae的详细教程，核心只是为了让大家能有一个 Claude Code 的套壳工具
Trae 的教程，**如果你感兴趣，自行 AI 加联网搜索**
</callout>

第一步：找到 Trae 的插件图标，打开商店，搜索 Claude Code 点击安装

> [!abstract]- 🖼 图片展示了在Trae中安装Claude Code插件的操作界面。左侧边栏
> 图片展示了在Trae中安装Claude Code插件的操作界面。左侧边栏有扩展图标，点击后弹出扩展商店，搜索框内显示“claude code”。图片右侧有红色箭头和文字提示，分别指向搜索框和安装按钮，提示“搜索 Claude Code，点击安装”及“1. 点击左侧边栏的扩展图标”。该图片与文档中“安装Claude Code插件”部分内容对应，直观呈现了操作步骤，帮助用户在Trae中找到并安装Claude Code插件。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WCTKbn2ndoIS5jxUZKCcO4idn3c) · `WCTKbn2ndoIS5jxUZKCcO4idn3c`

第二步：安装完成后，点击右上角的图标打开 Claude Code

<grid>

> [!abstract]- 🖼 图片展示了Claude Code for VS Code的插件页面。页面
> 图片展示了Claude Code for VS Code的插件页面。页面左上角有“IDE”“选择项目”“搜索”等选项，右上角有“...”等图标。页面中间是Claude Code for VS Code的图标及名称，下方有功能介绍，如使用Claude模型、与IDE协同工作等。右侧有“安装”按钮，旁边有“自动更新”选项。右上角有一个红色框突出显示的图标，旁边有红色箭头指向，箭头下方文字提示“安装完成后，点击打开Claude Code”。该图片与上下文关系紧密，直观呈现了安装完成后打开Claude Code的操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/PJFvbmRh5o7Tz7xhn2VcRasSnUe) · `PJFvbmRh5o7Tz7xhn2VcRasSnUe`

> [!abstract]- 🖼 图片展示了安装并打开Claude Code插件后的Trae界面。界面中突
> 图片展示了安装并打开Claude Code插件后的Trae界面。界面中突出显示“Claude Code”字样，下方有“Ask about this codebase or we can start writing code.”的提示，以及“Opus now defaults to 1M context”等信息。界面底部有“Ask Claude to edit...”和“Ask before edits”两个选项。图片与上文“安装Claude Code插件”内容相关，直观呈现了安装完成后进入的界面状态，帮助用户确认是否成功安装并打开Claude Code插件。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JeHBbPttuo1ch2xD4tHc1myDnxf) · `JeHBbPttuo1ch2xD4tHc1myDnxf`

</grid>

当你出现上边的第二张图之后，恭喜你，已经可以在 Tree 里面使用 Claude Code 了

## 3）Trae + Claude Code的最佳实践

<callout emoji="✨">
这里我通过一个视频来给大家演示
</callout>

> [!warning]- 🎬 视频（`video/quicktime`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/DLTYbGcmpoixeUx8lsPcqfBingf) · `DLTYbGcmpoixeUx8lsPcqfBingf`

## 4）总结说明

> [!abstract]- 🖼 图片展示了使用Claude Code的工作流程。首先打开Trae启动软件
> 图片展示了使用Claude Code的工作流程。首先打开Trae启动软件，接着打开项目选择文件夹，然后用自然语言聊天提需求，最后看结果，文件面板会实时更新。该图与文档中介绍的日常工作流程相呼应，直观呈现了从启动软件到查看结果的完整操作步骤，帮助用户理解Claude Code基于文件夹工作的本质。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ZJnob0jQkocLmaxBBGlcW9YTnod) · `ZJnob0jQkocLmaxBBGlcW9YTnod`

当你安装 Tree 和 Claude Code 之后，你日常的工作流程就是打开 Tree 选择一个文件夹，然后打开 Claude Code 用自然语言去提需求，你的文件面板也会实时更新

最后我想跟大家强调几点

1. 学会使用 Claude Code 的第一个点，**一定要理解它是基于一个文件夹去工作的本质**
2. 本教程不是Trae的使用教程，Trae只是它的一个套壳
3. 如果你真的理解了原理，我们也可以利用 Trae 帮我们去安装 Claude Code，这也是市面上一种比较主流的 Claude Code 的安装方式

# 附录

<callout emoji="✨">
除了Trae，还有一些开源作者，他们利用Claude Code去开发了Claude Code的UI软件。
我给大家找到了两个反馈不错的开源软件，大家自行去尝试比较
⚠️：但需要注意的是，**开源软件会有这样或者那样的 bug**
你的电脑可能用不了，你可以去他的 GitHub 上去提你的问题，也可以加入他的反馈群
**但是不要问我，因为我不是软件的开发作者，很多问题我解不了**
</callout>

## 小七姐的TOKEN NODE

地址：https://github.com/yiliqi78/TOKENICODE/blob/main/README_zh.md#%E5%AE%89%E8%A3%85

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/CvnZbS2AKoTimuxkEPbcrgTcn4b) · `CvnZbS2AKoTimuxkEPbcrgTcn4b`

## 归藏的CodePilot

https://github.com/op7418/CodePilot

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/LeVDbp9NCopODqxRRqxcywY4nxX) · `LeVDbp9NCopODqxRRqxcywY4nxX`
