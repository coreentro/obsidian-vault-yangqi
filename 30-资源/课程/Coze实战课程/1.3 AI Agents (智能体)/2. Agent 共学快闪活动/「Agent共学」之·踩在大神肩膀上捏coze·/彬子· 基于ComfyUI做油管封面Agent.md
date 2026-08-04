---
title: "彬子: 基于ComfyUI做油管封面Agent"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/U2TQwXLVpi5e3xkjgm8c2in7nLd
node_token: U2TQwXLVpi5e3xkjgm8c2in7nLd
obj_token: WWiTdnKdeoFcKKx61EJczzpVnEh
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 3
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - "「Agent共学」之\"踩在大神肩膀上捏coze\""
  - "彬子: 基于ComfyUI做油管封面Agent"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 23
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 彬子: 基于ComfyUI做油管封面Agent

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 › 「Agent共学」之"踩在大神肩膀上捏coze"

# 彬子: 基于ComfyUI做油管封面Agent

## 说在前面

我是个ComfyUI新人。在此之前更多的是使用Coze来做Agent，涉及到绘图的功能也是调用Coze的图像流来完成。

但当时的图像流还挺弱的，我曾为了优化这个问题在Glif上做了若干个Bot，以插件调用API的方式来完成绘图功能的调用。

> [!abstract]- 🖼 图片展示了彬子基于ComfyUI做油管封面Agent时所用的资源，共7项
> 图片展示了彬子基于ComfyUI做油管封面Agent时所用的资源，共7项，均为插件类型。包括搜索小能手、识图小能手、重绘小能手、微调小能手、绘画小能手、分析小能手和LLM智力增强器。每项资源旁都有绿色对勾标识，且对应功能说明。该图片与上下文紧密相关，直观呈现了彬子在开发Agent时所依赖的资源类型及功能，是对上文提到的Coze和ComfyUI图像流等绘图功能调用方式的补充说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Zz5kbkpjho5oAtxKI40cFhYVnsg) · `Zz5kbkpjho5oAtxKI40cFhYVnsg`

Glif提供了一个有限节点集合的云端ComfyUI，带来了更多图像的玩法。这个过程让我也有些新的体会

Coze的工作流和ComfyUI的图像流代表了在Agent内部这两个子领域最领先水平。但大多数同学是专注在其中一个领域中持续的精进。好处是在扎的够深才能做出真正落地的Agent。短期的短板另一块非常依赖平台或社区来建设弥补。

举两个相对的例子：

1. 从熟悉Coze的同学视角，在Coze上有非常丰富的工作流节点和配套能力，开发助理类Bot非常便捷，但在流程中如果想出图自由度是不高的，几乎依赖平台的封装，或一些三方的插件。
2. 从熟悉ComfyUI的同学视角，ComfyUI有非常繁荣开源的节点和图像模型来完成高水平的图像，视频流。但流程本身的Agent含量不高，可能在反推图像信息会使用到Ollama等一些本地大模型。

那其实我们只要从自己擅长的阵地向另一块阵地多迈出一步，就能揉合更整体的把控住在一个Agent中如何设计和运用各种节点来实现最终想要的，多掌握一些，限制就少一些。

**题外话：**现在Coze将图像流的概念弱化拆解掉，可能也是认为优秀的Agent开发者，在一个Agent中使用工程节点和图像节点应该是灵活相通的，不需要过多设限。

后来就是Coze专业版和普通版分家，体验和效果不生反退。就短期太想用了。也感觉，绑定在一个平台上玩一方面平台的上限就可能是你能发挥的上限，更主要是现在Agent没有一个标准范式，Coze只是交了自己觉得对的答案。还是要多看看多试试。

- 国内其他Agent平台几乎还在对齐Coze，没啥好说的。
- Glif算是站在Coze的另一个极端上，专注图处理的节点和玩法。做玩图的Bot非常方便，一个流从输入走到输出，默认带用户界面，发布就能扔出去用，贼快。问题就是太单薄，存储，状态什么都不存在，就没有多轮交互的可能性。据说他们在内测加了ChatUI的版本了。

      而最近Coze新版拆出一个带用户界面的应用概念，哈哈哈，这就有点意思了。Agent 的范式是什么？

- Myshell是我最近高频在用的Agent平台。

      用的理由很简单，有一些创作者收入，Myshell给出的Agent 范式阶段性解决了上面Coze和Glif面临的问题。

      对比国内被Coze大一统的工作流模式，状态机的架构设计也给我们带来一些耳目一新的体验。

**我不是说大家一定要在MyShell上开发Agent，而是拿Myshell来举例，面向未来的Agent开发者可能面临的多样性选择。**

未来一定会涌现出较多的AI Agent平台，那具备更强综合能力的开发者可以很快的将之前平台上的作品迁移到新平台上，抢到最早期的开发红利。

## MyShell：一句话：基于Web3经济资源在埋头搞AI的Agent平台。

MyShell的官网： https://myshell.ai/

MyShell的生态图：

