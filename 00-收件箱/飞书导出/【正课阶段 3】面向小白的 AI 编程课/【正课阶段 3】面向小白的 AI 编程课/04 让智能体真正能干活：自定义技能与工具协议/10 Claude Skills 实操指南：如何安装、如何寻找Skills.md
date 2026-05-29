---
title: "Claude Skills 实操指南：如何安装、如何寻找Skills"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/DyMPwfQHuiA2ghkoJ6FctM18n8f"
node_token: "DyMPwfQHuiA2ghkoJ6FctM18n8f"
obj_type: "docx"
document_id: "JBmjd1T8toXPxHxlcGJcJTYpnpf"
revision_id: "47"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/DyMPwfQHuiA2ghkoJ6FctM18n8f>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>Claude Skills 实操指南：如何安装、如何寻找Skills</title>

大家好，我是大圣



这节课讲解下Skills应该在那里用，去哪里找



# 一、Skills不是Claude Code的专利



## 1）一个类比：Skills就像USB接口



你家里的 U 盘，能插在联想电脑上，也能插在苹果电脑上，还能插在电视机上



因为 USB 是一个**接口标准**，不是联想发明的专属功能。只要设备支持 USB 接口，就能读取 U 盘里的内容



Skills 也是一样的道理



Anthropic 这家公司定义了一套规范：**文件夹该怎么命名、SKILL.md 该怎么写、目录结构该怎么组织**



这套规范是公开的。任何 AI 工具、任何平台，只要愿意按照这套规范去读取和解析，就能支持 Skills



所以这个认知首先必须清楚



<callout emoji="✨">
- **Skills 不是 Claude Code 的功能**，而是一套开放的文件规范
- **Claude Code 只是第一个支持这套规范的工具**，但不是唯一一个
- 你在 Claude Code 里创建的 Skill，拿到其他支持这套规范的平台上，照样能用
</callout>



## 2）目前支持Skills的主流平台



2025年10月份诞生的Skills，短短2个月后，Anthropic 就正式宣布将它发布为开放标准



Skills 这套规范正在快速被各大平台采纳。目前主流的 AI 工具和Agent平台，大部分都已经支持或者正在适配。



这些工具（主要是IDE/CLI）在Skills的安装和使用流程上大差不差，**区别主要在于Skills的安装路径**



比如我列举几家工具给大家感受下

<sheet sheet-id="P7rIyG" token="LcPisdzJFhw3g7t3LgGcUQS2nEJ"></sheet>



而我们比较熟悉和常用的几家工具：

<sheet sheet-id="kCCg8M" token="LcPisdzJFhw3g7t3LgGcUQS2nEJ"></sheet>



## 3）一个重要认知：效果 = 模型能力 \* 平台适配



在你选平台之前，有一个认知必须先建立：



<callout emoji="✨">
**同样一个 Skill，换个模型、换个平台，效果可能差很多**
</callout>



第一个核心逻辑：Skills 本质上是一本给 AI 大脑的操作手册。手册写得再好，大脑理解不了，也白搭



**决定效果的第一因素：模型能力**



SKILL.md 里写了工作流程、规则约束、输出规范，模型要能**真正理解**这些指令，并且**准确执行**，才能出好效果



目前来看，Claude Opus 系列（Anthropic 最强的模型）对 Skills 的理解和执行能力是最好的。



这很好理解：Skills 这套规范就是 Anthropic 自己定义的，他们的模型天然对这套"语言"最熟悉



如果你换一个能力稍弱的模型，比如扣子平台默认的豆包模型，同样的 Skill 效果就可能打折扣。



不是 Skill 有问题，是大脑理解不了手册



**决定效果的第二因素：平台适配程度**



即使你在 Cherry Studio 上也选了 Claude Opus 4 模型，效果大概率也比在 Claude Code 原生平台上稍差一点



因为Claude Code本身就是一个强大的智能体，它不只是一个简单的工具



**但请注意：不用去纠结具体差多少**



这个差距很难量化，也没必要量化。而且千万不要问我为什么，我不是工具测评博主



你只需要记住一个大致的排序：



**效果天花板：Claude Code + Claude Opus 模型（原生平台 + 最强模型）**



至于模型和平台到底哪个对Skills的执行影响更大，我的理解是模型 > 平台



比如在2026年2月21号我的测试发现：



