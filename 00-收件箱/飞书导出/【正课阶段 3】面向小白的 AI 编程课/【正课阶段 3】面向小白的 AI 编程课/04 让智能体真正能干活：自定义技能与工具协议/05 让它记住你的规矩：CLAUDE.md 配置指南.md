---
title: "让它记住你的规矩：CLAUDE.md 配置指南"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/N4E0wpDMli6DEXktRBMczga5nLb"
node_token: "N4E0wpDMli6DEXktRBMczga5nLb"
obj_type: "docx"
document_id: "Y77UdG9ZCoFrsWxgH3JcpjlNnM3"
revision_id: "392"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/N4E0wpDMli6DEXktRBMczga5nLb>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>让它记住你的规矩：CLAUDE.md 配置指南</title>

# 写在前面



你好，我是大圣。



上一节课我们已经学会了跟 Claude Code 对话：打开终端，进入文件夹，启动 Claude Code，用中文告诉它你想做什么，它就帮你干活



如果你已经用了几次，你大概率会遇到一个很烦的问题



# 一、一个你一定会遇到的问题



假设你经常用 Claude Code 帮你写公众号文章



你打开 Claude Code，说："帮我写一篇关于 AI 编程的文章。"



Claude Code 写了，但风格特别书面化，像论文一样，还用了综上所述、不言而喻这种词。字数也不对，洋洋洒洒写了五千字



你只好补充说："风格要接地气，说人话，字数控制在 1500 字左右，不要用套话。



它重新写了，这次对了。你很满意，关掉了 Claude Code



**第二天，你又打开 Claude Code**



帮我写一篇关于提示词的文章。



它又写成了论文风格。又是五千字。又用了综上所述



你又要重新说一遍：接地气、说人话、1500 字、不要套话……



**第三天，同样的事情再来一遍。**



为什么会这样？



因为**Claude Code 每次关掉再打开，就会失忆。** 上一次对话里你告诉它的所有信息，全部清零



这就像你公司每天换一个新实习生，你每天早上都要把你的写作风格从头介绍一遍



那怎么办？你会很自然地想到一个解决方案：**写一份文档，让每个新来的实习生自己先看**



这就是 CLAUDE.md 干的事



# 二、CLAUDE.md是什么？



CLAUDE.md 是一个放在你项目里的文件。这就是一个普通的文本文件，文件名叫 CLAUDE.md。



你可以在里面写上：

1. 项目的基本信息
2. 你的偏好
3. 你希望 AI 遵守的规矩
4. 任何你希望 Claude Code 一开始就知道的东西



**关键点在于：Claude Code 每次启动时，会自动读取这个文件**



不需要你手动告诉它先去读一下 CLAUDE.md，它自己就会读。



读完之后，里面的内容就变成了这次对话最底层的上下文



如果你看过我之前写的提示词文章，你知道我的核心观点：**一个有效的提示词 = 指令 + 上下文**



你每次跟 Claude Code 说的话是指令，而 CLAUDE.md 里的内容就是预装好的上下文



有了它，你不需要每次都重复交代背景信息。Claude Code 一启动就已经知道了



**类比一下：**



你去一家新公司入职，HR 第一天会给你一个《员工手册》，里面写了公司的工作规范、协作方式和注意事项。



之后你做任何事情都默认遵守手册里的内容，不需要每天有人给你重复讲一遍



