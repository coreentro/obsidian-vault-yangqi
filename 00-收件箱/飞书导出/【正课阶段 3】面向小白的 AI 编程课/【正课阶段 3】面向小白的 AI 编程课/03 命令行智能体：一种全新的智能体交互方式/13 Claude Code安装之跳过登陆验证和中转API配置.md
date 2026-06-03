---
title: "Claude Code安装之跳过登陆验证和中转API配置"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/Gr7bw5h0xiDYpJkd0wFca6eZnVb"
node_token: "Gr7bw5h0xiDYpJkd0wFca6eZnVb"
obj_type: "docx"
document_id: "JeLJdE47MoGlkox5rufclhO8npg"
revision_id: "6"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/Gr7bw5h0xiDYpJkd0wFca6eZnVb>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>Claude Code安装之跳过登陆验证和中转API配置</title>

# 写在前面



你好，我是大圣



安装完Claude Code之后，并不能立马去打开使用，还要做一些配置



# 一、为什么要做配置



![](https://feishu.cn/file/WseTbV2BkoeAVHxqEwPcKw0SnSb)



前面跟大家讲过，Claude Code它是一个执行架构，它要想干活，你必须给它配置大脑



所以这节课核心就是要给你的Claude Code去配置上AI模型



而这里面还有一个卡点，跟当初的Kimi Code一样，Kimi Code是Kimi Code的工具。



所以他当然希望你用它自家的模型  
  
于是我们在使用Kimi Code的时候，我们会登录Kimi的账号，然后就可以自动使用Kimi的官方订阅了



Claude Code也有这样的逻辑，但它最大的问题就是它的官方订阅太难了，需要解决各种问题，所以95%的人搞不定



但是它在启动的时候又有一个登录校验，所以我们要做的是两件事儿：



1. 跳过这个登录校验
2. 配置一个第三方的API



# 二、下载安装CC-Switch



我们上面要做的两件事儿，有一个工具专门帮我们做了



这个工具叫做CCswitch，从它的名字你也应该能够看出来，CC就是Claude Code，switch就是切换



这是一个开源项目，官方地址：https://github.com/farion1231/cc-switch/blob/main/README_ZH.md



下载地址：https://github.com/farion1231/cc-switch/releases





**上面的地址是github，国内网络是可以访问的，但可能会比较慢，偶尔也会抽风**



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="La1YbGRigoo6aIxZ7IOcttrSnld"/></figure>



# 三、配置中转API



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="IpAnbDRa5oM775xcWAvc1LZfn0g"/></figure>





后面你会不断地接各种模型的 API，**这个在前面的课程里，我已经给大家详细地讲解过了**



接下来这个图你一定要理解，不管你接什么 API，你一般都需要三个要素：



1. API 地址



这个地址就是一个网址，它决定了你付费、要访问的模型是谁家的



1. 密钥



密钥就是你要带着的一把钥匙，通过它去访问，方便人家识别你的身份，给你计费



1. 模型 ID



你要告诉它你访问的是哪个模型



这里我一定要强调，大家一定要在这个教程里面去理解它本质的逻辑



因为没有任何一个教程可以告诉你全部的接入 API 的方式，但只要你理解了它的逻辑，未来不管你是接入 Kimi、OpenAI 还是 Gemini，只要去找这三个点就好了。找到了，你就能配置成功



![](https://feishu.cn/file/LhdqbuZ75oUtAwxSTxbcGgvOniY)



我们接下来配置3个中转API



1. Kimi Code Plan：https://www.kimi.com/code/console



1. AIGOCode：https://aigocode.com/invite/WB3DJX6W



1. ClaudeCN：https://claudecn.top/register?aff=UyTK





# 写在最后



CC-Switch官方文档：https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/zh/1-getting-started/1.1-introduction.md
