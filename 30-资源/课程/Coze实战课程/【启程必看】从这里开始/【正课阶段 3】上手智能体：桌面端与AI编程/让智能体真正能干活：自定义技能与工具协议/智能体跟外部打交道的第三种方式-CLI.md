---
title: "智能体跟外部打交道的第三种方式-CLI"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/FM1PwvWRpi4xYCk4hW4cjmUvnbg
node_token: FM1PwvWRpi4xYCk4hW4cjmUvnbg
obj_token: StEBd3QiBo4qeExbeb3cieHOn4d
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "让智能体真正能干活：自定义技能与工具协议"
  - "智能体跟外部打交道的第三种方式-CLI"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 892
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 智能体跟外部打交道的第三种方式-CLI

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 让智能体真正能干活：自定义技能与工具协议

# 写在前面

你好，我是大圣

前面的课程已经给大家讲过了API、MCP还有Skill

这节课我们接触一个新名词，叫做CLI

我会给你讲清楚CLI到底是什么，他为了解决什么问题？它和API、MCP还有Skill之间的关系是什么

并且我会使用飞书CLI给你举个例子，带你从安装到使用，亲手走一遍闭环

**PS：本节案例我会使用Claude Code进行演示，但对于WorkBuddy、Kimi Code没有任何的不同**

# 一、智能体如何与外部交互

智能体之所以比AI大模型本身强大，是因为它能够和外部进行交互

比如，它可以通过API来获取证券交易所的股票数据

再比如它可以通过MCP与高德地图进行交互，从而查询最新的天气信息

所以前面不管我们讲的API还是MCP，它们的本质都是为了更好、更方便地让智能体和外部交互

而CLI则是智能体跟外部打交道的另一种方式

# 二、CLI到底是什么

CLI 的全称是 Command Line Interface，翻译过来叫命令行接口

用最熟的 Claude Code 举个例子：Claude Code 本身就是个 CLI 工具

第一步：你打开终端,敲一个命令：claude

然后点击回车，Claude Code就启动了；这就是CLI：你用一行命令，让一个应用动起来

> [!abstract]- 🖼 图片展示了Claude Code的CLI界面。终端中显示“Welcome
> 图片展示了Claude Code的CLI界面。终端中显示“Welcome back Russell!”及Claude Code版本信息，还呈现了当前用户、邮箱、组织等信息。右侧有“Tips for getting started”等内容，如“Run /init to create a CLA...”等。下方有“Try 'fix lint errors'”提示，以及Opus 4.6（1M context）和Pro状态标识。该图与上文介绍的CLI概念相呼应，直观呈现了使用CLI命令启动Claude Code及后续操作的界面情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/R8VRbe2tmoZ1IBxviQJcZF0Znof) · `R8VRbe2tmoZ1IBxviQJcZF0Znof`

---

Claude Code这个例子还有更妙的地方

启动之后，你跟它说："帮我看看当前文件夹里都有啥？"，它怎么做的?

它在背后帮你执行了 `ls` 这个命令

> [!abstract]- 🖼 图片展示了Claude Code的CLI界面。左侧显示当前用户信息及工作
> 图片展示了Claude Code的CLI界面。左侧显示当前用户信息及工作目录，右侧有欢迎信息和提示。中间部分是用户指令“ls -la /Users/lmh/projects/个人介绍网站”，用于列出指定目录下的文件和目录信息。下方有“Listing 1 directory...”提示，表明正在执行指令。右侧还列出了一些开始使用Claude的提示，如运行`/init`创建CLAUDE等。该图片直观呈现了文档中提到的CLI在后台执行命令的功能，辅助理解CLI在Claude Code中的应用。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SUGkbLaUroMZYPxGvGXcWrjXn0f) · `SUGkbLaUroMZYPxGvGXcWrjXn0f`

而且Claude Code本身也可以通过命令的方式来控制，比如你要退出，你输入exit

> [!abstract]- 🖼 图片展示了Claude Code v2.1.123的界面，上方显示欢迎信
> 图片展示了Claude Code v2.1.123的界面，上方显示欢迎信息及版本号等。右侧有“Tips for getting started”等内容。下方命令行区域，箭头指向“/e”命令，旁边文字说明“这就是Claude Code支持的命令”，并列出“/exit”“/effort”“/export”“/extra - usage”等命令及其功能，如退出CLI、设置模型使用努力水平等。该图片与上下文紧密相关，直观呈现了Claude Code支持的CLI命令，帮助理解其在背后执行操作的能力。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LoZhbEF7wot8a7xy60PcpSSZnGM) · `LoZhbEF7wot8a7xy60PcpSSZnGM`

这里有两层 CLI 在发生:

- 第一层：你用 CLI 启动了 Claude Code(敲 `claude`)
- 第二层：Claude Code 用 CLI 帮你操作电脑(敲 `ls`、`cd` 这些)

