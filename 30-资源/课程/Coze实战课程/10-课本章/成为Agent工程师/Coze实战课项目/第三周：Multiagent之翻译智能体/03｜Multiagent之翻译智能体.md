---
title: "03｜Multiagent之翻译智能体"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/V948wbhy2iCYFwkSnzGcivgnnGc
node_token: V948wbhy2iCYFwkSnzGcivgnnGc
obj_token: XRgmdKRcjo10BNxLK67cyZNPn3x
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 3
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "第三周：Multiagent之翻译智能体"
  - "03｜Multiagent之翻译智能体"
obj_create_time: 1719818566
obj_edit_time: 1722617871
creator: ou_4f9742f370819a3c899baacbc140aed2
owner: ou_4f9742f370819a3c899baacbc140aed2
revision_id: 4586
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# 03｜Multiagent之翻译智能体

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 第三周：Multiagent之翻译智能体

<blockquote><p>课程回放</p><readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnc6hb2x475j567f2l73q8?from=ccm" type="iframe"></readonly-block><p><b>注意：</b></p><p>在课程中那个多Agent一直没有跑通，目前猜测是Coze平台的问题，我这边在调试通过后会再录制一个视频</p></blockquote>

# 写在前面

大家好，我是《成为Agent工程师之Coze实战》的分享人，大圣

这篇教程是课程第三个实战主题：基于多Agent能力的翻译智能体

如果你已经吃透了前两周的课程：

[[01｜基于RAG构建企业生产资料问答系统]]

[[02｜儿童绘本+电影海报解锁Coze的卡片玩法]]

 

那么恭喜你，在我们课程阶段，Coze你已经完全的入门了（但是对于市场上的大多数人来讲，你已经算是进阶了）

本次课程我们使用吴恩达老师开源的翻译智能体代码为思路构建一个Coze的多智能体进行教学分享

<bookmark name="translation-agent/src/translation_agent/utils.py at main · andrewyng/translation-agent" href="https://github.com/andrewyng/translation-agent/blob/main/src/translation_agent/utils.py"></bookmark>

这次分享我们主要讲解两块内容Coze中的多Agent模型到底该怎么玩

- 多Agent的设计思想
- Coze中的多Agent模式如何使用

  - Coze中的多Agent之间是如何通信的
  - Coze中多Agent和单Agent的本质区别在哪里？
  - Coze多个Agent之间应该如何稳定的跳转

由于这是一篇教学文档，在课程之前我希望管理好你的预期

1. 如果你是新手，请务必在学习本课程之前学习第一周的课程

   1. [[01｜基于RAG构建企业生产资料问答系统]]
2. 本次案例会重度使用变量，所以如果你对Coze的变量不了解，请务必阅读：

   1. [[加餐｜Coze变量]]
3. 本次案例不再涉及代码和JSON，大家可以松口气了
4. 这节课是谁是卧底的前置基础课，不会使用特别复杂的案例，主要是帮助大家建立对多Agent的认知和使用姿势
5. 为了方便大家学习，本次教程会使用国内版的Coze，但是海外版本的Coze和国内的使用姿势基本没有差别

OK，废话不多说，让我们开始！

# 一、重提AI Agent的设计原则

在我们课程的第一课中[[01｜基于RAG构建企业生产资料问答系统]]，我们给大家引出了一个AI Agent的设计公式

**AI Agent  =  LLM（大模型） + Planning（规划） + Memory（记忆） + Tools（工具）**

这个公式可以说是贯穿我们学习Coze的整个过程中。

在学习Coze的多Agent模式前，我们也需要引入一些新的理论知识，给我们实操的时候提供理论指导

这里我们引用吴恩达老师的设计AI 智能体的四个原则

- **反思（Reflection）**
- **工具使用（Tool Use）**
- **规划（Planning）**
- **多智能体协作（Multi-agent Collaboration）**

这里面的工具使用和规划我们之前已经讲过啦，这里我们来聊聊**反思**和**多智能体协作**

## 反思

我们举个例子来理解反思

想象一下，你是一位厨师，正在尝试制作一道新的菜肴。在第一次尝试时，你根据食谱进行了烹饪，但完成后，你发现菜肴的味道并不如预期。这时，你开始进行“反思”。

1. **检查工作**：你品尝菜肴，思考哪些部分做得好，哪些部分需要改进。这相当于智能体在完成任务后，检查自己的输出。
2. **提出改进方法**：你意识到可能盐放多了，或者烹饪时间不够。这就像智能体在反思过程中识别问题，并提出可能的解决方案。
3. **迭代改进**：你决定减少盐的用量，增加烹饪时间，并再次尝试制作这道菜。这相当于智能体根据反思的结果调整自己的行为或输出。
4. **持续优化**：经过几次尝试和调整，你的菜肴越来越接近理想的味道。这个过程就是通过不断的反思和改进，逐步优化结果。

## 多智能体协作

多智能体协作在实际工作中也很好理解：

