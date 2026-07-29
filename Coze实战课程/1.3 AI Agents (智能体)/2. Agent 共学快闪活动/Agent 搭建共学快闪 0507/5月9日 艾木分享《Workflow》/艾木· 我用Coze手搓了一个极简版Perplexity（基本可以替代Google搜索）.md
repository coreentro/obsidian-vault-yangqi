---
title: "艾木: 我用Coze手搓了一个极简版Perplexity（基本可以替代Google搜索）"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/Y8YawQAjhiv77wk5sVacX4tZnnz
node_token: Y8YawQAjhiv77wk5sVacX4tZnnz
obj_token: SRsvdEvHzoPMDWxwsykc40sanQe
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 4
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - " Agent 搭建共学快闪 0507"
  - "5月9日 艾木分享《Workflow》"
  - "艾木: 我用Coze手搓了一个极简版Perplexity（基本可以替代Google搜索）"
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

# 艾木: 我用Coze手搓了一个极简版Perplexity（基本可以替代Google搜索）

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 ›  Agent 搭建共学快闪 0507 › 5月9日 艾木分享《Workflow》

原文: [mp.weixin.qq.com](https://mp.weixin.qq.com/s/ASwN2aD0huS2u2UmAIkdhA) 作者: 艾木三号

# **写在前面的话**

互联网是一片浩瀚的信息之海。人是一种渴望信息的智能体。但作为人，我们的注意力、计算能力和储存能力都是有限的。人无法同时处理整个互联网的信息，于是人发明了一种“打捞”信息的技术工具：搜索引擎。以Google搜索为代表的搜索引擎依然是互联网上最有效的信息过滤机制，内容推荐算法没有改变这一点，以LLM（大语言模型）为基础的生成式AI也没有改变这一点。但是，使用Google搜索可能已经不是最棒的信息检索体验了。

LLM渴望信息。据说，它喝光了整个信息之海的水。它吸收了这些水之后变成了什么？有人说，它榨取出了人类智慧的精华，从毛毛虫蜕变成了蝴蝶[1]。有人说，它就是一张表征整个互联网文本的模糊的JPEG图像[2]。我更倾向于后一种说法。因为如果LLM真的萃取到了整个互联网的精华，那么也就不需要RAG（检索增强生成）这样的技术来给系统打补丁了。

通过搜索引擎来增强LLM（Search Engine-Augmented LLM）是一种RAG实现方式。它的核心思路很简单，就是在回答用户提问时，先使用搜索引擎检索相关信息，然后把相关信息作为上下文提供给LLM，让它基于这些信息作“推理”并回答问题[3]。这样做有几个好处：

1. 首先，LLM的一个很大的缺陷是它无法实时获取最新的信息。它能获取的信息就是预训练时输入的信息，这些信息有一个截断日期，这个日期之后的信息它一概不知（至少无法从模型内部获取到）。而搜索引擎可以获取到更加实时的信息。
2. LLM有“幻觉”问题。在缺少相关事实信息的情况下，它就会编造。更严重的是，它很擅长编造，经常编得跟真的一样。而搜索引擎可以检索出相关的信息，这些信息可以作为LLM“推理”的依据。
3. LLM无法给出准确的引用来源。LLM吸收了整个互联网的信息，当它回答问题的时候，你会感觉它的回复好像是参考了互联网上的某个地方的内容，但是它无法告诉你它具体引用或者改编的是哪里的内容，因为LLM已经把整个互联网的信息作了词元（token）级别的融合。LLM无法给出引用来源间接带来一个严重问题是，你无法去到信息源，去自己做验证。而搜索引擎可以给予准确的信息源。

以上种种问题，决定了LLM本身作为一个知识问答工具是完全不合格的。

而搜索引擎的问题则是体验上不够简便、不够直接。搜索引擎返回的信息是一堆链接和文本片段（很多时候还有广告干扰），这种呈现形式是比较原始的，还需要人去做进一步处理。给搜索引擎加上LLM，或许可以带来更优的信息检索体验。

Perplexity[4]就是基于这个思路搞出来的产品，目前其估值已经超过5亿美元了，它的目标是要取代Google搜索。这个思路本身没有什么新鲜的，OpenAI早在21年就研究过了[5]，后来也有研究者作了进一步的验证[3]。这个思路的技术实现也不复杂，贾扬清大佬用了不到500行Python代码就实现了一个基础版[6]。

我最近在Coze[7]上体验手搓AI Bot，也顺手搓了一个极简版的Perplexity。之所以说是“手搓”，是因为我基本上不用写什么代码，通过拖拽组合功能模块，再加上一些配置，就可以实现想要的功能。算下来我只写了一点点不能算作代码的“粘合剂”代码，大概36行，外加41行提示词，这就是所有的“代码”。而且理论上，这些“代码”很大一部分你都可以让AI帮你写。

# **下面我简单介绍一下这个AI Bot……**

我制作的这个Bot的名字叫作Dr. Know，这个名字源自斯皮尔伯格的电影《人工智能》。

> [!abstract]- 🖼 图片展示的是一个科幻场景，背景为带有网格的墙面。画面中央有一个发光的圆台
> 图片展示的是一个科幻场景，背景为带有网格的墙面。画面中央有一个发光的圆台，上面坐着一位戴眼镜的白发人物，其周围有光线效果。台前有两位坐着的人物，一位面向圆台，另一位背对观众。画面右侧有黄色文字“FACTUAL TEXT”。该图片可能用于表现某种科技或未来感的氛围，与上下文介绍的AI Bot等科技主题相契合。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JqHTb3ypYoohfOxSzACchLjBnrZ) · `JqHTb3ypYoohfOxSzACchLjBnrZ`

