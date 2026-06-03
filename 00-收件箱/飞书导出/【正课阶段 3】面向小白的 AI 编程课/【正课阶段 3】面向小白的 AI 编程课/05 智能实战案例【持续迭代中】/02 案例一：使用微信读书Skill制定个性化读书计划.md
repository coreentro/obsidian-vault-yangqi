---
title: "案例一：使用微信读书Skill制定个性化读书计划"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/WV09wbGM4iFrIHkowM1cAJiZnJh"
node_token: "WV09wbGM4iFrIHkowM1cAJiZnJh"
obj_type: "docx"
document_id: "QmxedPdh8oe8v4xTCEecRzJynaf"
revision_id: "439"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/WV09wbGM4iFrIHkowM1cAJiZnJh>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>案例一：使用微信读书Skill制定个性化读书计划</title>

# 写在前面



你好，我是大圣



这个实战案例完全基于**微信读书开放的官方 Skill**



当有了这个skill，我们就可以基于自己的阅读习惯，制定个性化的读书计划



这个案例代表了一种**非常简单但是好用的案例类型**：



你不需要掌握复杂的编程知识，你也不需要自己去做一个网站



只要对方开放了自己的 Skill，你就可以依托这个 Skill 做很多有意思的事情。



# 一、微信读书Skill可以做什么



地址：https://weread.qq.com/



