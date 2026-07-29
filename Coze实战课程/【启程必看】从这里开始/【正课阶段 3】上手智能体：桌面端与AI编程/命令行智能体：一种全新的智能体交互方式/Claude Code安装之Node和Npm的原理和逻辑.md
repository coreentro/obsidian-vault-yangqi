---
title: "Claude Code安装之Node和Npm的原理和逻辑"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/LrfvwZtAoixeGWkl1tdchnf0n7d
node_token: LrfvwZtAoixeGWkl1tdchnf0n7d
obj_token: VUBjd9WXJooAQixOvmHcItjun3q
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "命令行智能体：一种全新的智能体交互方式"
  - "Claude Code安装之Node和Npm的原理和逻辑"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 9
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# Claude Code安装之Node和Npm的原理和逻辑

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 命令行智能体：一种全新的智能体交互方式

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

> [!abstract]- 🖼 图片展示了安装Node.js的必要性。Node.js是运行JavaScr
> 图片展示了安装Node.js的必要性。Node.js是运行JavaScript的“引擎”，浏览器内置JS引擎，但电脑运行JS需安装Node.js。图中用箭头表明浏览器、Node.js和电脑的关系，即Node.js让JS能在电脑上运行。还列出安装Node.js后才能运行的工具，包括Claude Code（AI编程助手，也是课程目标）、各类CLI工具（如Vite、ESLint等命令行开发工具）以及前端项目（如React、Vue等框架的运行基础）。此图与上文对Node.js的介绍相呼应，进一步阐释其重要性。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BdHAbsbgVoT2WRxBO6kcK0ijnSb) · `BdHAbsbgVoT2WRxBO6kcK0ijnSb`

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

> [!abstract]- 🖼 图片以手机应用商店类比NPM，直观呈现两者安装软件包的逻辑。左侧手机世界
> 图片以手机应用商店类比NPM，直观呈现两者安装软件包的逻辑。左侧手机世界，应用商店对应NPM官方仓库，搜索并下载APP对应npm install工具名，手机里装好的APP对应电脑上装好的工具包。右侧NPM世界，Nège addCriterion图片id为<<image7>>
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VnXvbureAoKZojxUgUscnG2enIe) · `VnXvbureAoKZojxUgUscnG2enIe`

---

整个的逻辑如下图

> [!abstract]- 🖼 图片展示了NPM（Node Package Manager）的逻辑流程。
> 图片展示了NPM（Node Package Manager）的逻辑流程。上方标题说明NPM是Node的包管理器。左侧为NPM仓库，标注有“全球包注册中心”“200万+工具包”等信息。中间是你的项目，显示“node_modules/依赖包下载到本地”。右侧是工具，标注“运行起来”。下方有常用命令速览，包括“npm install”安装项目所有依赖，“npm install xxx”安装指定工具包，“npm -v”查看 addCriterion图片展示了NPM（Node Package Manager）的逻辑流程。上方标题说明NPM是Node的包管理器。左侧为NPM仓库，标注有“全球包注册中心”“200万+工具包”等信息。中间是你的项目，显示“node_modules/依赖包下载到本地”。右侧是工具，标注“运行起来”。下方有常用命令速览，包括“npm install”安装项目所有依赖，“npm install xxx”安装指定工具包，“npm -v”查看NPM版本验证是否安装成功。该图与文档中介绍NPM概念及使用命令的上下文相关，直观呈现了NPM的逻辑流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HfSnb79FBoBLQexWQvcc0qQ1ndd) · `HfSnb79FBoBLQexWQvcc0qQ1ndd`

# 三、为什么要切换国内镜像源

装好 Node.js 和 NPM 之后，你如果直接用 `npm install` 去下载工具，会发现……**慢得要命，甚至直接失败**

这是因为NPM的官方仓库服务器在国外。如果你没有办法解决网络问题，下载速度就是慢，甚至失败

于是就有了镜像源的概念

国内有一些机构，把 NPM 官方仓库的全部内容复制了一份，放到国内的服务器上。而且定期同步

内容完全一样，但你下载走的是国内网络，速度快很多。这个就叫镜像源

最常用的是阿里云提供的 **npmmirror**（原来叫淘宝源）

> [!abstract]- 🖼 图片对比了默认走国外源和切换国内镜像源两种情况。默认情况下，国外源因GF
> 图片对比了默认走国外源和切换国内镜像源两种情况。默认情况下，国外源因GFW（防火墙）限制导致超慢或失败；切换后，直连国内服务器，下载飞速。国内镜像源是把国外NPM仓库内容“搬”到国内服务器，内容完全一样但速度更快。执行“npm config set registry https://registry.npmmirror.com”命令可永久切换为国内镜像源，之后所有npm install命令都走国内网络，无需每次设置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/T4QBbw32voNyVHxaWmkcjbswnjg) · `T4QBbw32voNyVHxaWmkcjbswnjg`

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

> [!abstract]- 🖼 图片展示了Node.js与NPM的关系。安装Node.js时，会同时得到
> 图片展示了Node.js与NPM的关系。安装Node.js时，会同时得到Node运行时和NPM包管理器。Node运行时执行JavaScript代码，让终端能跑.js文件，类似Python解释器；NPM是包管理器，下载和管理工具包，类似应用商店。两者结合，Claude Code等工具可正常运行。该图与上下文紧密相关，直观呈现了Node.js和NPM的捆绑安装及各自功能，帮助理解它们在安装Claude Code等工具中的作用。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QexubyIE0oanMixroakclpUnnUc) · `QexubyIE0oanMixroakclpUnnUc`

# 写在最后

不仅会实操，而且要知道底层的逻辑，这样你才能少踩坑，遇到问题才能做到举一反三
