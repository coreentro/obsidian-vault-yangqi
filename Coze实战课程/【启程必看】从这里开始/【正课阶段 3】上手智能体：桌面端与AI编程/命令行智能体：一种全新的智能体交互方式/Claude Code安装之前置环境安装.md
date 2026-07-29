---
title: "Claude Code安装之前置环境安装"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/HsIDwsNftilLGQk4OLOcOOixnsP
node_token: HsIDwsNftilLGQk4OLOcOOixnsP
obj_token: CR3TdFWznoMJr1xH7lNcjKwSnZb
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "命令行智能体：一种全新的智能体交互方式"
  - "Claude Code安装之前置环境安装"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 5
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# Claude Code安装之前置环境安装

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 命令行智能体：一种全新的智能体交互方式

# 写在前面

你好，我是大圣

这节课我们来解决安装Claude Code之前的前置环境的安装

# 一、安装命令行工具

<callout emoji="✨">
这部分在讲解Kimi Code的时候已经完成，请自行观看
</callout>

# 二、安装第一个前置工具：Git

Git 是一个基础依赖工具，后续安装很多其他工具时都会用到它

非程序员听到这个名字可能会有点懵，但没关系：这里我们不需要深入理解它是什么，只要能把它装上就行  

**同样，我们分 Windows 和 macOS 两种情况来讲**

## 1）Windows电脑

**这一操作我在自己电脑上试过，不需要解决网络问题**

经过多次测试，我发现在 Windows 上通过命令行安装 Git 容易踩坑，所以**建议大家直接下载安装包，手动安装**

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/CerybBIJcoINBQxsfVec6mhKnMc) · `CerybBIJcoINBQxsfVec6mhKnMc`

地址：https://git-scm.com/install/windows

> [!abstract]- 🖼 图片展示的是Git for Windows的安装页面。页面上方有“Ins
> 图片展示的是Git for Windows的安装页面。页面上方有“Install”选项，下方列出不同操作系统版本的Git下载链接，其中“Git for Windows/x64 Setup.”被红色箭头指向，旁边有文字提示“点这里就可以下载最新版本”。页面还提供了其他版本的下载选项，如“Git for Windows/ARM64 Setup.”等。该图片与文档中介绍在Windows系统上安装Git的内容相关，直观呈现了下载Git安装包的步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HnF6bD6nPoD7jcxdGsTcEDVnn46) · `HnF6bD6nPoD7jcxdGsTcEDVnn46`

使用的命令：**git --version     注意git和--version之间有空格**

**另外你安装的版本不需要和我的一样，因为它会不断更新**

> [!abstract]- 🖼 图片展示了在Windows PowerShell中使用“git --ve
> 图片展示了在Windows PowerShell中使用“git --version”命令查看Git版本的操作界面。画面中，以管理员身份运行的Windows PowerShell窗口下，输入“git --version”命令后，显示出版本信息为git version 2.53.0.windows.1。红色箭头指向命令“git --version”以及显示的版本信息。该图片与上文提到的在Windows系统中使用“git --version”命令查看版本的内容相对应，直观呈现了操作后的结果。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DOF4bN7OaoTwNdxXbz7cYBpGnMf) · `DOF4bN7OaoTwNdxXbz7cYBpGnMf`

## 2）苹果电脑

### 安装Homebrew方法1（国内网络可安装）

打开你的豆包，问如下问题：**国内网络如何安装Homebrew**

**全程跟着豆包来操作即可，他会帮你完成这件事情**

> [!abstract]- 🖼 图片展示了国内网络安装Homebrew的详细步骤。首先，需先安装Xcod
> 图片展示了国内网络安装Homebrew的详细步骤。首先，需先安装Xcode命令行工具，弹出安装框后点“安装”，等待完成。接着，通过一键自动安装（推荐）方式，复制“/bin/zsh -c “$(curl - -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)””命令，打开命令行Terminal，选择镜像（1清华/2中科大/3阿里云），输入开机密码，确认覆盖旧版（Y），最后等待自动完成。此图与文档中苹果电脑安装Homebrew方法1的内容相关，为国内网络安装Homebrew提供操作指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/J9k3bOTQWoJx0XxQ3XUcErsGnyh) · `J9k3bOTQWoJx0XxQ3XUcErsGnyh`

> [!abstract]- 🖼 图片 addCriterion
> 图片 addCriterion
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UTGKbtrzaoiTTzxh42gcmHl9nyf) · `UTGKbtrzaoiTTzxh42gcmHl9nyf`

首先是下载地址：https://git-scm.com/install/mac

> [!abstract]- 🖼 图片展示的是Git官网macOS安装页面。页面上方有“
> 图片展示的是Git官网macOS安装页面。页面上方有“
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/PDqObVsKFojMU2x646bcZoE7n0b) · `PDqObVsKFojMU2x646bcZoE7n0b`

### 安装Homebrew方法2（要解决网络问题）

可以在这个网站找到最新的命令：https://brew.sh/

> [!abstract]- 🖼 图片展示的是Home addCriterion addCriterion
> 图片展示的是Home addCriterion addCriterionId
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WAsvbO0xSoQfZOxCuYBcsVJfnAe) · `WAsvbO0xSoQfZOxCuYBcsVJfnAe`

 