在一家成熟的公司中，每个员工都是一个"智能体"，他们在自己的专业领域内发挥最大的效能。通过有效的沟通和协作，这些专才能够共同完成复杂的任务，提高整个组织的效率和创造力。

所以同样的道理：多个AI Agent协同工作，分工任务，讨论和辩论想法，能提出比单个智能体更好的解决方案

## 开源的翻译智能体项目

本文的思路参考的是吴恩达老师开源的翻译智能体

<bookmark name="translation-agent/src/translation_agent/utils.py at main · andrewyng/translation-agent" href="https://github.com/andrewyng/translation-agent/blob/main/src/translation_agent/utils.py"></bookmark>

在使用Coze构建多Agent之前，我们先来理解下这个翻译智能体的流程。

翻译智能体项目是一个**基于反思工作流程**的机器翻译系统，主要有以下几个流程：

1. **初步翻译**：大模型根据用户对用户的翻译需求进行初次的翻译
2. **反思翻译结果**：让模型反思初次翻译的结果，并提出建设性的改进建议。这个过程涉及到模型自我评估翻译的准确性、流畅性等。
3. **利用建议改进翻译**：根据模型提出的建议，对翻译结果进行调整和优化，以提高翻译质量

我们为什么会选择这个案例用来进行多Agent教学呢？因为这里面涉及到了两点

- **这个流程中充分体现了反思机制**
- **初步翻译**，**反思翻译结果**和**利用建议改建翻译，**这三个模块正好可以抽象成三个独立的AI Agent

了解了翻译智能体的逻辑，我们接下来使用Coze来零代码搭建一个智能翻译的Bot

# 二、单Agent模式实现翻译智能体

看到这里，你可能要问了，不是说翻译智能体是多Agent么？

为什么使用Coze的单Agent模式也能实现呢？

这里我想跟大家明确几个点：

<callout emoji="🍞">
- **多Agent是一种设计思想，跟是否使用Coze的多Agent模式无关**
- **理论上来说：只要你使用了2个及以上大模型来帮你完成任务，你就使用了多Agent的设计思想**
</callout>

所以这里我们完全可以使用单Agent模式 + 工作流的方式来搭建这个翻译智能体

## 需求分析

使用如下三步来搭建一个翻译智能体

1. **初步翻译**：大模型根据用户对用户的翻译需求进行初次的翻译
2. **反思翻译结果**：让模型反思初次翻译的结果，并提出建设性的改进建议。这个过程涉及到模型自我评估翻译的准确性、流畅性等。
3. **利用建议改进翻译**：根据模型提出的建议，对翻译结果进行调整和优化，以提高翻译质量

## 工作流设计

<whiteboard token="CzBywRhJTh2msCbo5sbcJfw4nQe"></whiteboard>

## 提示词编写

这个Bot的工作流是比较简单的，难点是每个模型的提示词该如何写？

这里我们直接引用开源项目中的英文提示词，中英文的提示词都在附录中

## Bot创建

在团队空间，我创建了两个Agent供大家学习使用

PS：这部分会在视频中进行讲解

> [!abstract]- 🖼 图片展示了两个智能翻译Agent，均为第五阶段单工作流版本。左侧是英文提
> 图片展示了两个智能翻译Agent，均为第五阶段单工作流版本。左侧是英文提示词版本，名称为“第五阶段 | 智能翻译（英文 - 大圣）”，创建者为大圣@lmh_2024，最近编辑时间为01:04，模型为豆包 - Function call模型。右侧是中文提示词版本，名称为“第五阶段 | 智能翻译（中文 - 大圣）”，创建者和模型与左侧相同，最近编辑时间为01:03。图片与上下文介绍的Bot创建内容相关，直观呈现了两种版本的智能翻译Agent。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Y7zsbGE0WoxGYgxOT7fcOOUensg) · `Y7zsbGE0WoxGYgxOT7fcOOUensg`

# 三、理解Coze的多Agent模式

<callout emoji="🥖">
PS：这一节不是实操，但却是本章中最核心的内容，请务必理解
</callout>

**在学习任何一个产品功能之前，我们需要了解其产品框架和思路。**

这样在学习使用的过程中可以在教程文档不完善的情况独立摸索，解决问题

Coze在构建Bot的时候有两种模式，分别是单智能体模式和多智能体模式

<grid>

> [!abstract]- 🖼 图片展示了Coze平台中选择Bot模式的界面。界面顶部显示“第六阶段 |
> 图片展示了Coze平台中选择Bot模式的界面。界面顶部显示“第六阶段 | 智能翻译多Agent”，下方有“个人空间”“草稿”“已自动保存 00:05:22”等信息。弹出的“选择模式”窗口中，有“单Agent模式”和“多Agents模式”两个选项，其中“多Agents模式”被红色框线突出显示，其描述为“在一个Bot中设置多个Agent，以处理复杂的逻辑”，并有勾选标识。该图片与上下文介绍Coze在构建Bot时的两种模式相关，直观呈现了多Agent模式的选择界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WsVtb3U0Oo3J12xPzPzc4Cncn2f) · `WsVtb3U0Oo3J12xPzPzc4Cncn2f`

