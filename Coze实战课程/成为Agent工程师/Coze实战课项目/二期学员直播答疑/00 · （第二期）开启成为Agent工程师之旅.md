---
title: "00 | （第二期）开启成为Agent工程师之旅"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/IYxIwJNHsi4070krpHBc3eLsnyb
node_token: IYxIwJNHsi4070krpHBc3eLsnyb
obj_token: IRJNdjcluoW6VZxBc7vcqXQPnpe
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 3
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "二期学员直播答疑"
  - "00 | （第二期）开启成为Agent工程师之旅"
obj_create_time: 1723895136
obj_edit_time: 1723904025
creator: ou_4f9742f370819a3c899baacbc140aed2
owner: ou_4f9742f370819a3c899baacbc140aed2
revision_id: 428
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# 00 | （第二期）开启成为Agent工程师之旅

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 二期学员直播答疑

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcn6z6361fwd62ju5n7j4uv?from=ccm" type="iframe"></readonly-block>

# 一、两位主讲自我介绍（6分钟）

## 大圣

- 河北石家庄人，现居住杭州余杭，一位Java开发工程师
- 有一个超级可爱的21个月的女儿，在探索AI育儿
- 通往AGI之路共创作者，组织参与AI Agent一期的共学快闪活动：[[1.3 AI Agents (智能体)/2. Agent 共学快闪活动/Agent 搭建共学快闪 0507/Agent 搭建共学快闪 0507|Agent 搭建共学快闪 0507]]
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
> 图片展示了Agent框架的架构图。分为三层，最上层是App Interface Layer，包含gRPC API Server、FastAPI Server、Chat Interface；中间层是Domain Layer，有Programming和未命名部分；最下层是Core Layer，包含Morph、Task、Captor in Workspace、Learning Cycle等模块，还有Agency、HyperFunction、Connectors等部分。该图与文档中大圣介绍开发过一个Agent框架的内容相关，直观呈现了框架的层次结构及各部分功能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MhAzbk3cXoO1yYxLA7Ac5h4inEh) · `MhAzbk3cXoO1yYxLA7Ac5h4inEh`

### 用 Coze 搓过 3 个 Bot：Dr. Know、谁是卧底 和 Harvest

> [!abstract]- 🖼 图片展示了大圣用Coze搓过的三个Bot，分别是Dr. Know、谁是卧
> 图片展示了大圣用Coze搓过的三个Bot，分别是Dr. Know、谁是卧底和Harvest。Dr. Know是一个信息检索Bot，类似极简版的Perplexity；谁是卧底是一个AI推理游戏，复杂度较高；Harvest是个人知识建构助理，可将Coze Bot连接到Notion数据库。图片与上下文紧密相关，直观呈现了大圣在Coze平台开发的Bot类型及功能，为听众了解其Bot开发经历提供了清晰示例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Smb6byuU7o4yGixZyEmc496XnTb) · `Smb6byuU7o4yGixZyEmc496XnTb`

- Dr. Know: https://www.coze.com/s/Zs8MUCQGU/（[[1.3 AI Agents (智能体)/2. Agent 共学快闪活动/Agent 搭建共学快闪 0523/5月23日 艾木分享 · 这也许是你一生中第一个Bot/5月23日 艾木分享 · 这也许是你一生中第一个Bot|5月23日 艾木分享 ｜ 这也许是你一生中第一个Bot]]）
- 谁是卧底: https://www.coze.com/s/Zs8MU9PGT/ （[[成为Agent工程师/Coze实战课项目/第四周：Multiagent之谁是卧底/04｜Multiagent之谁是卧底|04｜Multiagent之谁是卧底]]）
- Harvest: https://www.coze.com/s/Zs8MUkQPG/ （[[成为Agent工程师/Coze实战课项目/第五周：基于 Notion 连接器打造个人信息助理/05｜基于 Notion 连接器打造个人信息助理|05｜基于 Notion 连接器打造个人信息助理]]）

### 组织着一个498（+197）人的 [Coze 创作者社群](https://mp.weixin.qq.com/s/_mM7FG21tS2F3MZWPmgw9Q)

社群介绍：[一个程序员的AI社群运营心得](https://mp.weixin.qq.com/s/_mM7FG21tS2F3MZWPmgw9Q)

入群申请（申请要真诚，群主会筛选）：

> [!abstract]- 🖼 图片是一个二维码，位于文档中大圣介绍部分的入群申请处。二维码内有一个蓝色
> 图片是一个二维码，位于文档中大圣介绍部分的入群申请处。二维码内有一个蓝色箭头和绿色对勾的图标，周围有黑色线条装饰。下方有一个绿色圆形图标，内有白色图案。该二维码是入群申请的标识，申请时需真诚，群主会筛选，与上下文介绍的Coze创作者社群入群申请相关，方便有意愿加入社群的人员扫码申请。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/V5FSbF1BtogEe6x2326cSNuTnph) · `V5FSbF1BtogEe6x2326cSNuTnph`

# 二、课程预期声明

课程预期对齐：

- 二期课程是录播，所以教学内容已经准备好
- 不承诺变现，不承诺找到高薪工作，不承诺可以帮助落地企业级项目
- 本次课程会有部分编程相关的概念，我们会尽最大努力去讲解，但是最终能否听懂要看个人
- 集中答疑，日常答疑无法保证随叫随到，而且优先答疑课程相关内容，针对个人项目的问题不在服务范围内

我们的期望

- 我们讲Coze，又不仅仅是讲Coze，我们希望课程过后，无论出现怎样的智能体平台，你都能很快的上手
- 我们希望能通过这次课程改变你对AI的认知，结合自己的工作和生活场景找到一条能够持续学习和探索AI的路径，这条路径既能脚踏实地，又能仰望星空
- 成为Agent工程师不是一个噱头，工程师这个概念也与编程无关，它是一种能力，希望你在这门课程中可以掌握这种能力，为日后持续探索AI打下良好的基础

# 三、课程学习路径以及节奏

- 我们的课程是录播课，所以课程的文字教程+视频教程+团队空间都已经就绪
- 对于二期的学员，每周六都会有对应的飞书视频直播答疑，大家可以把这一周学习遇到的问题，在直播答疑时进行解决
- 我们的视频教程和文字教程非常详细，请大家不要跳着看，根据一期的经验，70%的问题都是因为不看课程视频导致的
- 每篇课程的前面都会有需要预先学习的内容，请大家务必首先掌握预先的知识点
- 等开始看课程视频之后，你会发现我们的课程信息密度非常高，希望大家可以保持自己的节奏，既不要操之过急，期望半个月就可以掌握所有内容，也不要自暴自弃，将课程放在收藏夹吃灰
- Coze有新功能出现后，我们会通过加餐的方式编写教程
- 在学习Coze的过程中，你可能需要一些前置的知识，比如提示词工程，大模型的基础概念等，如果你对这些概念有困惑，可以提前看下我们为大家准备的一个AI学习路径的文章：[大圣的AI学习路径3.0](https://axsppz4oyvj.feishu.cn/wiki/N1WUwd0QNiqZR0k0nEQcpORBnmf)

**课程目录串讲（请参考视频）**

# 四、如何学习和如何学编程（艾木 25 分钟）

> [!warning]- 📎 附件（`application/pdf`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/V6cHb04upoMTC4xCg5JcqtmSnng) · `V6cHb04upoMTC4xCg5JcqtmSnng`

# 五、针对课程的疑问