你天天用 Claude Code，其实你不只在用 CLI，你还在看着 AI 用其他的 CLI 帮你干活

# 三、终端是CLI么？

这是一个很容易让大家困惑的地方

终端不是CLI，它是一个窗口，它负责承载输入和输出

CLI是你在窗口里跟程序对话的方式

而那些被设计成通过命令调用的程序，比如Claude Code，比如Git，我们叫它CLI工具

> [!abstract]- 🖼 图片是一张表格，对比了终端、CLI和CLI工具的概念、定义及例子。终端（
> 图片是一张表格，对比了终端、CLI和CLI工具的概念、定义及例子。终端（Terminal）是一个窗口，负责承载输入和输出，例子有Terminal.app、iTerm、Warp等；CLI是一种交互方式，即敲命令、看输出，不是具体物体，是“形式”；CLI工具是被设计成“通过
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/A61ybzA6Do6ta7xxAyRcVDjrn3D) · `A61ybzA6Do6ta7xxAyRcVDjrn3D`

# 四、为什么CLI对智能体很友好

要回答这个问题，得先回到 CLI 的一个本质特点上：

**CLI 是文本进、文本出**

你敲一行命令文字进去，它吐一段文字出来

**而AI最擅长的正是生成文本、理解文本**

所以CLI的这种工作方式跟AI大模型是天作之合

世界上过去几十年积累的几万个CLI工具，AI一夜之间全部都能调用

这也是为什么Claude Code可以很方便地操纵你电脑上的文件，对它进行增删改查

因为增删改查文件都有专门的CLI工具，对AI非常友好

# 五、Skill、API、MCP和CLI到底什么关系？

我先给你画一张图

> [!abstract]- 🖼 图片是一张流程图，展示了Skill、API、MCP、CLI与外部世界的关
> 图片是一张流程图，展示了Skill、API、MCP、CLI与外部世界的关系。Skill位于最上方，其下分别连接API、MCP、CLI，三者再共同指向外部世界。其中，API是应用编程接口，MCP是模型上下文协议，CLI是
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VIATbBKmRoylySxHywbcEr4YnWg) · `VIATbBKmRoylySxHywbcEr4YnWg`

首先，skill是一个更上层的概念，它的本质是封装你的业务流

而在封装你的业务流的过程中，你可能需要跟外部世界进行数据的交换。那这个时候你会用到API、MCP或者CLI

相信你一定会问一个问题：这三者有什么区别？

**这三者的边界其实没那么硬，纠结对比意义不大，记住下面这个最佳实践就行**

我能给你的最佳实践就是：

<callout emoji="✨">
第一：如果他只提供了一种方式，那你没有别的选择
第二：如果他提供了多种方式，让你的AI帮你选择
第三：我自己倾向于CLI和API，MCP我现在很少用
</callout>

# 六、一个飞书CLI的例子

讲完了理论部分，接下来我们通过一个实际的例子，让你感受CLI的强大

飞书把自己的功能封装成了CLI

你可以安装它的CLI，然后让你的agent通过CLI去和飞书进行交互

接下来我的演示会让你感受到一种前所未有的交互体验

<callout emoji="✨">
本节案例我会使用Claude Code进行演示
但对于WorkBuddy、Kimi Code没有任何的不同
</callout>

## 6.1 安装飞书CLI

秉持我们的一贯作风，找到官方文档，丢给Claude Code或者CodeX，让它帮我们装

**这里有个注意的点，我们不仅要装CLI，更重要的是安装CLI Skill**

所以大家在使用安装的时候推荐

<callout emoji="✨">
帮我装一下这里面所有的东西：https://github.com/larksuite/cli/blob/main/README.zh.md
</callout>

> [!abstract]- 🖼 图片展示了lark-cli的相关信息。其为飞书官方CLI工具，由lark
> 图片展示了lark-cli的相关信息。其为飞书官方CLI工具，由larksuite团队维护，可让人类和AI Agent在终端中操作飞书，涵盖多种核心业务，提供200+命令及24个AI Agent Skills。突出显示了其为Agent原生设计、覆盖广、AI友好调优等优势，以及功能如三方登录、安全可控等。该图与上下文紧密相关，是对飞书CLI能力介绍与最佳实践的补充说明，帮助理解其特点和优势。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Zh1AbtqgpojrR7xxwBscPs9gned) · `Zh1AbtqgpojrR7xxwBscPs9gned`

---

如果你想通过官网来装，使用如下的途径，但它可能不会装skill

地址：https://www.feishu.cn/feishu-cli

<grid>

