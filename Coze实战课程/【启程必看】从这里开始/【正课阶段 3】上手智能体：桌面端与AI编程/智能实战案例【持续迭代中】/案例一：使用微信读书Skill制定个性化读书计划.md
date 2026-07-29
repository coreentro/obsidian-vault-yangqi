---
title: "案例一：使用微信读书Skill制定个性化读书计划"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/WV09wbGM4iFrIHkowM1cAJiZnJh
node_token: WV09wbGM4iFrIHkowM1cAJiZnJh
obj_token: QmxedPdh8oe8v4xTCEecRzJynaf
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "智能实战案例【持续迭代中】"
  - "案例一：使用微信读书Skill制定个性化读书计划"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 439
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 案例一：使用微信读书Skill制定个性化读书计划

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 智能实战案例【持续迭代中】

# 写在前面

你好，我是大圣

这个实战案例完全基于**微信读书开放的官方 Skill**

当有了这个skill，我们就可以基于自己的阅读习惯，制定个性化的读书计划

这个案例代表了一种**非常简单但是好用的案例类型**：

你不需要掌握复杂的编程知识，你也不需要自己去做一个网站

只要对方开放了自己的 Skill，你就可以依托这个 Skill 做很多有意思的事情。

# 一、微信读书Skill可以做什么

地址：https://weread.qq.com/

> [!abstract]- 🖼 图片展示了微信读书网页界面。界面上方有搜索栏，下方是“继续阅读”板块，显
> 图片展示了微信读书网页界面。界面上方有搜索栏，下方是“继续阅读”板块，显示多本图书封面。右侧“我的书架”旁有头像标识。图中有两个红色箭头分别指向头像及头像下方的“微信读书 Skill”选项，并标注“点击头像”“点击”。该图片与上下文的关系是，在介绍微信读书Skill可实现的功能（如书架管理等）时，通过图示直观展示在微信读书网页中找到“微信读书 Skill”的操作步骤，即点击头像查看相关选项。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/IWbKbX2cloi7naxHLnMcVygCnqg) · `IWbKbX2cloi7naxHLnMcVygCnqg`

> [!abstract]- 🖼 图片展示了微信读书Skill的介绍页面。上方标题为“让AI成为你的阅读搭
> 图片展示了微信读书Skill的介绍页面。上方标题为“让AI成为你的阅读搭档”，并有“连接微信读书账号，让AI助手随时查阅你的阅读记录”的说明，下方有“快速配置”蓝色按钮。下方分为六个功能板块，分别是查阅书架、书籍搜索、阅读统计、书籍详情、笔记和划线、推荐好书，每个板块配有图标和简要说明，如查阅书架可浏览书架全貌，书籍搜索可搜索书籍获取信息等。该图片与上下文介绍的微信读书Skill功能相呼应，直观呈现其功能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MgQCbNqKTotoSwxeipwcN8Hznoh) · `MgQCbNqKTotoSwxeipwcN8Hznoh`

> [!abstract]- 🖼 图片展示了微信读书Skill的快速配置界面。界面分为两部分，左侧是复制S
> 图片展示了微信读书Skill的快速配置界面。界面分为两部分，左侧是复制Skill安装指令，提示下载指定链接安装技能；右侧是获取API Key，显示已创建的API Key，下方有复制Key和重置Key按钮。该图片与上下文紧密相关，上下文介绍了微信读书Skill的功能，此图则是配置Skill获取个人阅读信息的步骤，帮助用户完成技能安装和API Key获取，以便后续通过Skill获取和分析个人阅读数据。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AEKrbf7udo7D0FxjWhicd7yKnce) · `AEKrbf7udo7D0FxjWhicd7yKnce`

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

> [!abstract]- 🖼 图片展示了WorkBuddy软件界面，左侧导航栏中“技能”选项被红色框线
> 图片展示了WorkBuddy软件界面，左侧导航栏中“技能”选项被红色框线突出显示。右侧是已安装技能列表，其中“微信读书助手”被红色框线重点标注，其功能为搜索微信读书书籍、管理书架、查看笔记划线、浏览书评、阅读统计与好书推荐。该图片与文档中“微信读书Skill安装”部分内容相关，直观呈现了微信读书Skill在WorkBuddy中的安装状态，与文档中介绍微信读书Skill安装步骤的上下文相呼应。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/KMWjbLlRKoiCsbxvmT9cTYSwnDc) · `KMWjbLlRKoiCsbxvmT9cTYSwnDc`

## 第一步：建立文件夹

我建立了一个文件夹，名字叫做：**微信读书Skill**

> [!abstract]- 🖼 图片展示了微信读书Skill的文件夹位置。在名为“智能体实战案例”的文件
> 图片展示了微信读书Skill的文件夹位置。在名为“智能体实战案例”的文件夹下，有一个名为“微信读书Skill”的文件夹，用红色框线突出显示。这与文档中“第一步：建立文件夹”部分内容相关，文档提到建立一个名为“微信读书Skill”的文件夹，此图直观呈现了该文件夹在文件夹结构中的位置，帮助用户确认文件夹创建情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XwYebaE6lonHjWxaDfacMrPsnub) · `XwYebaE6lonHjWxaDfacMrPsnub`

## 第二步：让Claude帮你装Skill

在Claude Code中把这个文件夹打开，输入如下提示词

