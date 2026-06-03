---
title: "智能体跟外部打交道的第三种方式-CLI"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/FM1PwvWRpi4xYCk4hW4cjmUvnbg"
node_token: "FM1PwvWRpi4xYCk4hW4cjmUvnbg"
obj_type: "docx"
document_id: "StEBd3QiBo4qeExbeb3cieHOn4d"
revision_id: "890"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/FM1PwvWRpi4xYCk4hW4cjmUvnbg>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>智能体跟外部打交道的第三种方式-CLI</title>

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



![](https://feishu.cn/file/R8VRbe2tmoZ1IBxviQJcZF0Znof)



---



Claude Code这个例子还有更妙的地方



启动之后，你跟它说："帮我看看当前文件夹里都有啥？"，它怎么做的?



它在背后帮你执行了 `ls` 这个命令



![](https://feishu.cn/file/SUGkbLaUroMZYPxGvGXcWrjXn0f)



而且Claude Code本身也可以通过命令的方式来控制，比如你要退出，你输入exit



![](https://feishu.cn/file/LoZhbEF7wot8a7xy60PcpSSZnGM)



这里有两层 CLI 在发生:



- 第一层：你用 CLI 启动了 Claude Code(敲 `claude`)
- 第二层：Claude Code 用 CLI 帮你操作电脑(敲 `ls`、`cd` 这些)



你天天用 Claude Code，其实你不只在用 CLI，你还在看着 AI 用其他的 CLI 帮你干活



# 三、终端是CLI么？



这是一个很容易让大家困惑的地方



终端不是CLI，它是一个窗口，它负责承载输入和输出



CLI是你在窗口里跟程序对话的方式



而那些被设计成通过命令调用的程序，比如Claude Code，比如Git，我们叫它CLI工具



![](https://feishu.cn/file/A61ybzA6Do6ta7xxAyRcVDjrn3D)



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



![](https://feishu.cn/file/VIATbBKmRoylySxHywbcEr4YnWg)



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



![](https://feishu.cn/file/Zh1AbtqgpojrR7xxwBscPs9gned)



---



如果你想通过官网来装，使用如下的途径，但它可能不会装skill



地址：https://www.feishu.cn/feishu-cli



<grid>
<column width-ratio="0.547715">
![](https://feishu.cn/file/KUu4b12L9og1FDxoo7zc1Hidnmh)
</column>
<column width-ratio="0.452285">
![](https://feishu.cn/file/BbmYb6plZoqMWxxnwUTcahz0nDg)
</column>
</grid>





官网使用指南：<cite doc-id="ILuTww7Xcimb6GkhH0mcK2f4nS7" file-type="wiki" title="飞书 CLI 能力介绍与最佳实践" type="doc"></cite>



## 6.2 授权与配置



这一步也非常好理解：我们到底要跟哪个飞书账号去通信？



那我们得把这个飞书账号授权给你的CLI



这里最大的误区就是，不是你有了CLI工具，你就可以访问所有的飞书文档了。



它是首先要完成授权，**而它能访问的权限和你的飞书账号所能访问的权限是一样的**



---



第二步：配置应用凭证



![](https://feishu.cn/file/FvARbuTntoyPROxrBPWcRqbLnId)



复制上述链接，在浏览器中打开，会让你创建一个飞书CLI应用



然后你点击创建，这个应用就创建完了



**PS：如果你以前创建过，可以选择已有的应用**



<grid>
<column width-ratio="0.501855">
![](https://feishu.cn/file/XW1lb8hBPoWGsLx7r1EcmOoWnBG)
</column>
<column width-ratio="0.498145">
![](https://feishu.cn/file/Gc2ZbwFqlo23DrxhCBacY4oHnJf)
</column>
</grid>





---



第三步：登录授权



复制Claude Code给你的链接，在浏览器中打开



![](https://feishu.cn/file/CZr0bklPzocegVx0uiEcl4u1nid)



![](https://feishu.cn/file/TryqbIBieohNUZx8uG1co7GJnZc)





第四步：告诉Claude Code授权完成，验证登录状态



![](https://feishu.cn/file/Thr8bTXjioeVMnxlHCMcdYSwnid)



到现在为止，你已经把飞书CLI安装完成，并且拥有如下的Skill



![](https://feishu.cn/file/HtMhbut47o0yMExtv3XcRennnWd)



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



<figure view-type="Preview"><source mime="video/mp4" token="Vt4PbZ06sobsKOxlmHqcEOC0n8b"/></figure>



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
