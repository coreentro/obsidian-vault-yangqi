---
title: "Commands 实战：把常用指令存成快捷方式"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/NRoAwDi9givCI9kUuwRckSmCnOc"
node_token: "NRoAwDi9givCI9kUuwRckSmCnOc"
obj_type: "docx"
document_id: "I7Mhd3tZ8oOYybxbgUbcUPwxnjf"
revision_id: "5"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/NRoAwDi9givCI9kUuwRckSmCnOc>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
# Commands 实战：把常用指令存成快捷方式

你好，我是大圣。



我们之前聊了一个理念：**如果一件事你做了三次以上，就该想办法把它固化下来**



这节课我们来学第一个固化工具：Commands



<callout emoji="✨">
这篇教程非常简单，大家先看文字版，视频我放最后了
</callout>



## 一、你在重复说同样的话



假设你经常让 Claude Code 帮你写朋友圈



每次你都要先说一段要求：



```Plain Text
我现在口述一段话，帮我改写成一条朋友圈。
要求：
1. 简短有力，不超过 200 字
2. 语气真实自然，像是随手写的，不要像广告
3. 适当加一点情绪感染力，但不要用力过猛
4. 不要用 emoji 轰炸，最多用 1-2 个
5. 如果合适，结尾可以留一个引发互动的钩子
我想说的是：今天去了一家特别好吃的日料店，三文鱼太新鲜了，环境也很好，下次还来
```



Claude Code 帮你写好了，效果不错



第二天你又想发朋友圈，又得把那段要求重新打一遍，只是把【最后想说的话】换了



再下次，又打一遍



**每次都打同样的要求，只有你想表达的内容在变，这太浪费时间了**



你会很自然地想：**能不能把这段话存起来，下次只输入主题就行了？**



## 二、Commands 是什么



Commands就是为了解决这个问题的



**把你常用的提示词存成一个文件，下次用** `/命令名` **一键调用**



你在项目里创建一个 Markdown 文件，写上你的提示词，保存。



之后在 Claude Code 里输入 `/文件名`，它就自动读取那个文件的内容去执行，**本质就是给提示词做了一个快捷方式**



这背后的思想叫模板化：把不变的部分固定下来，只留一个口子给变化的部分



而Commands 就是这个思想在 Claude Code 里的落地



## 三、动手：创建你的第一个命令



直接上手，你马上就能看到效果



### 第一步：创建命令目录



在你的项目文件夹里，创建这样一个目录结构：



<callout emoji="✨">
.claude 目录，我相信大家都不陌生了，这里我就不再多说了
</callout>



```Plain Text
你的项目文件夹/
└── .claude/
    └── commands/
```



你可以手动创建这两个文件夹，也可以直接在 Claude Code 里说：



```Plain Text
帮我创建 .claude/commands 目录
```



### 第二步：创建命令文件



在 `.claude/commands/` 目录下，创建一个文件叫 `pyq.md`



<callout emoji="✨">
这里的文件名称可以使用中文，比如朋友圈.md，看你的习惯
</callout>



写入以下内容：



```Markdown
我现在口述一段话，帮我改写成一条朋友圈。
要求：
1. 简短有力，不超过 200 字
2. 语气真实自然，像是随手写的，不要像广告
3. 适当加一点情绪感染力，但不要用力过猛
4. 不要用 emoji 轰炸，最多用 1-2 个
5. 如果合适，结尾可以留一个引发互动的钩子

我想说的是：$ARGUMENTS
```



保存文件



**注意里面的 `$ARGUMENTS`，**这是一个占位符，代表你在调用命令时输入的内容。后面马上就能看到它的作用



### 第三步：使用命令



启动 Claude Code，输入：



```Plain Text
/pyq 今天去了一家特别好吃的日料店，三文鱼太新鲜了，环境也很好，下次还来
```



Claude Code 会自动读取 `pyq.md` 文件的内容，把 `$ARGUMENTS` 替换成你口喷的那段话，然后按照你预设的朋友圈风格帮你润色



**你不需要再重复那一大段要求了。** 以后想发朋友圈，只需要随口说：



```Bash
/pyq 加班到十一点终于搞定了，累死但是很有成就感
/pyq 周末带娃去了动物园，小家伙看到企鹅兴奋得不行
/pyq 读完了一本特别好的书，关于AI的，刷新了我的认知
```