<callout emoji="✨">
下载 [https://cdn.weread.qq.com/skills/weread-skills.zip](https://cdn.weread.qq.com/skills/weread-skills.zip) 安装 skill
  
在这个项目下，我想做一个依托于微信读书Skill的案例，然后给我的学员去演示一个东西
所以你要先帮我安装Skill
</callout>

> [!abstract]- 🖼 图片展示了微信读书Skill安装成功后的相关信息。安装路径为`~/.cl
> 图片展示了微信读书Skill安装成功后的相关信息。安装路径为`~/.claude/skills/weread-skills/`，版本为1.0.3，包含9个文件。支持搜索书籍、书架管理、阅读统计、笔记计划线、热门划线、书评、个性化推荐等功能。使用前需配置API Key，已将Key写入shell配置里，重启Claude Code后生效。该图片与上文安装Skill的步骤紧密相关，直观呈现了安装结果及后续操作指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WwLhbxGwVoUt4GxBpolcvHHTnxh) · `WwLhbxGwVoUt4GxBpolcvHHTnxh`

Claude 会自动下载、解压，并把 Skill 文件放到 `~/.claude/skills/weread-skills/` 目录下

> [!abstract]- 🖼 图片展示了Claude Code中文件夹的目录结构。左侧目录中，红色框突
> 图片展示了Claude Code中文件夹的目录结构。左侧目录中，红色框突出显示了“claude”和“skills”文件夹。右侧目录中，同样有红色框突出显示了“skills”文件夹，其下包含“weread-skills”文件夹。该图片与文档中“第二步：让Claude帮你装Skill”内容相关，说明在Claude Code中打开“微信读书Skill”文件夹后，Claude会自动下载、解压并把Skill文件放到`~/.claude/skills/weread-skills/`目录下，此图直观呈现了Skill文件在文件夹中的位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MYjYbMPv2ofXMOx4DNScR1qonuf) · `MYjYbMPv2ofXMOx4DNScR1qonuf`

## 第三步：配置API Key

微信读书 Skill 需要一个 API Key 来识别"这是你的数据"

获取方式：在微信读书的 Skill 页面，按照页面引导生成一个属于你的 API Key

> [!abstract]- 🖼 图片展示的是微信读书Skill的快速配置界面。左侧显示复制Skill安装
> 图片展示的是微信读书Skill的快速配置界面。左侧显示复制Skill安装指令，下方有“复制指令”按钮。右侧是获取API Key区域，上方有“复制你的Key给到Claude Code不要泄露给别人”的提示，下方有“复制Key”按钮，还显示了Key的创建和最近使用时间。该图片与文档中“配置API Key”部分内容相关，用于指导用户在微信读书Skill页面获取API Key并复制给Claude Code。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FOrMbvp5koUEjjxGMXwc15LGnpw) · `FOrMbvp5koUEjjxGMXwc15LGnpw`

拿到 Key 之后，告诉 Claude：这是我的API Key，帮我配置

Claude 会把这个变量写进你的 shell 配置里（一般是 `~/.zshrc` 或 `~/.bashrc`）

配置完成后，重启 Claude Code（或者新开一个 Claude Desktop 窗口）让环境变量生效，就可以开始用了

> [!abstract]- 🖼 图片展示了Claude Code与用户关于微信读书Skill安装及API
> 图片展示了Claude Code与用户关于微信读书Skill安装及API Key配置的对话。用户告知已获取API Key并让Claude配置，Claude回复配置成功并验证通过，列出已进入`~/.zshrc`、当前会话已加载、共3个可用接口等信息。还提示重启Claude Code让环境变量生效，可开始使用。图片与上下文紧密相关，直观呈现了API Key配置后的反馈情况，是微信读书Skill安装流程中配置API Key步骤的对话记录。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/GHyRbXOZZofA4ixAehtc5Bzrn8g) · `GHyRbXOZZofA4ixAehtc5Bzrn8g`

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

> [!abstract]- 🖼 图片展示了微信读书Skill导出功能的使用示例。用户先调用技能获取划线和
> 图片展示了微信读书Skill导出功能的使用示例。用户先调用技能获取划线和想法，再用API获取内容，最终生成Markdown文件。关键信息有：找到1本有笔记的书，有2条划线和1条想法；数据为最近一周内容，所有笔记都是2026 - 05 - 19的；生成的“weared - notes - weekly.md”文件里有书、章节、划线结构，每条划线附有跳转链接。该图片与上下文紧密相关，直观呈现了导出功能的操作结果及文件内容。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UB4SbegvKoc4KqxQ7iQc9DCrn2g) · `UB4SbegvKoc4KqxQ7iQc9DCrn2g`

下面则是Agent帮我生成的文档

这里有一个主要注意的点：**跳转到原文不可用，因为微信读书的skill截止到目前是移动端APP的协议**

**而我是在电脑上操作的，所以这些链接格式都不对，不适配网页端**

> [!abstract]- 🖼 图片展示的是微信读书笔记界面，标题为“微信读书笔记 - 最近一周”，时间
> 图片展示的是微信读书笔记界面，标题为“微信读书笔记 - 最近一周”，时间范围是2026 - 05 - 13 - 2026 - 05 - 20。笔记内容为《纳瓦尔宝典》的推荐序一，作者埃里克·乔根森，译者赵灿。笔记中记录了两条划线内容，分别是2026 - 05 - 19的“这本书很薄，因为人生中真正重要的道理也确实不需要太多话”及“凡是写书的人都怕自己的书被说成是‘成功学’，而这本书的副标题竟然就是直白的‘财富与幸福源自选择’！”，并有“我的想法”栏，记录了对书的思考。下方显示本周统计：1本书、2条划线、1条想法。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QI2hbBG3Do7KZxx0BdMcMGLrndf) · `QI2hbBG3Do7KZxx0BdMcMGLrndf`

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