<callout emoji="✨">
我有一个Skills，在Cherry Studio平台，只有Claude Opus系列模型才能让他准确执行
</callout>



# 二、Skills的安装方式



一个非常实际的问题：**我找到了一个 Skill，怎么把它装到我的工具里？**



这一小节我们用一个真实的Skill做演示，把主流的安装方式走一遍



## 1）先拿到一个示例的Skill



我们用 Anthropic 官方开源的 **skill-creator** Skill 来做演示



> *🔗 官方 Skills 仓库：*[*https://github.com/anthropics/skil*](https://github.com/anthropics/skills)[*。*](https://github.com/anthropics/skills)

[*ls*](https://github.com/anthropics/skills)



<callout emoji="✨">
为什么选这个skill？它的作用极其重要，它是用来帮我们去创建skill的skill
</callout>



## 2）第一种：手动安装（强烈建议至少走一遍）



<figure view-type="Preview"><source mime="video/mp4" origin-height="2144.000000" origin-width="3824.000000" token="KLscboK88oY0EuxCq1JcHxoynXd"/></figure>



**手动安装的核心逻辑就一句话：把 Skill 文件夹放到指定位置**



关于Skill的理论篇讲过，指定位置就是 `.claude/skills/`。不记得的回去翻一下



**第一步：创建Skills的文件夹**



由于这个skill我想安装在**用户级别下（全局）**，因此需要在用户根目录下创建目录



<sheet sheet-id="D4qCqF" token="LcPisdzJFhw3g7t3LgGcUQS2nEJ"></sheet>



比如我是苹果电脑，我的目录是：



```Bash
/Users/lmh/.claude/skills
```



**注意**：`.claude` 是隐藏文件夹，默认看不到



- **macOS 显示隐藏文件**：在 Finder 中按 `Command + Shift + .`（英文句号）
- **Windows 显示隐藏文件**：打开文件资源管理器 → 顶部「查看」→ 勾选「隐藏的项目」



<callout emoji="✨">
*💡 不知道自己的用户名？打开终端输入 `whoami`，显示的就是*
</callout>



![](https://feishu.cn/file/MOGUbuqZNoBRGFxQ9mBcQl47nuh)



**第二步：下载Skill文件**



去 GitHub 上下载。两种方式



第一种方式：下载整个git项目，里面包含了多种Skill



访问 [https://github.com/anthropics/skills](https://github.com/anthropics/skills) ，点击绿色的 **Code** 按钮 → **Download ZIP**



![](https://feishu.cn/file/Mhn0bA88ioMNPHxaAPicKSd7nAb)



然后解压缩，找到你需要的那个Skill，将其放到合适的目录下



第二种方式：利用DownGit的在线工具，只下载某个目录



如果你不想下载整个仓库（里面有 16 个 Skill，你只要 1 个），可以用 **DownGit** 这个在线工具



1. 访问：https://downgit.github.io/
2. 粘贴 Skill 文件夹的 GitHub 链接，比如：https://github.com/anthropics/skills/tree/main/skills/skill-creator
3. 点击Download，会得到一个Zip包，解压缩即可
4. 将其放到～/.claude/skills/ 下面



**第三步：确认目录层级**



这一步很关键，很多人装完不生效就是因为层级搞错了



```Bash
✅ 正确的层级：
~/.claude/skills/skill-creator/SKILL.md

❌ 错误的层级（多了一层）：
~/.claude/skills/skills/frontend-design/SKILL.md

❌ 错误的层级（少了一层）：
~/.claude/frontend-design/SKILL.md
```



## 3）第二种：让AI帮你安装



<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1922.000000" token="RoXSbsn0CoEgkwxFMJXc2c21nqg"/></figure>



这种方式，我相信大家都不陌生了，就是让AI帮你做任何事情



你可以给你的Claude Code发这样一句话



```Bash
帮我在当前项目安装 skill-creator 这个 Skill，
项目地址是：https://github.com/anthropics/skills
```



AI 会自动去下载、放到正确的目录、完成安装



**但要注意**：这种方式不是每次都能成功，可以把它当作一个快捷方式，而不是唯一方式。



万一没装对，你还是得知道手动怎么装（所以方式二一定要会）



## 4）第三种：用第三方工具帮你安装



<figure view-type="Preview"><source mime="video/mp4" origin-height="2144.000000" origin-width="3828.000000" token="UmBwbnH65o35kEx2XO7cw5otngc"/></figure>



现在市面上有几十种 AI 编程助手（Claude Code、Cursor、Codex、Cline、Windsurf 等等），它们都支持Skills的安装，但同时它们各自把技能文件存放在**不同的目录**下，例如：



<sheet sheet-id="h38kpX" token="LcPisdzJFhw3g7t3LgGcUQS2nEJ"></sheet>



Vercel 官方出了一个工具叫 **add-skill**，专门解决这个问题：



**这个工具统一管理了 40+ 种 AI 编程助手的技能安装**，你不需要手动去搞清楚每个助手的目录结构



> github的地址：*🔗* [*https://github.com/vercel-labs/add-skill*](https://github.com/vercel-labs/add-skill)



它能做什么：



- **指定装到哪个工具**：支持几乎所有主流 AI 编程工具
- **指定生效范围**：全局或项目
- **指定 Skill 来源**：GitHub 仓库地址，甚至仓库里的某个具体 Skill



**这个工具适合已经在用多个 AI 编程工具的进阶用户，如果你目前只用一个工具，方式一或方式二就够了**



安装某个Skills有如下几种方式：



```Markdown
# 安装仓库里的【所有技能】（交互式选择）
npx skills add anthropics/skills

# 只安装仓库里的【某一个技能】
npx skills add anthropics/skills --skill skill-creator

# 只安装仓库里的【某个目录下的技能】
npx skills add https://github.com/anthropics/skills/tree/main/skills/skill-creator

# 先看看仓库里有哪些技能（不安装）
npx skills add anthropics/skills --list
```



# 三、如何找到优质的Skills



<figure view-type="Preview"><source mime="video/mp4" origin-height="2144.000000" origin-width="3824.000000" token="JK0ibQw6To9K1NxrRbGcYaqFnic"/></figure>



<callout emoji="✨">
-- 腾讯出的SkillHub，据说更适合中国宝宝体质  
https://skillhub.tencent.com/  
  
https://github.com/BehiSecc/awesome-claude-skills  
  
https://skillsmp.com/zh  
  
https://github.com/yusufkaraaslan/Skill_Seekers  
  
https://github.com/anthropics/skills/tree/main/skills  
  
-- 小龙虾的skills，应该同样适用于claude Code  
https://clawhub.ai/skills?sort=downloads
</callout>





# 写在最后



有一段话我想分享给大家，希望能给你带来一些启发（关于小龙虾的，同样适用于Skill）



<callout emoji="✨">
最近2群里面讨论，自己费尽心思安装了小龙虾，看到网上铺天盖地的skill，但是自己好像都用不起来
然后就跟龙虾聊天，聊着聊着欠费了
就这个现象，我想谈一下自己的看法。
第一点，我们可以在网上找到一些使用龙虾的最佳实践，但一般都是工具层的，没有人能给你业务层的最佳实践
第二点：你需要思考一下，当前真的需要安装龙虾吗？Cherry studio加一个顶级模型，你玩明白没有？
Claude code加一堆skill，你玩明白了没有
很多人说龙虾可以帮我爬数据，那OK，各种浏览器插件本身就具有爬虫能力，你玩明白了没有
----
我想表达的是：越成熟的工具，本身就是封装了一些底层逻辑，所有工具都是为业务服务的，业务不是只有一键自动化就能跑通。
你手动编排多个工具完成业务也叫跑通
如果无法手动编排多个工具跑通业务流，安装了龙虾确实不会有太大的用处，你安装了claude code之后也不会有太大的用处
或者我们问得再扎心一些，你真的有业务SOP吗？你到底缺的是工具？还是缺的对你业务的理解？
-----
学业务和学技术一定要分开。
我举个最实际的例子，很多人学AI是为了制作自媒体爆款短视频，但这是两码事儿
制作自媒体爆款短视频是业务，在没有AI之前，它就存在了
AI来了之后，只是对业务进行了效率的提升。或者说，给了普通人一个利用AI去学习短视频的底层逻辑的工具
-----
但如果你说你学了AI之后就能制作出自媒体爆款短视频，这是完全错误的，他们没有因果关系
这也是为什么我说我们的目标不是安装某个工具，我们的目标是学习一套与AI沟通的新范式，
所以每节课看的每篇文章都直指这个目标，而不是为了快速的把claude code安装上
没有价值，因为你装上之后，你发现自己不会用，或者说没有用处
</callout>
