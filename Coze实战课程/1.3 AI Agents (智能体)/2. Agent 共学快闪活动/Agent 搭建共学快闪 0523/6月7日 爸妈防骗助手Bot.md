---
title: "6月7日 爸妈防骗助手Bot"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/NUXtw6fHqiIip6kOngacDKtxnkf
node_token: NUXtw6fHqiIip6kOngacDKtxnkf
obj_token: C37ldPl1toLSBDxp1vnc1FwSnuc
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 3
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - " Agent 搭建共学快闪 0523"
  - "6月7日 爸妈防骗助手Bot "
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 32
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 6月7日 爸妈防骗助手Bot

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 ›  Agent 搭建共学快闪 0523

<callout emoji="📄">
# 概览
> 智能纪要依据会议录制内容生成，不代表平台立场，请谨慎甄别后使用
## **总结**
会议讨论了智能体 bot 爸妈防骗助手的产品设计、功能实现、开发流程等方面的内容，主要内容包括：
- **团队介绍**：包括团队成员、分工以及顾问团队。
- **产品定义**：重新定义真假新闻的功能，增加情绪价值。
- **制作流程**：包括基础工作流的设计和优化。
- **卡片制作**：包括工作流、开场白、内容设计、样式调整等。
- **卡片绑定**：介绍了如何创建卡片以及怎么绑定卡片。
- **AI 助手卡片制作经验分享**：包括卡片的调整、样式绑定变量、权重的设置等。
- **bot 的搭建和相关技术**：包括总结和推理能力的测试、落实方案的线上会议、团队沟通和分工等。
## **待办**
- [ ] 舒馨发送团队进入的空间链接
- [ ] 小明哥、瑞亚和凯门槛研究如何将公共项目转化为插件形式
- [ ] 王阳查看搜图入参的属性，确认是否可以调整比例
## **智能章节**
[00:24](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=24000)  **智能体 bot 爸妈防骗助手团队的创意与实践分享**
> 本章节主要介绍了智能体 bot 爸妈防骗助手的团队核心成员和顾问团队，以及团队的创意过程。该团队由王维恩发起，成员包括罗文、Kevin、郭琳、小明哥、王哲、陶姿、舒馨、夏快以及顾问团队 Sam 和赵波老师。他们最初的想法是做一个英语类的 bot，但后来调整为鉴别新闻真假的 bot，以帮助更多的人。在创意过程中，大家都深度参与并体验了如何捏 bot，罗文老师也提供了很多建议。
[10:54](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=654000)  **从需求出发，打造更具实用性和可玩性的智能体**
> 本章节主要是罗文老师的分享，他从产品定义和智能体的可延展性、可玩性两个方面进行了阐述。首先，他提出在开发智能体时，可以从产品的维度去定义，增加其存活度和使用率。接着，他通过密塔bot的案例，说明可以从场景和情绪价值等维度去考虑智能体的开发。其次，他指出智能体的可延展性和可玩性可以通过增加多轮对话、实时更新内容、增加更多的功能性和实用性等方式来实现。最后，他总结了制作新闻真假bot的思考过程，并对团队成员的工作表示了肯定和感谢。
[20:36](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=1236000)  **基于大语言模型的新闻真实性判别及优化**
> 本章节主要介绍了工作流的设计和实现过程。首先，马闻锴介绍了工作流的输入和输出，包括用户原文、URL 和图片等三种体裁，并对每个输入进行了详细的解释。接着，他讲解了选择器的使用，通过 Jina 软件进行 Web 标题和内容的获取，并利用大模型进行概述和辟谣。然后，他提到了基于搜索的生成主流程，通过碧瑶关键词让搜索更加精准，并在主流程中进行了规则的泛化和评分体系的引入，同时展示了推理分析的思考过程。最后，他介绍了整体的输出变量和一些关键技术点，包括记忆变量的使用和与前端 bot 的交互等。
[38:51](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=2331000)  **卡片设计与工作流结合的经验分享**
> 本章节主要介绍了如何将卡片与工作流和 bot 进行绑定，以实现卡片的输出。首先，小明哥分享了自己的卡片制作经历，接着介绍了 bot 的不同输出形式。然后，详细讲解了卡片的设计过程，包括开场白的设计、预置条件的设置、模板和组件的使用、结构模板的利用、循环渲染的应用等。最后，还介绍了卡片的外围设计，包括背景图的选择、行间距和边距的调整、标题的插入、分割线的使用等。
[01:00:25](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=3625000)  **卡片设计与变量绑定的实操演示**
> 本章节主要介绍了如何使用卡片组件创建可视化的工作流。小明哥通过实际操作演示了如何创建卡片、添加标题、日期、内容、图片等元素，并调整样式。他还介绍了如何绑定变量，以及如何使用循环渲染功能。此外，小明哥还分享了如何制作词云海报，包括如何上传字体和设置权重等。最后，他提到了一些插件的使用技巧，如翻译插件和增强搜索插件。
[01:13:55](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=4435000)  **构建 AI 机器人的经验分享**
> 本章节主要介绍了卡片项目的进展情况和经验分享。陶梓同学将制作关于卡片的分享文档并上传至 v to HR 公共知识库。组长维恩同学分享了项目的收获和经验，强调了在项目中需要有自己的想法，不断尝试和实践，以及通过多轮迭代来完成工作。会魔法的大人分享了自己的经验，通过学习如何编写提示词，发现可以在其中增加回复逻辑和变量逻辑，从而完成更多的工作。  
> 此外，会魔法的大人还介绍了一个角色互动模拟器，通过在其中增加各种互动和想法，可以学到很多东西。
[01:26:01](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=5161000)  **关于 vtoAGI 空间及 bot 制作的分享与答疑**
> 本章节主要是关于 vtoAGI 空间的介绍和答疑。会魔法的大人首先提出大家可以分享使用 bot 的心得，或者提出问题和建议，团队会继续优化 bot。接着，Joyful 询问 bot 的工作流和 TS 流程，会魔法的大人表示会将工作流放到 vtoAGI 空间供大家查看。然后，会魔法的大人介绍了 vtoAGI 空间，包括其中的学习资料、插件工作流等，并强调了变量在工作流中的重要性。最后，会魔法的大人和舒馨解答了如何加入 vtoAGI 空间的问题。
[01:33:41](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=5621000)  **关于 Kevin 界面运行流畅度、输入类型、数据传输及获取的讨论**
> 本章节主要介绍了 Kevin 界面运行流畅的原因，以及数据传输过程中保持输入类型一致的重要性。此外，会魔法的大人还分享了一个有趣的玩法，即在每个分支上获取的内容后面紧跟一个变量，并将其设置给 bot，最后从 bot 中获取用户输入的内容。
[01:37:48](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=5868000)  **如何排查和解决魔法运行过程中的问题**
> 本章节主要介绍了在运行过程中出现问题的排查方法。首先提出在调试过程中要逐步检查输入和输出，以找出问题所在。然后通过举例说明在选择字段时可能会出现选错的情况，导致输入错误，从而影响最终结果。最后强调在出现问题时不要害怕，要认真检查，从中吸取经验，逐渐提高自己的能力。
[01:40:36](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=6036000)  **关于 code 平台、变量及飞书文档 URL 地址的讲解**
> 本章节主要介绍了在 code 平台上，如何设置变量以及如何使用变量。会议首先提出大家应该抓住学习机会，积极参与学习和探索。接着，会议介绍了变量的设置方法，指出可以在记忆板块中设置变量，并为不同的 bot 设置不同的变量信息。例如，可以设置 current doc 变量来存储飞书文档的 URL 地址。最后，会议还提到了在外层设置变量后，可以在消息回复中读取 bot 中的信息。
[01:43:37](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=6217000)  **关于如何通过创建 bot 副本和工作流副本，并由主整合人进行整合，实现热情回复的讨论**
> 本章节主要介绍了如何通过创建副本、设定工作流等方式，实现根据用户输入的问题，调用工作流输出相应信息的功能。
[01:46:51](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=6411000)  **关于多模态输入、上传图片插件、制作海报插件的讨论**
> 本章节主要介绍了多模态输入上传图片的插件以及制作海报的插件。会魔法的大人为大家介绍了在测试时可以通过编排界面右下角的加号选择工具，上传图片需要选择支持上传文件的插件。针对海报制作，目前有两种方案，一种是 run 同学使用的图像流，但该方案不太稳定且运行时长较长；另一种是 Sam 老师封装的 fast poster 插件，该插件提供 API，生成效果较好，但需要收费。小明哥表示可以研究 fast poster 公共项目，尝试将其转化为插件形式供大家使用。
[01:52:14](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=6734000)  **关于图像搜索、海报制作、微推荐等问题的讨论**
> 你提供的内容中存在错误信息，修改后的内容如下：  
> 本章节主要讨论了图像搜索、海报制作、API 发布等相关问题。会议首先提出可以使用 API 将 bot 集成到微信聊天中，但需要收费。接着，他们提到了新闻防片助手的图像搜索功能，经过测试发现必应的图片搜索返回结果更准确，更贴合用户问题。他们还讨论了海报的制作，提出了两种方案，一种是使用别人的插件生成海报，另一种是使用图像流自己制作海报。他们提到了使用图像流制作海报时遇到的一些问题，如运行效率慢、容易出错等。最后，他们提到了在搜索结果中如何设置图像比例的问题。  
> 本章节主要讨论了如何使用搜索插件，并强调了在学习中发挥主动性的重要性。会魔法的大人介绍了搜索插件的参数设置，包括偏移量、关键词和返回数量等，并提醒大家注意插件中的小图标以了解变量的作用。吕昭波提出了关于微推荐的问题，以及如何通过主动学习和与他人合作来深入学习。会魔法的大人分享了自己的阅读体验，强调了主动性在学习中的重要性，并建议大家明确自己的需求，将想法落实到实处。
[02:03:55](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=7435000)  **关于卡片使用的分享及后续安排**
> 本章节主要内容为：  
> 1. 专场主持人思琳老师解答了大家的问题。  
> 2. 后续会有卡片使用文档分享到 v to a 加的知识库。  
> 3. 假期晚上的会议上线至今，90%的人都在线参与。  
> 4. 徐建老师认为吕昭波的主持需要改进，因此邀请了更有主持经验的苏西老师来帮忙。  
> 5. 第二期议程共学活动还未结束，下周将继续直播。
[02:06:16](https://waytoagi.feishu.cn/minutes/obcnsa2rszgw22fyc2n42hx3?t=7576000)  **开源社区端午节活动总结**
> 本章节主要是对会议的总结。会议上，大家对苏西老师的主持表示感谢，并对吕昭波的影响力表示赞赏。许键认为昭波的团队战斗力和主动性都很强，希望大家保持联系，在今后的活动中继续发扬开源精神。最后，会议在端午节的祝福声中结束。
</callout>

# 会议回顾

<readonly-block href="https://player.bilibili.com/player.html?bvid=1QJ4m1M7ti" type="iframe"></readonly-block>

# 相关会议纪要

<callout emoji="📌"><p><cite doc-id="THmbdGKIpo2oamxMv5scKhnunPe" file-type="docx" title="「共学快闪第三期」一起搭建「微信机器人」活动 2024年6月27日" type="doc"></cite></p><p><cite doc-id="Z0MzdKZfqoCYvqxCaIdcwurtnzt" file-type="docx" title="「共学快闪第三期」一起搭建「微信机器人」活动 2024年6月24日" type="doc"></cite></p><p><cite doc-id="DCNadTWAWoqL4MxkPmfcXLumnLb" file-type="docx" title="「共学快闪第三期」一起搭建「微信机器人」活动 2024年6月25日" type="doc"></cite></p><p><cite doc-id="A0JbdWVBroYOINxjqHLcihBcnte" file-type="docx" title="「共学快闪第三期」一起搭建「微信机器人」活动 2024年6月20日" type="doc"></cite></p><p><cite doc-id="JFx0dXCaloxMZ5xlOh2cBxgNn8g" file-type="docx" title="「共学快闪第三期」一起搭建「微信机器人」活动 2024年6月19日" type="doc"></cite></p><p><cite doc-id="DDvRdDurPodjlyxV6QEcr8jyn5e" file-type="docx" title="6月18日: Coze 比赛答疑" type="doc"></cite></p><p><cite doc-id="Yz0odbcWWoHO0pxLGeQcNyV6ngt" file-type="docx" title="6月4日 Bot冠军大揭秘：李小白" type="doc"></cite></p><p><cite doc-id="GeuedJ9wroHrT9x6JU6cgB0gnwd" file-type="docx" title="6月3日: 参赛bot一起试玩分享 -- 一定要看, 创意无限" type="doc"></cite></p><p><cite doc-id="R4zxdrOzvo4cIXx3ImccsHDynPd" file-type="docx" title="5月26日 银海分享 | 用AI重塑我的工作流" type="doc"></cite></p><p><cite doc-id="LasYdheEmorzmRxWhZXcRC0enaf" file-type="docx" title="5月25日 Stuart分享｜拆解“离谱村捏剧本”coze bot思路" type="doc"></cite></p><p><cite doc-id="FPjDdS88NoGElMx1p2fcYBwTnkg" file-type="docx" title="5月24日 来来 &amp; Stuart分享｜图像流重塑设计" type="doc"></cite></p><p><cite doc-id="KDQwdx4bKoLoUMxl61ncqSCsnDc" file-type="docx" title="5月23日 艾木分享 | 这也许是你一生中第一个Bot" type="doc"></cite></p><p></p></callout>
