---
title: "【选修】DeepSeek本地私有化部署实战"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/WkyiwpEPDi3BQpkCODpc1N8cnwg
node_token: WkyiwpEPDi3BQpkCODpc1N8cnwg
obj_token: Fiv0dlIIAo1cx3xQJs7cY9AsnSh
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 1】：AI 通识与底层逻辑"
  - "第五章：DeepSeek私有化部署"
  - "【选修】DeepSeek本地私有化部署实战"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 3
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 【选修】DeepSeek本地私有化部署实战

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 1】：AI 通识与底层逻辑 › 第五章：DeepSeek私有化部署

<callout emoji="💡">
**这一节课需要突破网络限制，需要魔法**
</callout>

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnvi1627374crf51t43mr4?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，这节课我们手把手带着大家过一遍DeepSeek的本地化部署。

这节课最大的价值是给你讲明白在本地部署时每个软件的作用，这样以后有了更好的软件，你也可以轻松替换新的方案

注意：

1. 这节课是一个Demo教程，我是在自己的Mac电脑上进行的操作
2. 这节课是实操课程，虽然教程已经足够细致，但是每个人可能会遇到不同的情况，比如网络波动等着，遇到问题的时候可以多问问DeepSeek辅助解决
3. **这一节课需要突破网络限制，需要魔法**

# 一个AI对话应用的架构

在本地部署之前，我们要先知道一个最简单的AI对话应用的部署架构。

我用一张图来表示

<whiteboard token="DzDwwaEc4h7VrwbFzXpczBd9nfh"></whiteboard>

这张架构图分为三个部分

**用户界面 :** 

<callout emoji="💡">
这是你与 AI 交互的对话界面。它允许用户和大语言模型进行交流。也就是你实际看到并使用的部分。
</callout>

"**模型管理器:** 

<callout emoji="💡">
模型管理器 就像一个中间人或者说是代理，它负责管理和运行大型语言模型 (LLM)。它简化了模型的使用，你不需要关心模型复杂的底层配置
简单来说，**模型管理器负责让大型语言模型 能够顺利运行，并提供一个简单易用的接口，供用户界面来调用。**
</callout>

**大型语言模型:**

<callout emoji="💡">
这是核心的 "大脑"，驱动对话进行。"
</callout>

下面我则进入到实操环节

# 安装模型管理器

模型管理器市面上有很多，这里我们选择使用最常用的软件：Ollama

网页端地址：https://ollama.com/

进入之后显示如下页面（先进官网，然后点击下载）

第一步：根据自己电脑选择下载的版本，我的是苹果电脑，所以选择macOS

**请注意操作系统版本的限制**

<grid>
<column width-ratio="0.511507">
> [!abstract]- 🖼 图片展示的是Ollama官网页面，上方有卡通羊驼图案，下方文字为“Get
> 图片展示的是Ollama官网页面，上方有卡通羊驼图案，下方文字为“Get up and running with large language models”，并列出了可运行的模型，如Llama 3.3、DeepSeek-R1等。页面中部有一个黑色的“Download”按钮，下方标注“Available for macOS, Linux, and Windows”。该图片对应文档中“安装模型管理器”部分，是进入Ollama官网后显示的页面，提示用户可在此下载适用于不同操作系统的模型管理器。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AtWObTZL8ouwmqx0rYScAaUInlh) · `AtWObTZL8ouwmqx0rYScAaUInlh`
</column>
<column width-ratio="0.488493">
> [!abstract]- 🖼 图片展示的是Ollama模型管理器的下载页面。页面上方显示“Downlo
> 图片展示的是Ollama模型管理器的下载页面。页面上方显示“Download Ollama”，下方有macOS、Linux、Windows三个操作系统选项，其中Windows选项被红色箭头指向，且下方提示“Requires Windows 10 or later”。该图片与文档中“安装模型管理器”部分的上下文相关，用于说明在下载Ollama时，需根据自身电脑操作系统选择对应的版本，且特别指出Windows版本有系统版本限制，需使用Windows 10或更高版本。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Dyp8b48kcoMJyFxzLDdc2MLDntc) · `Dyp8b48kcoMJyFxzLDdc2MLDntc`
</column>
</grid>

第二步：下载Ollama到本地，并且安装到自己电脑上

第三步：检验Ollama是否安装完成

在你的浏览器地址栏输入：http://127.0.0.1:11434/  如果出现以下内容，则代表安装成功