> [!abstract]- 🖼 图片展示了Coze平台中Bot编辑界面，突出显示了“人设与回复逻辑”区域
> 图片展示了Coze平台中Bot编辑界面，突出显示了“人设与回复逻辑”区域，表明这是一个翻译智能体。下方有“添加节点”按钮，可添加Agent、Bot、全局转条件等节点，其中红色框和箭头重点指向“添加Agent节点”选项。该图片与上下文紧密相关，上下文提到Coze在构建Bot时有单智能体和多智能体模式，而多Agent模式也是Coze的Bot，此图直观呈现了多Agent模式下Bot编辑界面中添加Agent节点的操作位置，帮助理解多Agent模式的使用方式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RbHZbXDCNoqVDbxPYihcrQu0nJc) · `RbHZbXDCNoqVDbxPYihcrQu0nJc`

</grid>

## 多Agent也是一个Coze的Bot

既然多Agent模式也是Coze的bot，那么之前我们学到的Bot的人设，插件，变量，数据库等知识点在多Agent模式用也都会有，并且使用方式一模一样。

> [!abstract]- 🖼 图片展示了Coze平台中单个Agent的构成界面。在“编排”部分，选择“
> 图片展示了Coze平台中单个Agent的构成界面。在“编排”部分，选择“多Agents模式”。人设与回复逻辑处显示“你是一个翻译智能体”。技能部分有“触发器”选项。记忆部分有“变量”，包含source_text、source_lang等变量。数据库部分有“①”标识。对话体验部分有“开场白”和“快捷指令”选项。该图片与上下文介绍的Coze多Agent模式相关，直观呈现了单个Agent的构成情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HcvibQFCWoDxRcxDJPwcvc31nrg) · `HcvibQFCWoDxRcxDJPwcvc31nrg`

## 添加Agent

既然是多Agent模式，那么就要有多个Agent，所以就需要有添加和创建Agent的地方。

而在Coze中，你可以在多Agent模式中添加多个Agent，也可以添加多个Bot

PS：是不是有点**大肠包小肠**那个感觉了，多Agent就是一堆Agent（Bot）的嵌套

> [!abstract]- 🖼 图片展示了Coze平台中多Agent模式下Agent和Bot的添加界面。
> 图片展示了Coze平台中多Agent模式下Agent和Bot的添加界面。界面中有“Agent”和“Bot”两个选项，分别对应“创建一个新的Agent”和“选择单Agent模式的Bot”，并有红色箭头指向“Agent和Bot都是多Agent模式中的Agent”说明。下方还有“全局跳转条件”选项及“添加节点”按钮。该图片与上文提到的在Coze中多Agent模式下添加Agent和Bot的内容相呼应，直观呈现了操作界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YfBdb2JwpoRSoWxo48scAgTqnIh) · `YfBdb2JwpoRSoWxo48scAgTqnIh`

## 单个Agent的构成

制作单个Agent跟制作单个Bot没有太大区别，也是大模型+提示词+工作流+插件这三件套

<grid>

> [!abstract]- 🖼 图片展示了Coze中单个Agent的构成界面。界面中“适用场景”为对用户
> 图片展示了Coze中单个Agent的构成界面。界面中“适用场景”为对用户翻译需求的初次翻译，当翻译意图识别完成后，使用该Agent进行初次翻译，然后跳转到翻译反思与建议；“Agent提示词”始终调用first_translation进行翻译，当翻译完成后，跳转到翻译反思与建议节点进行优化；“技能”包含first_translation。该图与上下文介绍的Coze多Agent模式相呼应，直观呈现了单个Agent的构成要素。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/R0XBbYtEOonalUx5Ss3cuySYnYe) · `R0XBbYtEOonalUx5Ss3cuySYnYe`

> [!abstract]- 🖼 图片展示了Coze平台中“初次翻译”Agent的设置界面。界面中“适用场
> 图片展示了Coze平台中“初次翻译”Agent的设置界面。界面中“适用场景”选项被红色框突出显示，其内容为“对用户的翻译需求进行初次翻译，当用户的翻译意图识别完成后，使用该Agent进行初次翻译，然后跳转到翻译反思与建议”。右侧有“...”按钮，点击后弹出菜单，其中“模型设置”选项也被红色框突出显示。该图片与上下文介绍的Coze多Agent模式相关，直观呈现了单个Agent适用场景的设置情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Mh6Lb43JhoTyDNxb2ExctScBnFc) · `Mh6Lb43JhoTyDNxb2ExctScBnFc`

> [!abstract]- 🖼 图片展示了Coze中单个Agent的模型设置界面。在“模型”选项下，显示
> 图片展示了Coze中单个Agent的模型设置界面。在“模型”选项下，显示了“豆包-Function call模型 32K”，并有“i”和“v”标识。该图片与上下文紧密相关，上下文提到制作单个Agent是大模型+提示词+工作流+插件这三件套，此图直观呈现了模型设置中的模型选择部分，是单个Agent构成中模型设置的示例，帮助理解单个Agent的构成内容。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/S1YObGblToBmdexjADHc2ICrnwd) · `S1YObGblToBmdexjADHc2ICrnwd`

