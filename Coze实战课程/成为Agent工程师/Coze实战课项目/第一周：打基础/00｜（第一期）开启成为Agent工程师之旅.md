---
title: "00｜（第一期）开启成为Agent工程师之旅"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/LIIOwll3WiKoeTkN75fcDrNanbd
node_token: LIIOwll3WiKoeTkN75fcDrNanbd
obj_token: WByddvgYQoLkROx8hn3cXtUNnkc
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 3
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "第一周：打基础"
  - "00｜（第一期）开启成为Agent工程师之旅"
obj_create_time: 1717304276
obj_edit_time: 1723897162
creator: ou_4f9742f370819a3c899baacbc140aed2
owner: ou_4f9742f370819a3c899baacbc140aed2
revision_id: 1702
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# 00｜（第一期）开启成为Agent工程师之旅

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 第一周：打基础

<blockquote><p>会议回放已经生成，大家可以按需观看<br/><cite doc-id="QH1vdWztZo2LtMxLRdjcnZ70n0b" file-type="docx" title="开课仪式：开启成为Agent工程师之旅 2024年6月15日" type="doc"></cite></p><p>单独的视频链接：</p><readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnxso23ei6l291yg8463lu?from=ccm" type="iframe"></readonly-block></blockquote>

# 一、两位主讲自我介绍（6分钟）

## 大圣

- 河北石家庄人，现居住杭州余杭，一位Java开发工程师
- 有一个超级可爱的19个月的女儿，在探索AI育儿
- 通往AGI之路共创作者，组织参与AI Agent一期的共学快闪活动：<cite doc-id="WMTYwmkyqiZBUSkOpircmxm1nlc" file-type="wiki" title="Agent 搭建共学快闪 0507" type="doc"></cite>
- 工作经历丰富，大中小厂都呆过，创业3年，目前在一家中厂上班
- 喜欢写作，热爱分享，擅长拆解复杂的AI知识，然后通过通俗易懂的方式讲解出来
- 不喜欢碎片化的知识，不喜欢将失败归结于各种信息差，喜欢沉淀体系化的知识

PS. 大家叫我大圣就好，尽量不要带“老师”～

我在课程中的角色：

- 擅长讲解基础的知识，帮助大家度过新手期
- 我的课基本都在前期，目的是帮助大家打下扎实的基础，方便学习后面的进阶课程

## 艾木

一名软件工程师。爱好看论文和写代码。

PS. 大家叫我“艾木”就好，尽量不要带“老师”～

### 开发过[一个 Agent 框架](https://mp.weixin.qq.com/s/G4iNbFHudLmG-LaOJpwmmg)，应用在[一个编程 Agent 产品](https://mp.weixin.qq.com/s?__biz=MzU5MDM4ODIxMw==&mid=2247484021&idx=1&sn=a7e9ee695aea397d3ac8bf920b9ffe01&scene=21#wechat_redirect)中

> [!abstract]- 🖼 图片展示了Agent框架的架构图。分为三层，最上层是App Interf
> 图片展示了Agent框架的架构图。分为三层，最上层是App Interface Layer，包含gRPC API Server、FastAPI Server、Chat Interface；中间层是Domain Layer，有Programming和未命名部分；最下层是Core Layer，包含Morph、Task、Captor in Workspace、Learning Cycle等模块，还有Agency、HyperFunction、Connectors等部分。该图与文档中介绍Agent框架的内容相关，直观呈现了框架的层次结构及各部分功能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/L7u2bObokozpwGxhHoWcieoqnPd) · `L7u2bObokozpwGxhHoWcieoqnPd`

### 用 Coze 搓过 3 个 Bots：Dr. Know、谁是卧底 和 Harvest

> [!abstract]- 🖼 图片展示了作者用Coze搓过的三个Bot。左侧是Dr. Know，介绍其
> 图片展示了作者用Coze搓过的三个Bot。左侧是Dr. Know，介绍其为信息检索Bot，极简版Perplexity；中间是“谁是卧底”，介绍其为AI推理游戏，复杂度较高；右侧是Harvest，介绍其为个人知识构建助理，可将Coze Bot连接到Notion数据库。图片与上下文紧密相关，直观呈现了作者在Coze平台开发的Bot类型及特点，是对上文提到的用Coze搓过3个Bots内容的具体说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QEWbbU8quotMPUxcxG0cgAxTnsb) · `QEWbbU8quotMPUxcxG0cgAxTnsb`

- Dr. Know: https://www.coze.com/s/Zs8MUCQGU/（<cite doc-id="RnJMwnX0UiEY6yk8cq6cTtZXnGy" file-type="wiki" title="5月23日 艾木分享 | 这也许是你一生中第一个Bot" type="doc"></cite>）
- 谁是卧底: https://www.coze.com/s/Zs8MU9PGT/ （<cite doc-id="RWN5wdpIBiDzyvkekEfcuCXxnbf" file-type="wiki" title="04｜Multiagent之谁是卧底" type="doc"></cite>）
- Harvest: https://www.coze.com/s/Zs8MUkQPG/ （<cite doc-id="UVYwws8o2iUfsqk6n5GczSmRnPe" file-type="wiki" title="05｜基于 Notion 连接器打造个人信息助理" type="doc"></cite>）

