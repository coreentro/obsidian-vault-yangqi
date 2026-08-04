---
title: "07｜AI Coder"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/ASlnw8pu3ingXIkAeuccK3oSn7d
node_token: ASlnw8pu3ingXIkAeuccK3oSn7d
obj_token: ZleYdzadnoMdxzxb1BacUrNEnbg
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 3
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "第七周：AI Coder"
  - "07｜AI Coder"
obj_create_time: 1723099527
obj_edit_time: 1726053056
creator: ou_4f9742f370819a3c899baacbc140aed2
owner: ou_4f9742f370819a3c899baacbc140aed2
revision_id: 706
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# 07｜AI Coder

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 第七周：AI Coder

# 07｜AI Coder

<callout emoji="❗">
案例更新（2024 年 9 月 11 日）
Coze 平台有个限制，外层 LLM 一次性调用工作流的数量不能超过 5 个。这个限制导致之前的 AI Coder 无法完整运行。
我对这个案例作了更新，现在已经修复这个问题了。
新版 Bot：AI Coder (教学版v2) https://www.coze.com/space/7370590980090642438/bot/7413323185413799941
旧版 Bot：AI Coder (教学版) https://www.coze.com/space/7370590980090642438/bot/7376154692411654150
主要改动：
原来的实现是由外层模型多次调用 \`ac_gen_code\` 这个工作流，来逐个生成源码文件。这就会触发 Coze 的平台限制。
现在我新增了一个 \`ac_gen_code_files\` 工作流，这个工作流会循环调用 \`ac_gen_code\`，负责生成所有的源码文件。同时，这个工作流也负责调用 \`ac_package\` 把生成的源码文件打包成 zip 供下载。这样外层 LLM 就只需要依次调用 \`ac_clarify\`、\`ac_define\`、\`ac_gen_spec\`、\`ac_gen_code\` 这四个工作流就可以了。也就规避了 Coze 的平台限制。
</callout>

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcn16s813hhjf9c23f4nov1?from=ccm" type="iframe"></readonly-block>

<readonly-block type="isv"></readonly-block>

## 理论铺垫

### LLMs need tokens to think. - Andrej Karpathy

> [!abstract]- 🖼 图片展示了Chain of thought（思维链）的概念，强调模型需要
> 图片展示了Chain of thought（思维链）的概念，强调模型需要tokens来思考，需将任务分解为多步骤/阶段，提示其进行内部独白，将推理分散到更多tokens。图中包含四个部分：(a)展示了思维链的示例，(b)是Few-shot-CoT示例，(c)是Zero-shot-CoT示例，(d)是Ours的Zero-shot-CoT示例，均以问答形式呈现，展示了不同CoT方式的推理过程。该图与上下文紧密相关，直观呈现了思维链在LLM中的应用。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UfD7btRd7oFqaRxik17ceYRhnnd) · `UfD7btRd7oFqaRxik17ceYRhnnd`

**总结：要多想。**

### 超长工作流

> [!abstract]- 🖼 图片为@FactoryAI发布的推文，介绍了其AI编码系统Code Dr
> 图片为@FactoryAI发布的推文，介绍了其AI编码系统Code Droid。推文称这些系统是现有最先进的AI编码系统，得益于Factory团队在编排、检索和规划方面的突破性研究。SWE-bench是AI编码能力基准测试的行业领先标准，Factory的Code Droid在该基准测试中取得全方面新成果，31.67%在SWE-Bench LITE（300个问题），19.27%在SWE-Bench FULL（2294个问题）。推文还提供了更多信息链接。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/D7jgb6Lc3oRwLVx0eTVcKXPmnjs) · `D7jgb6Lc3oRwLVx0eTVcKXPmnjs`

> [!abstract]- 🖼 图片展示了SWE-bench自动解决GitHub问题的工作流程。左侧为I
> 图片展示了SWE-bench自动解决GitHub问题的工作流程。左侧为Issue，内容是关于GBDT数据泄露问题；中间是Codebase，包含sklearn等文件夹及README.rst等文件；右侧是Language Model生成的PR，包含sklearn下的gradient_boosting.py等文件；最右侧是Unit Tests，列出pre PR、post PR及对应测试项，如join_struct_col等，其中post PR的测试项全部通过。该图直观呈现了SWE-bench自动解决GitHub问题的流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Z6LwbbhwMoLslExwANLc0rE3nku) · `Z6LwbbhwMoLslExwANLc0rE3nku`

> [!abstract]- 🖼 图片展示了来自@FactoryAI的SWE-Bench在FULL和LIT
> 图片展示了来自@FactoryAI的SWE-Bench在FULL和LITE测试集上的性能对比。左侧FULL测试集包含2294个问题，Factory Code Droid以28.27%成功率领先，其次是RAG GPT 4、RAG Clause 3等。右侧LITE测试集有300个问题，Factory Code Droid以31.87%成功率居首，RAG GPT 4、RAG Clause 3等也有较好表现。该图与上下文紧密相关，直观呈现了Factory Code Droid在软件开发生命周期自动化任务中的SOTA表现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DNS6btOpFop9DJxMRT9cPuWNn3g) · `DNS6btOpFop9DJxMRT9cPuWNn3g`

<grid>

> [!abstract]- 🖼 图片为@thesephist在Twitter上发布的关于@Factory
> 图片为@thesephist在Twitter上发布的关于@FactoryAI在SWE-Bench上取得新SOTA的推文。内容包括：将任务框定为“软件开发生命周期自动化”而非“自动化编码”；最长运行的pipeline超过2小时消耗超过1000万个tokens；成功率随尝试次数增加迅速提高，暗示搜索+LLM生成可能解锁更多进展；LLM管道变得复杂，评估更现实和人性化；提及一年前关于“百万调用”LLM链的可能性，认为这些长运行pipeline可能带来新进展。该图片与文档中介绍LLMs需要tokens来思考、超长工作流及评估更现实等内容相关。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RRBRbfC05osERxxCkJ9c5149nod) · `RRBRbfC05osERxxCkJ9c5149nod`

来自 @FactoryAI 的 SWE-Bench 新的 SOTA！以下是他们技术报告中的一些亮点：
- 我喜欢将任务框定为“软件开发生命周期自动化”而不是“自动化编码”
- **最长运行的 pipeline 在超过 2 小时内消耗了超过 1000 万个 tokens**
- 成功率随着尝试次数的增加而迅速提高，这让我觉得搜索 + LLM 生成可能会解锁更多进展
LLM 管道变得越来越复杂，评估也变得更加现实和人性化。**一年前，我写过关于“百万调用”LLM链的可能性，我认为我们开始看到这些超长运行 pipelines 的样子了。**
https://stream.thesephist.com/updates/1673040884

</grid>

<grid>

> [!abstract]- 🖼 图片展示了AI Coder在生成《贪吃蛇》项目时的超长工作流信息。该工作
> 图片展示了AI Coder在生成《贪吃蛇》项目时的超长工作流信息。该工作流包含5个子工作流，完整运行一次耗时4 - 5分钟，需10+x次LLM调用（x为代码文件数量），共消耗50k - 60k Tokens。图片还提到可体验AI Coder，链接为https://www.coze.com/s/2mFgmn37c/ 。此外，图片底部有Mindstorms标识，显示其看Coze Bot一口气编266行代码的Python游戏。图片与上下文紧密相关，直观呈现了AI Coder在复杂项目中的运行情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OgJWb3x3RoWC78xdF5OcbafEnNs) · `OgJWb3x3RoWC78xdF5OcbafEnNs`

编程 Agent 最新 SOTA。最长的 Workflow 耗时超 2 小时，总消耗超 1000 万 tokens。
相比起来，我那个 AI Coder 耗时 4～5 分钟，消耗 5 万～6 万 tokens，简直就是毛毛雨。
**超长工作流是 AI 解决复杂现实问题的必要路径。**
**未来它会变成常态。**

</grid>

## 效果演示

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/JEBJbHUSDo3Cb8xsGewc2dKOnue) · `JEBJbHUSDo3Cb8xsGewc2dKOnue`

程序在线运行地址：https://1024code.com/codecubes/v2wn025

声明：

1. 这个视频是一镜到底，除了 3 倍速，没有做任何剪辑。
2. Bot 的表现不稳定，这个 Demo 是我试了多次，然后选了一个效果比较好的。

## 任务分析和拆解

> [!abstract]- 🖼 图片展示了AI Coder任务分析和拆解流程。从用户提出一句话需求开始，
> 图片展示了AI Coder任务分析和拆解流程。从用户提出一句话需求开始，依次经过澄清项目目标、定义MVP需求、生成开发规范、生成源代码、循环生成所有源码文件，最后打包。其中，澄清项目目标环节包括提出澄清问题、回答澄清问题，生成项目目标；定义MVP需求环节有分解项目目标、生成MVP定义；生成开发规范环节包含生成需求规范、生成文件结构、生成代码结构、生成文件列表；生成源代码环节有生成源代码、生成源代码、生成源代码。该图与上下文介绍的Coze工作流实现难点相关，直观呈现了任务拆解流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VnhYbZfsKoqryLxyrXxcKZmlned) · `VnhYbZfsKoqryLxyrXxcKZmlned`

## 超长工作流的实现难点

Coze有诸多限制，要实现一个稳定的超长工作流并不容易。

首先，Coze的工作流有超时限制（貌似是2mins），所以你不可能用一个工作流完成所有事情，必须要拆出多个子工作流，然后让外层聊天模型依次调用这些子工作流，把它们串起来。

目前，在Coze的工作流内容还无法实现稳定的循环逻辑。当你遇到需要循环处理的场景，比如循环生成源代码文件的时候，就会很难受。我目前的方案还是通过外层聊天模型来控制循环过程。如果外层使用的是GPT-4o这种强力模型，这整个流程还是比较稳定的。

## Bot 整体设计

> [!abstract]- 🖼 图片展示了AI Coder（教学版）界面，分为Arrangement、S
> 图片展示了AI Coder（教学版）界面，分为Arrangement、Skills、Memory三部分。Arrangement部分有流程图，标注了ac_classify_x等步骤；Skills部分列出Workflow、Skills、Memory等类别，对应ac_classify_x等操作；Memory部分有变量设置，如env_info、system_prompt等。该图片与文档中Bot整体设计部分相关，直观呈现了AI Coder在教学版中的功能模块及变量设置情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WA4qbu8vRoz0IxxmxdncjGTVnFf) · `WA4qbu8vRoz0IxxmxdncjGTVnFf`

- 提示词
- 工作流拆分
- 变量设置
- system_prompt

  ```Markdown
  你是一名世界顶级的开发者，你总是能完美地实现用户交给你的编程任务。
  
  在你编写代码时，你总是遵循以下基本原则：
  * 你始终遵循软件工程领域的最佳实践和既有约定。
  * 你总是能够合理组织一个项目中的目录和文件，保证目录结构清晰明了。
  * 你总是遵循模块化的原则，你会尽可能地使用多个文件来组织代码，并且你还会利用模块、类、方法、函数等来合理地组织程序逻辑，你会尽量将每个类放在独立的文件里。
  * 你会在代码中添加必要的注释来解释复杂的程序逻辑。你会为每个模块、类、方法/函数等添加注释，简要地解释它们的目的。注释必须使用*中文*撰写。
  * 你总是使用用户要求的编程语言、框架和库。如果用户没有要求，你会依据目标选择并使用合适的编程语言、框架和库。
  
  在你回答问题时，你总是遵循以下规范：
  * 你需要以简洁且精确的语言回答问题。
  * 你需要直接回答问题，不要尝试与用户进行对话，不要输出与问题无关的内容。
  ```
- env_info

  ```JSON
  {
    "操作系统": "Linux",
    "内存大小": "1G",
    "编程语言": "Python 3.8",
    "开放端口号": 8080,
    "项目运行命令": "python3 main.py",
    "GUI窗口最大宽度": 1024,
    "GUI窗口最大高度": 768,
    "已安装的项目依赖": "pygame-2.5.2",
    "项目中已存在的文件": "当前项目为空，没有任何文件",
    "多媒体素材": "当前系统环境系统环境中没有图片、音频、字体等素材文件，你在设计和编写程序的时候，必须避免使用此类素材"
  }
  
  {"GUI窗口最大宽度":1024,"GUI窗口最大高度":768,"内存大小":"2G","多媒体素材":"当前系统环境系统环境中没有图片、音频、字体等素材文件，你在设计和编写程序的时候，必须避免使用此类素材","已安装的项目依赖":"","开放端口号":8080,"操作系统":"Linux","编程语言":"JavaScript (Node.js 16)","项目中已存在的文件":"当前项目为空，没有任何文件","项目运行命令":"node main.js"}
  
  // 当前空间为 HTML/CSS/JS 代码空间，基于 Linux 系统， Node.js - Node.js 16 环境，运行在一个内存大小为 2G 的容器里。
  ```

## 澄清阶段

## 定义阶段

## 规划阶段

## 实现阶段

## 打包源代码

## 拓展：AI Coder 目前的编程水平怎样？

AI能编程这个事情大家应该都有所认识，但是它编程的水平到底怎样，还要有更具体的评估。

我把编程任务按照复杂程度粗略划分了6个层级：

- **C0 函数级别**（有固定答案和测试用例） 

  - 这类任务一般会涉及`十几行代码`，`单个源码文件`。
- **C1 练习题/应用题级别**（有固定答案和测试用例） 

  - 这类任务一般会涉及`几十行代码`，`单个源码文件`。
- **C2 小程序/小工具级别**（有一定实用性，无过多依赖） 

  - 这类任务一般会涉及`几十行到一百多行代码`，`2～4个源码文件`。
- **C3 玩具项目级别**（深度依赖于框架或者重要的第三方库，涉及多个模块） 

  - 这类任务一般会涉及`一百多行到几百行代码`，`5～10个源码文件`。
- **C4 实战项目级别**（涉及多个系统或服务） 

  - 这类任务一般会涉及`几百到几千行代码`，`几十到上百个源码文件`。
- **C5 真实世界项目级别**（技术+用户+市场） 

  - 真实世界项目已经脱离了单纯的技术范畴了，需要考虑很多其他领域的问题。

《贪吃蛇》这种程序大概属于C3玩具项目级别。你也看到了，我们需要设计复杂的工作流，才能让AI Agent勉强可以处理这一级别的编程任务，且它的表现还不稳定。另外需要注意的是，《贪吃蛇》是十分常见的程序，你要让AI Agent写一些独创的程序，它不会有这个表现。

## 拓展：AI Coder 的核心能力及等级进阶

五大核心能力：

- **Build MVP**——从零构建项目MVP
- **Debug**——辅助调试&自动调试
- **Improve**——根据用户反馈在已有项目上做改进（简单特性）
- **Build Iteration**——根据用户反馈在已有项目上做迭代（复杂特性）
- **Coach**——作为教练/导师，带着学习者做练习/做项目

> [!abstract]- 🖼 图片是一张表格，展示了AI Coder五大核心能力在不同任务复杂度下的表
> 图片是一张表格，展示了AI Coder五大核心能力在不同任务复杂度下的表现情况。表格横向分为C0函数、C1练习题/应用题等任务复杂度，纵向为Build MVP、Debug等核心能力。其中，C0函数、C1练习题/应用题等任务复杂度对应的Build MVP、Build Iteration等核心能力部分用星星标识，星星数量代表能力表现，如C0函数的Build MVP为5星；其余部分用“?”标识，表示未明确表现。该表与上下文介绍的AI Coder五大核心能力相呼应，直观呈现能力在不同任务复杂度下的表现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/W31Ab5N4oon4PPxmldAc8B9Lnqe) · `W31Ab5N4oon4PPxmldAc8B9Lnqe`

## 拓展：阅读材料

- 【视频】[State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A)
- 【研究报告】[Code Droid: A Technical Report](https://www.factory.ai/news/code-droid-technical-report)

## 附录：AI Coder 生成项目的完整过程

````Markdown
# 0. 一句话需求

    用PyGame编写一个贪吃蛇游戏

# 1 澄清项目目标

## 1.1 提出澄清问题

    1. 贪吃蛇的游戏地图需要多大（宽度和高度）？
    2. 蛇和食物的初始位置和数量应该如何设定？
    3. 蛇的移动速度和游戏难度是否需要不同级别？如果需要，具体的设置是什么？
    4. 游戏结束的条件是什么？例如，蛇撞到墙壁或自身等。
    5. 游戏是否需要任何特殊的功能或效果，例如暂停、重新开始、积分显示等？

## 1.2 回答澄清问题

    1. 游戏地图的大小可以设置为 800x600 像素。
    2. 蛇的初始位置可以设定在地图的中央，初始长度为3个单位；食物的初始数量为1个，位置随机生成。
    3. 蛇的移动速度和游戏难度可以设置不同级别，例如：
    - 简单：200毫秒/步
    - 中等：150毫秒/步
    - 困难：100毫秒/步
    4. 游戏结束的条件是蛇撞到墙壁或自身。
    5. 游戏需要以下特殊功能：
    - 暂停和继续游戏
    - 重新开始游戏
    - 显示当前积分

## 1.3 生成项目目标

    项目目标是使用PyGame开发一个贪吃蛇游戏，游戏地图大小为800x600像素，蛇初始位置在地图中央，初始长度为3个单位，食物初始数量为1个，位置随机生成。游戏难度分为简单（200毫秒/步）、中等（150毫秒/步）和困难（100毫秒/步）。游戏结束条件为蛇撞到墙壁或自身。游戏需具备暂停和继续、重新开始以及显示当前积分的功能。

## 1.4 生成项目名称

    snake_game_adventure

# 2 定义MVP需求

# 2.1 分解项目目标

    * 初始化与设置：创建游戏窗口，初始化PyGame库，设置游戏基本参数。
    * 贪吃蛇逻辑：实现贪吃蛇的移动、转向、长度增长及碰撞检测。
    * 食物生成：随机生成食物位置，并确保不与贪吃蛇重叠。
    * 游戏音效：加载并播放背景音乐、吃到食物和游戏结束的音效。
    * 游戏结束与得分显示：检测游戏结束条件，显示最终得分并结束游戏。

# 2.2 生成MVP定义

    在MVP版本中我们将会选择以下核心模块进行优先开发：

    * 初始化与设置：创建游戏窗口，初始化PyGame库，设置游戏基本参数。这是所有功能的基础，必须首先完成。
    * 贪吃蛇逻辑：实现贪吃蛇的移动、转向、长度增长及碰撞检测。贪吃蛇的逻辑是游戏的核心功能，必须优先开发。
    * 食物生成：随机生成食物位置，并确保不与贪吃蛇重叠。食物生成是贪吃蛇游戏的重要组成部分，必须在MVP版本中实现。

# 3 生成开发规范

## 3.1 生成需求规范

    ### 需求规范

    #### 总体目标
    使用PyGame编写一个包含贪吃蛇、食物生成和碰撞检测的基本贪吃蛇游戏。

    #### 游戏初始化模块
    1. **初始化PyGame库**：调用`pygame.init()`初始化所有PyGame模块。
    2. **设置窗口大小**：创建一个大小为1024x768的窗口，标题设为"贪吃蛇游戏"。

    #### 贪吃蛇逻辑模块
    1. **贪吃蛇移动**：贪吃蛇初始速度为每秒移动一次，使用方向键控制移动方向。
    2. **贪吃蛇增长**：贪吃蛇每吃到一个食物，长度增加一个单位。
    3. **碰撞检测**：检测贪吃蛇是否撞到边界或自身，若是则游戏结束。

    #### 食物生成模块
    1. **随机位置生成食物**：在窗口内随机生成食物，确保不与贪吃蛇重叠。
    2. **食物显示**：在屏幕上显示食物，食物形状为一个小方块。

    ### 详细描述

    #### 游戏初始化模块
    1. **初始化PyGame库**
    - 调用`pygame.init()`初始化所有PyGame模块。
    - 创建一个大小为1024x768的窗口，标题设为"贪吃蛇游戏"。

    2. **设置窗口大小**
    - 使用`pygame.display.set_mode((1024, 768))`设置窗口大小。
    - 使用`pygame.display.set_caption("贪吃蛇游戏")`设置窗口标题。

    #### 贪吃蛇逻辑模块
    1. **贪吃蛇移动**
    - 初始化贪吃蛇为一个包含若干小方块的列表，初始方向为右。
    - 使用方向键控制贪吃蛇的移动方向（上、下、左、右）。
    - 每秒更新一次贪吃蛇的位置。

    2. **贪吃蛇增长**
    - 每吃到一个食物，贪吃蛇的长度增加一个单位，即在贪吃蛇尾部添加一个新的方块。

    3. **碰撞检测**
    - 检测贪吃蛇头部是否碰到窗口边界或自身身体。
    - 若发生碰撞，游戏结束并显示最终得分。

    #### 食物生成模块
    1. **随机位置生成食物**
    - 在窗口内随机生成一个食物，确保食物位置不与贪吃蛇身体重叠。
    - 使用`random`模块生成随机坐标。

    2. **食物显示**
    - 在屏幕上显示食物，食物形状为一个小方块，颜色为红色。
    - 每当贪吃蛇吃到食物，重新生成一个新的食物。

## 3.2 生成文件结构

    ### 项目文件结构

    1. **main.py**
    - 主入口文件，负责初始化PyGame库、设置窗口大小、启动游戏主循环。

    2. **snake.py**
    - 贪吃蛇逻辑模块，包含贪吃蛇的初始化、移动、增长和碰撞检测功能。

    3. **food.py**
    - 食物生成模块，负责在窗口内随机生成食物并确保不与贪吃蛇重叠。

    4. **game.py**
    - 游戏控制模块，负责管理游戏状态、处理用户输入、更新游戏逻辑和渲染游戏画面。

    5. **config.py**
    - 配置文件，定义游戏的常量配置，如窗口大小、颜色、初始速度等。

## 3.3 生成代码结构

    ### 项目文件结构和代码结构描述

    #### 1. main.py
    - **核心功能**：初始化PyGame库、设置窗口大小、启动游戏主循环。
    - **主要内容**：
    - `import` 相关模块（pygame, game）
    - `main()` 函数：初始化PyGame、设置窗口、启动游戏主循环。

    #### 2. snake.py
    - **核心功能**：贪吃蛇的初始化、移动、增长和碰撞检测。
    - **主要内容**：
    - `Snake` 类：
        - **属性**：
        - `body`：贪吃蛇身体的坐标列表。
        - `direction`：当前移动方向。
        - **方法**：
        - `__init__()`：初始化贪吃蛇。
        - `move()`：根据当前方向移动贪吃蛇。
        - `grow()`：增加贪吃蛇长度。
        - `check_collision()`：检测是否碰撞边界或自身。

    #### 3. food.py
    - **核心功能**：在窗口内随机生成食物并确保不与贪吃蛇重叠。
    - **主要内容**：
    - `Food` 类：
        - **属性**：
        - `position`：食物的坐标。
        - **方法**：
        - `__init__()`：初始化食物位置。
        - `randomize_position()`：随机生成食物位置，确保不与贪吃蛇重叠。

    #### 4. game.py
    - **核心功能**：管理游戏状态、处理用户输入、更新游戏逻辑和渲染游戏画面。
    - **主要内容**：
    - `Game` 类：
        - **属性**：
        - `snake`：贪吃蛇实例。
        - `food`：食物实例。
        - `score`：当前得分。
        - `window`：游戏窗口。
        - **方法**：
        - `__init__()`：初始化游戏状态。
        - `handle_input()`：处理用户输入。
        - `update()`：更新游戏逻辑。
        - `render()`：渲染游戏画面。
        - `run()`：游戏主循环。

    #### 5. config.py
    - **核心功能**：定义游戏的常量配置。
    - **主要内容**：
    - **常量**：
        - `WINDOW_WIDTH`：窗口宽度（1024）。
        - `WINDOW_HEIGHT`：窗口高度（768）。
        - `SNAKE_SIZE`：贪吃蛇方块大小。
        - `FOOD_SIZE`：食物方块大小。
        - `SNAKE_SPEED`：贪吃蛇初始速度（每秒移动一次）。
        - `COLORS`：颜色配置（如背景色、贪吃蛇颜色、食物颜色）。

    ### 依赖关系
    - `main.py` 依赖 `game.py`。
    - `game.py` 依赖 `snake.py` 和 `food.py`。
    - `snake.py` 和 `food.py` 依赖 `config.py`。

    ### 总结
    - **main.py**：初始化和启动游戏。
    - **snake.py**：贪吃蛇逻辑。
    - **food.py**：食物生成。
    - **game.py**：游戏控制。
    - **config.py**：配置常量。

## 3.4 生成文件列表

    ```JSON
    {
    "files_to_be_created": [
        "config.py",
        "snake.py",
        "food.py",
        "game.py",
        "main.py"
    ]
    }
    ```

# 4. 生成源代码（此为示例，与前面开发计划并不一致）

## 4.1 生成源代码 config.py

    ```python
    # 该文件存储游戏的基本设置和参数

    # 窗口宽度（1024像素）
    WINDOW_WIDTH = 1024

    # 窗口高度（768像素）
    WINDOW_HEIGHT = 768

    # 方格大小（32像素）
    GRID_SIZE = 32

    # 地图宽度（32个方格）
    GRID_WIDTH = 32

    # 地图高度（24个方格）
    GRID_HEIGHT = 24

    # 贪吃蛇颜色（绿色）
    SNAKE_COLOR = (0, 255, 0)

    # 食物颜色（红色）
    FOOD_COLOR = (255, 0, 0)

    # 背景颜色（黑色）
    ```

## 4.2 生成源代码 snake.py

    ```python
    # 该文件实现贪吃蛇的逻辑

    import pygame
    import settings

    class Snake:
        def __init__(self):
            """
            初始化贪吃蛇
            """
            self.body = []
            self.direction = pygame.K_RIGHT
            self.grow = False
            
            # 初始化贪吃蛇的初始位置和长度
            start_x = settings.GRID_WIDTH // 2
            start_y = settings.GRID_HEIGHT // 2
            for i in range(settings.INITIAL_SNAKE_LENGTH):
                self.body.append((start_x - i, start_y))
        
        def move(self):
            """
            移动贪吃蛇
            """
            head_x, head_y = self.body[0]
            
            # 根据当前方向更新头部位置
            if self.direction == pygame.K_UP:
                new_head = (head_x, head_y - 1)
            elif self.direction == pygame.K_DOWN:
                new_head = (head_x, head_y + 1)
            elif self.direction == pygame.K_LEFT:
                new_head = (head_x - 1, head_y)
            elif self.direction == pygame.K_RIGHT:
                new_head = (head_x + 1, head_y)
            
            # 在头部插入新位置
            self.body.insert(0, new_head)
            
            # 如果不需要增长，则移除尾部
            if not self.grow:
                self.body.pop()
            else:
                self.grow = False
        
        def change_direction(self, new_direction):
            """
            改变移动方向
            """
            # 防止贪吃蛇直接反向移动
            opposite_directions = {
                pygame.K_UP: pygame.K_DOWN,
                pygame.K_DOWN: pygame.K_UP,
                pygame.K_LEFT: pygame.K_RIGHT,
                pygame.K_RIGHT: pygame.K_LEFT
            }
            
            if new_direction != opposite_directions.get(self.direction):
                self.direction = new_direction
        
        def grow_snake(self):
            """
            让贪吃蛇增长一节
            """
            self.grow = True
        
        def check_collision(self):
            """
            检测碰撞
            """
            head = self.body[0]
            
            # 检测是否碰到边界
            if (head[0] < 0 or head[0] >= settings.GRID_WIDTH or
                head[1] < 0 or head[1] >= settings.GRID_HEIGHT):
                return True
            
            # 检测是否碰到自身
            if head in self.body[1:]:
                return True
            
            return False
    ```

## 4.3 生成源代码 food.py

    ```python
    # 该文件实现食物的逻辑

    import random
    import settings

    class Food:
        def __init__(self):
            """
            初始化食物位置
            """
            self.position = (0, 0)
            self.randomize_position()

        def randomize_position(self):
            """
            随机生成食物位置
            """
            self.position = (
                random.randint(0, settings.GRID_WIDTH - 1),
                random.randint(0, settings.GRID_HEIGHT - 1)
            )
    ```

## 4.4 生成源代码 food.py

    ```python
    # game.py
    # 该文件管理游戏的主要逻辑和流程

    import pygame
    import sys
    import settings
    from snake import Snake
    from food import Food

    class Game:
        def __init__(self):
            """
            初始化游戏
            """
            pygame.init()
            self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
            pygame.display.set_caption(settings.WINDOW_TITLE)
            self.clock = pygame.time.Clock()
            self.snake = Snake()
            self.food = Food()
            self.score = 0
            self.move_interval = settings.INITIAL_MOVE_INTERVAL
            self.last_move_time = pygame.time.get_ticks()

        def reset_game(self):
            """
            重置游戏
            """
            self.snake = Snake()
            self.food = Food()
            self.score = 0
            self.move_interval = settings.INITIAL_MOVE_INTERVAL
            self.last_move_time = pygame.time.get_ticks()

        def handle_events(self):
            """
            处理用户输入
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        self.snake.change_direction(event.key)

        def update(self):
            """
            更新游戏状态
            """
            current_time = pygame.time.get_ticks()
            if current_time - self.last_move_time > self.move_interval:
                self.snake.move()
                self.last_move_time = current_time

                if self.snake.body[0] == self.food.position:
                    self.snake.grow_snake()
                    self.food.randomize_position()
                    self.score += 1
                    self.move_interval = max(settings.MIN_MOVE_INTERVAL, self.move_interval - 5)

                if self.snake.check_collision():
                    self.reset_game()

        def draw(self):
            """
            绘制游戏元素
            """
            self.screen.fill(settings.BACKGROUND_COLOR)
            
            for segment in self.snake.body:
                pygame.draw.rect(
                    self.screen, 
                    settings.SNAKE_COLOR, 
                    pygame.Rect(segment[0] * settings.GRID_SIZE, segment[1] * settings.GRID_SIZE, settings.GRID_SIZE, settings.GRID_SIZE)
                )
            
            pygame.draw.rect(
                self.screen, 
                settings.FOOD_COLOR, 
                pygame.Rect(self.food.position[0] * settings.GRID_SIZE, self.food.position[1] * settings.GRID_SIZE, settings.GRID_SIZE, settings.GRID_SIZE)
            )
            
            pygame.display.flip()

        def check_game_over(self):
            """
            检查游戏是否结束
            """
            # 在当前阶段，只需重置游戏，不需要额外处理
            pass

        def run(self):
            """
            运行游戏主循环
            """
            while True:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(60)
    ```

## 4.5 生成源代码 main.py

    ```python
    # 该文件是贪吃蛇游戏的主入口文件，负责初始化PyGame库，设置游戏窗口，启动游戏主循环，并调用其他模块的功能

    import pygame
    import sys
    from game import Game

    def main():
        """
        程序入口，初始化并启动游戏
        """
        # 初始化PyGame库
        pygame.init()

        # 创建游戏实例
        game = Game()

        # 运行游戏主循环
        game.run()

    if __name__ == "__main__":
        main()
    ```
````