复制上述命令，打开你的命令行Terminal

> [!abstract]- 🖼 图片展示为苹果电脑安装Homebrew时在命令行Terminal中执行的
> 图片展示为苹果电脑安装Homebrew时在命令行Terminal中执行的安装命令界面。命令为“/bin - 自动生成
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/IL1kbduO1oEIQbxw3zVclHRrnD4) · `IL1kbduO1oEIQbxw3zVclHRrnD4`

**具体的安装过程参考下述视频**

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/AF4XbLaQ3orG8pxyGf9cVBzCnOc) · `AF4XbLaQ3orG8pxyGf9cVBzCnOc`

### 使用 brew 安装 git

因为你上一步已经安装了Homebrew，并且正确配置了镜像源，所以这一步你都能走通

直接在你的命令行中使用如下命令安装 git

```Bash
brew install git
```

具体实操看视频

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/EGpYb2Ej9oqbOsxb2IPcuPS0nLf) · `EGpYb2Ej9oqbOsxb2IPcuPS0nLf`

# 三、安装第二个前置工具：Node.js

老规矩：我们分为苹果和Windows电脑

这个工具的安装，我们采用走国内镜像的方式，不需要解决网络问题

## 1）Windows安装

**向你的豆包问一个问题：Winodows 国内网络如何安装Node.js**

> [!abstract]- 🖼 图片展示了Windows版Node.js在国内网络环境下安装的完整流程。
> 图片展示了Windows版Node.js在国内网络环境下安装的完整流程。首先，推荐使用国内镜像，速度最快，可访问阿里云/淘宝Node.js镜像。进入后选择LTS版本，找到对应版本的.msi安装程序（图形化、自动配置PATH，新手首选），或.zip绿色版（解压即用，手动配PATH）。该图与文档中Windows安装Node.js的内容相关，是对下载步骤的详细说明，帮助用户正确选择安装包并进行下载。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XPn2buR4LodSI4xhHJocRs9Ynrf) · `XPn2buR4LodSI4xhHJocRs9Ynrf`

我们选择这个安装包地址：https://npmmirror.com/mirrors/node/

打开选择Windows需要的安装源（**截止2026年4月2号，Node.js的稳定版本是v24**）

> [!abstract]- 🖼 图片展示的是Node.js国内镜像网站上Node.js稳定版本的文件夹列
> 图片展示的是Node.js国内镜像网站上Node.js稳定版本的文件夹列表。列表中包含多个以“latest -”开头的版本文件夹，如latest - arpoon/、
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YDpUb0qmXoc52HxQi5kc9Ky3neb) · `YDpUb0qmXoc52HxQi5kc9Ky3neb`

点击进去latest-v24.x版本文件夹，然后往下选择Windows相关的版本

这里一定要.msi版本，因为这个版本它会自动帮你配置环境变量，对小白最友好

**而至于版本号，不用纠结，在稳定版里选最大的即可**

> [!abstract]- 🖼 图片展示了Node.js v24.9.0版本的多个安装包文件列表，其中“
> 图片展示了Node.js v24.9.0版本的多个安装包文件列表，其中“node-v24.9.0-x64.msi”文件被红色箭头指向并突出显示，旁边有文字标注“下载.msi版本”。这与文档中Windows安装Node.js的内容相关，文档提到选择.msi版本是因为它会自动配置环境变量，对小白最友好，而版本号在稳定版里选最大的即可，此图直观呈现了.msi版本文件。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HbULbeCZKoa41bxGVBYcbYgknWc) · `HbULbeCZKoa41bxGVBYcbYgknWc`

---

当然你也可以直接选择去

> [!abstract]- 🖼 图片展示了Node.js vv24.9.0版本的多个安装包文件列表，其中
> 图片展示了Node.js vv24.9.0版本的多个安装包文件列表，其中“node-v24.9.0-x64.msi”文件被红色框和 自动生成的文本
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/U4cgb1eOtokwzKxWOOzcqOG4nld) · `U4cgb1eOtokwzKxWOOzcqOG4nld`

---

**安装完成之后，继续跟着你的豆包操作验证**

> [!abstract]- 🖼 图片展示了Node.js安装后的验证步骤及配置npm国内镜像的操作。在C
> 图片展示了Node.js安装后的验证步骤及配置npm国内镜像的操作。在CMD/PowerShell中，执行“node -v”和“npm -v”显示版本号，出现版本号即成功。配置npm国内镜像时，使用“npm config set registry https://registry.npmmirror.com”命令，验证时执行“npm config get registry”返回上述地址即成功。图片还列出常用国内源地址，如阿里云、华为云、腾讯云等。该图片与上文安装Node.js后验证安装的内容相呼应，指导用户完成相关操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Ke4ybZli1oAPQkxwjD5c4NzMnoe) · `Ke4ybZli1oAPQkxwjD5c4NzMnoe`

## 2）Mac电脑安装

**向你的豆包问一个问题：Mac电脑国内网络如何安装Node.js**

你会发现豆包会推荐你使用brew去安装

> [!abstract]- 🖼 图片展示了苹果电脑（Mac）
> 图片展示了苹果电脑（Mac）
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CMnjbBqkuouEgjx0JG9cu5vunPf) · `CMnjbBqkuouEgjx0JG9cu5vunPf`
