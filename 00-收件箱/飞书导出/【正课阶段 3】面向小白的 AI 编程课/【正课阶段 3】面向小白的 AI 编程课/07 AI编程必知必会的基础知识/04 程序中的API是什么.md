---
title: "程序中的API是什么"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/FHMYwB7epiTJt1kirNTcLiLMn1f"
node_token: "FHMYwB7epiTJt1kirNTcLiLMn1f"
obj_type: "docx"
document_id: "HWaHdDSEboAb9Uxo9Bsc8SOlncf"
revision_id: "11"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/FHMYwB7epiTJt1kirNTcLiLMn1f>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>程序中的API是什么</title>

<callout emoji="✨">
这篇文章的目的：
**让非程序员同学真正理解 API 的概念，并且亲手调通一个大模型的 API。**
概念部分我会用最通俗的方式来讲，实操部分我会手把手带你完成。
当你亲手调通 DeepSeek API 的那一刻，你会发现 API 并没有那么神秘。
</callout>



# 一、为什么要了解 API



在 AI 时代，你一定会频繁听到 API 这个词：



- 我们要调用 DeepSeek 的 API
- **这个 Agent 工具需要配置大模型的 API**
- **把你的 API Key 填进去就能用了**



如果你不理解 API 是什么，你会在这些场景里一次又一次地卡住，或者说你只能照做，但照做最大的问题就是，一旦出了问题，你不知道怎么解决



但如果你花 30 分钟把这篇文章读完并且实操一遍，以后再碰到任何 API 相关的内容，你都不会发怵了



# 二、初识 API



## 1）什么是 API



API 全称：**应用程序接口（Application Programming Interface）**



名字看起来很唬人，但概念其实很简单。我换一个方式来说：**接口人**



想象一个场景：你因为工作需要跟一家公司谈业务，但对方老板不想直接跟你见面，于是对方指定了一个接口人来传递消息。



你想说什么，告诉接口人；对方想回复什么，也通过接口人转达给你



<whiteboard token="Y1v5wk8MohrE3gb6kZwcm1E7nLd"></whiteboard>



接口人是用来在**人和人之间传递信息**的



那么 API（应用程序接口）就是用来在**程序和程序之间传递信息**的



这里的应用程序就是你日常用的各种软件：DeepSeek 是一个应用程序，微信也是一个应用程序，你用的各种 AI 工具都是应用程序



## 2）谁在跟应用程序通信



有两类角色需要跟应用程序通信



**人可以跟应用程序通信：**比如你打开 DeepSeek 的网页，输入一个问题，DeepSeek 返回一个回答。这就是你在跟 DeepSeek 这个应用程序通信



**程序也可以跟应用程序通信：**比如你用的某个 AI Agent 工具，它背后需要调用 DeepSeek 的大模型能力。



这个 Agent 工具本身就是一个程序，它通过 API 跟 DeepSeek 的服务器进行通信，把你的问题传过去，再把 DeepSeek 的回答拿回来