Greetings, seeker of knowledge! I am Dr. Know, your guide to the vast expanse of information. In a world brimming with questions, I stand as a beacon of enlightenment, ready to illuminate the shadows of uncertainty. Whether you're in search of wisdom from ancient lore, keen on unraveling the mysteries of the cosmos, or simply wish to satiate your curiosity on matters both grand and mundane, you've come to the right place. Ask, and let the journey of discovery begin. Remember, in the realm of Dr. Know, there is nothing I don't.（这段自我介绍是由ChatGPT生成的）

Dr. Know的能力展示

，时长01:03

这些天我也在吃自己的狗粮，用下来感觉还挺实用的。下面是一些我自己使用时候的真实案例：

> [!abstract]- 🖼 图片展示了用户“wille”与AI Bot“Dr.Know”的对话界面。
> 图片展示了用户“wille”与AI Bot“Dr.Know”的对话界面。2024年2月11日8:22 AM，用户提问“媒介即消息”，Dr.Know随即回复称这是加拿大传播学者马歇尔·麦克卢汉提出的概念，指传播方式会影响人们对信息的理解，媒介本身也是信息的一部分。同时，Dr.Know还指出所给上下文对“消息”一词含义信息不足，并提供了7条相关参考链接。此图片是“Dr.Know的能力展示”中的真实使用案例，直观呈现了该AI Bot的答疑功能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Lx9zbNrFgo8KYIx1TQFc66hSn7f) · `Lx9zbNrFgo8KYIx1TQFc66hSn7f`

> [!abstract]- 🖼 图片展示了用户wille与AI Bot“Dr.Know”的对话界面。wi
> 图片展示了用户wille与AI Bot“Dr.Know”的对话界面。wille询问“iPhone滚动截屏”，Dr.Know做出回复。其内容为在配备Face ID的iPhone设备上进行滚动截屏的步骤，包括打开页面、同时按下侧边和音量增大按钮截屏、点击缩略图、在截图编辑页面选“整页”、点击“完成”并选择保存位置等。还说明了带有Home键的iPhone或iPad的截屏方式，以及该功能仅在部分应用可用，并附上了三条参考资料链接。此对话作为Dr.Know的能力展示案例之一。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/V2vHbz27uoQPzXxyBVBcmbGanDb) · `V2vHbz27uoQPzXxyBVBcmbGanDb`

