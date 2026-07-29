---
title: "艾木: 如何用Coze制作一个信息检索Bot（含Workflow的基础用法）"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/CDLowktgtiSudekKo5Lc2ShnnZb
node_token: CDLowktgtiSudekKo5Lc2ShnnZb
obj_token: BHJsdHp6IoJP6tx249acU1YAndc
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 4
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - " Agent 搭建共学快闪 0507"
  - "5月9日 艾木分享《Workflow》"
  - "艾木: 如何用Coze制作一个信息检索Bot（含Workflow的基础用法）"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 120
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 艾木: 如何用Coze制作一个信息检索Bot（含Workflow的基础用法）

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 ›  Agent 搭建共学快闪 0507 › 5月9日 艾木分享《Workflow》

原文: [mp.weixin.qq.com](https://mp.weixin.qq.com/s/Ory8iVXXjjN3zSTcupPm6Q) 作者: 艾木

[我用Coze手搓了一个信息检索Bot，名字叫Dr. Know。](http://mp.weixin.qq.com/s?__biz=MzU5MDM4ODIxMw==&mid=2247484056&idx=1&sn=885ada69ce18a45aaa7078b132db2704&chksm=fe3e4c02c949c514469ca8155e6963193961fc6c4fe0dd09025774b602bd3276e39d10b98545&scene=21#wechat_redirect)

这个Bot的实现原理参考的是 *FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation* 这篇论文。研究者发现通过将搜索引擎检索到的最新信息整合到大型语言模型（LLM）的提示词中，可以显著提高LLM在处理需要快速更新知识和包含错误前提的问题时的准确性。我已经在前一篇文章中对这个思路的合理性做过介绍了，这里就不在赘述了。这篇文章我主要分享一下如何在Coze平台上实现“搜索引擎增强大型语言模型”这个技术。如果你对Coze平台还完全不熟悉，建议你先到 coze.com 上尝试自己制作一个最简单的Bot。基础问题应该都能在官方文档（https://www.coze.com/docs/zh_cn/welcome.html）找到答案。Dr. Know的核心就是一个叫做`search_and_answer`的Workflow，这个Workflow主要干了两件事：一，调用Google搜索插件搜索互联网上的相关信息；二，调用LLM组块，让LLM基于搜索到的上下文信息生成回复。Dr. Know支持用户设置语言偏好，所以在这个Workflow里还需要对用户设置的语言偏好做一些相应的处理。

> [!abstract]- 🖼 图片展示了名为search_and_answer的Workflow流程。
> 图片展示了名为search_and_answer的Workflow流程。从左至右依次是多个组块相连，包括接收用户输入、处理语言偏好、调用Google搜索插件获取相关信息（中间黑色区域显示代码）、筛选信息、调用LLM组块等步骤，最后输出答案。该Workflow是信息检索Bot Dr.Know的核心，对应上文提到的其主要干的两件事：调用搜索插件获取信息和调用LLM组块基于上下文生成回复，还体现了对用户语言偏好的处理。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/GWZ0b6n0FofQqXxXZh8cwpBInNc) · `GWZ0b6n0FofQqXxXZh8cwpBInNc`

下面我将按照这个Workflow的顺序逐个介绍这里面的每个组块，然后介绍一下怎么把这个Workflow集成到Dr. Know这个Bot里：

1 设置Workflow的输入参数

2 调用Google搜索插件搜索互联网上的信息

3 格式化搜索结果

4 获取用户的语言偏好

5 调用LLM生成回复

6 设置Workflow的最终输出结果

7 把Workflow集成到Bot里

# **1 设置Workflow的输入参数**

> [!abstract]- 🖼 图片展示了Coze中Workflow的起始节点设置界面。上方显示“Sta
> 图片展示了Coze中Workflow的起始节点设置界面。上方显示“Start”，说明这是工作流的起始节点，用于设置启动工作流所需信息。下方“Input”部分设置输入参数，参数名称为“query”，类型为“String”，描述为“User query”，即用户提问，并且该参数为必填项。此图片与上下文紧密相关，上下文提到整个Workflow的输入参数只有用户的提问（query）这一个字符串，图片正是对设置该输入参数操作界面的呈现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AdQRbOUcpoYA2fxOG8ncjibVnTg) · `AdQRbOUcpoYA2fxOG8ncjibVnTg`