## 四、\$ARGUMENTS：**不变的部分和变化的部分**



刚才你已经看到了 `$ARGUMENTS` 的作用。



我再讲清楚一点，因为这是 Commands 里唯一需要理解的概念：`$ARGUMENTS` **接收你在命令后面输入的所有内容**



```Bash
/pyq 今天去了一家特别好吃的日料店
     └── 这部分就是 $ARGUMENTS
```



命令文件里写的是"不变的部分"，`$ARGUMENTS` 是你留给变化的部分的口子



这就是模板化思想的直接体现：



```Bash
不变的部分：朋友圈的风格要求、字数限制、语气规范 → 写在文件里
变化的部分：你每次想表达的内容 → 用 $ARGUMENTS 接收
```



**核心规律就是：把不变的部分写在文件里，把变化的部分用 `$ARGUMENTS` 代替。**



---



## 五、举几个小例子



我再给你举几个小例子，但是里面的提示词我就不优化了。大家注意，我核心是为了举场景：



### 文章润色命令



`.claude/commands/polish.md`：



```Markdown
请帮我润色以下文章内容。

润色要求：
1. 保持原意不变
2. 让表达更加流畅自然
3. 删除冗余的废话
4. 优化段落结构

需要润色的内容：
$ARGUMENTS
```



使用：`/polish 这里粘贴你的文章内容`



### 会议纪要命令



`.claude/commands/meeting.md`：



```Markdown
请根据以下会议记录，整理出一份结构清晰的会议纪要。

格式要求：
1. 会议主题
2. 关键讨论点（分条列出）
3. 决策事项
4. 待办事项（标注负责人和截止日期）

会议记录：
$ARGUMENTS
```



使用：`/meeting 这里粘贴你的会议记录`



### 代码解释命令



`.claude/commands/explain.md`：



```Markdown
请用通俗易懂的方式解释以下代码。

要求：
1. 假设读者是编程小白
2. 先说这段代码整体在做什么
3. 再逐行解释关键逻辑
4. 最后给一个生活中的类比

代码内容：
$ARGUMENTS
```



使用：`/explain 这里粘贴你看不懂的代码`



**你会发现，Commands 能干什么，完全取决于你的提示词写得怎么样。**



它只是一个快捷方式，真正的核心是你写在里面的提示词



## 六、两个作用域：项目级和用户级



我们刚才创建的命令放在项目文件夹下的 `.claude/commands/` 里



这意味着：**只有在这个项目里启动 Claude Code，这些命令才可用。**



这是**项目级**的命令。适合放跟特定项目相关的命令：比如你在 A 项目里写公众号文章，在 B 项目里写技术文档，两个项目的写作规范不一样，命令自然也不同



但有些命令你到处都想用：比如翻译、润色，不管在哪个项目里都一样。



这时候你可以创建**用户级**的命令，把命令文件放到这个位置：



```Plain Text
~/.claude/commands/
```



> `~` 是你的用户主目录。Windows 上是 `C:\Users\你的用户名`，Mac 上是 `/Users/你的用户名`



放在这里的命令，对你所有的项目都生效。不管你在哪个项目里启动 Claude Code，都能使用



**怎么选？**



- **项目级**（`.claude/commands/`）：命令跟特定项目相关
- **用户级**（`~/.claude/commands/`）：命令你到处都想用

建议先都放项目级。等你发现某个命令你在每个项目里都要创建一遍，再把它移到用户级



## 七、命令的组织



当你的命令越来越多，你可以用文件夹来分类。



比如：



```Plain Text
.claude/commands/
├── write.md              → /write
├── translate.md          → /translate
├── polish.md             → /polish
└── dev/
    ├── explain.md        → /dev:explain
    └── review.md         → /dev:review
```



放在子文件夹里的命令，调用时用 `文件夹名:命令名` 的格式：



```Plain Text
/dev:explain 这里粘贴代码
/dev:review 这里粘贴代码
```



这样你的命令就不会乱糟糟堆在一起了。



不过刚开始不需要想这么多，命令少的时候全放在 commands 根目录就行。等多了再整理不迟



---



视频如下：



<readonly-block href="https://axsppz4oyvj.feishu.cn/minutes/embed/obcnyxp9hvc42yn5ri196t36?from=ccm" type="iframe"></readonly-block>