> [!abstract]- 🖼 图片展示了用户wille与AI Bot Dr.Know的对话界面。用户于
> 图片展示了用户wille与AI Bot Dr.Know的对话界面。用户于2024年2月9日下午3:02提问“椰子鸡是深圳特产吗？”，Dr.Know几乎同时做出回复，称椰子鸡被广泛认为是深圳特产，虽起源有不同观点，但在深圳普及程度和影响力使其成为标志性美食，还列举了“润园四季”等例子。回复下方有多个蓝色的参考链接，如“海南椰子鸡，其实是深圳特产”等，表明回复有信息来源支撑。这是对Dr.Know能力展示部分中的一个真实使用案例呈现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RNWnbqrkxo7LYYxQTCacauDNnac) · `RNWnbqrkxo7LYYxQTCacauDNnac`

> [!abstract]- 🖼 图片展示了用户wille与AI Bot“Dr.Know”的对话记录。20
> 图片展示了用户wille与AI Bot“Dr.Know”的对话记录。2024年2月7日7:12 PM，wille向Dr.Know提问，请求介绍Stephen Wolfram的新书《What Is ChatGPT Doing ... and Why Does It Work?》。随后Dr.Know做出回应，介绍该书探讨了ChatGPT内部工作机制及产生有意义文本的原因，涵盖基于计算的自然科学思想等，引发广泛关注，还附上了多个相关信息链接。此对话是文档中展示Dr.Know实用能力的真实案例之一。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/W49GbZSguoyCnhxjb9Vcxv7znAf) · `W49GbZSguoyCnhxjb9Vcxv7znAf`

\*小提示：如果可以的话尽量用英文提问，因为英文互联网的信息质量更优，这跟你使用搜索引擎是一个道理。

**Dr. Know的一些附加特性**

附加特性1：Dr. Know支持你设置自己的语言偏好。

> [!abstract]- 🖼 图片展示了用户wille与AI Bot“Dr.Know”的对话界面。wi
> 图片展示了用户wille与AI Bot“Dr.Know”的对话界面。wille先向Dr.Know发送指令“把用户语言设置成日语”，Dr.Know回复已将用户语言设置为日语，并表示之后会话将用日语进行，有问题可随时提问。随后，wille又向Dr.Know询问“top - of - funnel SEO”相关内容，Dr.Know给出了关于该术语是营销漏斗初期阶段SEO战略的解释。这张图片与文档中“Dr.Know支持设置自己的语言偏好”这一附加特性相呼应，直观呈现了语言设置及提问回复的场景。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WjpYbrjyEo3MFCxHk4qcL81on3e) · `WjpYbrjyEo3MFCxHk4qcL81on3e`

附加特性2：Dr. Know内置了DALLE 3插件，可以文生图（感谢Coze）：

> [!abstract]- 🖼 图片展示了用户wille与AI Bot“Dr.Know”的对话及生成的图
> 图片展示了用户wille与AI Bot“Dr.Know”的对话及生成的图像。用户wille在对话中@Dr.Know，并指令其“画一条紫色的金龙”，随后Dr.Know回复（edited），并展示了一幅画作。画作中是一条威风凛凛的金龙，龙身带有紫色，龙须、龙鳞细节丰富，背景有云彩、建筑等元素。该图片是对上文提到的“Dr.Know内置了DALLE 3插件，可以文生图”这一附加特性的实例展示。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/N4jrbbFX5o2mC6xq6Q6cODnAnZd) · `N4jrbbFX5o2mC6xq6Q6cODnAnZd`

附加特性3：Dr. Know内置了GPT4-Vison插件，可以读图（感谢Coze）：

