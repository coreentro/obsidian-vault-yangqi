---
title: "Claude Code安装之正式安装"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/XaDPwtAi4iw3ShkR7smcO4Oenfg"
node_token: "XaDPwtAi4iw3ShkR7smcO4Oenfg"
obj_type: "docx"
document_id: "CvcFdggTqoueWhxYhnEcrEXinhe"
revision_id: "1"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/XaDPwtAi4iw3ShkR7smcO4Oenfg>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>Claude Code安装之正式安装</title>

# 写在前面



你好，我是大圣



这节课我们终于可以正式安装Claude Code了



我会给大家介绍两种方式，一种是国内安装，一种是官方脚本安装



能解决网络问题的，可以用官方脚本安装，不能解决的就使用国内安装



两者没有什么大的区别，不用纠结



**我这里要多说一嘴，这节教程大家只负责安装，不要打开，也不要使用，否则可能造成错误**



# 一、国内安装



国内安装的逻辑我相信大家已经非常清楚了



使用NPM的方式安装，并且采用国内的镜像源



老规矩，先问豆包，她的回答已经很完美了，把这段提示词发给你的豆包



PS：根据你的电脑系统，把下方标黄的地方改掉



```Bash
我已经安装了Node.js，并且配置了国内的镜像源

我也已经安装完了Git

我现在想要使用国内的网络安装Claude Code

我是Windows / Mac电脑，帮我给出完整的流程，只管帮我安装，不用管我中转API的配置
```



**第一步：检查环境**



![](https://feishu.cn/file/R7L3bv9buoIrT5x2BjBcL6TGnJb)



**第二步：使用npm命令进行安装**



![](https://feishu.cn/file/CwzCb6MGEop9TjxzqX8czVJonhb)



**第三步：验证安装并且解决问题**



**PS：遇到任何问题，截图给到豆包，让他帮你解决**



**验证安装只要用claude --version即可，不要用claude doctor验证**



![](https://feishu.cn/file/OLKvbuvDsoVjIKxaJEjcU1FMnPd)



# 二、官网安装



官网后面提供了一键脚本安装，不需要有node.js的环境



但他需要去访问Claude官方网站去下载安装包，这里面有几个点需要注意



1. **你的终端必须能访问外网才可以使用这种方式**
2. **就算你的终端可以访问外网，也有可能下载得非常慢。因为Claude的官方网站对你的工具要求较高**



## 1）Windows安装



老规矩，问豆包，把如下提示词发给豆包：



```Bash
我已经安装了Node.js

我也已经安装完了Git

我现在想要使用官网的方式安装Claude，我是Windows电脑，帮我给出完整的流程，只管帮我安装

并且你要考虑到PowerShell的权限拒绝问题

你要提醒用户，安装完成后环境变量的配置问题。你不用提前帮用户配置，他安装完成后，你要让他关注安装完成后有没有提醒他环境变量，然后让他把那个截图给到你

安装完成后，只用claude --version验证
```



![](https://feishu.cn/file/MyGfbc06MoSngPxm4Tfch7Hpnac)



![](https://feishu.cn/file/ShWSbmPKXou6XxxdFv6c6jbVnQb)





![](https://feishu.cn/file/QOHQbjWTUoAU9hx2Lx4cOnDrnbh)



安装完成后，**你可能会出现这样的提醒，把这张截图给到你的豆包，让他帮你加环境变量**



<callout emoji="✨">
这里的路径 C:\Users\YYang\\.local\bin
**YYang 是别人电脑的用户文件名称，每个人的不一样哈**
</callout>



![](https://feishu.cn/file/SU65bF3A8o5Rvvx6WYBcmsTjnI6)



**添加环境变量完成后最终验证：搞定；你出来的版本一定比这个高**



![](https://feishu.cn/file/PAvLb84X8oIruXxKdE6cYBbEnqg)



## 2）Mac电脑安装



**你可以直接问豆包，也可以看我下面的视频**



```Bash
我已经安装了Node.js

我也已经安装完了Git

我现在想要使用官网的方式安装Claude，我是Mac电脑，帮我给出完整的流程，只管帮我安装

安装完成后，只用claude --version验证
```



![](https://feishu.cn/file/DGVPbus3JohxcjxsK0mchYFyn1n)



<figure view-type="Preview"><source mime="video/quicktime" origin-height="2160.000000" origin-width="3326.000000" token="VyECbvJ24o0wfxxb4vOcQ7pJnBh"/></figure>



# 写在最后



到这里这一节就完成了，大家不要去打开Claude



这一节我想给大家传达的不仅仅是安装完成，而是你看到我是怎么跟豆包去协作的



这会是大家未来解决问题最常用的方式