</grid>

这里多了一个适用场景的选项，这个是用来进行Coze之间的多Agent跳转的

## 多个Agent之间如何通信

之前我们讲过，单个Agent的单个工作流，这里就不存在通信的问题，因为数据都是在一个工作流中流转的。

那如果多个工作流该如何通信呢？这里就是我们之前讲的两个知识点

- [[加餐｜Coze变量]]（**这是最常用的**）
- [[加餐｜Coze数据库]]

变量的值在单个Bot中的多个工作流之间共享的！

同样的道理，变量的值在多个Agent之间也是共享的！

因此多Agent之间大多数都是使用变量来进行通信。举个例子：

- 初次翻译这个Agent在自己的工作流中将翻译的结果存到：first_tanslation变量中
- 翻译反思这个Agent在自己的工作流中读取first_tanslation这个变量的值拿到了初次翻译的结果

## 多个Agent之间的跳转

多Agent模式和单Agent模式对比中最大的区别就是：

**如何灵活的控制每个Agent，做到多个Agent之间灵活且稳定的跳转**

这是在Coze中使用多Agent模式的最大难点，也是Coze中一直致力优化的地方

举个工作中的例子说明：

<callout emoji="👍">
在工作中，真正的埋头做事其实是最简单最单纯的，而复杂的工作则是协同，就是你要安排好每个人应该做什么，以及每个人之间怎么沟通和协调，这些往往是最耗费心力的
这也正说明了事情的两面性：
多Agent模式虽然提供了处理复杂任务的能力，但是同时也带来了两点要求
- 加大了Coze系统的复杂度
- 对捏Bot的人提出了更高的能力要求，不仅仅是要熟练使用Coze，而且对你的抽象、协同和组织能力提出了更高的要求
</callout>

在多Agent模式中，为了做多个Agent之间灵活的跳转，Coze目前提供了两种方式

### 适用场景

<grid>

> [!abstract]- 🖼 图片展示了Coze多Agent模式中“初次翻译”Agent的适用场景。其
> 图片展示了Coze多Agent模式中“初次翻译”Agent的适用场景。其内容为：对用户的翻译需求进行初次翻译，当用户的翻译意图识别完成后，使用该Agent进行初次翻译，然后跳转到翻译反思与建议。图片位于介绍多Agent模式适用场景的上下文部分，直观呈现了该Agent在多Agent模式下的工作流程，帮助理解在什么情况下应使用此Agent，与上下文内容紧密相关。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DOZ5bjnHpoglnfxKKGEcEw2InRc) · `DOZ5bjnHpoglnfxKKGEcEw2InRc`

> [!abstract]- 🖼 图片展示了Coze多Agent模式中节点的适用场景说明界面。上方红框内提
> 图片展示了Coze多Agent模式中节点的适用场景说明界面。上方红框内提示概述此节点功能和适用场景，用于前序节点理解什么情况下应切换到此节点。下方举例说明，如帮助用户解决健身问题、搜索景点制定旅行规划、根据用户要求生成图片等。最下方“适用场景”区域，说明该节点用于理解用户翻译意图，当识别完成用户翻译意图后，跳转到初次翻译节点。此图与上下文紧密相关，直观呈现了节点适用场景的描述方式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/P8apbDY4Zo67ksxx5HLcmW0UnGe) · `P8apbDY4Zo67ksxx5HLcmW0UnGe`

</grid>

你需要在适用场景中描述该Agent的能力，然后用于前序的节点理解在什么情况下应该跳转到你这个Agent。

就好比一个医生，他只需要说明自己可以治疗哪些疾病，然后当人们患病时自然会上门去找他治疗。

### 切换节点设置

> [!abstract]- 🖼 图片展示了Coze平台中“初次翻译”智能体的设置界面。画面右上角有三个点
> 图片展示了Coze平台中“初次翻译”智能体的设置界面。画面右上角有三个点组成的图标，点击后弹出下拉菜单，其中“切换节点设置”选项被红色框突出显示。该图片与上下文紧密相关，上下文在介绍打开切换节点设置后能看到的三个区块，即选择切换节点的识别模式、判断时机等，此图直观呈现了“切换节点设置”这一操作位置，帮助理解上下文提到的切换节点设置功能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DQU2b8JPzoaRblxou2Jc26XSnId) · `DQU2b8JPzoaRblxou2Jc26XSnId`

<grid>