![](https://feishu.cn/file/YzTubN9ovo99msxgzz1cqgbknac)



当你在网页上跟 DeepSeek 聊天的时候，其实浏览器的背后也是在通过 API 跟 DeepSeek 的服务器通信。



只不过浏览器帮你把这个过程藏起来了，你感知不到而已



![](https://feishu.cn/file/T0cObrBYLoQFhIx0edRcbh79nlo)



## 3）一个具体的例子



你有没有想过，为什么很多 AI 工具都可以接入 DeepSeek 的大模型？



原因很简单：**DeepSeek 提供了 API 给其他程序使用**



任何工具只要按照 DeepSeek 规定的格式，把用户的问题通过 API 传给 DeepSeek 的服务器，DeepSeek 就会返回大模型处理后的结果



这就是 API 的核心作用：**让不同的程序之间可以互相通信、互相协作**



# 三、API 的三要素



讲完了 API 是什么，接下来我们来看：跟一个 API 通信，需要哪些东西？



答案是三个要素：



1. **请求地址**：去哪里找这个程序
2. **输入参数**：你想跟这个程序说什么
3. **返回结果**：这个程序给你的回复



用生活中的例子来类比。当你需要跟一个人（叫小A）进行一轮完整的对话时



- 首先你要**找到小A的位置**，确保你们之间可以传递消息 → 对应**请求地址**
- 然后你要**准备好想说的话** → 对应**输入参数**
- 最后你要**接收小A的回复** → 对应**返回结果**



![](https://feishu.cn/file/DA4hbLZd5ozMOWxInvnc9cCfn3c)



# 四、请求地址



请求地址的作用就是：**定位到你要通信的那个程序在哪里**



我们以 DeepSeek 对话 API 的请求地址为例：



```Plain Text
https://api.deepseek.com/chat/completions
```



这串地址看起来很长，但其实可以拆成三部分：



- `https://` → **通信协议**
- `api.deepseek.com` → **域名**
- `/chat/completions` → **接口路径**



下来给大家讲一下这三部分的作用



## 通信协议



`https://` 代表你跟这个 API 通信时使用的"语言"



就好比人跟人说话可以用中文、英文，程序跟程序通信也有自己的"语言"。



最常见的就是 `http://` 和 `https://` 两种



其中 `https://` 更安全，所以现在大多数 API 都用它



这个不需要深究，你只要知道看到 `https://` 开头就是在说"这是一个网络通信地址"就行



## 域名



`api.deepseek.com` 是 DeepSeek API 服务器的域名



如果你已经了解了服务器的概念，你会知道每台服务器都有一个 IP 地址（类似门牌号），而域名就是 IP 地址的别名，方便人类记忆



`api.deepseek.com` 的背后就是 DeepSeek 某台服务器的 IP 地址。你访问这个域名，就是在找到 DeepSeek 的服务器



## 接口路径



`/chat/completions` 是接口路径



一台服务器上可以运行很多功能。DeepSeek 的服务器上既有对话功能，也有查询余额的功能，还有其他功能。怎么区分你想用哪个功能？就靠接口路径



举个例子：

- `https://api.deepseek.com/chat/completions` → 这是**对话**功能



- `https://api.deepseek.com/user/balance` → 这是**查询余额**功能



它们的域名一样，但接口路径不一样，所以定位到了不同的功能



![](https://feishu.cn/file/DTACbUO6iooRlzx4DFZcUgAXn2d)



# 五、权限与 Token



搞懂了请求地址之后，还有一个问题：**凭什么人家的 API 要给你用？**



想象一下，DeepSeek 的 API 每调用一次都会消耗计算资源，这些资源是要花钱的。



DeepSeek 怎么知道是谁在调用，该扣谁的钱？



答案就是 **API Key**（有时候也叫 Token）



<callout emoji="✨">
⚠️ 这里的 token 不是指我们讲大模型时提到的 AI 的 token
</callout>



API Key 就是你的**身份标识**。你在 DeepSeek 平台上注册账号后，可以生成自己的 API Key。



每次你调用 DeepSeek 的 API 时，都需要把这个 API Key 带上，这样 DeepSeek 就知道是你在调用，就能精准地扣你的费用



这就好比你去银行取钱要带身份证一样。没有身份证（API Key），银行（DeepSeek）不会理你



# 六、输入参数与返回结果



## 1）输入参数



输入参数就是你想跟 API 说的话



对于 DeepSeek 的对话 API 来说，最核心的输入参数就是：**你想问 DeepSeek 什么问题**



当然，除了问题本身，你还可以告诉 API 一些额外的信息，比如：

- 你想使用哪个模型（DeepSeek 有不同的模型可以选择）
- 你希望回复的风格是什么（比如更严谨还是更有创意）



这些输入参数有一种固定的格式，这种格式就是 **JSON**。在后面的实操环节你会看到具体长什么样，这里先不展开



## 2）返回结果



返回结果就是 API 给你的回复



对于 DeepSeek 的对话 API 来说，返回结果里最核心的内容就是：**DeepSeek 大模型生成的回答**



返回结果同样是 JSON 格式。你会在实操环节看到完整的返回内容



## 3）关于请求方式的补充



在实际使用中，API 有两种常见的请求方式：



- **POST 请求**：一般用于"提交数据"的场景。比如你给 DeepSeek 发送一个问题，这就是在提交数据，所以用 POST。
- **GET 请求**：一般用于"查询数据"的场景。比如你查询 DeepSeek 账户余额，这就是在查询，所以用 GET。

对应的，输入参数也有两种携带方式：

- **Body 参数**：参数以 JSON 格式放在请求体里面。POST 请求通常使用这种方式。
- **Query 参数**：参数直接拼在请求地址后面。GET 请求通常使用这种方式。比如：

```Plain Text
https://api.example.com/users?name=大圣&age=18
```



问号后面的 `name=大圣&age=18` 就是 Query 参数



这些概念你现在有个印象就行，后面实操的时候你会自然地理解它们



# 七、实操：亲手调通 DeepSeek 的 API



好了，概念讲完了，接下来，我带着大家：**亲手调通一个大模型的 API**



<callout emoji="✨">
在开始之前，我想多说两句，我选择 DeepSeek 来做演示
但我真正希望你学到的：**不是如何调通 DeepSeek 的 API，而是调通任何一个 API 的底层逻辑**
未来你会接触到很多很多的 API：Kimi 的、Minimax 的、Claude 的、ChatGPT 的，以及各种你现在可能还没听说过的服务。它们的平台界面不一样，API 文档的格式也不一样，但底层逻辑永远是相同的：
1. **找到平台的开放平台或开发者页面**
2. **注册账号，获取 API Key**
3. **阅读 API 文档，搞清楚请求地址和参数格式**
4. **用工具发送请求，调通它**
5. **充值，常态化使用**
这五步适用于你未来遇到的任何 API。
所以接下来的实操，请你带着举一反三的心态来跟，不要只是照猫画虎地跑通。
**理解每一步在做什么、为什么这么做，比单纯跑通结果重要一百倍**
</callout>



要完成这个实操，我们需要准备两样东西：



1. **DeepSeek 的 API Key**（身份标识）
2. **一个可以发送 API 请求的工具**



## 第一步：获取 DeepSeek 的 API Key



1. 打开 DeepSeek 开放平台：https://platform.deepseek.com
2. 注册并登录你的账号



![](https://feishu.cn/file/L1cBb5r4woo08DxLEZIcwYTPnNh)



1. **在左侧菜单找到 API Keys**
2. 点击**创建 API Key**，系统会生成一串类似 `sk-xxxxxxxxxxxxxxxx` 的字符串



![](https://feishu.cn/file/EHZFbBT8IowxRwxOMLlc1tf6ngc)



**请务必把这串 API Key 复制保存好，不要透露给别人，因为别人拿到你的 APIK 就相当于拿到了你家的钥匙**



DeepSeek 的 API key 只显示一次，也就是在你创建的时候，你得把它复制下来，后面就看不到了



## 第二步：阅读 API 文档



拿到 API Key 之后，你要做的第二件事是：**去看它的 API 文档**



**任何一家正规的 API 厂商都会提供文档，这是标配。**



DeepSeek 的 API 文档地址是：[https://api-docs.deepseek.com/zh-cn/](https://api-docs.deepseek.com/zh-cn/)



打开文档之后，你需要关注三样东西：



1. **请求地址（域名 + 接口路径）**：文档会告诉你该往哪个地址发请求。DeepSeek 的对话接口地址是



<callout emoji="✨">
https://api.deepseek.com/chat/completions
</callout>



1. **请求格式**：文档会告诉你输入参数长什么样、需要哪些字段。比如 DeepSeek 要求你传入 `model`（模型名称）和 `messages`（对话内容）

![](https://feishu.cn/file/DYTNb8zHCoUE1ixIyUccv9sdnWb)



1. **调用示例**：大多数文档都会直接给你一个 curl 命令或代码示例，你照着改就能跑



<callout emoji="✨">
注意，下面的 CURL 方式只是让你用来测试，我们大多数情况下根本用不上这种方式，你不需要自己写那么复杂的命令
</callout>



![](https://feishu.cn/file/XM9nb0dZeocvq5xRfgucrPqenkh)





说白了，调通一个 API 就是这么回事：



**在文档里找到请求地址、找到参数格式、找到调用示例，然后把你的 API Key 填进去**



---



**重要‼️**



<callout emoji="✨">
这里再教你一个 AI 时代的技巧：
**当你看不懂某家的 API 文档时，直接把文档内容复制下来，发给你的 AI（DeepSeek、ChatGPT、Kimi 都行），让 AI 帮你读。** 
你可以跟 AI 说：帮我看看这份 API 文档，告诉我该怎么调用它的对话接口。
AI 会非常清楚地告诉你请求地址是什么、参数该怎么填、命令该怎么写
**记住这个方法，它适用于你未来遇到的任何 API 文档：Kimi 的、Minimax 的、OpenAI 的，都一样**
</callout>



## 第二步：用 curl 命令调用 API



接下来给大家讲一下用CURL命令去调用API，这种方式乍一看好像只有程序员才能玩得转，但我告诉你，静下心来花个5分钟，你就知道它什么意思了



curl 是一个命令行工具，几乎所有的电脑都自带。它的作用就是：**从命令行发送一个网络请求**



打开你电脑的终端（Windows 上叫 命令提示符 或 PowerShell，Mac 上叫终端），输入以下命令：



![](https://feishu.cn/file/JYRxbSYnboYE81x2fUIcPewpnVc)



**在执行之前，请把 `你的API_Key替换到这里` 换成你刚才保存的 API Key。**比如我的是：



```Bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-07860036d0bc45fe9c0a581b82d0a" \
  -d '{
        "model": "deepseek-chat",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "你是谁，请介绍一下自己"}
        ],
        "stream": false
      }'
```



按下回车，等待几秒钟，你就会看到 DeepSeek 返回的结果了！



如果你看到了一段包含 DeepSeek 回答的内容，那么**你已经成功调通了人生中第一个大模型 API**



![](https://feishu.cn/file/YQVmbtpuFoTNLFxYqypc1yUXnYD)



### 拆解这条 curl 命令



我们来逐行看看这条命令里每一部分对应的是什么：



```Plain Text
curl https://api.deepseek.com/chat/completions
```



这一行是**请求地址**，告诉 curl 我们要访问 DeepSeek 的对话功能



---



```Plain Text
-H "Content-Type: application/json"
```



这一行告诉 API：我发给你的数据格式是 JSON。（`-H` 代表 Header，也就是请求头信息）



---



```Plain Text
-H "Authorization: Bearer sk-xxxxxxxxxx"
```



这一行是**权限验证**，把你的 API Key 带上，证明你的身份



---



```Plain Text
-d '{
      "model": "deepseek-chat",
      "messages": [
        {"role": "user", "content": "你好，请用一句话介绍你自己"}
      ],
      "stream": false
    }'
```

这一行是**输入参数**（Body 参数），用 JSON 格式告诉 DeepSeek：



- `model`：我要用的模型是 deepseek-chat
- `messages`：我想问的问题是 "你好，请用一句话介绍你自己"
- `stream`：不需要流式输出，一次性给我完整的回答



看到了没有？前面讲的概念：请求地址、权限、输入参数，全都在这一条命令里体现了



### 我记不住这种命令怎么办？



再说一次，我们这是AI时代，curl这种语法，AI比谁都清



这些命令你根本不需要记，当你需要的时候  

打开任何一个 AI 对话工具（DeepSeek、ChatGPT、Kimi 都行），跟它说：



> 帮我写一条 curl 命令，调用 DeepSeek 的对话 API，我的 API Key 是 sk-xxx，我想问的问题是：今天天气怎么样"



AI 会直接帮你生成完整的 curl 命令，你复制粘贴到终端就能跑



**这就是 AI 时代学编程的方式：你不需要记住所有的语法，你只需要理解概念，然后让 AI 帮你写**



<callout emoji="✨">
当然这里要确定的是，AI 知道 DeepSeek 的 API 地址
</callout>



## 第三步：用在线 HTTP 测试工具调用 API



<figure view-type="Preview"><source mime="video/mp4" origin-height="1880.000000" origin-width="3004.000000" token="BZRpbdOmcoP0Ifxn2Ywcoh7enCg"/></figure>



如果你对命令行还是不太习惯，没关系，还有更直观的方式



在线 HTTP 测试工具是一个网页，它把 API 请求的各个部分（地址、Header、参数）做成了表格的形式，你只需要往里面填内容就行。



这里推荐一个工具：https://tool.chinaz.com/tools/httptest.aspx



使用方式如下：

1. **请求方式**选择：POST
2. **请求地址**填入：`https://api.deepseek.com/chat/completions`
3. **Header** 填入两条： 

   - `Content-Type: application/json`
   - `Authorization: Bearer 你的API_Key`
4. **Body** 填入：

```JSON
{
  "model": "deepseek-chat",
  "messages": [
    {"role": "user", "content": "你好，请用一句话介绍你自己"}
  ],
  "stream": false
}
```

1. 点击提交，等待返回结果



你会发现，不管是用 curl 命令还是用在线工具，**本质上做的是同一件事**：



向一个地址发请求、带上身份标识和参数、拿到结果，**工具不同，但 API 的三要素是完全一样的**



## 第四步：看懂返回结果



当你成功调用之后，DeepSeek 会返回一段 JSON 格式的数据，大致长这个样子：



```JSON
{
    "id": "d2ea6b14-6413-494f-b94d-06b3f8fff4f9",
    "object": "chat.completion",
    "created": 1773046031,
    "model": "deepseek-chat",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "你好，我是DeepSeek，一个由深度求索公司创造的AI助手，致力于用热情和细心为你提供帮助！😊"
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 11,
        "completion_tokens": 28,
        "total_tokens": 39,
        "prompt_tokens_details": {
            "cached_tokens": 0
        },
        "prompt_cache_hit_tokens": 0,
        "prompt_cache_miss_tokens": 11
    },
    "system_fingerprint": "fp_eaab8d114b_prod0820_fp8_kvcache"
}
```

你现在不需要看懂所有的字段，只需要找到最关键的部分：

`choices` → `message` → `content`

这里面的内容就是 DeepSeek 大模型给你的回答。



其他字段的含义：

- `model`：使用的模型名称
- `usage`：这次调用消耗了多少 Token（可以理解为字数，用来计费）
- `finish_reason`：回答结束的原因（`stop` 表示正常回答完毕）



这段返回的结果是一个叫 JSON 的格式，我后面也会出教程给大家讲到，这里你先不用关心



<callout emoji="✨">
你要知道，这个 JSON 的返回结果不是给人看的，它是给应用程序看的
**应用程序会把这段 JSON 里面的内容解析出来，翻译成人能看懂的语言，渲染在界面上**
</callout>



# 八、如何调用其他平台的API



<figure view-type="Preview"><source mime="video/mp4" origin-height="1956.000000" origin-width="3004.000000" token="HfUZbNOtwok0PLx3Z2JchBl3nch"/></figure>



# 写在最后



最后希望这节课能带给你它能带来的价值
