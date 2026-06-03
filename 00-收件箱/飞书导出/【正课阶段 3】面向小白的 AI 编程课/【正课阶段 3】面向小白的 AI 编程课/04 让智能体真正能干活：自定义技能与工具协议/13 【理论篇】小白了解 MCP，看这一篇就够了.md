---
title: "【理论篇】小白了解 MCP，看这一篇就够了"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/OHtQwPfvuiiXrbkRSHicdwMXnje"
node_token: "OHtQwPfvuiiXrbkRSHicdwMXnje"
obj_type: "docx"
document_id: "A7gudFuxqoxQ4Mxyk8McH3LCnAc"
revision_id: "12"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/OHtQwPfvuiiXrbkRSHicdwMXnje>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>【理论篇】小白了解 MCP，看这一篇就够了</title>

# 写在前面



大家好，我是大圣，我希望通过这篇文章来聊一下 MCP



---



我会从以下8个部分讲清楚 MCP的来龙去脉（**非技术向**）



1. 什么是 MCP
2. 为什么要给大模型传递上下文
3. 给大模型传递上下文的主流方案
4. MCP的前世：Function Calling
5. 为什么需要 MCP
6. MCP的三个核心角色
7. 写在最后 & 我对 MCP的看法
8. 延伸阅读



# 什么是 MCP



了解任何一个概念，都要从他的名字开始



MCP全称是 Model Context Protocol，中文翻译：模型上下文协议



M = Model，是大模型，这是 MCP服务的对象



C= Context，是上下文，这个是理解 MCP的关键，我们要专门讲解



P = Protocol，是协议的意思，协议意味着标准



**用一句话来表述 MCP的作用：MCP是一种给大模型传递上下文的协议**



# 为什么要给大模型传递上下文



大模型是通过互联网公开数据训练的



当大模型训练完成后，模型的知识就会停留在训练的那一刻，是一个静态知识



这就会导致大模型的数据存在两个明显的缺陷



1. 没有办法自动获取训练日期之后的互联网公开信息
2. 没有办法获取用户/企业的私有数据（训练时并未参考）



但是在实际业务需求中，静态知识远远不能满足我们的需求



如果我要做一个旅游规划，我需要实时的天气和航班信息；如果我要做一个企业客服助手，我需要企业私有的产品文档数据，这些都是单独的大模型所不能完成的



因此我们需要给大模型提供额外的信息辅助他更好的完成任务，这些额外的信息在专业术语中就叫做上下文



**如果你想要详细了解上下文的概念，请关注文章最后的延伸阅读**



# 给大模型传递上下文的主流方案



## 客户端存储



当你跟 DeepSeek、豆包等 AI对话应用在一个窗口聊天的时候，为什么他能记住你之前说的话？



这里面涉及到一个基本的逻辑



<callout emoji="🎼">
**在一个独立的对话窗口中，当 AI 回答你的最新问题时，此前所有的聊天记录都会被打包，作为“上下文”一同提交给它，AI 正是依据这些历史信息，来理解你当前问题的背景。**
</callout>