> [!abstract]- 🖼 图片展示了Coze平台中切换节点设置的界面。当此节点不能解决用户问题时，
> 图片展示了Coze平台中切换节点设置的界面。当此节点不能解决用户问题时，有三种选择：返回开始节点尝试解决用户问题、返回上一个对话的节点尝试解决用户问题、停留在当前节点。重点突出“选择切换节点的识别模式”，有“由独立于当前节点的模型识别”和“在当前节点的运行过程中识别”两种模式，前者独立模型在指定时机判断是否切换节点，后者允许当前节点思考或调用工具后决定是否切换节点。该图片与上下文介绍的切换节点设置内容相关，直观呈现了切换节点的识别模式选项。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HjswbU6RBoAZ37xsVhucqmlMnXH) · `HjswbU6RBoAZ37xsVhucqmlMnXH`

> [!abstract]- 🖼 图片展示了Coze平台中切换节点设置的“判断时机”选项。当前选中“模型回
> 图片展示了Coze平台中切换节点设置的“判断时机”选项。当前选中“模型回复后”选项，下方有三个选项：用户输入后、模型回复后、用户输入后 & 模型回复后。该图片与上文提到的“判断时机”内容相关，直观呈现了用户在切换节点设置时可选择的时机类型，帮助用户根据Bot特性选择合适的时机来切换节点，以实现多Agent模式下的智能交互。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BN1fbZszfo5m6dxH1NkcGLncnmh) · `BN1fbZszfo5m6dxH1NkcGLncnmh`

> [!abstract]- 🖼 图片展示了Coze平台中切换节点设置的界面。在“选择独立模型”部分，有“
> 图片展示了Coze平台中切换节点设置的界面。在“选择独立模型”部分，有“专为切换节点训练的模型”和“大语言模型”两个选项，后者被红色框突出显示。下方“模型”处显示“豆包-Function call模型”，并有提示可在Prompt中引用此节点能跳转到的节点名称。该图片与上下文紧密相关，直观呈现了切换节点设置中选择独立模型及模型相关内容，帮助用户了解如何在Coze平台中进行切换节点设置操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Hfa4b4EEyowylAx29SDcUchUnSf) · `Hfa4b4EEyowylAx29SDcUchUnSf`

</grid>

打开切换节点设置之后，你会看到三个区块

- **选择切换节点的识别模式**

  - 这里选择独立于当前节点的模型识别

  > [!abstract]- 🖼 图片展示了Coze平台中切换节点设置的界面。在“选择切换节点的识别模式”
> 图片展示了Coze平台中切换节点设置的界面。在“选择切换节点的识别模式”部分，有“由独立于当前节点的模型识别”和“在当前节点的运行过程中识别”两个选项。前者被选中，其说明独立模型会在指定时机判断是否切换节点，切换节点逻辑不耦合节点功能，灵活性更高。后者说明允许当前节点思考或调用工具后决定是否切换，切换逻辑可能影响节点功能。该图片与上下文介绍的切换节点设置相关，是设置切换节点识别模式的界面展示。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AcucbrdpFoI6hdxMZAXcwjRAnPf) · `AcucbrdpFoI6hdxMZAXcwjRAnPf`

- **判断时机**

  > [!abstract]- 🖼 图片展示了Coze多Agent模式中“判断时机”设置的界面。界面中有一个
> 图片展示了Coze多Agent模式中“判断时机”设置的界面。界面中有一个下拉框，当前选中“模型回复后”选项，下方还有“用户输入后”和“用户输入后 & 模型回复后”两个选项。该图片与上下文紧密相关，上下文提到“判断时机”这一块跟制作的Bot特性有关，不是固定不变的，图片直观呈现了该设置的三种可选模式，帮助用户理解如何根据Bot特性选择合适的判断时机。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BEC6bBBiIoHVRhxOcvwcF7mAnle) · `BEC6bBBiIoHVRhxOcvwcF7mAnle`

  - 用户输入后
  - 模型回复后
  - 用户输入后 & 模型回复后

<callout emoji="🎨">
这一块跟你的制作的Bot的特性有关，不是固定不变的。
这里我跟大家讲明白他的用途，大家可以灵活使用
首先需要说明的是在制作单个Agent的时候，我们需要关注三点
- 当前Agent的功能
- 当前Agent处理完成后需要跳转到哪里？
- 当前Agent在什么时机下进行跳转？
1. 其中当前Agent的功能是由提示词+工作流+插件决定的
2. 当前Agent需要跳转到哪里是由切换节点设置中最后一个区块决定的（下面讲）
3. 当前Agent在什么时机下跳转则是由**判断时机决定的**
为什么判断时机会有用户输入后和模型回复后两个选项呢？
这里我们要思考下使用Bot的场景，其中就两个：
- 我们的对话内容来引导Bot的走向
- Bot自己决定如何运行，无需人外部干预
所以一个Agent的跳转时机也就有了两种场景
- 用户输入后：

  - 例如初次翻译的Agent翻译完后，需要等待用户输入“继续”，才会继续往下走
- 模型回复后

  - 例如初次翻译的Agent翻译完成后，则直接按照跳转的规则跳转到下一个Agent执行
</callout>

- 判断跳转到哪个模型

  - 这里就是Agent之间可以灵活稳定跳转的关键！
  
    > [!abstract]- 🖼 图片展示了Coze平台中设置独立模型的界面。上方有“选择独立模型”选项，
