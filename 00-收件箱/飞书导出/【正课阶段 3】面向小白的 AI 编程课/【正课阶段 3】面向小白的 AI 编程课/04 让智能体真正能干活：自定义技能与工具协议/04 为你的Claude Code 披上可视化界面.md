---
title: "为你的Claude Code 披上可视化界面"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/DiRgwyalJiF9Y1ke9NacyswCnud"
node_token: "DiRgwyalJiF9Y1ke9NacyswCnud"
obj_type: "docx"
document_id: "YoptdolSZogXC5xGD2ecoq1inFd"
revision_id: "442"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/DiRgwyalJiF9Y1ke9NacyswCnud>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>为你的Claude Code 披上可视化界面</title>

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



![](https://feishu.cn/file/QbggbNq0rodFyfxH5Hacy7CSnJb)



你已经装好的 Claude Code 还是那个 Claude Code，Trae 只是给它提供了一个更友好的操作界面



# 二、Trae + Claude Code的操作全流程



## 1）下载并安装Trae



1. 打开 Trae 官网：https://www.tra e.cn/ide/download



![](https://feishu.cn/file/BuDTbzXh2of0n5x7yFnc4lnsn7g)



<callout emoji="✨">
注意，由于苹果系统和 Windows 系统没有本质的区别，所以我们这里不再区分版本写教程
本教程使用的是苹果系统
</callout>



1. 下载并且安装



<callout emoji="✨">
这里给大家说一个小插曲：
为了给大家演示从零安装的整个过程，我让 Claude Code 把我的 trae 给深度清删除
</callout>



![](https://feishu.cn/file/XoJ7bJDWroEAjUxpprPcVlbqnxv)



---



我下载了苹果版本的 Trae，然后安装成功之后点击打开



<grid>
<column width-ratio="0.464882">
![](https://feishu.cn/file/YHahbrESIodjasxYrsAciEVPnmd)
</column>
<column width-ratio="0.535118">
![](https://feishu.cn/file/ELKEbVJQoo04mCxK9wbc8iG0nCb)
</column>
</grid>



<grid>
<column width-ratio="0.468989">
![](https://feishu.cn/file/D9v8bBTq9ok4j4xCuVscl3T7nFh)
</column>
<column width-ratio="0.531011">
![](https://feishu.cn/file/J2vNbsjsEomcK3xNcIjczrqYn0b)
</column>
</grid>



![](https://feishu.cn/file/EurLbJf0TonNFwxXpsrc44E7nah)



![](https://feishu.cn/file/Hvb1bR7JVoQ89oxb2M1cotHznWh)



## 2）安装Claude Code插件



<callout emoji="✨">
请注意，我们这里不是Trae的详细教程，核心只是为了让大家能有一个 Claude Code 的套壳工具
Trae 的教程，**如果你感兴趣，自行 AI 加联网搜索**
</callout>



第一步：找到 Trae 的插件图标，打开商店，搜索 Claude Code 点击安装



![](https://feishu.cn/file/WCTKbn2ndoIS5jxUZKCcO4idn3c)



第二步：安装完成后，点击右上角的图标打开 Claude Code



<grid>
<column width-ratio="0.619540">
![](https://feishu.cn/file/PJFvbmRh5o7Tz7xhn2VcRasSnUe)
</column>
<column width-ratio="0.380460">
![](https://feishu.cn/file/JeHBbPttuo1ch2xD4tHc1myDnxf)
</column>
</grid>



当你出现上边的第二张图之后，恭喜你，已经可以在 Tree 里面使用 Claude Code 了



## 3）Trae + Claude Code的最佳实践



<callout emoji="✨">
这里我通过一个视频来给大家演示
</callout>



<figure view-type="Preview"><source mime="video/quicktime" origin-height="1080.000000" origin-width="1664.000000" token="DLTYbGcmpoixeUx8lsPcqfBingf"/></figure>



## 4）总结说明



![](https://feishu.cn/file/ZJnob0jQkocLmaxBBGlcW9YTnod)



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



<figure view-type="Preview"><source mime="video/mp4" origin-height="2148.000000" origin-width="3820.000000" token="CvnZbS2AKoTimuxkEPbcrgTcn4b"/></figure>



## 归藏的CodePilot



https://github.com/op7418/CodePilot



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1664.000000" token="LeVDbp9NCopODqxRRqxcywY4nxX"/></figure>