### 组织着一个498（+197）人的 [Coze 创作者社群](https://mp.weixin.qq.com/s/_mM7FG21tS2F3MZWPmgw9Q)

社群介绍：[一个程序员的AI社群运营心得](https://mp.weixin.qq.com/s/_mM7FG21tS2F3MZWPmgw9Q)

入群申请（申请要真诚，群主会筛选）：

> [!abstract]- 🖼 图片是一个二维码，位于文档中介绍Coze创作者社群入群申请方式的上下文位
> 图片是一个二维码，位于文档中介绍Coze创作者社群入群申请方式的上下文位置。二维码内有一个蓝色箭头和绿色对勾的图标，周围有黑色线条装饰。下方有一个绿色圆形图标，内有白色字母“S”。该二维码是入群申请的入口，申请时需真诚，群主会筛选。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JkuSbOm66oH8AXxfaUicJ5Oqn0c) · `JkuSbOm66oH8AXxfaUicJ5Oqn0c`

# 二、课程介绍及声明（大圣5分钟）

课程预期对齐：

- 不承诺变现，不承诺找到高薪工作，不承诺可以帮助落地企业级项目
- 本次课程会有部分编程相关的概念，我们会尽最大努力去讲解，但是最终能否听懂要看个人
- 集中答疑，无法随叫随到，而且优先答疑课程相关内容，针对个人项目的问题不在服务范围内
- 我们希望帮你打开思维，从解决问题的角度出发

我们的期望

- 我们讲Coze，又不仅仅是讲Coze，我们希望课程过后，无论出现怎样的智能体平台，你都能很快的上手
- 我们希望这次课程可以帮助你找到一条学习AI的路径，这条路径既能脚踏实地，又能仰望星空
- 成为Agent工程师不是一个噱头，工程师这个概念也与编程无关，它是一种能力

  - 扎实的技术知识
  - 解决复杂问题的能力

课程介绍：

- 开课仪式
- 第一周：基于RAG构建企业生产资料问答系统

  - 从AI Agent的视角去看待Coze这款工具
  - 通过一个教学案例，帮助大家打好Coze的基础（插件、工作流、数据库、知识库、变量等核心概念）
  - 深入了解知识库到底是什么？市场上都有哪些解决方案
- 第二周：图像流（待定）

  - 引入Coze新出不久的图像流
  - Coze中的卡片功能如何使用
- 第三周：多Agent之多人辩论

  - 引出Coze中多Agent的模式，为后面的《谁是卧底》案例打基础
- 第四周：多Agent之谁是卧底（艾木）
- 第五周：Coze接入微信

  - 服务器、Linux操作系统、Docker这些概念到底是什么
  - 大家看到的微信小机器人是如何搭建出来的
- 第六周：Notion连接器（艾木）
- 第七周：AI Coder（艾木）
- 第八周、第九周：答疑

<callout emoji="💡">
**这是最后一次退款的机会，本次开课仪式之后，如果课程有跟你预期不符，可以联系我们退款**
**但是请注意，一旦我们将你拉入到我们的Coze团队空间，便不再接受退款。请知晓**
</callout>

# 三、AI学习进阶路径（大圣15分钟）

学习AI Agent是需要一些基础的知识的，对于AI新手小白上手会不太友好。

为了帮助新人同学更好的学习AI Agent，我将自己的AI学习路径分享给大家，供新手同学模仿和学习，减少摸索的时间

同时我更希望你能找到适合自己的路径，在AI这条路上越走越远

<cite doc-id="N1WUwd0QNiqZR0k0nEQcpORBnmf" file-type="wiki" title="大圣的AI学习路径3.0" type="doc"></cite>

# 四、如何学习和如何学编程（艾木 25 分钟）

<figure view-type="Preview"><source mime="application/pdf" token="JSxVbDhbzoe6jaxvQ5WcCzzsnxm"/></figure>

# 五、WaytoAGI知识库使用指引（15-20分钟）

声明：

我们跟WaytoAGI没有关系，只是为了分享我们知道的有质量的免费的信息。

我们不会以WaytoAGI知识库里的其他作者的内容作为课程内容。

## 第一位分享者：YoYo

<cite doc-id="Cy5MwenLfiuXXUkIe2Sciilbnjg" file-type="wiki" title="我在通往AGI的学习之路心得" type="doc"></cite>

## 第二位分享者：BZ起点

直接看视频即可

## 第三位分享者：Summer

<cite doc-id="ZVcUwn1Qcib3TVkMZiDcNlx7nTh" file-type="wiki" title="自我介绍与学习路径分享" type="doc"></cite>