![](https://feishu.cn/file/XEAfbZqZroVji1xvJxxcFiWrnFh)



## RAG（知识库）



知识库的作用就是为了解决大模型无法获取私有数据的问题



在使用 RAG时，会有如下 3 个流程



1. 将外部需要检索的知识（资料）构建一个向量数据库
2. 当用户提问时，会使用用户的问题去向量数据库检索匹配对应的内容
3. 将从向量数据库检索到的信息作为上下文提供给大模型，从而得出更准确的回答



![](https://feishu.cn/file/SBlSb4PAEoiuntxwFXvc0uu5n6c)



如果需要详细了解 RAG，我有一篇 1.6 万字的文章，请关注文章最后的延伸阅读



## Function Calling



AI智能体有一个典型的公式



<callout emoji="🎼">
**AI Agent（智能体） = LLM（大模型）+ Planning（规划）+ Memory（记忆）+ Tools（工具）**
</callout>



![](https://feishu.cn/file/RAytbiSzZoMEXoxkRMEcSHBoneb)



在智能体中，大模型需要调用不同的工具来获取额外的信息



比如AI搜索场景，大模型需要调用搜索引擎工具获取最新的互联网信息



比如旅游规划场景，大模型需要调用天气接口和航班接口获取最新的天气和航班信息



Function Calling 就是由 OpenAI公司定义的一种大模型调用外部工具的流程



这其实就是 MCP的前生，我们会在接下来中详细了解 Function Calling的流程



## MCP



MCP的出现就是为了解决 Function Calling存在的一些问题，在此基础上做了更高级的抽象



目的仍然是让大模型应用可以更简单、更高效的调用外部工具，从而为大模型提供额外的上下文



接下来我们会详细讲解 Function Calling的流程



# 前置知识：客户端与服务端



在讨论Function Calling之前，我们必须先了解两个基本概念：**客户端（Client）和服务端（Server）**



这两个概念会贯穿我们在讲解Function Call的整个流程中。



我用简单的概念来解释：



- 客户端就是日常你操作的软件或者网站页面，比如你使用豆包网站，其实就是一个客户端。



- 服务端通常是用户看不到的，它经常用来存储数据，处理请求并且返回响应。



我用豆包举个例子：



豆包这个网站其实就是个客户端，用户可以在这个页面上输入文字，或者点击按钮等动作



![](https://feishu.cn/file/U4PxbrQZFo4gPBxl1lZcZobfnkc)



当你把你的问题发送到豆包的聊天对话框的时候，豆包是如何给你回复的呢？



第一步：客户端把你的消息发送给了服务端



第二步：服务端就是大模型真正存在的地方，服务端处理你的请求，再把结果返回给客户端。



第三步：客户端将服务端返回给你的答案显示出来



<callout emoji="💡">
**下面我们在讲调用工具的过程，也是遵循这个基本的客户端-服务端模式的**
</callout>



# 大模型调用工具的前世：Function Calling



最早让AI学户使用工具的方法就是OpenAI公司提出来的Function Calling（函数调用）。



我们这里不讲定义，我直接通过一个让大模型查询天气的例子来理解Function Calling的整个过程



我们以使用ChatGPT为例子（毕竟是OpenAI公司提出的Function Calling）



**PS：这一段有些难啃，但是我希望你可以看完，这是我花费时间最长的一段**



![](https://feishu.cn/file/Ha0wbZA1FoiP10x6SSBcRhF7n6l)





时序图可以帮助你快速了解架构，详细内容请看下方具体文案



## 第一步：定义好查询天气的方法



OpenAI的开发人员会提前定义好ChatGPT需要支持的所有工具



我们假设有两个工具：



工具1：get_current_weather【获取当前的天气】



工具2：get_hotel_list【获取酒店列表】



## 第二步：用户在客户端提出问题



用户在ChatGPT的对话框中提出输入：请问杭州今天的天气如何？



客户端会把你的问题和所有的工具列表（不仅仅是天气工具）一起发送给服务端，请求数据类似：



**PS：这是JSON的格式，其实很容易阅读，非程序员小伙伴不要发怵，可以关注文章最后的延伸阅读**



```JSON
{
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": "请问杭州今天的天气如何？"
        }
    ],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "获取指定城市的实时天气",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "城市名，例如 杭州"
                        }
                    },
                    "required": [
                        "location"
                    ]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_hotel_list",
                "description": "获取可用的酒店列表",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "address": {
                            "type": "string",
                            "description": "具体的地址"
                        }
                    },
                    "required": [
                        "address"
                    ]
                }
            }
        }
    ],
    "tool_choice": "auto"
}
```



这里面的核心就是客户端将用户的问题和**支持调用的所有工具**都给到服务端



## 第三步：服务端给出响应，告诉客户端要调用哪个工具



为什么用户问的是天气，客户端要把所有的工具列表都给到服务端，而不是只给get_current_weather呢？



因为客户端是没有大模型的，他没有办法根据用户的一句话：“请问杭州今天的天气如何？”就能判断出要调用哪个工具。



**他发送请求给服务端就是为了让服务端的大模型告诉他，针对用户的这个问题，应该调用哪个工具？**



因为客户端把所有的信息都给可以服务端：包含用户的问题和所有的工具详细描述，因此服务端的大模型可以根据意图识别判断这个时候需要调用：get_current_weather这个工具



于是服务端返回给客户端如下内容：



```JSON
{
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": null,
                "tool_calls": [
                    {
                        "id": "call_abc123",
                        "type": "function",
                        "function": {
                            "name": "get_current_weather",
                            "arguments": "{\"location\": \"杭州\"}"
                        }
                    }
                ]
            }
        }
    ]
}
```



**你会发现返回的content 为空，但是tool_calls却有内容**



这代表着本次服务端告诉客户端，我先不回答用户的问题，但是我先告诉你：



**你需要调用的是get_current_weather这个工具，并且参数都帮你组装好了**



## 第四步：客户端执行工具调用



客户度端收到服务端的指令，解析出要到用的工具名称和参数，然后在本地执行代码（这时候调用的是天气API）。



**PS：关于API的定义：非程序员同学请自行百度**



于是客户端得到了杭州的天气



```json
{
    "temperature": "25",
    "unit": "celsius",
    "description": "晴朗"
}
```



## 第五步：客户端再次发消息给服务端



客户端将执行结果包装成一条新的消息，连同之前的对话历史，再次发送给服务端：



这里的上下文包括：



- 用户的问题：请问杭州今天的天气如何？
- 服务端第一次的回答：要调用get_current_warther这个工具
- 客户端调用工具后的结果：**"{\\"temperature\\": \\"25\\", \\"unit\\": \\"celsius\\", \\"description\\": \\"晴朗\\"}"**



```JSON
{
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": "请问杭州今天的天气如何？"
        },
        {
            "role": "assistant",
            "tool_calls": [
                {
                    "id": "call_abc123",
                    "type": "function",
                    "function": {
                        "name": "get_current_weather",
                        "arguments": "{\"location\": \"杭州\"}"
                    }
                }
            ]
        },
        {
            "tool_call_id": "call_abc123",
            "role": "tool",
            "name": "get_current_weather",
            "content": "{\"temperature\": \"25\", \"unit\": \"celsius\", \"description\": \"晴朗\"}"
        }
    ]
}
```



## 第六步：服务端给出最终回答，客户端显示



服务端的大模型收到了客户端完整的上下文之后，就可以生成自然语言回复给客户端了



```json
{
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "杭州今天天气晴朗，气温 25 摄氏度。"
            }
        }
    ]
}
```



于是客户端收到消息，返回给用户：**杭州今天天气晴朗，气温 25 摄氏度。**



以上就是Function Calling的核心流程



# 为什么需要 MCP



不得不承认，Function Calling很巧妙，但是他有一个核心的局限：没有标准化。



Function Calling 由 OpenAI 首创，而且其 JSON 结构已公开，很多的大模型都已经支持这个方法了



**但是目前未有独立标准组织维护，主要由 OpenAI 文档定义**



在MCP出现前，接入不同 API 或工具需各自编写适配逻辑，导致“ N \* M ”集成问题，接口调用方式千差万别，维护与扩展成本极高



比如同样都是调用一个天气的查询工具，ChatGPT要写一套代码，DeepSeek也要写一套代码，用下面这个图会非常的清晰



![](https://feishu.cn/file/M0BCbnUXHoAMGdx8zb5ca9GTnyf)



# MCP的三个核心角色



<callout emoji="🎼">
**用一句话来说明 MCP的核心价值：一次构建，处处可用**
</callout>



为了解决 Function Calling 的问题，Anthropic公司于2024年11月推出并开源了MCP这种新的、更灵活的标准。



MCP核心定义了3 个角色，并且明确了他们之间的协作模式



![](https://feishu.cn/file/E28Rb8nmCokkOIxWkPLcpMU0nFd)



## **第一个角色：主机（Hosts）**



Host 是基于 LLM 的应用，它作为中枢，负责管理 Client 实例、调度模型与工具交互，以及处理用户界面逻辑



比如扣子空间可以调用多个 MCP工具来完成任务，那么扣子空间就是 Host



![](https://feishu.cn/file/YycJb8q0posBguxDhH9ca4wRnvk)



## **第二个角色：服务器（Server）**



Server（服务器） 是核心。



在 MCP 的世界里，**Server 是指那个掌握着上下文信息、并按照 MCP 规范提供这些信息的系统**。



它可以是一个数据库，一个 API 接口，或任何能够响应模型请求的外部工具。它的本质是服务提供者



![](https://feishu.cn/file/FoFUbylAPoBFeMxsy14cxnkmnic)



## **第三个角色：客户端（Client）**



客户端是连接主机和服务器的桥梁，嵌入在主机中，**与服务器是 1:1 对应关系**



其主要职责是连接管理，即与服务器建立和维护连接，从而帮助主机实现与外部数据的交互



---



有一张非常经典的**笔记本电脑扩展坞**的图片非常适合来快速理解 MCP



![](https://feishu.cn/file/HuMYbeBLdorVMgxeMd1cb1zSnLh)



有一台笔记本电脑想要跟外部数据通信，但是由于笔记本电脑的接口有限，没有办法访问更多的外部数据



这时候我们会外接一个扩展坞，这个扩展坞会通过标准化的协议接口，为电脑提供连接各种外部系统的能力



**这个扩展坞本身就是 MCP协议**



而无数的外设可以通过扩展坞连接到电脑，**这些外设就是 MCP的 Server角色**



**笔记本电脑上和这些外设通信的独立进程就是 MCP Client的角色**



---

# 写在最后 & 我对MCP的看法



当初MCP刚出来的时候，各种炸裂，给我的感觉是MCP出来之后，好像大模型调用工具更智能了



确实，从 Function Calling 到 MCP，大模型与外部世界交互的方式正变得越来越标准化、灵活和强大。



MCP 通过动态发现、解耦、并发调用和流式响应等特性，为构建更复杂、更智能、能够接入万千工具的 AI Agent 系统构建了基础



但是再次回到大模型工具调用工具的问题出发点，我谈下我的看法，各位小伙伴有任何问题欢迎在评论区与我交流



PS：我并没有说MCP不行，而是说它可能被一些自媒体夸大或者说曲解了，我希望这段文字可以引发你的思考



<callout emoji="💡">
MCP是一种协议，也就是让大模型调用工具的方式标准化了。
但是我们再回到那个问题的起点：解决大模型调用工具的问题
这里涉及到两个问题：
1. **让大模型能够调用工具**：MCP和Function Calling解决了
2. **让大模型能够识别用户意图，准确的调用工具（这块好像还不太好）**
这也是Coze之前为什么要有工作流，因为工作流是固定好的路程，不会让大模型自己的随意发挥。
在通用模型能力没有提高的情况下，就算有了MCP这个协议，外挂了很多的MCP工具，但是模型使用工具的能力不行，工具再多有什么用呢？
这让我想到了GPT的Deep Research很强，为什么强，是因为他工具多么？不是，是因为DR背后的模型是经过专门训练优化的（不是通用大模型了）
所以当下MCP是让大模型接入工具的流程变得标准化，但是并没有提升模型的能力，那么工具再多可能也没啥用，就好比Coze智能体中放入一堆的插件，但是效果一般
所以要解决大模型调用工具更精准的问题，有两点：
1. 提升通用模型调用工具的能力，做到无论添加什么工具，都可以让模型精准调用
1. 训练专有的模型，该模型专门针对特定场景的工具集合做优化，提升调用准确率
</callout>
