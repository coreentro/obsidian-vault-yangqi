---
title: "OpenClaw的命令和插件配置"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/A654wmnTgi8kjfkooAvc63Z7ntc"
node_token: "A654wmnTgi8kjfkooAvc63Z7ntc"
obj_type: "docx"
document_id: "AjzkdnsJvoL8NTxbcakciMEknGd"
revision_id: "210"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/A654wmnTgi8kjfkooAvc63Z7ntc>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>OpenClaw的命令和插件配置</title>

<callout emoji="✨">
当我们部署完龙虾之后，有一些最初始的命令和插件需要大家了解一下。这涉及到一些最佳实践
</callout>



# 一、OpenClaw的版本



OpenClaw 的版本更新非常快，所以我们要学会查看它的版本，并且做出更新



```Bash
openclaw -v
```



![](https://feishu.cn/file/OLGLbw0Fwodcjsx3yKtc2pMHnOh)



<callout emoji="✨">
像扣子上购买的，这个 OpenClaw 还会提醒你需要升级版本
</callout>



![](https://feishu.cn/file/T41Sbikomop79vxsqgJcbhxtnFd)



---



现在OpenClaw的版本升级非常快，有时候一天一个版本。我们可以自行选择是否更新



<callout emoji="✨">
这里最重要的是大家要注意，版本更新可能会导致bug，大家要有这个预期
我讲这个并不是不让大家去更新，一个新生软件，它的每一次更新可能都会带来非常好用的能力
</callout>

```Bash
openclaw update
```



我们可以直接使用龙虾的管理助手帮我们去更新



![](https://feishu.cn/file/ZGCtbJPlToQ0wPxLj0HcCE2En9c)



但是你会发现飞书妙搭不让你更新，这个也非常容易理解。

云端必须统一管理，用户如果可以随意更新的话，那很可能就会把系统更新崩



![](https://feishu.cn/file/IOwWbxWekoxJ7ZxLwe5ccLUnnQe)



---



<callout emoji="✨">
扣子是可以做OpenClaw更新的，但更新之后有一个小插曲，飞书用不了了
所以我让龙虾管理助手帮我修复了飞书的问题，它也成功修复了
这个案例是想告诉伙伴们，龙虾就是这么的不稳定
</callout>

![](https://feishu.cn/file/RLYubBsnToSXzvxzJXIcCVxxnVg)



![](https://feishu.cn/file/C0k3bOPa0osAx2xZnhOc34Z7nWb)



![](https://feishu.cn/file/EOG4b3XtXoLQj0xzka0ctlGlngT)



# 二、飞书官方插件



插件你可以认为是对于 OpenClaw 能力的一个扩展



比方说，我想要 OpenClaw 和飞书深度集成。如果单单 OpenClaw 去开发这个功能的话，会非常麻烦。但如果飞书官方下场，他们可以开发一个叫插件的功能，就可以方便地把 OpenClaw 和飞书集成起来



下方两个文档就是飞书官方插件的说明和使用教程



[OpenClaw飞书官方插件上线｜一文讲清功能、安装更新教程与常见问题！ - 飞书官网](https://www.feishu.cn/content/article/7613711414611463386)



<cite doc-id="MFK7dDFLFoVlOGxWCv5cTXKmnMh" file-type="docx" title="OpenClaw飞书官方插件使用指南（公开版）" type="doc"></cite>



## 1）安装并开启飞书官方插件



在我做教程的当下，飞书妙搭天然支持飞书插件，用如下方式测试即可



![](https://feishu.cn/file/Ce9EbLoCZoUrgdxzdpFci5LTnlc)



![](https://feishu.cn/file/SH96bi1yEoPMUpxFQqzczvlRnHe)



---



但是扣子，它默认使用的是 OpenClaw 内置的飞书插件



![](https://feishu.cn/file/OCYgbhOcJog68rx2nrBcVKwfnbd)
