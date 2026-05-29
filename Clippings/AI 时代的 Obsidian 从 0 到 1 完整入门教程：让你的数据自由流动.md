---
title: "AI 时代的 Obsidian 从 0 到 1 完整入门教程：让你的数据自由流动"
source: "https://x.com/gengdaJ/article/2059944134924988807"
author:
  - "[[逸尘 (@gengdaJ)]]"
published: 2026-05-28
created: 2026-05-29
description: "AI时代，应该以Obsidian为根基，打通你本地、飞书、X、公众号等数据，让它们自由流动。读完这篇，你就能搭建逸尘同款Obsidian的工作台：搞懂 Obsidian 是什么，为什么它适合存放自己的宝贵资料。认清 Obsidian 的主界面：左边找文件，中间读写内容，右边放工具..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HJZiQplbkAAQDd9?format=jpg&name=large)

AI时代，应该以Obsidian为根基，打通你本地、飞书、X、公众号等数据，让它们自由流动。读完这篇，你就能搭建逸尘同款Obsidian的工作台：

1. 搞懂 Obsidian 是什么，为什么它适合存放自己的宝贵资料。
2. 认清 Obsidian 的主界面：左边找文件，中间读写内容，右边放工具。
3. 从下载安装到创建本地仓库，把资料一开始就放在长期能找到的位置。
4. 把本地仓库连接到 GitHub，让每一次修改都有记录，也能多一层备份。
5. 配好 Obsidian Git 插件，知道每个关键设置到底要不要开。
6. 写文章前先想清楚用途，再决定文件夹结构，不上来就乱分类。
7. 用 Custom Attachment Location 管图片，让文章图片自动跟着文章走。
8. 学会写文章够用的 Markdown：标题、加粗、列表、引用、链接、图片和表格。
9. 设置常用快捷键，把写作时反复点鼠标的动作省掉。
10. 用 Advanced Tables 管表格，让选题、素材和发布记录更好整理。
11. 用 Excalidraw 梳理复杂选题、脚本、流程和内容结构。
12. 用 Terminal 在 Obsidian 里打开命令行，配合 Codex 或 Claude Code 工作。
13. 用 Obsidian Web Clipper 把网页资料剪到本地仓库。
14. 用飞书 CLI 打通飞书文档、多维表格和 Obsidian 资料库。
15. 用公众号预览插件检查排版，并把文章上传到公众号草稿箱。
16. 用 X 长文插件预览文章，并上传到 X Article 草稿箱。
17. 遇到插件、Git、图片、上传失败时，按故障清单一步步排查。
18. 最后收束成一套最小可用系统：本地写作、GitHub 备份、飞书协作、公众号和 X 发布。

## 1\. Obsidian 是什么

Obsidian 是一个安装在电脑上的本地笔记软件。它管理的不是某个平台里的账号数据，**而是你电脑里的一个普通文件夹**，打开Obsidian，就等于把这个文件夹通过一种便于查看的方式进行展现。

这个文件夹里放着一篇篇 Markdown 文档，就是.md后缀的那个文件，可以把它理解成“带一点格式规则的文字文件”。

