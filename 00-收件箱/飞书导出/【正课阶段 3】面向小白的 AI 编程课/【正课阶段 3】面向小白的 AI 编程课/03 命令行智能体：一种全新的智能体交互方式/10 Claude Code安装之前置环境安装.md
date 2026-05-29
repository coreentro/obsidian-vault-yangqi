---
title: "Claude Code安装之前置环境安装"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/HsIDwsNftilLGQk4OLOcOOixnsP"
node_token: "HsIDwsNftilLGQk4OLOcOOixnsP"
obj_type: "docx"
document_id: "CR3TdFWznoMJr1xH7lNcjKwSnZb"
revision_id: "5"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/HsIDwsNftilLGQk4OLOcOOixnsP>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>Claude Code安装之前置环境安装</title>

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



<figure view-type="Preview"><source mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" token="CerybBIJcoINBQxsfVec6mhKnMc"/></figure>



地址：https://git-scm.com/install/windows



![](https://feishu.cn/file/HnF6bD6nPoD7jcxdGsTcEDVnn46)



使用的命令：**git --version     注意git和--version之间有空格**



**另外你安装的版本不需要和我的一样，因为它会不断更新**



![](https://feishu.cn/file/DOF4bN7OaoTwNdxXbz7cYBpGnMf)



## 2）苹果电脑



### 安装Homebrew方法1（国内网络可安装）



打开你的豆包，问如下问题：**国内网络如何安装Homebrew**



**全程跟着豆包来操作即可，他会帮你完成这件事情**



![](https://feishu.cn/file/J9k3bOTQWoJx0XxQ3XUcErsGnyh)



![](https://feishu.cn/file/UTGKbtrzaoiTTzxh42gcmHl9nyf)



首先是下载地址：https://git-scm.com/install/mac



![](https://feishu.cn/file/PDqObVsKFojMU2x646bcZoE7n0b)



### 安装Homebrew方法2（要解决网络问题）



可以在这个网站找到最新的命令：https://brew.sh/



![](https://feishu.cn/file/WAsvbO0xSoQfZOxCuYBcsVJfnAe)

 

复制上述命令，打开你的命令行Terminal



![](https://feishu.cn/file/IL1kbduO1oEIQbxw3zVclHRrnD4)



**具体的安装过程参考下述视频**



<figure view-type="Preview"><source mime="video/mp4" origin-height="1964.000000" origin-width="3024.000000" token="AF4XbLaQ3orG8pxyGf9cVBzCnOc"/></figure>



### 使用 brew 安装 git



因为你上一步已经安装了Homebrew，并且正确配置了镜像源，所以这一步你都能走通



直接在你的命令行中使用如下命令安装 git



```Bash
brew install git
```



具体实操看视频



<figure view-type="Preview"><source mime="video/mp4" origin-height="1964.000000" origin-width="3024.000000" token="EGpYb2Ej9oqbOsxb2IPcuPS0nLf"/></figure>



# 三、安装第二个前置工具：Node.js



老规矩：我们分为苹果和Windows电脑



这个工具的安装，我们采用走国内镜像的方式，不需要解决网络问题



## 1）Windows安装



**向你的豆包问一个问题：Winodows 国内网络如何安装Node.js**



![](https://feishu.cn/file/XPn2buR4LodSI4xhHJocRs9Ynrf)



我们选择这个安装包地址：https://npmmirror.com/mirrors/node/



打开选择Windows需要的安装源（**截止2026年4月2号，Node.js的稳定版本是v24**）



![](https://feishu.cn/file/YDpUb0qmXoc52HxQi5kc9Ky3neb)



点击进去latest-v24.x版本文件夹，然后往下选择Windows相关的版本



这里一定要.msi版本，因为这个版本它会自动帮你配置环境变量，对小白最友好



**而至于版本号，不用纠结，在稳定版里选最大的即可**



![](https://feishu.cn/file/HbULbeCZKoa41bxGVBYcbYgknWc)



---



当然你也可以直接选择去

![](https://feishu.cn/file/U4cgb1eOtokwzKxWOOzcqOG4nld)



---



**安装完成之后，继续跟着你的豆包操作验证**



![](https://feishu.cn/file/Ke4ybZli1oAPQkxwjD5c4NzMnoe)



## 2）Mac电脑安装



**向你的豆包问一个问题：Mac电脑国内网络如何安装Node.js**



你会发现豆包会推荐你使用brew去安装



![](https://feishu.cn/file/CMnjbBqkuouEgjx0JG9cu5vunPf)