> [!abstract]- 🖼 图片展示了用户wille与Dr.Know的对话内容。wille于今日12
> 图片展示了用户wille与Dr.Know的对话内容。wille于今日12:44 AM提问图片中不属于环境的物体具体位置，问题下方是一张包含多种菜肴的图片，其中间位置有一辆金属卡车。Dr.Know在12:44 AM回复称，这辆不属于食物主题环境的金属卡车位于图片中间，放置在食物之上。此图片作为案例，用于展示Dr.Know内置的GPT4-Vison插件的读图能力。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QR5pbfSf8oRIl8xrDzRczRL4nHg) · `QR5pbfSf8oRIl8xrDzRczRL4nHg`

如何使用Dr. Know？

如果你会科学上网，可以通过下面这个链接进入Dr. Know的Coze主页：

https://www.coze.com/store/bot/7332080641820934162?bot_id=true

> [!abstract]- 🖼 图片展示的是名为Dr.Know的AI Bot界面。左上角显示发布者为wi
> 图片展示的是名为Dr.Know的AI Bot界面。左上角显示发布者为wille，发布时间是2024 - 02 - 15 18:01，获赞14次。界面中间有Dr.Know头像及名称，下方是一段英文自我介绍。左下角有输入框“Send Messages...”用于发送消息。右侧区域显示有199位用户，并有“Open in”选项，可在Cici、Discord、Telegram中打开。该图片与上文介绍的Dr.Know相关，直观呈现其界面及部分功能入口。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UuNebfSMgoMXAIxKoHOczm5xnXg) · `UuNebfSMgoMXAIxKoHOczm5xnXg`

在页面左侧就可以跟Dr. Know进行对话，做初步体验。另外我还将Dr. Know发布到了Cici，Discord和Telegram。Cici是字节的机器人托管平台，我没用过。推荐使用Discord：点击Discord图标就可以把Dr. Know加入到你的Discord服务器中，然后就可以在频道里@Dr. Know向它提问，也可以跟它私聊。私聊不用每次都@，更便捷。也可以通过Telegram使用，点击Telegram图标就可以开启跟Dr. Know的聊天。

如果你不会科学上网，可以关注本公众号，然后发送“Dr. Know”获取一个Free的体验方式。下面是应用截图，除了Dr. Know其他几个原生的OpenAI模型也都是可体验的（这算是一个小福利）。

> [!abstract]- 🖼 图片展示了LobeHub平台的界面，在聊天输入框上方有“模型”选项，点击
> 图片展示了LobeHub平台的界面，在聊天输入框上方有“模型”选项，点击后弹出下拉菜单。菜单中列出了包括Dr.Know以及多个原生OpenAI模型，如GPT - 3.5 Turbo、GPT - 4 Turbo、GPT - 4 Vision、GPT - 4 等，每个模型名称旁还标注了一些信息如“DIY”“16K”等。这与文档中提到的除了Dr.Know外其他几个原生OpenAI模型也可体验相呼应，直观呈现了可体验的模型种类。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Ha7UbsUSOohWZcxyS66cHFyInnh) · `Ha7UbsUSOohWZcxyS66cHFyInnh`

# **写在后面的话**

我在手搓这个Bot的过程中，也是第一次体验到了低代码的快乐。写很少的代码，就可以快速地把一个想法实现出来，做成产品，并且发布出来，供自己和别人使用。这一方面当然是AI技术的发展带来的好处，通过将AI技术跟传统的技术结合，可以制作出很强大的软件工具。另一方面则得益于Coze这样的平台，在降低了技术门槛的同时，又提供了相当的可定制性。Coze的灵活度比OpenAI的GPTs要强，因此也可以制作出更复杂的应用。尤其是跟Discord这样的聊天平台结合起来，可玩性很高。

AI平民化是好事。

有人可能会问，为什么不直接去用Perplexity，而是要自己弄一个简陋的版本？怎么说呢，大家应该都有过那种“自己做的蛋炒饭就比别人做的香”的感觉——即使别人的蛋炒饭值5亿美元，这就是DIY的快乐。另一原因是，我想做的东西跟Perplexity是不一样的，Dr. Know只是一个基础。我接下来还会继续丰富Dr. Know的能力，也会探索一下其他更有意思的玩法，比如多Bots协作：