![Image](https://pbs.twimg.com/media/HJZZsdYakAAPiqI?format=jpg&name=large)

**为什么要把自己的所有资料存放到Obsidian，而且尽量用Markdown的格式保存？**

第一，资料在本地。飞书文档、公众号后台、X 后台都在云端，账号权限、网络、平台规则都会影响使用。Obsidian 的根在你的电脑上，哪怕以后换工具、换平台、换发布渠道，原始资料还在。

第二，它适合小白阅读 Markdown。很多 Markdown 文档在代码编辑器里看，对程序员顺手，对普通用户有门槛。Obsidian 可以把文档变成接近正常文章的阅读效果，也能随时切回编辑状态。

第三，它能扩展。你可以用插件接入 GitHub、终端、AI、公众号预览、X 草稿、图片管理、表格编辑和画图，让Obsidian直接编程内容工作台。而且Markdown很适合Agent阅读，所以用Obsidian和Agent（Codex、Claude Code）协作非常丝滑

## 2\. 理解Obsidian的主界面——分三块理解

Obsidian 的日常界面只按三块理解：左边、中间、右边。

左边是文件区，用来找文件夹和文档。中间是正文区，用来读和写。右边是工具区，用来放目录大纲、预览、AI对话、终端、发布工具以及其他插件。

![Image](https://pbs.twimg.com/media/HJZZphvaYAAUhs_?format=jpg&name=large)

## 3\. 第一步：下载Obsidian到建好本地仓库

搜搜Obsidian官网：[https://obsidian.md/download](https://obsidian.md/download)搜搜 Obsidian 官网：[https://obsidian.md/download](https://obsidian.md/download)

Obsidian 官网下载页面如下，后面会按系统选择安装包。

![Image](https://pbs.twimg.com/media/HJZZmgebEAAzR7p?format=jpg&name=large)

按你的电脑选择安装包。

**Windows用户：**

- 找到下载好的 Obsidian 安装文件（.exe）
- 双击打开，会自动启动安装程序
- 按照提示点击"Next"，选择安装位置（默认即可）
- 等待安装完成，自动打开Obsidian

**Mac用户：Mac 用户：**

- 找到下载好的 .dmg 文件，双击打开
- 将Obsidian图标拖到Applications文件夹
- 打开Applications，找到Obsidian，双击启动

**安装完成后，你会看到一个欢迎界面。**

![Image](https://pbs.twimg.com/media/HJZZjh-bkAA8mpv?format=png&name=large)

第一次打开 Obsidian 时，它会让你选择创建新仓库或打开已有仓库。这里选创建新仓库。

“仓库”不用理解成复杂的技术词，它就是一个装文档的本地文件夹。你之后写的文章、存的图片、装的插件配置，都会装在这个文件夹里面。

推荐把仓库放在你能长期找到的位置，例如：

> /Users/你的用户名/AI知识库 /Users/你的用户名/Documents/Obsidian D:\\AI知识库

不要放在下载目录，也不要放在临时桌面文件夹。这些地方都只适合临时文件，不适合放长期知识库。知识库还是要找一个地方好好保存。

创建仓库时记得做好：

- 起一个清楚的名字，例如“AI知识库”或“内容工作台”。
- 选择一个长期使用的本地路径。
- 进入仓库后，先不要急着写文章，先把备份和文件结构搭好。

## 4\. 第二步：连接本地仓库和GitHub仓库

记得一定要把本地仓库（你刚建好的Obsidian文件夹）安装Git插件并连接到GitHub仓库。

首先搞懂Git是什么？Github等同于飞书开了“历史版本”——你对一篇文章的所有修改，都会记录在案，如果你想后悔，就可以回溯到原来的版本。

GitHub又是什么？它相当于一个在云端保存你的文章的地方，就等于你的文章在云端有了备份，如果你的电脑损坏了、不小心删减了内容、换了一台设备时，它能把整个文件夹恢复回来。

打开浏览器，进入这个地址：[https://github.com/new](https://github.com/new)

如果 GitHub 让你登录，就先登录自己的账号。登录后会看到下面这个新建仓库页面。

![Image](https://pbs.twimg.com/media/HJZZgiOagAANSp-?format=jpg&name=large)

这张图按照以下进行操作就行。

**位置：Repository name** 怎么填：填一个仓库名，比如 \`obsidian-vault-backup\`

**位置：Choose visibility** 怎么填：选 Private，不要选 Public（public代表你的仓库所有人都能看到，private只有自己能看到）

**位置：Start with a template** 怎么填：保持 No template**位置：从模板开始** 怎么填：保持 无模板

**位置：Add README** 怎么填：保持关闭

**位置：Add .gitignore** 怎么填：保持 No .gitignore

**位置：Add license** 怎么填：保持 No license

都确认好后，再点绿色的 Create repository。

成功后，你会进入一个新的仓库页面。这个页面的网址一般长这样：[https://github.com/](https://github.com/)你的账号/你的仓库名

把这个仓库地址复制下来，后面要交给 Codex，告诉它：

> 请把这个本地 Obsidian 仓库连接到这个 GitHub 仓库：<粘贴你的 GitHub 仓库地址> 本地路径：<粘贴你的 Obsidian 本地仓库路径>

然后你这个本地仓库（文件夹）就算连接到云端 GitHub 了。

## 5\. 第三步：安装 Git 插件做自动备份

命令行连接 GitHub 解决的是“第一次接上云端”。Git 插件解决的是“以后写完自动在本地保存一份，再自动同步到 GitHub”。

先装 Git 插件。打开 Obsidian 左下角设置，进入“第三方插件”，点“浏览”，在搜索框里输入 \`Git\`。认准作者 \`Vinzent\`，说明里会写 \`automatic backup\`。

![Image](https://pbs.twimg.com/media/HJZZdiJaEAAB5UY?format=jpg&name=large)

如果按钮显示 \`Install\`，点它。安装完成后再点 \`Enable\`。如果像截图一样显示“已安装”，说明这一步已经完成。

装好后，在设置左侧点 \`Git\`。下面这些设置按页面从上往下配置：

![Image](https://pbs.twimg.com/media/HJZZaiWbMAABAM8?format=jpg&name=large)

这一页管“多久自动保存一次，以及保存后要不要同步”：

**设置项：\`Split timers for automatic commit and sync\`** 建议：关闭 解释：不把“保存记录”和“上传 GitHub”拆成两套时间。小白用一套时间就够。

**设置项：\`Auto commit-and-sync interval\`** 建议：\`10\` 解释：每 10 分钟把这段时间的改动做成一次记录，并按后面的同步规则处理。

**设置项：\`Auto commit-and-sync after stopping file edits\`** 建议：开启 解释：停止编辑后再处理，避免你正在打字时突然保存。

**设置项：\`Auto commit-and-sync after latest commit\`** 建议：关闭 解释：不需要按上一条保存记录重新计算时间。

**设置项：\`Auto push interval\`** 建议：不单独配 解释：上面第一项关闭后，这一项会变灰。按 10 分钟那套规则走。

**设置项：\`Auto pull interval\`** 建议：\`0\` 解释：不按固定时间从 GitHub 拉内容。打开 Obsidian 和同步前拉取就够。

**设置项：\`Auto commit-and-sync only staged files\`** 建议：关闭 解释：关闭后会把所有改过的文件一起保存。小白不用管 Git 里的暂存区。

**设置项：\`Specify custom commit message on auto commit-and-sync\`** 建议：关闭 解释：关闭后不会每次弹窗问你这次保存叫什么。

**设置项：\`Commit message on auto commit-and-sync\`** 建议：可保持 \`📝 {{date}}\` 解释：自动保存记录的名字。\`{{date}}\` 会自动变成当前时间。

继续往下，是每次保存记录的文字格式：

**设置项：\`Commit message\`** 建议：\`vault backup: {{date}}\` 解释：手动保存时用的记录名字。\`vault backup\` 可以理解成“仓库备份”。

**设置项：\`Commit message script\`** 建议：留空 解释：用脚本自动生成记录名。小白不用。

**设置项：\`{{date}}\` 时间格式** 建议：\`YYYY-MM-DD HH:mm:ss\` 解释：控制时间长什么样。这个格式会显示年月日、小时、分钟、秒。

**设置项：\`{{hostname}}\` 设备名替换** 建议：留空 解释：多台电脑共用时，可以填电脑名。只有一台电脑就留空。

**设置项：\`Preview commit message\`** 建议：不用配置 解释：点一下可以预览记录名，不影响备份。

**设置项：\`List filenames affected by commit in the commit body\`** 建议：关闭 解释：不把每次改过的文件名塞进记录正文。小白看不太用得上。

再往下，是从 GitHub 拿内容和往 GitHub 传内容。

![Image](https://pbs.twimg.com/media/HJZZXh-boAEkC1i?format=jpg&name=large)

**设置项：\`Merge strategy\`** 建议：\`Merge\` 解释：本地和 GitHub 都有新改动时，尽量把两边内容合到一起。

**设置项：\`Merge strategy on conflicts\`** 建议：\`None\` 解释：真撞车时不要让插件自动替你决定。让 Codex 或你自己看清楚再处理。

**设置项：\`Pull on startup\`** 建议：开启 解释：每次打开 Obsidian，先从 GitHub 拿一遍最新内容。

**设置项：\`Push on commit-and-sync\`** 建议：开启 解释：保存记录之后，把记录传到 GitHub。

**设置项：\`Pull on commit-and-sync\`** 建议：开启 解释：每次上传前先拿一遍 GitHub 最新内容，减少两台电脑互相覆盖。

再往下，是编辑器里显示改动痕迹的功能：

**设置项：\`Signs\`** 建议：关闭 解释：关闭后不在正文旁边显示每一行的改动标记。写文章时更干净。

**设置项：\`Hunk commands\`** 建议：关闭 解释：这是给熟悉 Git 的人逐块处理改动用的。小白不用。

**设置项：\`Status bar with summary of line changes\`** 建议：\`Monochrome\` 解释：底部 Git 信息用单色显示，不抢注意力。这里不是把 Obsidian 主界面拆成第四块。

再往下，是历史记录、左侧 Git 面板刷新、对比页面：

![Image](https://pbs.twimg.com/media/HJZZUhLbIAAoYk3?format=jpg&name=large)

**设置项：\`Line author information\`** 建议：关闭 解释：不在每一行旁边显示是谁改的。一个人写文章时用不上。

**设置项：\`Show Author\`** 建议：\`Hide\` 解释：查看历史记录时不显示作者列，页面更干净。

**设置项：\`Show Date\`** 建议：关闭 解释：历史记录里不额外显示日期。需要时间时看记录名里的时间。

**设置项：\`Automatically refresh source control view on file changes\`** 建议：开启 解释：文件变化后，Git 面板自动刷新。

**设置项：\`Source control view refresh interval\`** 建议：\`7000\` 解释：文件变化后等 7 秒再刷新。电脑卡就把数字调大。

**设置项：\`Diff view style\`** 建议：\`Split\` 解释：对比改动时左右分栏显示，左边旧内容，右边新内容。

再往下，是提示、菜单和作者信息：

**设置项：\`Disable informative notifications\`** 建议：关闭 解释：关闭这个开关，正常保存、上传时还能看到提示。

**设置项：\`Disable error notifications\`** 建议：关闭 解释：关闭这个开关，出错时能看到提醒。

**设置项：\`Hide notifications for no changes\`** 建议：开启 解释：没有新改动时不弹“没东西可保存”的提示。

**设置项：\`Show status bar\`** 建议：开启 解释：显示底部 Git 信息，例如当前分支和最近一次保存。

**设置项：\`File menu integration\`** 建议：开启 解释：右键文件时多出 Git 相关操作。平时不用点，但开着不碍事。

**设置项：\`Show branch status bar\`** 建议：开启 解释：底部显示当前分支名，比如 \`main\`。

**设置项：\`Show the count of modified files in the status bar\`** 建议：开启 解释：底部显示有几个文件还没保存到记录里。

作者信息这里按自己的 GitHub 账号填。截图里的邮箱已经遮挡，你不要把私人邮箱直接放进教程图里：

![Image](https://pbs.twimg.com/media/HJZZRg1bIAAHi_N?format=jpg&name=large)

**设置项：\`Author name for commit\`** 建议：填自己的名字 解释：GitHub 里会看到这次记录是谁保存的。

**设置项：\`Author email for commit\`** 建议：填 GitHub 邮箱 解释：建议用 GitHub 提供的 \`noreply\` 邮箱，减少暴露私人邮箱。

**设置项：\`Update submodules\`** 建议：关闭 解释：这是仓库里再嵌套别的仓库时才用。小白不用。

**设置项：\`Custom Git binary path\`** 建议：\`git\` 解释：让插件调用电脑里的 Git。能正常用就别改。

**设置项：\`Additional environment variables\`** 建议：留空 解释：特殊环境变量。小白不用。

**设置项：\`Additional PATH environment variable paths\`** 建议：留空 解释：找不到 Git 时才需要手动补路径。能正常备份就留空。

**设置项：\`Reload with new environment variables\`** 建议：不用点 解释：改了上面两项才需要重载。

**设置项：\`Custom base path\`** 建议：留空 解释：只有 Git 仓库不在 Obsidian 仓库根目录时才填。

最底部这几项也照着保持默认：

**设置项：\`Custom Git directory path\`** 建议：\`.git\` 解释：Git 的隐藏配置文件夹。正常仓库都叫 \`.git\`。

**设置项：\`Disable on this device\`** 建议：关闭 解释：打开后，这台电脑上的 Git 插件会停用。不要开。

**设置项：\`Copy Debug Information\`** 建议：出错时再点 解释：复制排查信息，发给 Codex 看。

**设置项：\`Debugging and logging\`** 建议：不用配置 解释：这是开发者排查日志用的。

这套配置的结果是：Obsidian 负责写，本地文件夹负责存，Git 插件负责每 10 分钟保存记录并同步到 GitHub。

成功标志有三个：底部能看到 \`main\`，GitHub 仓库能看到新提交，换一台电脑打开前会先拿到 GitHub 上的最新内容。

![Image](https://pbs.twimg.com/media/HJZZOiJbsAAy38X?format=png&name=large)

## 6\. 第四步：不要先搭文件夹，先写文章

绝对不要先搭建文件夹结构树，因为文件夹不是为了好看，而是为了让这个知识库真正有结构，以后不管是你找资料，还是AI找资料，都能有一个清晰的路径。

所以文件夹结构树的建立是一个长期的过程，需要慢慢的去摸索、重构。这部分建议根据自己的真实业务情况来仔细和Codex探讨建立。

但是可以先试着创建一个文件夹和几篇文章开始熟悉Obsidian。

## 7\. 第五步：安装Custom Attachment Location 插件调整图片顺序

内容创作者最容易丢的是图片。文章移动了，图片路径断了，发布时就会出现空图。

Custom Attachment Location 插件的作用是：每篇文章都有自己的图片文件夹，图片名称自动生成，文章改名时图片也跟着整理。

![Image](https://pbs.twimg.com/media/HJZZLmraYAAcg4P?format=jpg&name=large)

建议配置如下。

> 新附件位置：./assets/${noteFileName} 生成的附件文件名：file-${date:{momentJsFormat:'YYYYMMDDHHmmssSSS'}} 引用路径：assets/${noteFileName}/${generatedAttachmentFileName} 改名时同步处理：开启

这套配置的效果是：

> 文章.md assets/文章/file-20260524203000123.png assets/文章/file-20260524203000456.png

你以后移动文章、复制文章、上传文章时，图片都能按文章名集中管理。

## 8\. 第六步：只学写文章要用的 Markdown

Markdown 不需要系统学。写文章先掌握四个规则。

> \# 一级标题 ## 二级标题 ### 三级标题 - 无序列表 - 无序列表 1. 有顺序的步骤 2. 有顺序的步骤 > 这里放引用或提醒

写文章时，标题决定结构，列表承接步骤，表格用于对比。先用这三样，不要一开始追求复杂排版。

实在不行，右键都能手动改格式：

![Image](https://pbs.twimg.com/media/HJZZIiCawAAUzUA?format=jpg&name=large)

## 9\. 第七步：把常用格式改成快捷键

小白不需要记一堆符号。把常用动作做成快捷键，写文章时直接按。 设置路径是：打开设置，进入快捷键。

![Image](https://pbs.twimg.com/media/HJZZFgdbMAA1tTm?format=jpg&name=large)

**快捷键：Command + Option + 1** 动作：设为一级标题

**快捷键：Command + Option + 2** 动作：设为二级标题

**快捷键：Command + Option + 3** 动作：设为三级标题

## 10\. 第八步：用 Advanced Tables 管表格

Markdown 表格手写容易歪。Advanced Tables 插件的作用是：你在表格里按回车、Tab、方向键时，它帮你维持表格形状。

![Image](https://pbs.twimg.com/media/HJZZCg4boAAIi8Y?format=jpg&name=large)

小白只需要开启这几项。

**配置：显示工具按钮** 建议：开启 作用：需要时能快速找到表格工具

**配置：回车自动处理表格** 建议：开启 作用：写表格时不容易断行错位

**配置：Tab 在表格中移动** 建议：开启 作用：像表格软件一样切换单元格

**配置：表格格式** 建议：normal 作用：保持普通 Markdown 表格，兼容性更好

使用场景：选题清单、发布清单、素材对照、账号数据记录。只要涉及“几列信息对比”，就用表格。

## 11\. 第九步：用 Excalidraw 梳理复杂思路和脚本

Excalidraw 是画图工具，适合在写复杂脚本、教程、流程、业务结构时先画一张草图。

![Image](https://pbs.twimg.com/media/HJZY_h3bgAAETMz?format=jpg&name=large)

默认配置即可。

## 12\. 第十步：在 Obsidian 里打开终端（Terminal）

Terminal 插件让你不用离开 Obsidian，就能在当前仓库打开命令窗口。

先安装 Terminal。打开设置，进“第三方插件”，点“浏览”，搜索 \`Terminal\`。第一张卡片就是本教程要用的 Terminal，作者是 \`polyipseity\`。

![Image](https://pbs.twimg.com/media/HJZbwZVbUAAxRGJ?format=jpg&name=large)

如果按钮显示 \`Install\`，点它。安装完成后再点 \`Enable\`。如果像截图一样显示“已安装”，说明这一步已经完成。

打开后会看到类似这样的效果，说明已经把终端打开成功。

然后你就可以在终端打开claude code或者codex进行内容创作了。 但是注意：这里面Claude Code和外面的Claude Code的记忆是不互通的。

![Image](https://pbs.twimg.com/media/HJZY5d4aUAAzFtk?format=jpg&name=large)

## 13\. 拓展一：浏览器Obsidian剪藏插件

浏览器剪藏不是装在 Obsidian 里的插件，而是装在Chrome浏览器里的扩展。它的作用是：你看到一篇网页，点一下浏览器右上角的小按钮，就能把网页内容保存到 Obsidian 本地仓库里。

先去 Chrome 应用商店安装官方扩展。扩展名字叫 Obsidian Web Clipper。

![Image](https://pbs.twimg.com/media/HJZY2d1bEAIorVm?format=jpg&name=large)

这张图里如果显示 \`Add to Chrome\`，就点它；如果显示 \`Remove from Chrome\`，说明已经装好了。安装时 Chrome 会弹出确认框，点添加扩展。

装好后，浏览器右上角会多出一个扩展按钮。找不到时，点浏览器右上角的拼图图标，把 Obsidian Web Clipper 固定到工具栏。

然后打开扩展设置。设置页长这样。

这里先看三个地方：

**位置：Vaults** 怎么处理：保存到哪个 Obsidian 仓库。仓库名要和 Obsidian 里显示的一模一样。

**位置：New template** 怎么处理：新建一个剪藏模板。

**位置：Default** 怎么处理：默认模板。不会配置时先用这个。

实际剪藏时按这个顺序：

- 先打开 Obsidian，并确认当前打开的是你的内容仓库。
- 在浏览器里打开要保存的网页。
- 点浏览器右上角的 Obsidian Web Clipper。
- 选择“网页剪藏”模板。
- 看一下保存仓库是不是你的仓库。
- 看一下保存位置是不是之前设置好的仓库路径。
- 点保存到 Obsidian。
- 回到 Obsidian，在设置好的仓库里检查是否多了一篇新笔记。

![Image](https://pbs.twimg.com/media/HJZYze6asAABMrw?format=jpg&name=large)

## 14\. 拓展二：用飞书CLI打通飞书和Obsidian数据

飞书云文档适合多人协作和对外展示（可以把链接很方便地分享给别人阅读文档），Obsidian 适合个人长期沉淀。两者的关系应该是：飞书负责协作，Obsidian 负责归档和再加工。

飞书 CLI 可以理解成“给 Codex 用的飞书遥控器”。你只需要告诉 Codex：要读哪篇飞书文档、要新建什么文档、要建什么多维表格、最后要保存到 Obsidian 哪个位置，Codex就能非常精准地帮你完成所有飞书相关的操作。

第一次使用时，直接让 Codex 帮你安装和检查。可以这样说：

> 请帮我检查这台电脑能不能使用飞书 CLI。 如果缺少运行环境，先告诉我缺什么。 如果可以安装，请帮我安装飞书官方 CLI，并安装给 Codex 使用的飞书能力包。 安装完成后只做健康检查，不读取我的飞书资料。

安装后通常还需要授权。授权时，Codex 会给你一个浏览器链接或提示你扫码。这个动作必须你自己完成，因为这是你的飞书账号权限。授权成功后，再让 Codex 检查能不能正常访问。

常用协作方式是这三种。

第一种：飞书文档进 Obsidian。

> 请读取这篇飞书文档：<粘贴飞书文档链接> 整理成 Obsidian 笔记。 保存到：00-收件箱/飞书导出/<文档标题>.md 要求：保留原飞书链接；保留原文重点；不要编造来源里没有的内容。

第二种：Obsidian 文章发到飞书。

> 请把这篇 Obsidian 文章发到飞书，创建一篇新文档。 用途：给团队协作修改。 要求：保留标题层级、列表、图片说明和原文顺序。 完成后把飞书文档链接发给我。

第三种：新建飞书多维表格。

> 请在飞书里新建一个多维表格，用来管理选题。 字段包括：选题、来源、状态、平台、负责人、截止时间、备注。 建好后，把表格链接发给我。 不要把任何账号凭证写进 Obsidian 或 GitHub。

飞书 CLI 的边界要讲清楚：它负责把飞书资料拉出来、把 Obsidian 内容送回飞书、按你的要求建文档和表格。

每次让 Codex 操作飞书时，都要给清楚范围：哪篇文档、哪个文件夹、哪个时间段、保存到哪里。不要说“把我飞书里的资料都整理一下”。

飞书 token、应用密钥、用户凭证都不要写进文章，也不要提交到 GitHub。

## 15.拓展三： 公众号预览和一键上传草稿

MP Preview 插件解决两件事：在 Obsidian 里看公众号排版，把文章上传到公众号草稿。 这个插件能够在第三方插件里面搜索到，但是我自己新增了一个“上传文章到公众号草稿”的功能。

![Image](https://pbs.twimg.com/media/HJZYwbrbwAEEnky?format=jpg&name=large)

实际使用界面如下：

使用流程：

- 打开要发布的文章。
- 点击右侧工具里的“公众号预览”。
- 选择背景、模板、字体、字号。
- 先点“复制到公众号”，检查复制后的排版。
- 如果已经配置公众号 AppID 和 AppSecret，再点“上传封面素材”。
- 封面上传成功后，点“上传公众号草稿”。
- 到公众号后台手动检查草稿标题、封面、摘要、正文、图片。

这里的“一键发布”准确说是“一键上传草稿”。最后是否群发，必须由你自己在公众号后台确认。

公众号 AppID、AppSecret、IP 白名单属于账号安全信息。截图教程里不要展示具体值。GitHub 仓库里也不要保存这些值。

如果上传草稿时报 IP 白名单错误，处理顺序是：先查当前出口 IP，再到公众号开发设置里手动加入白名单，然后重新上传。不要让任何工具代替你操作微信界面。

最后：如果啥都不想懂，就让Codex来帮你完成上述所有操作！

## 16\. 拓展四：X 长文预览和草稿上传

X Article in Obsidian 插件解决两件事：在 Obsidian 里看 X 长文排版，把文章上传到 X 草稿。

这一步不要和公众号预览混在一起。公众号是完整教程阅读场景，X 长文更像一篇可以被快速扫读的公开笔记。

设置页主要看这几个位置：

![Image](https://pbs.twimg.com/media/HJZYtbjacAE_ZJn?format=jpg&name=large)

**设置位置：预览入口** 作用：在 Obsidian 里打开 X 长文效果 小白怎么处理：保持开启，写完文章后用它检查排版

**设置位置：上传入口** 作用：把当前文章送到 X 草稿 小白怎么处理：只在排版检查完之后再用

**设置位置：本地路径** 作用：让插件找到当前文章和图片 小白怎么处理：路径不要乱改，文章移动后先重新预览

**设置位置：登录信息** 作用：让插件知道上传到哪个账号 小白怎么处理：不要写进文章，不要提交到 GitHub

截图里只保留路径和开关，不展示任何账号凭证。X 登录态、cookie、token 都属于敏感内容。

预览效果如下。重点看三处：标题是否清楚，段落是否太长，图片是否能正常显示。

![Image](https://pbs.twimg.com/media/HJZYqc1bMAAQp2Z?format=jpg&name=large)

建议流程：

- 在 Obsidian 写完母稿。
- 复制一份，文件名改成 \`标题-X文章版.md\`。
- 打开 X 长文预览。
- 检查标题、首图、段落、列表和图片。
- 把公众号专用话术删掉，比如“点击阅读原文”“关注公众号”。
- 把表格改成短段落，因为 X 长文对表格支持不好。
- 上传到 X 草稿。
- 打开草稿后再手动检查一遍。

公众号文章和 X 长文不要完全共用一版。公众号适合完整教程，X 长文适合短段落、强标题、少层级。

## 17\. 新手最常见的故障

**现象：插件装不上** 先查什么：是否关闭安全模式，网络是否能访问插件市场 处理方式：能访问后再安装；不要乱复制未知插件

**现象：GitHub 推送失败** 先查什么：本地是否已连接远程仓库，账号是否有权限 处理方式：让 Codex 先查 \`git status\` 和远程地址

**现象：图片显示不出来** 先查什么：图片路径是否还在文章旁边的 assets 文件夹 处理方式：用图片插件重新整理，不要手动乱改路径

**现象：飞书导出失败** 先查什么：CLI 是否登录，应用权限是否开通 处理方式：先让 Codex 做健康检查，再确认文档或妙记权限

**现象：公众号草稿上传失败** 先查什么：AppID、AppSecret、IP 白名单 处理方式：不展示密钥，只检查配置和白名单

**现象：X 草稿上传失败** 先查什么：登录态、cookie、token、浏览器权限 处理方式：重新登录后再上传，不把凭证写进笔记

**现象：终端打不开 Claude Code** 先查什么：命令是否安装，当前路径是否正确 处理方式：先跑 \`pwd\`，再确认 \`claude\` 或 \`codex\` 是否存在

**现象：担心敏感内容传到 GitHub** 先查什么：是否有 \`.env\`、cookie、token、key 文件 处理方式：先让 Codex 扫描敏感词，再提交

遇到问题时，先判断它属于哪一层：本地文件、插件配置、账号权限、网络环境、发布平台。不要一上来重装 Obsidian。

## 18\. 这套系统的最小可用版本

如果你从零开始，只做下面这些就能用了:

- 安装 Obsidian。
- 创建一个长期使用的本地仓库。
- 连接 GitHub 私有仓库。
- 安装 Git、Custom Attachment Location、Terminal、MP Preview、X Article in Obsidian。
- 把图片路径改成每篇文章单独管理。
- 设置标题和列表快捷键。
- 写完文章后先在 Obsidian 预览，再上传公众号草稿或 X 草稿。
- 确认 Git 插件已经把修改推到 GitHub。

做到这一步，Obsidian 就不是一个笔记软件，而是你的本地内容底座。飞书、公众号、X、AI、GitHub 都可以围绕它工作。

哦对了，温馨提醒：以上绝大部分工作都可以由codex来完成。

如果不想折腾，想要插件安装包（就是那种你把它丢给Codex，就能一键拥有我的插件配置【不包含key】）以及配套安装skill（指导你进行配置）的朋友，可以私聊我发给你，就是说能不能请我喝杯咖啡，谢谢～❤️

好啦，快去安装你的Codex吧～