> [!abstract]- 🖼 图片展示了飞书CLI的安装页面。上方标题为“飞书CLI 仅需一行指令，在
> 图片展示了飞书CLI的安装页面。上方标题为“飞书CLI 仅需一行指令，在任意 Agent 操作飞书”，下方有“手动安装”和“通过 AI Agent 安装”两个选项，其中“手动安装”被红色框突出显示。下方灰色区域显示安装命令“npx @larksuite/cli@latest install”，并有“复制”按钮。底部有绿色勾选图标及文字说明，配置完成后重启AI Agent即可开始使用，并给出使用指南、开源地址、更新日志等链接。该图片与上下文介绍的飞书CLI安装步骤相关，直观呈现了安装页面及操作指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/KUu4b12L9og1FDxoo7zc1Hidnmh) · `KUu4b12L9og1FDxoo7zc1Hidnmh`

> [!abstract]- 🖼 图片展示了飞书CLI的安装页面。上方标题为“仅需一行指令，在任意Agen
> 图片展示了飞书CLI的安装页面。上方标题为“仅需一行指令，在任意Agent操作飞书”，并有“手动安装”和“通过AI Agent安装”两个选项，其中“通过AI Agent安装”被红色框突出显示。下方提示词区域有“帮我安装飞书CLI”及对应网址，下方还有“复制提示词”按钮。页面底部有绿色勾选框，提示配置完成后重启AI Agent即可开始使用，并给出“使用指南”“开源地址”“更新日志”等链接。该图片与上下文紧密相关，直观呈现了飞书CLI安装的途径之一，即通过AI Agent安装。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BbmYb6plZoqMWxxnwUTcahz0nDg) · `BbmYb6plZoqMWxxnwUTcahz0nDg`

</grid>

官网使用指南：[飞书 CLI 能力介绍与最佳实践](https://axsppz4oyvj.feishu.cn/wiki/ILuTww7Xcimb6GkhH0mcK2f4nS7)

## 6.2 授权与配置

这一步也非常好理解：我们到底要跟哪个飞书账号去通信？

那我们得把这个飞书账号授权给你的CLI

这里最大的误区就是，不是你有了CLI工具，你就可以访问所有的飞书文档了。

它是首先要完成授权，**而它能访问的权限和你的飞书账号所能访问的权限是一样的**

---

第二步：配置应用凭证

> [!abstract]- 🖼 图片展示了飞书CLI安装成功后的界面，其中突出显示了“第2步 - 配置应
> 图片展示了飞书CLI安装成功后的界面，其中突出显示了“第2步 - 配置应用凭证”步骤。画面中有一个红色箭头指向“复制该链接，打开浏览器登录你的飞书账号授权”文字，强调了此操作。该图片与文档中介绍飞书CLI安装流程的内容相关，是安装完成后进入配置应用凭证步骤前的提示，帮助用户明确下一步操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FvARbuTntoyPROxrBPWcRqbLnId) · `FvARbuTntoyPROxrBPWcRqbLnId`

复制上述链接，在浏览器中打开，会让你创建一个飞书CLI应用

然后你点击创建，这个应用就创建完了

**PS：如果你以前创建过，可以选择已有的应用**

<grid>

> [!abstract]- 🖼 图片展示的是创建飞书CLI应用的界面。上方显示“创建飞书CLI应用”，下
> 图片展示的是创建飞书CLI应用的界面。上方显示“创建飞书CLI应用”，下方有头像选择区域，可选择多个头像。名称处输入“大圣的飞书CLI”，下方提示“创建后，自动完成所有配置”。下方有“创建”和“选择已有应用”两个按钮。该图片对应文档中“配置应用凭证”步骤，即复制链接在浏览器打开后，点击创建飞书CLI应用的界面，用于创建飞书CLI应用，与上下文介绍的飞书CLI配置流程紧密相关。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XW1lb8hBPoWGsLx7r1EcmOoWnBG) · `XW1lb8hBPoWGsLx7r1EcmOoWnBG`

> [!abstract]- 🖼 图片展示的是飞书CLI应用创建成功界面。画面中央有一个手握画笔的卡通形象
> 图片展示的是飞书CLI应用创建成功界面。画面中央有一个手握画笔的卡通形象，画笔上有一个绿色的对勾。下方文字显示“创建成功”，并提示“现在可前往 CLI，开始使用飞书 CLI 应用”。该图片与文档中“配置应用凭证”步骤相关，说明在浏览器中打开链接创建飞书CLI应用后，若选择“创建”则应用创建成功，可继续后续操作，如登录授权等。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Gc2ZbwFqlo23DrxhCBacY4oHnJf) · `Gc2ZbwFqlo23DrxhCBacY4oHnJf`

</grid>

---

第三步：登录授权

复制Claude Code给你的链接，在浏览器中打开