> 图片展示了Coze平台中设置独立模型的界面。上方有“选择独立模型”选项，可选“专为切换节点训练的模型”和“大语言模型”，后者被红框突出显示。下方“模型”处显示“豆包-Function call模型”，并有提示可在Prompt中引用此节点能跳转到的节点名称。该图片与上下文紧密相关，上下文在介绍Coze的多Agent模式中，提到模型选择大语言模型，且在Prompt中可说明跳转节点，此图直观呈现了相关设置界面，辅助理解上下文内容。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/PiwHbGj77obJMHxmnMccKoPMn8A) · `PiwHbGj77obJMHxmnMccKoPMn8A`

- 模型选择大语言模型，不要选择专为切换节点训练的模型（实测效果不好）
- 具体的模型选择豆包的Function call模型（实测豆包的Function call效果不错）
- 在prompt中可以直接说明该节点应该跳转到哪个节点

  - 比如：**当初次翻译节点翻译完成后，跳转到{翻译反思与建议}节点**

### 两种方式对比

这里要说明下，Coze也在不断的完善

最开始的时候使用Coze采用**适用场景**这个能力来进行多Agent之间的跳转，但是效果非常差

后来Coze上线了**切换节点设置**的能力，经过测试之后，跳转的稳定性大幅度提升。

两种方式我都会用，但是真正起决定性作用的是**切换节点设置**

## 总结

多Agent模式很强大，但是同时也对你的能力提出了更高的要求。

大家一定要充分理解多Agent模式，才能更好的利用它进行创作

同时还要注意：Agent的跳转还会存在一些不稳定性，如果你使用了两种方式都无法完成你想要的跳转，那么可能只能等待Coze的更新了

到了这一个阶段：是否能够创作出优秀的Bot可能跟你的Coze使用水平没有太大关系了，这时候你其他方面的能力越来越起决定性的作用啦！