> [!abstract]- 🖼 图片展示了MyShell的生态图，核心为$SHELL Token。创作者
> 图片展示了MyShell的生态图，核心为$SHELL Token。创作者可构建AI应用，使用和购买数据，获得奖励；AI模型贡献者与API开发者可贡献并获奖励。Token持有者可进行投资、治理等操作。AI应用可通过API/Plugin接入MyShell AI应用商店，用户使用并订阅应用，产生的数据反馈至MyShell模型与API平台。此图与上文提到的MyShell是基于Web3经济资源搞AI的Agent平台相呼应，呈现其生态运作模式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/K3acbNBgNoVFWIx0Vt0ciuOanHb) · `K3acbNBgNoVFWIx0Vt0ciuOanHb`

### 开发者需要关注的分层结构：

<whiteboard token="HQkbw6jEYhRhFCbFfzDc3y2GnLo"></whiteboard>

## ShellAgent的安装：

下载地址：https://github.com/myshell-ai/ShellAgent/releases（Windows/Linux/Mac）

选择自己电脑对应的版本下载安装即可，我后面以本地是Mac上演示。

### 以ThumbMaker这个 Agent 来举例

ThumbMaker目前是 Myshell上工具类里流量比较大的一个：

https://app.myshell.ai/bot/u6ve63?utm_channel=referral&utm_source=share

> [!abstract]- 🖼 图片展示的是Myshell上工具类中流量较大的ThumbMaker界面。
> 图片展示的是Myshell上工具类中流量较大的ThumbMaker界面。上方文字提示用户选择最适合的模式制作完美封面，若不确定封面内容，可在按钮下方输入框聊天，还可上传喜欢的缩略图作为参考。下方有“Freestyle Mode”“Template Mode”“Upload reference image”三个功能按钮，且均标注“8 +”，表明适合8岁及以上人群使用。该图与上下文紧密相关，直观呈现了ThumbMaker的交互界面与功能入口。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Yp3SboGLCo8rl4xvnVncsvHmnud) · `Yp3SboGLCo8rl4xvnVncsvHmnud`

其实这个需求的出发点观察到 Glif上一个高频的bot：

https://glif.app/@saqib/glifs/cm0zceq2a00023f114o6hti7w

> [!abstract]- 🖼 图片展示的是Glif上一个高频的bot“YouTube Thumbnai
> 图片展示的是Glif上一个高频的bot“YouTube Thumbnail Maker (Flux Dev)”界面。左侧紫色区域为Prompt输入框，示例内容为“an android robot smiling and showing a phone screen which says 'GLIF.APP'”，下方有“Run This Glif”按钮。右侧展示了生成的三个封面图，分别是夕阳下的建筑、两个男子在发光物体前、蓝色背景的图表等。该图片与上下文关系紧密，直观呈现了目标用户可能关注的封面制作需求，为介绍ThumbMaker这个Agent平台上的工具类流量较大的需求提供参考。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HLK3bPigEoPefZx2KEDcFITUnkb) · `HLK3bPigEoPefZx2KEDcFITUnkb`

目标用户可能都是油管上希望快速做封面的达人，这类封面有个特点是需要比较精细的图文混排。可以对比看下：

Glif里的 Thumbnail Maker：只提供了通过纯文字描述的方式来绘制封面。

我做的 ThumbMaker：提供了类似Glif这种自由输入的方式，同时也提供了结构化输入的方式，同时给了参考图分析的功能，另外一点是可以跟 Agent 去 chat 方式来提修改建议，而这块的修改又比较好的融合进结构化输入里面。

那这样能更快更精细的画一个跟自己想象中或看到的封面相似的出来，提高了画一幅适合自己内容的封面的效率。

## 在ShellAgent中的演示

通过一个Demo理解Shellagent的状态机（Tips：视频最后的地方有点操作错误，正确是打开Messages中的Image来关联ComfyUI的输出图片进行展示）

大家可以在部署好环境的后跟着做一遍

> [!warning]- 🎬 视频（`video/quicktime`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/JmOvbELEXopSzrxA2yMcysM3nfe) · `JmOvbELEXopSzrxA2yMcysM3nfe`

配套的配置Prompt的 JSON文件

> [!warning]- 📎 附件（`application/json`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/Oh5FbdQmRogB61xXxi1cvLD2n2e) · `Oh5FbdQmRogB61xXxi1cvLD2n2e`

配套的Flux的模版ComfyUI流

> [!warning]- 📎 附件（`application/json`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/Re2cbk67NoxECkxc9PtczPUhnad) · `Re2cbk67NoxECkxc9PtczPUhnad`

**ThumbMaker的操作见直播里的讲解会更清楚些：👉【告别Coze限制：基于ComfyUI+MyShell的全新Agent开发思路 】 https://b23.tv/1JR5Iyc**

**直播中提到的黑神话悟空的PRG小游戏体验地址**:https://app.myshell.ai/bot/Y7FVJv?utm_channel=referral&utm_source=share，里面有上百个状态来保证游戏过程中与20多个Boss的互动是稳定独立的。这可能也反映出状态机和工作流各自优势的Agent场景。

### 说在最后，本次分享的初衷是希望我们社区的Agent开发者看到Agent平台的多样性，不给自己设限，在新老Agent平台喷涌之中，抓住早期创作红利。

我在MyShell上的HomePage，欢迎大家体验下我做的一些Bot，共同探讨学习：https://app.myshell.ai/explore/profile/Binzi?nametag=%238550&invite=02b9cc