> [!abstract]- 🖼 图片展示的是Ollama模型管理器安装成功后的界面。地址栏显示“http
> 图片展示的是Ollama模型管理器安装成功后的界面。地址栏显示“http://127.0.0.1:11434”，页面中“i”图标旁有文字“http://127.0.0.1:11434”，下方文字为“Ollama is running”。该图片与文档中“检验Ollama是否安装完成”部分对应，用于说明在浏览器地址栏输入特定网址后，若出现此界面内容，则代表Ollama安装成功。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CNtUbW6dXoJHMcxhdcUcHzgxnLW) · `CNtUbW6dXoJHMcxhdcUcHzgxnLW`

# 下载DeepSeek-R1模型

当我们安装好Ollama这个模型管理器之后，我们就可以使用其进行DeepSeek-R1模型的下载和安装了

这里我们要根据自己的电脑配置选择安装的参数规模

第一步：我们在官网点击Models 或者直接在搜索框搜索

> [!abstract]- 🖼 图片展示了Ollama官网的Models页面。页面左上角有Discord
> 图片展示了Ollama官网的Models页面。页面左上角有Discord、GitHub图标，中间是“Models”选项。右侧有搜索框，可输入“search models”。下方显示了“deepseek-r1”和“llama3.3”两款模型，其中“deepseek-r1”被红色箭头指向，标注“或者直接在这里搜索DeepSeek-R1”，并有参数规模、Pulls、Tags等信息。该图片与上下文关系紧密，用于指导用户在Ollama官网搜索DeepSeek-R1模型，是下载该模型步骤中的关键指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XITubTMyLoysY6x5OB0cCAmgnzh) · `XITubTMyLoysY6x5OB0cCAmgnzh`

第二步：为了保证多数人运行流畅，我选择1.5b的参数模型

**你可以根据自己的电脑配置选择更大参数规模的模型**

> [!abstract]- 🖼 图片展示的是在Ollama官网下载DeepSeek-R1模型时的页面。页
> 图片展示的是在Ollama官网下载DeepSeek-R1模型时的页面。页面上方介绍DeepSeek-R1为推理模型，性能与OpenAI -01相当。下方有不同参数规模的选项，其中1.5b被红色框突出显示，旁边有红色箭头指向，提示选择1.5b。右侧有“ollama run deepseek-r1:1.5b”命令，用于在终端下载模型。页面还展示了模型相关信息，如更新时间、架构、参数量、量化等。该图片与上下文紧密相关，是下载DeepSeek-R1模型步骤中选择参数规模的直观呈现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/GnFgbWawaoGMKqxpkYqcxv0Nn9g) · `GnFgbWawaoGMKqxpkYqcxv0Nn9g`

第三步：打开终端，下载DeepSeek 模型

如果你是Windows电脑

- 按住win + R
- 输入cmd，点击回车

> [!abstract]- 🖼 图片展示了在Windows电脑上打开终端的步骤。画面中显示“运行”窗口，
> 图片展示了在Windows电脑上打开终端的步骤。画面中显示“运行”窗口，提示Windows将根据输入名称打开相应程序等。窗口下方“打开”栏内输入了“cmd”，表明在运行窗口中输入命令以打开命令提示符。该图片与文档中“如果你是Windows电脑，按住win+R，输入cmd，点击回车”这一操作步骤对应，直观呈现了在Windows系统下通过运行窗口输入命令打开终端的操作界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JSkPbZaAgoEZrfxoXMbc0LjInrd) · `JSkPbZaAgoEZrfxoXMbc0LjInrd`

如果你是Mac电脑

- 按下 Command(⌘)  + Space 键打开Spotlight搜索
- 输入“Terminal”或者“终端”，然后从搜索结果中选择终端应用程序

> [!abstract]- 🖼 图片展示了Mac电脑上 自动生成
> 图片展示了Mac电脑上 自动生成
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/PoN4bjyX2oxLVYxK0YQcq2Xhnec) · `PoN4bjyX2oxLVYxK0YQcq2Xhnec`

在终端粘贴以下命令

```Markdown
ollama run deepseek-r1:1.5b
```

点击回车后，自动开始下载