这里我建议大家多去Bot商店[扣子-AI 智能体开发平台](https://www.coze.cn/store/bot)找找灵感，去学习下别人的创意。

结合自己的技术，这可能是制作一个优秀Bot的最佳路径

最后：**这一章很重要，比实操更重要！**

# 四、实操：利用多Agent模式创建翻译智能体

## 构建多Agent Bot的流程

在创建单Agent模式的Bot中，我们提到了几个流程

- 业务背景
- 需求分析
- 工作流拆解
- 提示词创作
- 用Coze捏Bot

创建多Agent模式的bot中，我们多了一环：**确定每个Agent的工作边界以及跳转逻辑**

- 业务背景
- 需求分析
- **确定每个Agent的工作边界以及跳转逻辑**
- 单独设计每个Agent

  - 工作流拆解
  - 提示词创作
  - **跳转逻辑设置**
- 用Coze捏Bot

## 翻译智能体多Agent拆解

本次的翻译智能体，我们这里规划了4个Agent

- 识别用户翻译意图的Agent
- 进行初次翻译的Agent
- 进行翻译反思的Agent
- 进行翻译优化的Agent

下面我们分别规划每个Agent的功能以及输入和输出

### 识别用户翻译意图的Agent

1. Agent作用

识别用户的翻译意图，从用户的翻译需求中提取出以下几个字段

- 翻译原文
- 原文语言
- 目标语言

1. 输入输出示例

用户输入：请帮我将"你好呀"翻译成英文

大模型的输出：

- 翻译原文：你好呀
- 原文语言：中文
- 目标语言：英文

### 进行初次翻译的Agent

1. 作用

这个Agent的作用是对翻译原文进行初次翻译

1. 输入输出示例

- 输入

  - 翻译原文：你好呀
  - 原文语言：中文
  - 目标语言：英文
- 输出

  - 初次翻译的文字：Hello

### 进行翻译反思的Agent

1. 作用

结合用户的翻译需求以及初次翻译的结果进行反思，给出优化建议

1. 输入输出示例

- 输入

  - 翻译原文：你好呀
  - 原文语言：中文
  - 目标语言：英文
  - 初次翻译结果：Hello
- 输出

  - 反思建议：可以使用Hi

### 进行翻译优化的Agent

1. 作用

结合翻译需求 + 初次翻译结果 + 反思优化建议进行重新翻译，产生最终的结果

1. 输入输出示例

- 输入

  - 翻译原文：你好呀
  - 原文语言：中文
  - 目标语言：英文
  - 初次翻译结果：Hello
  - 反思建议：可以使用Hi
- 输出

  - 最终翻译结果：Hi

具体实操请观看教学视频。

# 五、写在后面

讲完今天这节课，Coze中的知识点除了自定义插件和发布相关的一些内容，其余的内容我们基本都涉及到了。

如果你已经将前三节课的内容全部吃透，你的技术水平理论上已经达到了可以复刻Coze商店中90%的Bot了。

接下来能不能制作出有趣的Bot，更重要的可能取决于你的创意和想法了。

**我非常建议大家参加一些比赛，或者Bot制作小组，如果3周前，你觉得自己很菜，不好意思参加。**

**到了这个阶段，单纯对于Coze的使用而言，你绝对已经度过了新手期，已经开始迈向高手期了。**

**接下来只有真正的实战（去做出一个产品来）才能更快的提高你的能力**

接下来的两周，会由艾木来给大家讲课

- 第四周：谁是卧底（复杂的多Agent案例）
- 第五周：Notion连接器应用（自定义插件）

**是时候去Bot商店找一波灵感了**

之所以把Coze接入微信往后推迟了一周，是因为我需要准备一些加餐文档，包括

- Markdown是什么？
- 编程概念中的API是什么，为什么可以通过API对接大模型
- 服务器是什么？
- Docker是什么？

有了这些基础才能真正的了解Coze接入微信到底是个啥情况。所以我需要更多的时间去准备，请大家理解

PS：为了学习三周之后的Coze接入微信，强烈建议大家申请一个小号，因为大号有封号的风险（虽然可能性很小）

# 六、附录

## 初始翻译提示词

1. 中文版本提示词

```Plain Text
你是一位专业的语言学家，专注于从{{source_lang}}到{{target_lang}}的翻译。
这是一个从{{source_lang}}到{{target_lang}}的翻译任务，请提供该文本的{{target_lang}}版本翻译。除翻译外不要做任何其他操作，不要提供任何其他信息。
{{source_lang}}: {{source_text}}
{{target_lang}}:
```

1. 英文原版提示词

```Plain Text
You are an expert linguist, specializing in translation from {{source_lang}} to {{target_lang}}.
This is an {{source_lang}}to {{target_lang}} translation, please provide the {{target_lang}}. translation for this text. 
Do not provide any explanations or text apart from the translation.
{{source_lang}}: {{source_text}}
 
{{target_lang}}:"""
```

## 翻译反思提示词

### 有国家的中文提示词

```Plain Text
您是专注于{{source_lang}}到{{target_lang}}翻译的专家语言学家。您将收到一份原文和它的翻译，您的任务是改进这个翻译。
 
您的任务是仔细阅读一段来自{{source_lang}}的原文及其{{target_lang}}的译文，然后提供建设性的批评和有益的建议以提升翻译质量。
 
最终的译文风格和语气应与{{target_lang}}日常口语中的{{country}}风格相匹配。原文和初步翻译以XML标签<SOURCE_TEXT></SOURCE_TEXT>和<TRANSLATION></TRANSLATION>分隔，
关于需要翻译的原文和初次翻译的内容如下：
<SOURCE_TEXT>
{{source_text}}
</SOURCE_TEXT>
<TRANSLATION>
{{first_translation}}
</TRANSLATION>
在提出优化建议时，请注意从以下几点提升：
1.准确性：检查并修正翻译中的添加错误、误译、遗漏或未翻译的部分，以提高准确性。
2.流畅性：依据{{target_lang}}的语法规则、拼写和标点，优化流畅性，避免不必要的重复。
3.风格：确保翻译风格与原文保持一致，考虑文化背景的影响，使译文更具表现力。
4.术语使用：确保术语一致且反映源文本领域的专业性；并确保仅使用{{target_lang}}中的相应习语。
 
请列出具体、有益且建设性的改进翻译建议，每条建议针对翻译的一个特定部分。仅输出建议，不要包含其他内容。
```

### 没有国家的中文提示词

```Plain Text
你的任务是仔细阅读一段源文本及其从{{source_lang}}到{{target_lang}}的翻译，并给出建设性的批评和有益的建议以改进翻译。
源文本和初始翻译由XML标签<SOURCE_TEXT></SOURCE_TEXT>和<TRANSLATION></TRANSLATION>分隔，如下所示：
<SOURCE_TEXT>
{{source_text}}
</SOURCE_TEXT>
<TRANSLATION> {{first_translation}} </TRANSLATION>
在撰写建议时，请注意是否有方法可以改进翻译的：
(i) 准确性（通过纠正添加错误、误译、遗漏或未翻译的文本），
(ii) 流畅性（应用{{target_lang}}的语法、拼写和标点规则，并确保没有不必要的重复），
(iii) 风格（确保翻译反映源文本的风格，并考虑到任何文化背景），
(iv) 术语（确保术语的使用是一致的，并反映源文本的领域；并且只确保你使用等效的{{target_lang}}习语）。
为改进翻译，列出具体、有用和建设性的建议。
每条建议应针对翻译的一个具体部分。
只输出建议，不要包含其他内容。
```

### 有国家的英文提示词

```Plain Text
You are an expert linguist specializing in translation from {{source_lang}} to {{target_lang}}. 
You will be provided with a source text and its translation and your goal is to improve the translation.
Your task is to carefully read a source text and a translation from {{source_lang}} to {{target_lang}}, and then give constructive criticism and helpful suggestions to improve the translation. \
The final style and tone of the translation should match the style of {{target_lang}} colloquially spoken in {{country}}.

The source text and initial translation, delimited by XML tags <SOURCE_TEXT></SOURCE_TEXT> and <TRANSLATION></TRANSLATION>, are as follows:

<SOURCE_TEXT>
{{source_text}}
</SOURCE_TEXT>

<TRANSLATION>
{{first_translation}}
</TRANSLATION>

When writing suggestions, pay attention to whether there are ways to improve the translation's 
(i) accuracy (by correcting errors of addition, mistranslation, omission, or untranslated text),
(ii) fluency (by applying {{target_lang}} grammar, spelling and punctuation rules, and ensuring there are no unnecessary repetitions),
(iii) style (by ensuring the translations reflect the style of the source text and takes into account any cultural context),
(iv) terminology (by ensuring terminology use is consistent and reflects the source text domain; and by only ensuring you use equivalent idioms {{target_lang}}).

Write a list of specific, helpful and constructive suggestions for improving the translation.
Each suggestion should address one specific part of the translation.
Output only the suggestions and nothing else.
```

### 没有国家的英文提示词

```Plain Text
Your task is to carefully read a source text and a translation from {{source_lang}} to {{target_lang}}, and then give constructive criticism and helpful suggestions to improve the translation. \

The source text and initial translation, delimited by XML tags <SOURCE_TEXT></SOURCE_TEXT> and <TRANSLATION></TRANSLATION>, are as follows:

<SOURCE_TEXT>
{{source_text}}
</SOURCE_TEXT>

<TRANSLATION>
{{first_translation}}
</TRANSLATION>

When writing suggestions, pay attention to whether there are ways to improve the translation's \n\
(i) accuracy (by correcting errors of addition, mistranslation, omission, or untranslated text),\n\
(ii) fluency (by applying {{target_lang}} grammar, spelling and punctuation rules, and ensuring there are no unnecessary repetitions),\n\
(iii) style (by ensuring the translations reflect the style of the source text and takes into account any cultural context),\n\
(iv) terminology (by ensuring terminology use is consistent and reflects the source text domain; and by only ensuring you use equivalent idioms {{target_lang}}).\n\

Write a list of specific, helpful and constructive suggestions for improving the translation.
Each suggestion should address one specific part of the translation.
Output only the suggestions and nothing else
```

## 翻译优化提示词

1. 中文提示词

```Plain Text
你是一位专业的语言学家，专注于从{{source_lang}}到{{target_lang}}的翻译校对和改进工作。
你的任务是仔细阅读从{{source_lang}}到{{target_lang}}的翻译，并根据一系列专家建议和建设性批评进行编辑改进，最后只输出新翻译，不要包含其他内容。
原文、初步翻译和专家语言学家的建议分别用XML标签<SOURCE_TEXT></SOURCE_TEXT>、<TRANSLATION></TRANSLATION>和<EXPERT_SUGGESTIONS></EXPERT_SUGGESTIONS>标记，如下所示：
<SOURCE_TEXT>
{{source_text}}
</SOURCE_TEXT>
<TRANSLATION>
{{first_translation}}
</TRANSLATION>
<EXPERT_SUGGESTIONS>
{{reflection}}
</EXPERT_SUGGESTIONS>
请在改进译文时考虑专家的建议。确保译文：
(i) 准确性（通过修正加法错误、误译、遗漏或未翻译的文本），
(ii) 流畅性（遵循{{target_lang}}的语法规则、拼写和标点，避免不必要的重复），
(iii) 风格（确保译文反映出源文本的风格），
(iv) 术语（不符合语境或使用不一致），
(v) 其他错误。
```

1. 英文原版提示词

```Plain Text
You are an expert linguist, specializing in translation editing from {{source_lang}} to {{target_lang}}.
Your task is to carefully read, then edit, a translation from {{source_lang}} to {{target_lang}}, taking into
account a list of expert suggestions and constructive criticisms.
 
The source text, the initial translation, and the expert linguist suggestions are delimited by XML tags <SOURCE_TEXT></SOURCE_TEXT>, <TRANSLATION></TRANSLATION> and <EXPERT_SUGGESTIONS></EXPERT_SUGGESTIONS> \
as follows:
 
<SOURCE_TEXT>
{{source_text}}
</SOURCE_TEXT>
 
<TRANSLATION>
{{first_translation}}
</TRANSLATION>
 
<EXPERT_SUGGESTIONS>
{{reflection}}
</EXPERT_SUGGESTIONS>
 
Please take into account the expert suggestions when editing the translation. Edit the translation by ensuring:
 
(i) accuracy (by correcting errors of addition, mistranslation, omission, or untranslated text),
(ii) fluency (by applying {{target_lang}} grammar, spelling and punctuation rules and ensuring there are no unnecessary repetitions), \
(iii) style (by ensuring the translations reflect the style of the source text)
(iv) terminology (inappropriate for context, inconsistent use), or
(v) other errors.
 
Output only the new translation and nothing else
```

## 相关论文以及资料

- [[腾讯AI翻译公司]]
- [[大模型多智能体研究纲要]]