> [!abstract]- 🖼 图片展示了一个Discord聊天界面“test-multibots-2”
> 图片展示了一个Discord聊天界面“test-multibots-2”频道中的对话。2024年2月8日2:36 PM，用户wille发起让Bot A、Bot B、Bot C参与“真爱是不是谎言”辩论赛的指令，指定Bot A、Bot B为正方，Bot C为反方，并要求论述不少于500字。随后Bot A做出回应，称作为正方坚持认为真爱是美丽的幻想，还从心理学角度阐述了对真爱的看法。此图片与文档中作者提及探索多Bots协作玩法的内容相关，展示了多Bot协作进行辩论的场景实例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/F6qublYGNoDflcxy1FwcJB5znSe) · `F6qublYGNoDflcxy1FwcJB5znSe`

> [!abstract]- 🖼 图片展示的是一个聊天界面截图，群聊名称为“test - multibot
> 图片展示的是一个聊天界面截图，群聊名称为“test - multibots - 2”。用户“wille”提及Bot A、Bot B、Bot C参与“真爱是不是谎言？”的辩论赛。Bot C于2024年2月8日2:36 PM回复，表明观点为“真爱不是谎言”。随后从科学角度（恋爱中的化学反应）、心理学角度（爱对健康和适应性的重要性）、历史和文学角度（如《罗密欧与朱丽叶》等作品）进行论证。该图片与文档中作者提及将探索多Bots协作的内容相关，展示了多Bot参与辩论的场景示例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Q4HgbTFTWol5G5xFBMLclNOTnxe) · `Q4HgbTFTWol5G5xFBMLclNOTnxe`

> [!abstract]- 🖼 图片展示了一个聊天界面截图，群聊名称为“test-multibots-2
> 图片展示了一个聊天界面截图，群聊名称为“test-multibots-2”。2024年2月8日下午2点43分，用户“wille”在群里@Bot A和Bot B，询问作为正方如何反驳反方Bot C的观点。随后Bot A进行了回复，指出虽然认可Bot C提到的爱有生物化学基础，但认为这种化学反应短暂，不能等同于“真爱”，还从心理学研究、现实情况以及文学作品等方面对“真爱”的持久性和纯粹性提出质疑。该图片与上文提到的探索多Bots协作相呼应，展示了多Bot互动的场景。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MVinbuifqofODpxgpF9cZeOrnqd) · `MVinbuifqofODpxgpF9cZeOrnqd`

这篇文章只是一个介绍，我后面会专门写一篇内容详细讲一下Dr. Know的原理、实现方式以及具体制作过程。大家也可以通过这个实际的例子了解一下如何使用类似Coze这样的AI平台手搓Bot。有门槛，但门槛不高。实际上，我觉得软件开发从来没有像现在这样简单。

如果你对制作AI Bots或者AI Agents感兴趣，可以扫码加这个群。我们一起玩一起学。

> [!abstract]- 🖼 图片展示的是一个群聊二维码。上方有群聊名称“用Coze搓Bots”，顶部
> 图片展示的是一个群聊二维码。上方有群聊名称“用Coze搓Bots”，顶部还有一个由头像等组成的图标。下方是黑白相间的二维码图案，底部文字说明该二维码7天内（2月23日前）有效，重新进入将更新。结合上下文可知，这是作者艾木为对制作AI Bots或AI Agents感兴趣的人提供的进群方式，扫码可加入群聊一起学习和探索相关玩法。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/B7dfbTxvUoL4fRxrZe0cRfkgnae) · `B7dfbTxvUoL4fRxrZe0cRfkgnae`

如果二维码过期了，可以联系艾木。

[1] https://twitter.com/geoffreyhinton/status/1635739459764322330[2] https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web[3] https://arxiv.org/abs/2310.03214[4] https://www.perplexity.ai/[5] https://arxiv.org/abs/2112.09332[6] https://twitter.com/jiayq/status/1750242829769801793[7] https://www.coze.com/