> [!abstract]- 🖼 图片展示的是在终端中使用Ollama运行DeepSeek-R1:1.5b
> 图片展示的是在终端中使用Ollama运行DeepSeek-R1:1.5b模型的命令执行界面。命令为“ollama run deepseek-r1:1.5b”，执行过程中显示“pulling manifest”和“pulling aabd4debf0c8... 2%”，表明模型正在下载中，进度为2%，已下载24 MB，总大小为1.1 GB。该图片与文档中“下载DeepSeek模型”步骤相关，直观呈现了下载命令执行时的终端反馈情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/K5YtbNUC5obNvrxOj34c5og9nXe) · `K5YtbNUC5obNvrxOj34c5og9nXe`

> [!abstract]- 🖼 图片展示的是在终端 addCriterion图片内容:
> 图片展示的是在终端 addCriterion图片内容:
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Flk3bAuq0oTcPtxlB8ocoYohn8c) · `Flk3bAuq0oTcPtxlB8ocoYohn8c`

下载完毕之后，验证下模型是否可以回答

> [!abstract]- 🖼 图片展示了在终端下载DeepSeek模型并验证安装成功的界面。左侧显示模
> 图片展示了在终端下载DeepSeek模型并验证安装成功的界面。左侧显示模型下载进度，右侧列出各部分文件大小。下方红框内是命令行输入“你好呀”后的回复，模型回复“你好！很高兴见到你，有什么我可以帮忙的吗？😊”，表明模型已安装成功。该图片与文档中“下载完毕之后，验证下模型是否可以回答”内容对应，直观呈现了验证模型安装成功的操作结果。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LHpsbH4XYoZxsqxRV2YclM4knEc) · `LHpsbH4XYoZxsqxRV2YclM4knEc`

当你输入你好呀，模型可以回答的时候，则证明你的模型已经安装成功啦

# 安装用户对话界面

这里我们使用一个Chrome插件来满足界面对话的诉求

第一步：点击下方链接，安装浏览器插件，添加到拓展程序

https://chromewebstore.google.com/detail/page-assist-%E6%9C%AC%E5%9C%B0-ai-%E6%A8%A1%E5%9E%8B%E7%9A%84-web/jfgfiigpkhlkbnfnbobbkinehhfdhndo

> [!abstract]- 🖼 图片展示的是Chrome应用商店中“Page Assist - 本地AI
> 图片展示的是Chrome应用商店中“Page Assist - 本地AI模型的Web UI”插件页面。页面上方有“chrome应用商店”标识，中间是插件名称及评分，下方有“添加至Chrome”按钮。下方展示了插件的宣传图，左侧图中显示“OLLAMA-POWERED A WEB UI FOR YOUR OLLAMA”，右侧图中显示“OLLAMA-POWERED SIDEBAR FOR YOUR BROWSING”。该图片对应文档中“第一步：点击下方链接，安装浏览器插件，添加到拓展程序”步骤，直观呈现了插件安装的入口。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Yo94bmckKoYzjdxcwbDcKDXQnwh) · `Yo94bmckKoYzjdxcwbDcKDXQnwh`

第二步：运行插件

> [!abstract]- 🖼 图片展示了在浏览器中安装的Page Assist插件界面。左侧为浏览器标
> 图片展示了在浏览器中安装的Page Assist插件界面。左侧为浏览器标签栏，右侧是插件界面，显示“New Chat”和“Select a Model”等选项。关键信息是“Select a Model”下拉菜单中，突出显示了“deepseek-r1.1.5b”模型，下方还有“llama2_latest”模型。界面右下角有“Ollama is running...”提示，表明Ollama正在运行。该图片对应文档中“运行插件”步骤，直观呈现了选择模型和检测Ollama运行状态的操作界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Slkib5cVIo3vd6xJkGtc1tzSn1g) · `Slkib5cVIo3vd6xJkGtc1tzSn1g`

第三步：开始对话

> [!abstract]- 🖼 图片展示了DeepSeek本地私有化部署实战中用户对话界面的示例。上方显
> 图片展示了DeepSeek本地私有化部署实战中用户对话界面的示例。上方显示用户提问“帮我用鲁迅的文风写一篇体育圈饭圈文化
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WyWobtmz5oHae8xnQR0cw8Hanvf) · `WyWobtmz5oHae8xnQR0cw8Hanvf`

# 写在最后

至此，我们完成了整个本地部署，这节课我希望你不仅仅会部署这个demo

我更希望你能来了解本地部署的三件套

- 模型管理器
- 大语言模型
- 用户对话页面

这三部分大家都可以根据自己的实际情况进行选择

比如大语言模型你可以选择DeepSeek-R1 的7b模型、用户对话页面你可以选择其他合适的工具

重要的是你要理解这个架构