![](https://feishu.cn/file/IWbKbX2cloi7naxHLnMcVygCnqg)



![](https://feishu.cn/file/MgQCbNqKTotoSwxeipwcN8Hznoh)



![](https://feishu.cn/file/AEKrbf7udo7D0FxjWhicd7yKnce)





微信读书把内部能力，通过 Skill 的方式开放给你的 Agent，目前主要包括：



- **书架管理**：看你书架上有哪些书、读到第几本
- **划线笔记**：拉取你在每本书里划过的线和写过的想法
- **章节信息**：每本书的章节目录、阅读进度
- **热门划线**：其他读者在某本书或某一章高频划过的句子（很适合"精读他人精华"）
- **阅读统计**：每天/每周/每年的阅读时长、读完了几本书、偏好题材
- **搜索 & 推荐**：搜书城、看书评、获取个性化推荐书单



也就是说，**只要你日常在微信读书里产生的数据，几乎都能通过 Skill 拿到，再由 AI 帮你二次加工**



> **PS**：为了方便操作，我开了一个微信读书的包月会员，每个月 19 块，手机端开通。
> 
> 学员可以根据自己情况选择是否开通



# 二、微信读书Skill安装



我这里使用的是Claude Code，Claude Desktop的桌面端



**你可以使用WorkBuddy、Kimi Code、Claude Code CLI都可以**



**多说一嘴：Workbuddy天然就有微信读书的Skill，毕竟都是腾讯自家的产品**



![](https://feishu.cn/file/KMWjbLlRKoiCsbxvmT9cTYSwnDc)



## 第一步：建立文件夹



我建立了一个文件夹，名字叫做：**微信读书Skill**



![](https://feishu.cn/file/XwYebaE6lonHjWxaDfacMrPsnub)





## 第二步：让Claude帮你装Skill



在Claude Code中把这个文件夹打开，输入如下提示词



<callout emoji="✨">
下载 [https://cdn.weread.qq.com/skills/weread-skills.zip](https://cdn.weread.qq.com/skills/weread-skills.zip) 安装 skill
  
在这个项目下，我想做一个依托于微信读书Skill的案例，然后给我的学员去演示一个东西
所以你要先帮我安装Skill
</callout>





![](https://feishu.cn/file/WwLhbxGwVoUt4GxBpolcvHHTnxh)



Claude 会自动下载、解压，并把 Skill 文件放到 `~/.claude/skills/weread-skills/` 目录下



![](https://feishu.cn/file/MYjYbMPv2ofXMOx4DNScR1qonuf)



## 第三步：配置API Key



微信读书 Skill 需要一个 API Key 来识别"这是你的数据"



获取方式：在微信读书的 Skill 页面，按照页面引导生成一个属于你的 API Key

![](https://feishu.cn/file/FOrMbvp5koUEjjxGMXwc15LGnpw)





拿到 Key 之后，告诉 Claude：这是我的API Key，帮我配置



Claude 会把这个变量写进你的 shell 配置里（一般是 `~/.zshrc` 或 `~/.bashrc`）



配置完成后，重启 Claude Code（或者新开一个 Claude Desktop 窗口）让环境变量生效，就可以开始用了



![](https://feishu.cn/file/GHyRbXOZZofA4ixAehtc5Bzrn8g)



# 三、开发功能



基建装完，接下来就是开发功能



## 3.1 确定需求



我们用一个最常见的阅读场景：**读书划线 → 整理沉淀**



读微信读书的时候，我们会划线、写想法。这些划线和想法是最有价值的部分：它记录了你当时的思考和状态



但问题是，**划了就划了，很少有人会回头整理**



有了微信读书 Skill，我们可以让 AI 帮我们把这些划线用起来：



- 整理成结构化的读书笔记
- 提炼成内容创作的选题素材
- 分析阅读偏好和盲区，推荐下一步该读什么



**使用节奏很简单**：



白天通勤、间隙的时候自由读书，晚上用 Claude Code 调一个 Skill，把今天的所感所想自动整理好



这就是我们这个案例要做的事



---



讲到这里要先点破一个认知：



**Skill 给的是能力，不是产品**



微信读书把接口开放给了 Agent，但它不会主动告诉你"该怎么用"。你拿到 Skill 之后如果只问"我读了什么书"、"我有多少笔记"，问两次也就没新鲜感了



**真正的价值是你自己设计场景：**把 Skill 的零散能力，串成一个对你日常有用的工作流



这也是这节课要带你做的事



## 3.2 直接使用：用提示词驱动微信读书Skill



安装完skill之后，我们先用最简单的方式直接使用微信读书Skill 来感受下他的功能



你**不需要写任何代码**，直接用自然语言跟 Claude 对话就行



我们围绕一条用户旅程来设计场景：**导出 → 反思 → 创作**



每个阶段对应一组提示词，你可以直接复制体验



---



**第一阶段：导出 - 把今天的划线归档下来**



```Markdown
帮我看看我最近一周在微信读书里的划线和想法，按"书 → 章节 → 划线"的结构整理好，保存成一个 Markdown 文件到当前目录
```



![](https://feishu.cn/file/UB4SbegvKoc4KqxQ7iQc9DCrn2g)



下面则是Agent帮我生成的文档



这里有一个主要注意的点：**跳转到原文不可用，因为微信读书的skill截止到目前是移动端APP的协议**



**而我是在电脑上操作的，所以这些链接格式都不对，不适配网页端**



![](https://feishu.cn/file/QI2hbBG3Do7KZxx0BdMcMGLrndf)



---



**第二阶段：反思 - 让 Skill 暴露你的真实阅读状态**



仅仅归档还不够，你还可以看见自己



```Markdown
帮我分析一下我书架上的书和最近半年的阅读记录，告诉我：
我主要关注哪 3-5 个领域？
哪些书是真的"读进去了"（有划线有想法），哪些是"焦虑式收藏"（在书架但没读完）？
我可能存在哪些知识盲区？
```



Claude 会把你的书架、阅读时长、划线密度综合起来，给一份**不粉饰**的诊断



很多人第一次跑这个提示词都会被结果"扎一下"：比如发现自己半年没读完一本书，或者收藏了 10 本理财书但全是同一类



这里我们就不再演示案例了，大家根据自己的需要运行即可



---



**第三阶段：创作 - 把读过的书变成你的素材库**



读书不只是输入，还可以变成输出



```Markdown
我在写一篇关于「长期主义」的文章
从我读过的书里，找 5 条最相关的划线或想法作为引用素材
每条标注原文、书名、作者，并给我一句话的使用建议
```



这个场景特别适合做内容创作的同学



你读过的书、你划过的线，本身就是最好的素材库，只是以前没有工具帮你串起来



## 3.3 进阶：封装成你自己的Skill



3.2中，我们用简单的提示词感受了微信读书的skill



但是如果有一些是你常驻的工作流程，比如每天都要划线归档，那每次都敲一遍提示词是有点麻烦的



这时候你就可以依托于微信读书的skill，在上层封装成你的skill



### 什么样的需求值得封装



不是所有提示词都需要做成 Skill。判断标准很简单，符合下面任意两条就值得封装：



- ✅ 你已经手动跑过 **3 次以上**，每次效果都满意
- ✅ 流程比较稳定，每次步骤几乎一样
- ✅ 输出格式固定（比如总要存成 Markdown 到某个目录）
- ✅ 你希望以后用**一句话**就能触发



这个案例里面，我们直接用导出的自己的读书划线笔记来封装自己的一个Skill



### 用Skill Creator来打造自己的技能



我们直接看视频



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="K94iblU7XowdTlxC6WvcyikEn7d"/></figure>



### 参考开源技能



下面两个都是GitHub上的开源文档，可能需要解决网络问题



https://github.com/zephyrwang6/space-weread/blob/main/space-weread-export/SKILL.md



https://github.com/LearnPrompt/carl-weread



# 写在最后



这篇文章想给大家分享的是，很多情况下，我们基于开源的skill封装自己的skill，就已经满足90%的场景了



另外也想跟大家再次强调的是skill这个概念以及它的实际应用是非常重要的。



如果你对它的理解还不够深，可以回去再看我们的课程
