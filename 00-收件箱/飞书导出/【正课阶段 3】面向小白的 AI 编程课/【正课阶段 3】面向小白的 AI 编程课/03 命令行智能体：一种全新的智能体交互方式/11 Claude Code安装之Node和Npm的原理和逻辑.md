---
title: "Claude Code安装之Node和Npm的原理和逻辑"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/LrfvwZtAoixeGWkl1tdchnf0n7d"
node_token: "LrfvwZtAoixeGWkl1tdchnf0n7d"
obj_type: "docx"
document_id: "VUBjd9WXJooAQixOvmHcItjun3q"
revision_id: "9"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/LrfvwZtAoixeGWkl1tdchnf0n7d>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>Claude Code安装之Node和Npm的原理和逻辑</title>

# 写在前面



你好，我是大圣



这是一节理论知识课，不涉及动手实操



**你可以选择跳过，但我强烈建议你看一遍**



# 一、为什么要装Node.js



你可能会问：我又不写代码，为什么要装 Node.js？



我们自己不写代码，但我们需要AI帮我们写代码，我们还要运行代码



Node.js你可以理解为是一种环境，一种可以让你的电脑跑代码的环境



---



再详细一点，Node.js是运行一种叫做JavaScript的引擎环境



你平时打开网页，网页里面有很多动态效果，比如点个按钮弹出来一个框，这些都是用 JavaScript（简称 JS）写的



浏览器天生就能运行 JS，因为它内置了一个"引擎"



但是电脑默认不能运行JS，因为他不认识



Node.js 就是解决这个问题的：它把JS 引擎装到了你的电脑上，让 JS 代码可以直接在终端里跑，不需要打开浏览器



所以 **Node.js = 让你的电脑能跑 JS 的运行环境**



![](https://feishu.cn/file/BdHAbsbgVoT2WRxBO6kcK0ijnSb)



# 二、Npm是什么？



我们后面打交道最多的就是这个npm命令



它是 **Node Package Manager** 的缩写，翻译过来就是Node 的包管理器



**什么是包（Package）？**



你就可以理解为安装包。就像你今天安装微信，安装Claude Code都是通过安装包去安装的



这些软件安装包别人开发好之后，就会放到一个NPM的官方仓库里



当我们想要去安装某一个软件的时候，就可以使用如下命令：



```Bash
npm install 工具名
```



我拿手机应用商店给你举个例子



![](https://feishu.cn/file/VnXvbureAoKZojxUgUscnG2enIe)



---



整个的逻辑如下图



![](https://feishu.cn/file/HfSnb79FBoBLQexWQvcc0qQ1ndd)



# 三、为什么要切换国内镜像源



装好 Node.js 和 NPM 之后，你如果直接用 `npm install` 去下载工具，会发现……**慢得要命，甚至直接失败**



这是因为NPM的官方仓库服务器在国外。如果你没有办法解决网络问题，下载速度就是慢，甚至失败



于是就有了镜像源的概念



国内有一些机构，把 NPM 官方仓库的全部内容复制了一份，放到国内的服务器上。而且定期同步



内容完全一样，但你下载走的是国内网络，速度快很多。这个就叫镜像源



最常用的是阿里云提供的 **npmmirror**（原来叫淘宝源）



![](https://feishu.cn/file/T4QBbw32voNyVHxaWmkcjbswnjg)



👆上图对比了两种情况：默认走国外源，中间有一堵墙，经常卡住；



切换成国内镜像源之后，直连国内服务器，下载飞速



**切换方法只需要在终端执行这一行命令：**



```Bash
npm config set registry https://registry.npmmirror.com
```



执行一次就永久生效，以后所有 `npm install` 都会自动走国内镜像，不需要每次都设置



**我们后面安装Claude Code就是采用国内镜像源的方式**



# 四、Node和Npm的关系



这里很多人会困惑：这是两个软件吗？要分开装吗？



**它们是绑在一起的**



你只需要去官网下载安装 Node.js，NPM 会自动跟着一起装好



![](https://feishu.cn/file/QexubyIE0oanMixroakclpUnnUc)



# 写在最后



不仅会实操，而且要知道底层的逻辑，这样你才能少踩坑，遇到问题才能做到举一反三
