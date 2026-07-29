---
title: "5月9日 艾木分享《Workflow》"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/GzODwp2vuimGamkl8hDcqKscnnh
node_token: GzODwp2vuimGamkl8hDcqKscnnh
obj_token: SbS2dK8F5o9bWBx69RvcbzUgn0b
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 3
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - " Agent 搭建共学快闪 0507"
  - "5月9日 艾木分享《Workflow》"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 47
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 5月9日 艾木分享《Workflow》

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 ›  Agent 搭建共学快闪 0507

<readonly-block href="https://player.bilibili.com/player.html?bvid=1is421N72j&amp;spm_id_from=333.788&amp;vd_source=290a2836f7818edc2c18c6eb525d4abe" type="iframe"></readonly-block>

<figure view-type="Preview"><source mime="application/pdf" token="TG2HbCPpBo7ayBx9YRncTky4nnd"/></figure>

<callout emoji="📄">
# 概览
> 智能纪要内容由 AI 生成，可能不准确，请谨慎参考，这些内容不代表平台立场
## **总结**
会议讨论了 AI 模型的 agent 系统和 workflow、基于谷歌搜索结果的智能回答系统的设计与实现、RPA 和 AI 的关系及应用等问题，主要内容包括：  
1. agent 系统的概念和组成部分。  
2. GPT 的工作原理和应用场景。  
3. auto GPT 的工作原理和设计。  
4. agent 的概念和测试 agent 通用性的方法。  
5. 模型在不同任务中的表现。  
6. AI 模型加上 workflow 后表现的提升。  
7. 智能对话系统的理论及案例演示。  
8. 基于谷歌搜索结果的智能回答系统的设计与实现。  
9. RPA 和 AI 的关系及应用。  
10. AI 大模型的落地实现和商业化变现。  
11. agent 的语义分析和优化反馈。  
12. 多 agent 场景下的身份识别和记忆上下文机制。  
13. 如何使用代码处理对话。  
14. 大模型的智能表现和应用。  
15. 技术发展过快导致部分人跟不上节奏的问题及解决方案。
## **待办**
- [ ] 张梦飞找几个同学来分享经验，并在微信群里聊一聊
- [ ] WillLee发送更新过的代码到群里；尝试玩游戏并复刻；罗文老师分享如何串联提升生产力
## **智能章节**
[00:00](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=0)  **关于学习、作业、会议等问题的答疑**
> 本章节主要内容为大圣、AJ 与参会者的答疑互动。会议首先提到了今晚有答疑专场，结束后大家可以在群内自行组队学习。接着，大圣提出查看问题收集，发现没有提交记录，猜测大家可能还没来得及动手搭建。然后，AJ 分享了会议链接，并表示大家可以自己动手搭建，遇到问题再进行复制调整。
[07:06](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=426000)  **工作流在 agent 系统概念背景下的应用**
> 本章节主要内容为：Will Lee 做了简短的自我介绍，然后分享了 agent 系统背景下的工作流。
[08:27](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=507000)  **Will Lee 分享他用 code 制作的三个 bot**
> 本章节主要介绍了 Will Lee 开发的三个 bot，分别是信息检索 bot doctor no、AI 推理游戏卧底和知识助理 MVP。其中 doctor no 是一个极简版的 perplexity，可以通过谷歌搜索和大语言模型进行信息检索和总结；卧底是一个多议程模式的 bot，用于测试 AI 是否能骗过人类玩家；知识助理 MVP 则是一个产品 MVP，特色功能是可以实现 cos 与 notion 的连接，将网页上的信息存入 notion。
[12:12](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=732000)  **理论与实践并重：bot 实际操作与理论讲解**
> 本章节主要讲解了 doctor no 和卧底这两个案例的实际操作，并且提供了获取相关资料的途径。同时，Will Lee 提醒大家理论和实践同样重要，鼓励大家将两者结合起来。
[14:22](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=862000)  **深入理解 Agent 系统：大洋洋模型、规划、记忆与工具使用**
> 本章节主要介绍了 agent 的相关内容和大洋洋模型的记忆部分与工具使用部分。首先，大聪明以相声的形式为大家梳理了 agent 的前世今生，Will Lee 从偏概念的角度出发，为大家推荐了一篇 OpenAI 工程师写的有关大源模型的 agent 的综述文章，文章提出 agent 系统的概念，并指出其核心组成部分包括大源模型、规划能力、channel sort 和问题分解。其次，介绍了大洋洋模型的记忆部分和工具使用部分，包括上下文和外部记忆，以及 IM 模型和一些传统程序。最后，Will Lee 提出了一个疑问，即系统中似乎没有 workflow，这需要大家进一步思考。
[20:34](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=1234000)  **OpenAI 的 GPT 模型与插件**
> 本章节主要介绍了 OpenAI 的 GPT 模型，包括其 agent 形态、核心组成部分以及面向用户的界面。其中，核心组成部分包括系统提示词、知识库和插件。系统提示词是用户输入的指令，知识库存储了外部文档和信息，插件则是可供调用的工具。会议提供了一个 GPT 的系统提示词示例，展示了 ChatGPT 部分和 tools 部分的内容。  
> 此外，还介绍了 OpenAI 提供的一些工具，包括 GPT、ChatGPT 等，并解释了 Custom GPT 的概念和工作原理。最后，探讨了 Workflow 的问题，认为 OpenAI 可能存在 Workflow，但没有给用户自己定义的权限。
[27:27](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=1647000)  **Auto GPT：探索 GPT-4 通用 agent 的边界**
> 本章节主要介绍了 auto GPT 这个现象级的开源项目。Will Lee 认为 auto GPT 值得关注和欣赏，因为它具有实验精神，推动了 AI 可能性的边界。auto GPT 是一个实验性项目，旨在探索基于 GPT 4 的通用 agent 的能力边界。视频演示了 auto GPT 的交互方式，用户输入一个 GPT 的名字、目标数据，它会自动规划、自动调工，完成任务。Will Lee 还提出了在 auto GBD 项目中，workflow 在哪里的问题。
[32:49](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=1969000)  **Auto GPT 工作原理及应用价值探讨**
> 本章节主要介绍了通用 agent 的 workflow 设计，并以 auto GBD 和 auto GPT 为例进行了详细说明。auto GBD 的 workflow 包括用户输入目标和任务信息、外层循环负责 plan、内层循环负责具体任务执行等。auto GPT 是一个实验性项目，它在设计领域的表现让人震撼，但在某些任务上也会出现不稳定的情况。
[41:36](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=2496000)  **关于 workflow 的理论探讨**
> 本章节主要讨论了工作流（workflow）的概念。Will Lee 认为 work 的意思就是干活，包括脑力活和体力活。他还解释了 workflow 是 agent 的核心，需要对其有字面上的理解。
[43:17](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=2597000)  **关于 AGI 的正确理解与思考**
> 本章节主要讲述了不要过度迷信 AGI 中的“g”，并介绍了 Mana hugging face 和 auto GBG 团队的测试集。通过该测试集可以看出，人和大洋模型在表现上存在很大的差异。同时，还介绍了一个关于任务完成情况的对比测试，发现人类与其他方式相比存在较大差异，并且在选择和使用工具方面具有明显优势。最后，提出了几个值得思考的问题，如任务的多模态性等。
[49:11](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=2951000)  **如何客观看待大语言模型的基础表现？**
> 本章节主要讨论了盖亚测试集的测试结果。其中，GPT-4 的表现可能受到了不公平的评价。测试集中，基地四维和 Gemini 4V 在多模态任务上有明显提升，而微软的 Multi agent 框架在周一议程模式下表现出色。需要注意的是，这些测试的提示词简单，没有复杂的工作流设计，因此测试结果仅能反映大语言模型作为 agent 大脑的基础表现。基于这些数据，我们应该对大语言模型有一个客观的认知，避免过度解读。
[52:03](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=3123000)  **人工智能在编程领域的应用及挑战**
> 本章节主要讨论了在编程领域中使用 agent 的经验教训。其中提到了 Audio GPT 过于通用和自动化，而在实践项目中需要考虑其可控性和实用性。他们曾经做过一个实验性的项目，设计了一个在编程领域的 agent，但发现即使限定了编程场景并控制了流程，仍然很难达到预期效果。因此，他们建议采用从受控到半受控再到通用 agent 的路线，并且受控方式应该是由程序控制而非人控制，这样可以降低成本并实现自动化。
[56:42](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=3402000)  **从提示词工程到 flow 工程：AI 在代码生成领域的研究与应用**
> 本章节主要介绍了从提示词工程到 flow 工程的相关研究。首先，Will Lee 提到了 Codem 团队的测试集，该测试集比 open i 的 human evaluate 测试集题目稍难一些，并且使用了尽可能多的流程来完成编程任务。其次，他介绍了该研究的结果，结果表明通过长流程去完成复杂的任务可以有很大的提升，而且这种提升不受模型本身能力的影响。最后，他还提到了 Devin 的测试集，该测试集直接模拟了实际程序员的工作场景。
[01:00:31](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=3631000)  **人工智能在开源项目测试集中的表现与工作流的重要性**
> 本章节主要介绍了一种新的测试方法，该方法使用了从 GitHub 上的开源项目中获取的测试集，其中包含了用户提出的问题。通过运行 agent 来修复这些问题，并观察测试结果是否通过，可以直接反映出 agent 在实际工作任务中的表现。这种测试方法更接近于实际工作场景，能够更准确地评估 agent 的能力。  
> 同时，本章节还强调了工作流的重要性，有工作流和没有工作流的 agent 表现差异巨大。通过这种测试方法，我们可以对当前最强的 agent 加工作流的表现有一个基础的认识，避免被忽悠。
[01:02:24](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=3744000)  **关于 workflow 的介绍与案例演示**
> 本章节主要介绍了 workflow 的相关内容。Will Lee 提到了 Devin，并解释了最近丹阳开始关注 workflow 的原因，即吴恩达老师在 Twitter 上建议大家关注 workflow。Will Lee 认为 workflow 是符合时代的技术或概念，并分享了吴恩达老师在官网上的 workflow 设计模式。他还介绍了 reflection 和 TOOLS 两种可靠的设计模式，以及 planning 和 mount agent 两种不太稳定的设计模式，并强调具体实现方式会影响稳定性。最后，Will Lee 通过两个案例演示了 workflow 和 mountain agent flow 的具体形式。
[01:04:22](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=3862000)  **Doc No 与 Open i GTS 对比，聚焦基于大人模型的 Agent 文案**
> 本章节主要介绍了基于单 agent 的 bot——doc no。doc no 与 open i 的 GTS 相比，多了 Workflow or money agent flow。它可以根据用户输入的信息进行搜索并给出回答，其核心是 workflow，主要负责搜索和回答，并且可以调用各种插件辅助工作。  
> 此外，doc no 中还有 code 节点，可以进行数据格式转换，方便后续单元模型处理。最后，doc no 会将格式化后的信息和用户语言偏好等参数传入大洋洋模型节点，生成回答。
[01:12:05](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=4325000)  **对 Workflow 的理解与分析**
> 本章节主要讲解了 workflow 的结构和语义函数的特殊之处。Will Lee 认为 workflow 是传统程序加自然语言程序形成的程序，并提出可以将其中的模块理解为函数。他还介绍了语义函数的两个特点：一是由自然语言编写，更容易被理解；二是可以模拟人的高阶思维，这一点在传统编程中很难实现。
[01:15:37](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=4537000)  **解析智能对话系统的工作原理与设计**
> 这一章节主要介绍了 agent 系统中的 workflow，包括其构成、核心模型以及在游戏中的应用。首先，Will Lee 展示了 workflow 的基本构成，包括基础节点、value 保存、code m 提供的其他节点、plugin 等。多个 workflow 可以组合起来添加到 bot 中，实现 bot 的能力或技能。其次，他讲解了 workflow 中的两个重要模型：推理模型和对话模型。推理模型负责完成任务，对话模型则负责管理 workflow 和 plugin，理解用户任务要求，调用相应的 workflow 来完成任务。接着，他结合“谁是卧底”bot 的设计界面，解释了 Multi agent 的实现方案，并强调了多 agent 之间的协作方式可以非常多样化。然后，他介绍了游戏中的 agent 如何与人类玩家互动，包括人类玩家发言、AI 玩家发言、投票、报告游戏结果等流程。其中，AI 玩家发言的策略是模仿人类的思考过程，通过猜测与自己对应的词汇，并根据发言记录、轮次等信息进行推理。  
> 同时，他还介绍了 workflow 的作用，以及如何通过添加插件、知识库等方式扩展 agent 的功能。最后，他展示了一个基于 AI 的线上发言策略的基础版，该策略混合了传统的程序逻辑、Felse 判断以及大语言模型的节点。
[01:31:16](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=5476000)  **关于 m 大老师分享的答疑与讨论**
> 本章节主要讨论了 m 大老师分享内容的答疑、工作流的使用场景、语言模型的进化是否会减少对工作流的依赖、当前模型的能力上限和在实际应用中的稳定性问题、在复杂场景下如何调用多个 bot 或工作流的问题、扣子的商业化问题以及 AI 技术在不同领域的应用。其中，重点探讨了工作流的使用场景、语言模型的进化是否会减少对工作流的依赖、当前模型的能力上限和在实际应用中的稳定性问题、在复杂场景下如何调用多个 bot 或工作流的问题以及扣子的商业化问题。
[01:56:57](https://waytoagi.feishu.cn/minutes/obcn8e8mrz9u721s1j13hxva?t=7017000)  **关于 AI 在不同领域的应用及商业化落地的讨论**
> 本章节主要讨论了 AI 在具体业务场景中的应用，包括微信机器人的引流和推销、AI 解读检测设备报告、脑机接口等。商业化变现问题也被提及。答疑环节中，SD 解释了 memory 的作用和相关功能。陶梓提出了如何实现根据输入内容分析和判断用户水平，并进行优化反馈的问题。大模型的记忆和上下文问题也被讨论，包括如何通过增加上下文信息来提高大模型的回答质量。在使用 agent 和 workflow 时，给上位增加大量文字可能导致其无法记住所有内容的问题也被提出。  
> 会议还讨论了在使用大语言模型时，如何为其提供上下文信息以确保一致性。此外，会议还讨论了微调模型的成本问题，指出微调模型的成本是原始模型的 5 倍，因此需要谨慎使用。最后，会议还提到了中国大模型自主研发的情况，指出 Llama3 卡住了中国大模型自主研发的脖子。
</callout>

# 会议回顾

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcn8e8mrz9u721s1j13hxva?from=ccm" type="iframe"></readonly-block>

# 会议议程

<agenda></agenda>

# 相关会议纪要

<callout emoji="📌"><p><cite doc-id="DTEedj6CBoDJXGxQEDzclGQfnCb" file-type="docx" title="「共学快闪活动」 AI Agent篇  Coze搭建 2024年5月11日" type="doc"></cite></p><p><cite doc-id="Tq6vdpmW5oW0IlxNwB4cp1CqnIf" file-type="docx" title="5月10日 罗文分享「共学快闪活动」 AI Agent篇 认识插件" type="doc"></cite></p><p><cite doc-id="UEC7dF0xzoY7dMxDgIqccd4fnwk" file-type="docx" title="5月8日 大圣分享《Coze全流程搭建 》" type="doc"></cite></p><p><cite doc-id="FEgAd81d1oLY1wx6DrScjzfdn3e" file-type="docx" title="「共学快闪活动」 AI Agent篇  Coze搭建 2024年5月7日" type="doc"></cite></p><p></p></callout>