[CLAUDE.md](http://CLAUDE.md) 就是你写给 Claude Code 的项目手册



# 三、创建你的第一个 CLAUDE.md



<figure view-type="Preview"><source mime="video/quicktime" origin-height="2160.000000" origin-width="3840.000000" token="WakDb2mkwo7pIYxu5O3cQVBrn3d"/></figure>



## 1）在项目根目录中创建文件



打开你的项目文件夹，在**根目录**下创建一个文件，命名为CLAUDE.md



或者你可以使用 Claude Code本身帮你创建CLAUDE.md



打开你的 Claude Code，在命令行中输入下述命令



```Bash
## Claude Code自动帮你初始化
claude init

## 或者你直接创建文件
touch CLAUDE.md
```



## 2）在 CLAUDE.md中写入内容



这里我要说一下，CLAUDE.md 其实有很多的最佳实践



我们在这节课里面不去讲那么多的最佳实践，因为它的好多最佳实践是涉及到具体写代码的过程。



咱们先给大家一个框架性的认知，然后我会通过一个案例让你对它有所了解



在后面真正的做项目过程中，你会不断地反复去调你的 CLAUDE.md



---



打开这个文件，写入你希望 Claude Code 每次都记住的信息



**假设我们用 Claude Code 辅助公众号写作**，我们可以写一个风格化的提示词



```Markdown
# 写作规范

我是一名公众号 小绿书博主，日常使用 Claude Code 辅助写作。

## 风格要求

- 语言风格：接地气，说人话，不要用书面化的表达
- 不要使用"综上所述""首先其次最后"这类套话
- 多用类比和例子来解释抽象概念
- 段落要短，每段不超过 4 行

## 格式要求
- 第一句话必须是你好，我是大圣
- 文章字数控制在 500-1000 字
- 标题不超过 30 个字
- 文章保存为 Markdown 格式
```



如果你是使用 Claude Code 辅助编程，你可以这样写：



```Markdown
# 项目说明

这是一个 React + TypeScript 的前端项目

## 技术规范

- 使用函数式组件，不使用 class 组件
- 使用 TypeScript，不使用 JavaScript
- 样式使用 Tailwind CSS

## 代码风格
- 变量命名使用 camelCase
- 组件命名使用 PascalCase
- 每个组件一个文件

## 注意事项
- Git commit message 使用中文
- 不要使用 var，统一使用 const 和 let
```



**核心思路就是：你每次都要重复说的东西，写进 CLAUDE.md 里**



## 3）如何验证是否生效



现在进入项目文件夹，启动 Claude Code：



输入一条命令



```Bash
帮我写一篇关于 AI 时代孩子如何学习 AI 的公众号文章
```



# 四、两个作用域：项目级和用户级



到这里你已经会创建 CLAUDE.md 了。但我还想多讲一个概念：**作用域**



你会发现，有些规范是某个项目特有的。比如你有一个项目专门写 AI 类文章，另一个项目专门写职场类文章，两个项目的写作风格可能完全不一样



但有些偏好是你个人通用的，不管在哪个项目里都一样，比如"不要用套话""段落要短""用中文回复"。



所以 CLAUDE.md 有两个可以存放的位置：



## 项目级：放在项目的根目录



```Bash
你的项目文件夹/
├── CLAUDE.md          ← 在这里
├── 文章/
├── 素材/
└── ...
```



这个 CLAUDE.md 只对当前项目生效。你切换到另一个项目，它就不起作用了



**适合放什么：** 跟这个项目强相关的信息。比如这个项目的写作主题、目标读者、特定的格式要求；或者编程项目的技术栈、项目结构等。



## 用户级：放在你的个人目录



<figure view-type="Preview"><source mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" token="BJTrbrlYNoO2YdxaQp2cCEJKnVe"/></figure>



```Bash
~/.claude/
└── CLAUDE.md          ← 在这里
```



> *这里的 `~` 就是你的用户主目录。*
> 
> *Windows 上是 `C:\Users\你的用户名`，Mac 上是 `/Users/你的用户名`*
> 
> 比如说我的：/Users/lmh



这个 CLAUDE.md 对你所有的项目都生效。不管你打开哪个项目的 Claude Code，它都会先读这个文件



**适合放什么：** 你个人的通用偏好。



比如你喜欢中文回复、你的通用写作风格、你希望 Claude Code 回答时遵循的通用原则



**类比理解**



- **用户级 CLAUDE.md** = 公司的员工手册（所有部门都遵守）
- **项目级 CLAUDE.md** = 某个部门的工作规范（只在这个部门生效）



当两个级别的内容有冲突时，**项目级优先**。就像部门规范可以在公司总则的基础上做特殊调整



# 写在最后



这一节课的核心就一句话：CLAUDE.md 是你给 Claude Code 预装的上下文。



你写在里面的内容，Claude Code 每次启动都会读取，从此你不需要每次重新交代项目背景。



这里我特别想跟大家多说一点。在后面的课程里，你会接触到 Claude Code 的其他功能，你会发现其中有些功能跟 CLAUDE.md 做的事情看起来很像，都是在给 AI 提供信息，让它更好地完成任务



这时候你可能会纠结：这个内容到底该写在 CLAUDE.md 里面，还是放到其他地方？



我的建议是不要纠结边界。这些工具之间没有一个清晰的分界线，它们的能力是有重叠的



就像你自己记笔记，用备忘录、笔记本或者便利贴都可以



没有标准答案，只有最适合你当前场景的选择：



1. 当前阶段，先用 CLAUDE.md 把你最重复的话写进去就够了
2. 不要纠结 CLAUDE.md 到底要写什么，我只是给你讲这个知识点。
3. 如果你不知道写什么，就不用写，不写也能干活

所以，先用起来，慢慢优化。