> [!abstract]- 🖼 图片展示了飞书CLI安装过程中登录授权的步骤。画面中显示了命令行界面，有
> 图片展示了飞书CLI安装过程中登录授权的步骤。画面中显示了命令行界面，有“lark-cli”相关命令及输出信息。关键部分是红色框标注的“应用配置完成！现在执行第 3 步 - 登录授权”，并有箭头指向“Claude Code会自动跳到第三步，登录授权”说明。该图片与上下文紧密相关，是对上文“复制Claude Code给你的链接，在浏览器中打开”步骤的呈现，指导用户完成登录授权操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CZr0bklPzocegVx0uiEcl4u1nid) · `CZr0bklPzocegVx0uiEcl4u1nid`

> [!abstract]- 🖼 图片展示的是飞书CLI登录授权界面。上方显示“飞书 CLI”，中间有“确
> 图片展示的是飞书CLI登录授权界面。上方显示“飞书 CLI”，中间有“确定开通并授权以下权限吗？”的提示，下方列出多项权限，如复制多维表格、创建多维表格等，其中“一并开通审批、多维表格、日历、通讯录、文档、消息与群组、邮箱、电子表格、幻灯片、任务、视频会议的常用权限”被红色框突出显示。图片中还有一处红色箭头，标注“由于是我自己的账号，我就全开了”，并有“开通并授权”蓝色按钮。该图片与文档中“登录授权”步骤相关，展示了授权时的权限选择界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/TryqbIBieohNUZx8uG1co7GJnZc) · `TryqbIBieohNUZx8uG1co7GJnZc`

第四步：告诉Claude Code授权完成，验证登录状态

> [!abstract]- 🖼 图片展示的是飞书CLI安装完成后，登录授权步骤的验证结果界面。画面中“授
> 图片展示的是飞书CLI安装完成后，登录授权步骤的验证结果界面。画面中“授权完成”以红色框突出显示，下方有安装结果信息，包括应用ID、品牌、登录状态、用户、token有效期等，还提到已授权飞书日历、消息、文档等业务。该图片与上文“登录授权”步骤相关，用于说明在浏览器打开链接完成授权后，通过此界面验证登录状态，是飞书CLI安装完成并拥有相应Skill的确认步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Thr8bTXjioeVMnxlHCMcdYSwnid) · `Thr8bTXjioeVMnxlHCMcdYSwnid`

到现在为止，你已经把飞书CLI安装完成，并且拥有如下的Skill

> [!abstract]- 🖼 图片展示了飞书CLI安装完成后所拥有的Skill列表，包含lark - 
> 图片展示了飞书CLI安装完成后所拥有的Skill列表，包含lark - base、lark - calendar、lark - contact等多项。这些Skill从名字可看出对应飞书云文档、云盘、聊天、邮件等能力。其与上下文关系为，上文介绍了飞书CLI从授权、配置应用凭证、登录授权到验证登录状态的安装步骤，图片则是安装完成后所具备Skill的呈现，直观地让读者了解飞书CLI可实现的功能范围。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HtMhbut47o0yMExtv3XcRennnWd) · `HtMhbut47o0yMExtv3XcRennnWd`

通过名字你就可以看出它的能力，飞书云文档、飞书云盘、飞书聊天、飞书邮件等等

## 6.3 为什么要把CLI封装成Skill

当我们使用飞书 CLI干活的时候，我们本质是在使用Skill干活

你可能会问为什么要把飞书CLI做成skill

因为skill是Claude Code、CodeX这样的agent执行任务的统一标准

所以你如果想要在Claude Code CodeX中使用飞书 CLI，封装成skill是最方便的方式

**所以在后面任何一家应用提供了自己的CLI之后，本质都会再去把它封装成skill**

因为在AI时代，人不会自己去敲命令使用CLI，而是让agent去使用。

而agent使用外部能力的规范，就是Skill

## 6.4 使用飞书Skill进行工作

说实话，这一节真的没什么可讲的，就是自然语言口喷

你唯一需要注意的可能就是：你想要的能力飞书CLI是否有提供，以及你是否开了权限

而如果没有开权限，你也完全可以让你的agent去重新申请新的权限

接下来我们通过一个简单的案例进行分享

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/Vt4PbZ06sobsKOxlmHqcEOC0n8b) · `Vt4PbZ06sobsKOxlmHqcEOC0n8b`

# 七、写在最后

未来会有更多的应用去封装自己的CLI或者skill

比如微信读书已经出了自己的skill

所以我希望大家能够通过这节课去理解未来你重要的能力到底是什么？

AI编程的门槛一再降低。在没有CLI、没有agent之前，如果你要跟飞书通信，只有程序员能做到

而现在所有人都可以

最后给大家分享我的三个认知

第一：程序员不再是一个职业，而是一项技能

第二：技术的实现不再重要，重要的是你的业务

第三：未来所有的产品不仅要让人容易使用，更重要的是，要让Agent更容易使用

如果你的产品不能让Agent更容易使用，那你就不会有竞争力