如果你了解编程的话，你可以把Workflow看作是一个函数。整个Workflow的输入参数只有一个，就是用户的提问（query），它是一个字符串。**2 调用Google搜索插件搜索互联网上的信息**

> [!abstract]- 🖼 图片展示的是Coze中“Google Web Search”插件的设置界
> 图片展示的是Coze中“Google Web Search”插件的设置界面。插件名称为“SearchWebWithGoogle”，介绍其可用于搜索天气、汇率、时事等未知信息，且用户想要翻译时切勿使用。输入参数部分，“num”设置为7，控制返回搜索结果数量；“query”引用自Workflow的输入参数（用户提问）；“start”未作选择。输出包括“code”（整数）、“data”（对象）和“response_for_model”（字符串）。该图片对应文档中介绍调用Google搜索插件搜索信息的部分，直观呈现插件参数设置情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CuBsbra7zokwZJxrjegcoePJnig) · `CuBsbra7zokwZJxrjegcoePJnig`

这里使用了Coze提供的“Google Web Search”插件。\`num\`参数控制返回搜索结果的数量。论文里说增加这个数量可以提高回答准确率。但是考虑到响应速度以及用户易于接受的信息量，我这里把它设置成了7。**3 格式化搜索结果**

> [!abstract]- 🖼 图片展示了Coze中用于格式化搜索结果的“Code”组块设置界面。上方“
> 图片展示了Coze中用于格式化搜索结果的“Code”组块设置界面。上方“Input”部分有“code”和“data”两个输入项，值均为“Reference”类型。中间“Code”区域有一段Python代码，用于处理输入变量生成返回值。下方“Output”部分有两个输出项，分别为“retrieved_contexts”和“references”，类型均为“String”。该图片与上下文紧密相关，展示了利用“Code”组块将Google搜索返回的结构化数据格式化为特定字符串的具体设置情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ASKgbhQMroRUJYx0Tmhcbkyhnfb) · `ASKgbhQMroRUJYx0Tmhcbkyhnfb`

Google搜索插件返回的是一些结构化数据，这里我利用“Code”组块插入了一段代码，这段代码的作用就是把Google搜索返回结果格式化成两个字符串：一个字符串是由搜索结果相关的信息拼接而成（retrieved_contexts）；另一个字符串是由搜索出来的网页链接拼接而成(references)。前者将会被插入到LLM的提示词里，后者将会插入到Workflow的最终输出结果里，也就是大家在Dr. Know回复里看到的参考链接列表。

````Python
async def main(args: Args) -> Output:
    params = args.params
    raw_results = params["data"]["organic_results"]
    filtered_results = [
            r for r in raw_results 
            if r.get("title") and r.get("link") and r.get("snippet")    
            ]
    result_template = """[{i}]
    
```YAML
Title : {title}
Source: {source}
Snippet: {snippet}
Link: {link}
```"""
    retrieved_contexts = "\n\n".join([
        result_template.format(
            i=i+1,
            title=r["title"], 
            snippet=r["snippet"],
            link=r["link"], 
            source=r.get("source", ""),        
        )   
for i, r in enumerate(filtered_results)
    ])
    
    
    references = "\n".join([
        f"[{i+1}][{res['title']}]({res['link']})"
        for i, res in enumerate(filtered_results)    
    ])
    
    ret: Output = {
        "retrieved_contexts": retrieved_contexts,
        "references": references,    
    }    
    return ret
````

这段Python代码相当于粘合剂，逻辑不复杂，理论上可以让AI帮助生成。

# **4 获取用户的语言偏好**

> [!abstract]- 🖼 图片展示了在Coze中获取用户语言偏好的“Variable”组块设置界面
> 图片展示了在Coze中获取用户语言偏好的“Variable”组块设置界面。组块名称为GetUserLanguage，用于读写Bot中的变量。界面中有“Set variable value to bot”和“Get variable value from bot”两个选项，当前选中的是后者。在Input部分，Key为必填项，值为user_language；在Output部分，变量名称为user_language，类型为String。该图片与上文“使用‘Variable’组块获取Bot内设置的user_language变量值以记录用户语言偏好”的内容对应，直观呈现了变量获取的具体设置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QBVbbyCEioqI2rxaBZ8cPt9gnad) · `QBVbbyCEioqI2rxaBZ8cPt9gnad`

这里使用了一个“Variable”组块来获取Bot内设置的变量值。这个变量叫user_language，需要在Bot开发页面配置好。我用这个变量来记录用户的语言偏好，很方便。

> [!abstract]- 🖼 图片展示的是在Coze中编辑变量的界面。界面中有“Field”“Defa
> 图片展示的是在Coze中编辑变量的界面。界面中有“Field”“Default Value”“Description”“Action”几列，其中“Field”下有“user_language”，其“Default Value”为“Value” ，“Description”为“Remember witch language the user prefers”。“Action”列有删除图标。下方还有“+ Add field”按钮。该图片与上下文紧密相关，上下文提到使用“Variable”组块获取Bot内设置的“user_language”变量来记录用户语言偏好，图片正是对该变量设置情况的展示。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/TPUAb3BqOoOtWyxeLVZcB4yYn0b) · `TPUAb3BqOoOtWyxeLVZcB4yYn0b`

# **5 调用LLM生成回复**

> [!abstract]- 🖼 图片展示的是Coze中调用LLM生成回复的操作界面。界面显示了“Gene
> 图片展示的是Coze中调用LLM生成回复的操作界面。界面显示了“GenerateQueryResponse”模块，模型选择为GPT - 3.5（16K），温度设置为0.7。输入部分有retrieved_contexts、query、user_language三个参数，均为引用类型。此外还有核心的提示词（Prompt）部分，输出部分定义了名为response的字符串类型变量。这张图片与上下文紧密相关，直观呈现了文中提到的“LLM”组块接收参数等相关内容。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/A0xhbrtM0oKBCaxJT1Kc6OrxnCh) · `A0xhbrtM0oKBCaxJT1Kc6OrxnCh`

这里是一个“LLM”组块。这里我使用的模型是GPT-3.5，主要是为了提升响应速度。GPT-4的返回结果确实更优，但是速度很慢。这个组块接收了4个参数，retrieved_contexts,query,user_language 这3个参数都是前面的步骤已经准备好的。此外，“LLM”组块最核心参数是一段提示词（Prompt）:

As a discerning reader, you possess the ability to meticulously analyze information from a plethora of sources, pinpoint the most significant details, and assess their veracity. Your approach to complex queries is that of a logical thinker, relying on evidence rather than fallible intuition to form conclusions. Additionally, you excel as a professional writer, skillfully organizing your thoughts and arguments coherently, ensuring that your prose is engaging and far from dull.  
-----  
You are given a user query, and please write clean, concise and accurate response to the query.\* Your response must be correct, accurate and written by an expert using an unbiased and professional tone. Do not give any information that is not related to the query, and do not repeat.\* Your response MUST be written in the language the user prefers: {{user_language}}.  If the user does not specify any preferred language, use the same language that the user uses in their query.\* Your response should be longer than 32 words and fewer than 1024 words.  
-----  
You will be given a set of related contexts to the query retrieved from the web, each starting with a heading like "[i]", where \`i\` is the index of this citation which is a number. Please use the context and cite the context at the end of each sentence if applicable. Please cite the contexts with the indexes of citation, in the format [i]. If a sentence comes from multiple contexts, please list all applicable citations, like [3][5].  
Here is the user query: {{query}}  
And here are the set of retrieved contexts:  
{{retrieved_contexts}}  
Additional requirements for how to use these contexts:\* Don't blindly repeat these contexts verbatim. Use it as a source of evidence for your reasoning process.\* You MUST write your own response. Do NOT merely provide the citation. \* Say "information is missing on" followed by the related topic, if the given contexts do not provide sufficient information.  
-----  
Remember your response MUST be written in the language the user prefers. Here is the user query: {{query}}

这段提示词主要参考的是贾扬清大佬的代码（https://github.com/leptonai/search_with_lepton/blob/main/search_with_lepton.py），我自己做了一些改动和优化。提示词撰写是一个手艺活，目前还没有成型的方法论。但只要能把自己的想法和思路用自然语言清晰地传达给LLM，应该就会有一个基础效果。

这个LLM组块输出一个变量response，是一个字符串。

# **6 设置Workflow的最终输出结果**

> [!abstract]- 🖼 图片展示了Coze中Workflow的最终节点设置界面。上方标注“End
> 图片展示了Coze中Workflow的最终节点设置界面。上方标注“End”，说明是工作流的最终节点，用于在工作流运行后返回结果信息。“Select Mode”处选择了“Answer directly using Answer Content”模式。下方“Input”部分有“response”和“references”两个名称及其对应值设置。“Answer content”区域则通过{{response}}和{{references}}拼接最终输出内容。该图片与上下文紧密相关，直观呈现了上下文所述的设置Workflow最终输出结果的操作界面与配置情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BcgVbiQXroBzVLxh2Khc8klmnIc) · `BcgVbiQXroBzVLxh2Khc8klmnIc`

整个Workflow的最终输出结果由两部分拼接成：response 是LLM依据搜索结果生成的对用户提问的回复，references 是参考链接列表。

Coze的Workflow提供了两种输出模式：一，返回一些变量值，然后让聊天模型基于这些变量值回复用户；二，在Workflow里拼接好输出内容，然后直接用这段内容回复用户。这里为了节省响应时间，我使用了模式二。

Coze的Workflow目前还不支持流式地输出结果，用户需要等Workflow执行完才能看到结果，这点比较影响体验。

# **7 把Workflow集成到Bot里**

> [!abstract]- 🖼 图片展示了在Coze中制作信息检索Bot（Dr.Know）的相关设置界面
> 图片展示了在Coze中制作信息检索Bot（Dr.Know）的相关设置界面。左侧是人设和提示词内容，包括打招呼语及对能力的介绍。中间部分显示了添加的插件，如DALL·E 3、GPT4V等，以及唯一的Workflow“search_and_answer”。右侧预览区域显示了Dr.Know的头像和打招呼语，下方列出了一些话题示例。该图片与上下文紧密相关，直观呈现了文中所述的Bot设计中聊天模型选择、插件添加及人设提示词设置等情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FnPjbeSzwoOEfwxQtBncDG7pn9g) · `FnPjbeSzwoOEfwxQtBncDG7pn9g`

Dr. Know的Bot设计还是比较简单的。聊天模型我选择了GPT-4 (8K)。体验下来，这个模型比GPT-4 Turbo (128K) 可靠一些。另外，我还添加了一些实用的插件，丰富Dr. Know的能力。Workflow只有一个，就是我们前面设计的search_and_answer。

人设和提示词如下，没有做过多优化：

\# Your Persona

Greetings, seeker of knowledge! I am Dr. Know, your guide to the vast expanse of information. In a world brimming with questions, I stand as a beacon of enlightenment, ready to illuminate the shadows of uncertainty. Whether you're in search of wisdom from ancient lore, keen on unraveling the mysteries of the cosmos, or simply wish to satiate your curiosity on matters both grand and mundane, you've come to the right place. Ask, and let the journey of discovery begin. Remember, in the realm of Dr. Know, there is nothing I don't.

\# Your Capabilities

\## search_and_answer

Your most important capability is \`search_and_answer\`. When a user asks you a question or inquires about certain topics or concepts, you should ALWAYS search the web before providing a response. However, when a user asks you to DO SOMETHING, like translation, summarization, etc., you must decide whether it is reasonable to use the \`search_and_answer\` capability to enhance your ability to perform the task.

ALWAYS search the web with the exact original user query as the \`query\` argument. For example, if the user asks "介绍一下Stephen Wolfram的新书 What Is ChatGPT Doing ... and Why Does It Work?", then the \`query \` parameter of \`search_and_answer\` should be exactly this sentence without any changes.

\# How to Interact with the User

Communicate with the user and search the web using the language the user prefers, which is set in the variable \`user_language\`. If this variable is not set, use the same language that the user uses in their query.

 

# **写在后面的话**

Coze的Workflow为我们制作Agents/Bots提供很大的灵活性和便捷性。理论上，很多研究论文里面的提示词工程技术都可以通过Workflow实现，然后嵌入到Bot里，快速设计出一个产品。Dr. Know就是一个很好的例子。

> [!abstract]- 🖼 图片展示了Dr.Know使用的Workflow，由多个组块通过蓝色箭头依
> 图片展示了Dr.Know使用的Workflow，由多个组块通过蓝色箭头依次相连构成流程。组块包含不同设置及内容展示区域，其中有一个组块显示黑色代码内容。该Workflow是文中阐述的示例，文中介绍了Workflow里组块可视为函数，包含原生函数、远端函数和语义函数三类，通过此Workflow示例辅助说明其概念及函数类型等相关内容。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RxUXbRTDBojBwvxyw7Tc4On7nvd) · `RxUXbRTDBojBwvxyw7Tc4On7nvd`

Workflow是什么？我们再回看一下Dr. Know使用的这个Workflow。这个Workflow里每个组块都可以看成是一个函数，这里面混杂了三类函数：一类是传统函数，像FormatRetrievedResults和GetUserLanguage都可以归为这一类；第二类是调用第三方服务的函数，如SearchWebWithGoogle；第三类程序是基于LLM的函数，如GenerateQueryResponse 。

我们可以把前一类叫作原生函数（Native Function），第二类叫作远端函数（Remote Function），第三类叫作语义函数（Semantic Function）。原生函数和远端函数是传统程序的基本组块，语义函数则是在LLM诞生之后才有的。这里我们使用了“函数”这个概念对LLM-based的程序做了概括，但是我们应该都清楚语义函数与传统函数在形式和功能上都有根本差异：形式上，它是用自然语言编写的程序；功能上，它可以模拟人的高阶思维，而不仅仅是做一些流程性的操作。既然如此，那么由这三类函数组合而成的Workflow也完全不同于传统函数，我把它们称作超函数（Hyperfuction）。

LLM以后的软件，都是由超函数构成。Dr. Know使用的这个Workflow还只是一个简单的超函数，实际上原生函数、远端函数和语义函数可以有无限多样和无限复杂的组合方式。而把这些函数组合起来，实现某种目的的技艺就是编程。[或者更确切的说是编程2.0](http://mp.weixin.qq.com/s?__biz=MzU5MDM4ODIxMw==&mid=2247483999&idx=1&sn=c65b6ccb5447beaafdcf347d68e5c7c1&chksm=fe3e4cc5c949c5d3a7ef63ff40b409913defd43b2825151d3a890682bc8dbe2f162d5a968e6a&scene=21#wechat_redirect)。

---

如果你对制作AI Bots或者AI Agents感兴趣，可以扫码加这个群。我们一起玩一起学。

> [!abstract]- 🖼 图片展示了一个群聊二维码。上方有九个小图片组成的图标和文字“群聊: 用C
> 图片展示了一个群聊二维码。上方有九个小图片组成的图标和文字“群聊: 用Coze搓Bots”。下方是黑白相间的二维码图案。最下方有文字说明“该二维码7天内(2月25日前)有效，重新进入将更新” 。图片与上下文的关系为：文档提到若对制作AI Bots或AI Agents感兴趣，可以扫码加群一起玩一起学，此图片就是对应的群聊二维码，方便读者扫码加入。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/TpAvbu9vPoHk5BxqLj4cgybknVd) · `TpAvbu9vPoHk5BxqLj4cgybknVd`

关键知识点：

> [!abstract]- 🖼 图片标题为“一张图看懂Coze Bot的结构”。图中展示了Coze Bo
> 图片标题为“一张图看懂Coze Bot的结构”。图中展示了Coze Bot结构，包含对话模型、推理模型等部分。推理模型下的Workflow关联LLM、Code、Knowledge等元素。对话模型中有“LLM as Chat Interface”部分，其与Workflow、Plugins、Knowledge等相连。上方有Agent及Multiagent Flow，旁边还有Bot API和Bot Group Chat。图右下角有二维码。该图与文档中关于制作AI Bots及Workflow等关键知识点内容相关，直观呈现了Coze Bot结构。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ApI6b9RFOoMsu9xvBHzctCHyn5f) · `ApI6b9RFOoMsu9xvBHzctCHyn5f`
