---
title: "Claude Code安装之解决网络问题"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/UJMOwbQm5iyjwpkbQmJciFe7nWe"
node_token: "UJMOwbQm5iyjwpkbQmJciFe7nWe"
obj_type: "docx"
document_id: "Id7vdXvEsoBQBYxRSfbcCZ8Hnfc"
revision_id: "5"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/UJMOwbQm5iyjwpkbQmJciFe7nWe>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>Claude Code安装之解决网络问题</title>

# 写在前面



你好，我是大圣



这节课告诉大家应该如何解决前置的网络问题



**⚠️：这块的内容你必须得看，但可以不去解决**



因为在本次安装Claude Code的过程中，我会尽最大努力，让国内网络也能走下来



**所以这是一节必看，但是可以选修的内容**



# 一、网络问题的逻辑



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1664.000000" token="KZvdb6Kssolo19xZaOScSbMcnEc"/></figure>



有一个问题就是有些伙伴即使有网络工具，平时也可以访问谷歌，但是在安装 Claude Code的时候还是会出现问题，这是什么原因呢？



<callout emoji="✨">
这里有个知识点：
网络工具的作用也是有范围的，最基本的作用范围就是你的浏览器网络
但是你在安装 Claude Code的时候，你使用的是终端，而魔法工具如果没有经过设置，是无法影响终端网络的
</callout>



我用一张图来表示



![](https://feishu.cn/file/J2nBbizkNoMYIqxXCs8c86a1n4e)



那怎么判断你的终端是否有被魔法工具影响到呢？



Mac电脑用这个命令



```Bash
curl https://www.ipinfo.io
```



**Windows电脑可以这样问你的豆包**



![](https://feishu.cn/file/EJ9FbWmQ3oOzpmxcjC3cLAuhnec)



# 二：让你的网络工具覆盖终端（方法一）



直接看视频：



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1662.000000" token="BQP2bHhXfoGJzkxNiW1cueE6nSQ"/></figure>



**这是使用 Panda的小伙伴的代理增强的界面（理论上每个工具都应该有才对）**



![](https://feishu.cn/file/N0kVb5vWKoAZYNxKY6bcn64Bnsf)



---



如果这个方式解决不了，你就要进入到第二种比较麻烦的方式了



如果你没有折腾精神，就不要尝试下一种方法了，直接往后看课



# 二：让你的网络工具覆盖终端（方法二）



请直接看下方视频，视频中使用的提示词如下：



<callout emoji="✨">
**由于本教程没有开复制权限，请自行截图用 AI提取文字，谢谢理解**
</callout>



```Bash
我正在写一个教程，背景是这样的：我要让学员安装软件，过程中需要用到终端。

由于魔法工具默认无法覆盖到终端，通常需要开启虚拟网卡模式（即 TUN 模式），但并非所有软件都支持 TUN 模式。因此，我们需要通过命令找到本地代理端口，然后在命令行中配置环境变量（使用 export 命令）来接入代理。

我需要一份完整的教程交给学员，详细说明配置终端代理的几种方式：

1. 基础逻辑与端口查找
   (a) 解释如何找到端口号（因为不同软件的默认端口不同）
   (b) 列出一些常用软件的默认端口号
   (c) 最好能提供一个命令，可以直接查找到用户电脑上当前代理配置的端口号

2. 终端代理配置方式
   (a) 临时方案：仅在当前窗口生效，关闭后需重新配置（需提供开启和关闭的命令）
   (b) 永久方案：配置后持续生效（需提供开启和关闭的命令）
   (c) 别名方式（Alias）：本质也是临时生效，但使用起来更方便

请根据以上逻辑，告诉我如何查找端口并教我这三种配置方式的具体命令。
```



<figure view-type="Preview"><source mime="video/mp4" token="Rm9ibTMbJolejkxHJ7ccSQ1EnrW"/></figure>
