---
title: "10｜程序中的API是什么"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/KIhnwTnuuiy11rkU0z6cz5WFn1d
node_token: KIhnwTnuuiy11rkU0z6cz5WFn1d
obj_token: UDPpdVSx2oMhA9xDiRwcjZ1PnUf
obj_type: docx
space_id: 7334260678754041858
space_name: "付费星球/AI零基础"
depth: 2
breadcrumb:
  - "AI零基础到智能体高手"
  - "小白也能听懂的AI编程基础课"
  - "10｜程序中的API是什么"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 14
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - AI零基础到智能体高手
---

# 10｜程序中的API是什么

> [!info] 位置
> AI零基础到智能体高手 › 小白也能听懂的AI编程基础课

<callout emoji="❤️">
这篇文章必须加个开篇，因为这应该这个教程中最难写的一篇了。
一共花费了我3天的晚上，大概10个小时
这篇文章我希望可以带给你：
- 非编程小白真正了解API的概念，我们已经了解了JSON，再了解完API，就完美了
- 手把手教你调通Coze的API，这可能是你第一个调用API，那种感觉非常爽！
这篇文章真正做到了授人以鱼，又授人以渔！希望能对你有帮助～
</callout>

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnyiu7ufkkad92j1258ry7?from=ccm" type="iframe"></readonly-block>

# 引言

在编程概念中，API（应用程序接口）这个概念非常重要。

为了完整的讲清楚API的概念，我们先需要了解两个概念

- <cite doc-id="BohSwor9NibXtMk7nqjcyvJRnlg" file-type="wiki" title="06｜数据的桥梁，理解与应用JSON" type="doc"></cite>
- <cite doc-id="Gxpnw56QUi06aZk3uK9c9v59naf" file-type="wiki" title="08｜数据类型，一切数据的基础" type="doc"></cite>

本文则是关于API的收尾章节

# 初识API

API全称：应用程序接口

**我们先来理解下什么是接口**，我换个方式来说：接口人

当你因为工作需要和一个人谈业务的时候，但是对方不想直接跟你见面，所以对方指定一个接口人来传递消息

然后你所有信息的传达都是通过这个接口人来完成的

<whiteboard token="GAxzwQMSAhyfMubs4Rec3ayandd"></whiteboard>

接口人是用来进行人和人之间传递信息的

**那么API（应用程序接口）就是用来和应用程序进行传递信息的**

那么应用程序又是什么呢？

- Coze就是个应用程序
- Kimi也是个应用程序
- 你用的各种软件都是应用程序

**谁会和应用程序进行通信呢？**

- 人可以和应用程序通信
- 其他应用程序也可以和应用程序通信

什么情况下需要和应用通信通信呢？

既然我们在学习Coze，我们就举个Coze的例子，你有没有想过为什么字节Coze可以支持Kimi的大模型？

> [!abstract]- 🖼 图片展示的是一个应用程序的模型设置界面，处于“预览与调试”选项卡下。界面
> 图片展示的是一个应用程序的模型设置界面，处于“预览与调试”选项卡下。界面中“模型”部分显示当前选中“豆包·Function call模型 32K”。下方有多个模型选项，其中“Moonshot（8K）”“Moonshot（32K）”“Moonshot（128K）”被红色框突出显示。这些模型选项对应不同大小的参数量，分别为8K、32K、128K。该图片与上下文介绍应用程序接口相关，可能用于说明应用程序中可选择的不同模型类型。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JwDOb3Rt4ojVTjxJTsAcdQmenhc) · `JwDOb3Rt4ojVTjxJTsAcdQmenhc`

因为Kimi这家公司提供了一个（或者多个）应用程序接口给到Coze使用。

Coze只要将用户的输入给到Kimi提供的API，然后这个API就会返回经过Kimi大模型处理的结果给到Coze

# API组成的三要素

老样子，在正式的学习API之前，我们先要对其进行抽象，用生活中容易理解的场景进行类比。

前面我们讲到了，API是用来和应用程序进行通信的。

接下来我们就来讲解一下，在与应用程序通信时需要的三个要素。

- 应用程序的请求地址
- 输入参数
- 接收应用程序的返回参数

用生活中的例子来说明与人通信需要哪些要素，方便大家理解。

当我们需要跟一个人（名字为小A）进行完整的一轮对话时，我们需要这么几步：

- 找到小A的位置，确保你们两个之间可以相互传递消息（**确定应用程序的请求地址**）
- 准备好你想要跟小A说的话（**输入参数**）
- 接收小A说的话（**接收应用程序的返回参数**）

# 以Coze API文档为例

对于非程序员而言，我们平常90%都是阅读别人家提供的API文档。

因此这里我们就带领大家阅读一下Coze的API官方文档

Coze API官方文档：[扣子 - 开发指南](https://www.coze.cn/docs/developer_guides/chat_v3)

我们以和Coze Bot对话的API为例子，来解读下API的文档。

接下来我们会通过3个部分来讲一个API的组成揉碎掰开了来讲

- 请求路径的定义
- 输入参数
- 返回响应

# 请求路径定义

> [!abstract]- 🖼 图片展示了API基础信息相关内容。其中，请求方式为POST；请求地址为h
> 图片展示了API基础信息相关内容。其中，请求方式为POST；请求地址为https://api.coze.cn/v3/chat；权限为chat，需确保调用该接口使用的个人令牌开通此权限；接口说明为调用此接口发起一次对话，支持添加上下文和流式响应。该图片与文档中请求路径定义及请求方式部分内容相关，直观呈现了API基础信息的具体参数设置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/GnKCb7w32owYwGx1j4bcyEgAn3c) · `GnKCb7w32owYwGx1j4bcyEgAn3c`

## 请求方式

> [!abstract]- 🖼 图片展示了API请求方式为POST的内容。其中“请求方式”以红色框突出显
> 图片展示了API请求方式为POST的内容。其中“请求方式”以红色框突出显示，其右侧对应“POST”。下方还有请求地址、权限、接口说明等信息，如请求地址为https://api.coze.cn/v3/chat，权限为chat，接口说明为调用此接口发起一次对话，支持添加上下文和流式响应。该图片与文档中介绍API请求方式的内容相关，直观呈现了POST请求方式在API中的具体体现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/C5n9bfDZbo6SslxPmVkcc3SknLh) · `C5n9bfDZbo6SslxPmVkcc3SknLh`

这是一种约定，一个API有两种最常见的请求方式

- POST（一般用于写入类的API）
- GET（一般用于查询类的API）

## 请求地址

> [!abstract]- 🖼 图片展示了API请求地址的相关信息。其中“请求地址”栏以红色框突出显示，
> 图片展示了API请求地址的相关信息。其中“请求地址”栏以红色框突出显示，内容为“https://api.coze.cn/v3/chat”，表明这是API通信时确定应用程序位置的关键部分。该图片与上下文紧密相关，上下文在介绍API请求地址时提到，其作用是确定需要通信的应用程序位置，而图片直观呈现了请求地址的具体内容，帮助理解其在API通信中的重要性。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WoqDbDgi4oaS89xF52QcDtBJn4e) · `WoqDbDgi4oaS89xF52QcDtBJn4e`

这是API非常重要的一环，请求地址的作用就是确定需要通信的应用程序的位置

```HTTP
 https://api.coze.cn/v3/chat
```

我们将请求地址进行拆解：

- https://（**一种通信协议**）
- api.coze.cn（**域名，这块会详细讲**）
- /v3/chat（**接口的路径**）

这三部分组成就可以完整的确定一个功能点

### 通信协议

https:// 代表你使用这个API通信时使用的是https通信协议，所谓的通信协议可以类比人与人之间说话的语言，比如中文、英文等

程序之间的通信协议有很多，最常用的就是http:// 和https:// 两种

### 域名

域名大家肯定都不会陌生，比如：www.baidu.com

**在讲域名之前，我们需要先了解另一个概念：IP地址**

互联网是由无数台服务器（先简单理解为电脑）组成的一张网络，那么在这张网中是怎么找到每一台服务器的呢？

这里就是我们给每台服务器分配了一个**公网IP**地址，就好比给每一座房子分配了一个门牌号。

大家用这个网站来查看自己的IP地址：https://www.sojson.com/myip/

> [!abstract]- 🖼 图片展示的是一个查询IP地址的网页界面。上方显示“我的IP地址是：124
> 图片展示的是一个查询IP地址的网页界面。上方显示“我的IP地址是：124.160.201.181”，并有“其他IP查询”和“此处广告位招租”两个蓝色文字选项。下方表格中，左侧“IP”栏显示124.160.201.181，“IPv6”栏显示::7ca0:c9b5。右上角有“查看自己的IP地址”蓝色文字。该图片与文档中介绍IP地址的内容相关，用于直观呈现查询IP地址的结果，帮助理解互联网中服务器通过公网IP地址进行定位的原理。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/NlMjbWBcnoTkiBxz7Xqc4zcYnqS) · `NlMjbWBcnoTkiBxz7Xqc4zcYnqS`

---

那域名和IP地址的关系是什么呢？

简单来讲，域名和IP地址是一一对应的，域名的存在就是为了解决IP地址不好记忆的问题。

举个例子：今天你要访问百度，有两种选择：

1. 你访问百度的IP地址：https://180.101.50.188
2. 你访问百度的域名地址：https://www.baidu.com

正常人都会选择2，因为有意义，所以更容易被记忆。

**所以简单来讲：域名的在就是为了解决IP地址不好传播和记忆的问题**。

### 端口号

你可能会问，请求地址中没有端口号这么个东西呀？是因为这里有个默认值。

Coze的这个请求地址的完全体是：

```Markdown
https://api.coze.cn:443/v3/chat
```

你访问下面这两个链接，你就会发现，他们都指向了百度

- 访问：https://www.baidu.com
- 访问：https://www.baidu.com:443

为什么要讲端口呢，因为这是接口地址中一个非常重要的组成部分！

那既然重要，为什么要隐藏443呢？其实很简单：

https://www.baidu.com:443

看着是不是比

https://www.baidu.com 

要糟心？，糟心就对了，一串好好的文字后面带一串数字，多恶心，所以我们就进行了这么一个约定！

请注意这个约定仅仅适用于https://的通信协议，如果你使用的是http://的通信协议，端口号可以随意指定：

未来你可能看到如下的请求地址：

```HTTP
https://api.coze.cn/v3/chat(这是最标准的)

http://127.0.0.1:8080/v3/chat

http://176.288.198.21:9527/v3/chat
```

好了，言归正传，费了老鼻子劲，就是为了能不那么突兀的引出端口号，为什么要有端口号呢？

你可以这么理解：

- **ip地址指向的是你家的房子地址**
- **端口号则是你家每一间屋子的标识**

如果你家的房子很大，但是只有一间屋子，那是不是很尴尬，来了两个朋友就住不下了，除非大家男女混住，但是这样总归是不方便的！

**用专业的语言来讲：**

- **端口是一台服务器上可以和外部通信的通道。端口号则是一个通道的唯一标识**
- **端口号的范围从0到65535。**

你想一下，为什么你的一台电脑可以运行很多的应用程序，抖音、小红书等等，他们之间为什么不打架，因为他们使用的是不同的端口号。

你可以认为所有的设计都是为了解决某种问题，**端口号的存在则是为了解决通信时大家数据隔离的问题**

### 接口的路径

```Markdown
https://api.coze.cn/v3/chat
```

这里我们讲解一个请求地址的最后一部分：接口路径

- https://（**一种通信协议**）
- api.coze.cn（**域名，这块会详细讲**）
- **/v3/chat（接口的路径）**

接口路径是偏程序的概念了，不理解也没有关系，但是我还是想给你讲一讲！

前面讲过：

- 一个域名（其实就是一个IP地址）指向的是一台服务器（也就是一台电脑）
- 一台服务器上的很多端口号则是指向了不同的应用程序，例如Coze有自己的端口号

那接口路径又是什么作用呢？

当你使用Coze网页端的时候，你是不是会用到注册、登陆这些功能，那Coze怎么区分你是使用的登陆功能，还是注册功能呀？

这就是接口路径的作用了，我给大家举个例子：

- https://api.coze.cn/v3/login （这是登陆功能）
- https://api.coze.cn/v3/sign-up （这是注册功能）

发现了没有，他们的域名，端口号都一样，但是接口路径不一样，这样就可以定位到不同的功能了！

### 总结

最关键的总结部分来啦！

<callout emoji="🏆">
请求地址的目的就是为了定位到**某台机器**的**某个端口**的**某个功能点**
- 某台机器：ip或者域名来指定
- 某个端口：用端口号指定
- 某个功能点：用接口路径来指定
</callout>

## 权限

> [!abstract]- 🖼 图片展示了Coze API接口的相关信息。其中“权限”部分以红色框突出显
> 图片展示了Coze API接口的相关信息。其中“权限”部分以红色框突出显示，明确指出调用该接口使用的个人令牌需开通“chat”权限，详情可参考“鉴权”。该图片与文档中“权限”部分内容对应，直观呈现了使用Coze API接口时对权限的具体要求，帮助开发者了解在调用相关接口前需确保个人令牌已开通相应权限，以确保接口调用成功。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Y0JPbU1sJoYySqxiTGVcvkhxnzd) · `Y0JPbU1sJoYySqxiTGVcvkhxnzd`

权限我们只讲大家会遇到的场景：

想象一下，你给Coze充值了100块，你在使用Coze的API接口的时候，你使用一次，Coze就能扣你钱。

Coze凭啥能够精准的扣你的钱，肯定是因为他能识别你的身份呀。这个就叫做Token

你要使用Coze的API，你就得先生成自己的Token，这就是你的身份标识，当你使用Coze的API的时候，请你把Token给他带过去，这样他就知道是你啦

## 接口说明

> [!abstract]- 🖼 图片展示了Coze API中“基础信息”部分的接口说明。其请求方式为PO
> 图片展示了Coze API中“基础信息”部分的接口说明。其请求方式为POST，请求地址为https://api.coze.cn/v3/chat，权限为chat。接口说明指出，调用此接口可发起一次对话，支持添加上下文和流式响应。该图片与上下文紧密相关，上下文提到Coze API需先生成Token作为身份标识，此图则详细说明了调用接口的具体要求和功能，帮助开发者理解如何使用该接口进行对话。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CRbQbQ63LoxWunxjhbYc2P2Vnse) · `CRbQbQ63LoxWunxjhbYc2P2Vnse`

接口文档的文字说明，用人话给你讲清楚接口的作用

PS：一般接口说明讲的都不是人话，大家不要试图通过接口说明了解其作用，要亲自去测试

# 输入参数

这一环节我们正式进入到输入参数的部分，这部分为了方便大家理解，我进行了一些非专业的讲解，不过这样更有利于大家学习！

可以携带输入参数的部分有两个部分：

- 其中一个叫做Header
- 另一个叫做参数

## Header

> [!abstract]- 🖼 图片展示了API调用中Header部分的参数设置。包含两个参数：Auth
> 图片展示了API调用中Header部分的参数设置。包含两个参数：Authorization，取值为Bearer {Personal_Access_Token}，用于验证客户端身份的访问令牌，可在扣子平台生成；Content-Type，取值为application/json，解释请求正文的方式。该图片与上下文紧密相关，上下文介绍了Header的主要用途，即携带Authorization身份识别证明和Content-Type，此图直观呈现了Header参数的具体内容和取值说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/M5MqbtqzJoHJKRx6tAacBQNRnYg) · `M5MqbtqzJoHJKRx6tAacBQNRnYg`

Header我就不去解释他的含义了，大家记住他的主要用途就可以：

1. 如果你在调用API的时候需要使用到Header，那么90%的情况下你是为了携带**Authorization**，也就是你的身份识别证明
2. 另外就是Content-Type：这个一般就两个选择

   1. application/json
   2. **`application/x-www-form-urlencoded`**
3. 如果你真对Content-Type感兴趣，可以去问Kimi哈

> [!abstract]- 🖼 图片展示了Content-Type的常用类型，其中“applicatio
> 图片展示了Content-Type的常用类型，其中“application/json”被红色框突出显示，其含义为表示发送的是JSON格式的数据。此外，还列举了如text/html、text/plain等其他数据类型。该图片与文档中介绍Header输入参数部分内容相关，文档提到Header主要用于携带身份识别证明及Content-Type，而Content-Type是HTTP头字段，用于告知浏览器或服务器发送的数据是哪种类型，此图直观呈现了其常用类型，帮助理解Header中Content-Type的含义。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Gr7jb4gNjoLUz7xWsO3cLPS9nWc) · `Gr7jb4gNjoLUz7xWsO3cLPS9nWc`

Header的输入方式就是Key和Value，后面我在举例子的时候会讲到，大家不急。

总之一句话：Header理解起来有一些复杂，但是用起来很简单，所以不用深究

## API的入参

这一部分才是真正意义上的API的入参，也就是说，当你需要和另一个人沟通时，你需要说的话！

这一部分会涉及到两种情况，为了防止造成大家以后的困扰，这里必须都讲解一下。

一个API有两种最常见的请求方式

- POST（一般用于写入功能的API）
- GET（一般用于查询功能的API）

一个API的入参参数一般也有两种表示方式

- Query
- Body

大多数情况下，遵循这样的原则

<callout emoji="❤️">
- GET 请求中一般只会有Query形式的参数
- Post请求中一般都使用Body形式的参数，也可以用Query形式的参数，但是用的很少
</callout>

### GET请求 & Query形式的参数

[扣子 - 开发指南](https://www.coze.cn/docs/developer_guides/published_bots_list)

> [!abstract]- 🖼 图片展示了API接口信息，请求方式为GET，请求地址为https://a
> 图片展示了API接口信息，请求方式为GET，请求地址为https://api.coze.cn/v1/space/published_bots_list，权限为getPublishedBot，接口说明是调用接口查看指定空间发布到Bot as API渠道的Bot列表。该图片与上下文紧密相关，上下文在介绍API的入参时，提到一个API的入参参数一般有Query和Body两种表示方式，且GET请求中一般只会有Query形式的参数，此图即为一个典型的GET请求&Query参数的例子。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/PV02bsinqoASwuxtydTc6lYTnlb) · `PV02bsinqoASwuxtydTc6lYTnlb`

> [!abstract]- 🖼 图片展示了API的Query形式参数示例。表格中包含参数、类型、是否必选
> 图片展示了API的Query形式参数示例。表格中包含参数、类型、是否必选及说明四列。参数有space_id、page_size、page_index，类型均为String或Integer，其中space_id为必选，page_size和page_index为可选。space_id说明为Bot所在空间的唯一标识，page_size说明默认为20，page_index说明默认为1。该图片与上下文紧密相关，是对GET请求中Query形式参数的说明，为理解API入参参数的表示方式提供示例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UQPGbqRYCo39DJxzeL2cFGImn1b) · `UQPGbqRYCo39DJxzeL2cFGImn1b`

这里是一个典型的GET请求 & Query参数的例子。**如果文档中标注的是Query参数，这代表这些参数都是通过?放置在请求地址后面的，如下图所示**

<callout emoji="🏖️">
https://api.coze.cn/v1/space/published_bots_list?space_id=737620236629291&page_size=10&page_index=2
</callout>

这里面有三个请求参数

- 参数1:space_id，参数值：737620236629291
- 参数2:page_size，参数值：10
- 参数3:page_index，参数值：2

**为什么是这个样子？不用纠结，这是前辈们定下的规范哈，我们只要学习，不需要理解**

好了关于GET请求方式的入参，我们就讲完啦

### POST请求 & Body参数 & Query参数

我们用另一个API：[扣子 - 开发指南](https://www.coze.cn/docs/developer_guides/chat_v3)进行讲解POST请求的入参，PSOT的入参就用到我们使用的JSON啦！

**这个API将所有情况都用到了，用来做例子有些复杂，但是正好可以理解全面**

> [!abstract]- 🖼 图片展示了API的请求方式、请求地址、权限及接口说明等信息。其中，请求方
> 图片展示了API的请求方式、请求地址、权限及接口说明等信息。其中，请求方式为POST；请求地址为https://api.coze.cn/v3/chat；权限为chat，需确保调用该接口使用的个人令牌开通了chat权限；接口说明是调用此接口发起一次对话，支持添加上下文和流式响应。该图片与上文介绍API的入参内容相关，直观呈现了API请求的基本配置信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/P0gpbueCSoyCjqxPNN7cxhypnyP) · `P0gpbueCSoyCjqxPNN7cxhypnyP`

> [!abstract]- 🖼 图片展示了API中Query部分的参数说明。参数包括conversati
> 图片展示了API中Query部分的参数说明。参数包括conversation_id，类型为String，可选，说明标识对话发生在哪一次会话中，一个会话包含一条或多条消息，对话是会话中对Bot的一次调用，Bot会将对话中产生的消息添加到会话中，且只能有一个进行中的对话，否则调用此接口时会报错4016。该图片与文档中介绍API入参的内容相关，是对Query部分参数的详细说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Ulgzbj20soL8ltxBUQgcu771n5f) · `Ulgzbj20soL8ltxBUQgcu771n5f`

> [!abstract]- 🖼 图片展示了API中Query部分的参数说明。参数包括conversati
> 图片展示了API中Query部分的参数说明。参数包括conversation_id，类型为String，可选，说明标识对话发生在哪一次会话中，一个会话包含一条或多条消息，对话是会话中对Bot的一次调用，Bot会将对话中产生的消息添加到会话中，且只能有一个进行中的对话，否则调用此接口时会报错4016。该图片与文档中介绍API入参的内容相关，是对Query部分参数的详细说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/EfV4bxzQyopRxVx7wOdc7GWGnUh) · `EfV4bxzQyopRxVx7wOdc7GWGnUh`

PS：**如果文档中标注的是Body参数，代表这些参数是通过JSON的方式输入的**

这时候大家一定要先去了解下JSON的格式哦：<cite doc-id="Gye5w5o26iLzJWk4DAxcfDChnic" file-type="wiki" title="数据的桥梁｜理解与应用JSON" type="doc"></cite>

Body的入参很多，这里我就不一个个讲解了，这个太难讲了，而且没有必要。我们直接上例子吧：

PS：下面是一个简化版本的输入参数

```JSON
{ 
    "bot_id": "7348293334459318316", 
    "user_id": "123456789", 
    "stream": false, 
    "auto_save_history":true, 
    "additional_messages":[ 
        { 
            "role":"user", 
            "content":"今天杭州天气如何", 
            "content_type":"text" 
        } 
    ] 
}
```

# 返回的响应

返回的响应里面，大家会看到两个类型：

- 流式输出
- 非流式输出

这里大家学习非流式输出就好了，因为流式输出有点复杂。

非流式输出的内容就是JSON：：[[成为Agent工程师/Coze实战课项目/加餐文档/成为Agent工程师之AI编程/09｜程序中的变量|09｜程序中的变量]]

```JSON
{ 
    "data":{ 
        "id": "123", 
        "conversation_id": "123456", 
        "bot_id": "222", 
        "created_at": 1710348675, 
        "completed_at": 1710348675, 
        "last_error": null, 
        "meta_data": {}, 
        "status": "completed", 
        "usage": { 
            "token_count": 3397, 
            "output_count": 1173, 
            "input_count": 2224 
        } 
    }, 
    "code":0, 
    "msg":"" 
}
```

# API总结

请注意，本文讲的是API的概念，并不是给大家讲解Coze API的参数哦，因为Coze的API参数含义理解起来的话真的需要专业的程序员了。

本文是后续Coze接入微信教程的一个基础，在那个教程中我们不需要用到Coze的参数含义。

最后我们对API进行一个总结：

- 请求地址用来定位到某台服务器的某个端口的某个功能
- 输入参数用来携带传递给应用程序的入参
- 输出参数是应用程序返回的结果

大家先建立概念，然后在阅读API文档的时候就不会那么懵逼了，然后再结合API文档中的例子，基本是能够看到这个API的作用的

好了，接下来我们进入激动人心的环节：实操环节，我教你如何靠自己测试跑通一个API

# 如何测试一个Coze的API

要完成一个Coze的API测试，我们需要这么几步：

1. **在个人空间创建一个Bot**，发布的时候勾选Bot API（**这里不要用太复杂的Bot，弄个提示词Bot体验一把**）

**PS：注意，这里不一定要发布到Coze商店，只要发布到Bot as API就可以**

> [!abstract]- 🖼 图片展示的是Coze平台发布Bot的界面。在“选择发布平台”部分，有多个
> 图片展示的是Coze平台发布Bot的界面。在“选择发布平台”部分，有多个平台选项，如抖音、飞书等，其中“Bot as API”选项被红色框线突出显示，其状态为“已提交”。右上角有“发布”按钮。该图片与文档中“在个人空间创建一个Bot，发布的时候勾选Bot API”的内容相关，直观呈现了在Coze平台发布Bot时选择Bot as API的操作界面，帮助用户明确操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/S3nWbBrx1oLSlxxmEUrcJRpXn9f) · `S3nWbBrx1oLSlxxmEUrcJRpXn9f`

1. Coze发布成功之后，**在个人空间，点击刚刚发布的Bot，一定要在个人空间哦**

> [!abstract]- 🖼 图片展示了Coze平台个人空间中Bot管理界面。左侧导航栏选中“个人空间
> 图片展示了Coze平台个人空间中Bot管理界面。左侧导航栏选中“个人空间”，右侧显示多个Bot，其中“小红书API测试”Bot被红框突出显示，其下方有“豆包 - Function call模型”“最近编辑 00:13”等信息，以及“大圣 @lmh_2024”的发布者标识。该图片与上文“在个人空间，点击刚刚发布的Bot，一定要在个人空间哦”的内容对应，用于说明在个人空间找到并点击发布成功的Bot的操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Hen5bMHr5o09XUxnucHc9dhznwg) · `Hen5bMHr5o09XUxnucHc9dhznwg`

> [!abstract]- 🖼 图片展示了在浏览器中打开Coze Bot的页面，地址栏内容为“https
> 图片展示了在浏览器中打开Coze Bot的页面，地址栏内容为“https://www.coze.cn/space/7331741379686826035/bot/7393008672953679913”。画面中有一个红色框突出显示地址栏内容，并有红色箭头指向，旁边文字提示“复制地址栏内容”。这与文档中“在个人空间，点击刚刚发布的Bot，一定要在个人空间哦”及“提取最后面那串数字：7393008672953679913”的内容相关，用于指导用户获取Bot的地址栏内容以提取BotId。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AhZSbjfE2oMTgsxJ7crcOLjxnld) · `AhZSbjfE2oMTgsxJ7crcOLjxnld`

<callout emoji="🥖">
https://www.coze.cn/space/7331741379686826035/bot/7393008672953679913
</callout>

提取最后面那串数字：**7393008672953679913**

**BotId = 7393008672953679913**

1. 申请自己的Coze Token

https://www.coze.cn/open/oauth/pats

> [!abstract]- 🖼 图片展示的是Coze平台中个人访问令牌管理界面。界面上方有“个人访问令牌
> 图片展示的是Coze平台中个人访问令牌管理界面。界面上方有“个人访问令牌”“OAuth应用”“已授权应用”三个选项卡，当前选中“个人访问令牌”。下方列表显示了两个令牌信息，包括名称、创建时间、最近使用时间、过期时间、状态及操作栏。右上角有“添加新令牌”蓝色按钮，下方有红色箭头指向该按钮，旁边文字提示“点击添加”。该图片与文档中申请Coze Token部分内容相关，用于说明申请Token时添加新令牌的操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SnGsbzSbioA7nQxvBh8c4cDznLh) · `SnGsbzSbioA7nQxvBh8c4cDznLh`

> [!abstract]- 🖼 图片展示了在Coze中申请个人访问令牌的界面。名称处填写“Secret 
> 图片展示了在Coze中申请个人访问令牌的界面。名称处填写“Secret token”，过期时间选择“永久有效”，访问团队空间选“所有团队空间”，权限部分勾选“Bot”“chat”“getMetadata”。下方有“取消”和“确定”按钮，其中“确定”按钮被红色框突出显示。该图片与文档中“申请自己的Coze Token”部分内容相关，是申请Token时的操作界面展示，需将Token用于后续调用API等操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/U6N0bomTkot5LJxyVHNcbSHSnIb) · `U6N0bomTkot5LJxyVHNcbSHSnIb`

> [!abstract]- 🖼 图片展示了Coze平台申请个人访问令牌的界面。界面中强调令牌仅显示一次，
> 图片展示了Coze平台申请个人访问令牌的界面。界面中强调令牌仅显示一次，需保存在安全且可获取的地方，不可与他人共享或在代码中暴露。下方有“名称”“过期时间”“令牌”等信息栏，其中“令牌”处显示了长字符串的令牌，右侧有一个文件夹图标。该图片与文档中“申请自己的Coze Token”部分内容相关，是申请Token时的展示界面，用于说明获取令牌的过程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JInwbPU5kocgFkxm0wUcpX42nOg) · `JInwbPU5kocgFkxm0wUcpX42nOg`

**我们用到了调用API的第二个东西：Token = pat_etmxdA4eeGB4pKJZR0uyR89c7VWyc5J4rG7x3F3lf4fox11hcYZ2QyXnIYhP2jea**

OK，准备条件就绪，我们开始调用这个API，我们把各个部分准备好

<table><colgroup><col/><col/></colgroup><tbody><tr><td>请求地址</td><td>https://api.coze.cn/v3/chat</td></tr><tr><td>Header</td><td>Content-Type: application/json<br/>Authorization: <b>Bearer</b> <b>pat_etmxdA4eeGB4pKJZR0uyR89c7VWyc5J4rG7x3F3lf4fox11hcYZ2QyXnIYhP2jea</b></td></tr><tr><td>入参</td><td><pre lang="JSON"><code>{ <br/>    "bot_id": "<b>7393008672953679913</b>", <br/>    "user_id": "123456789", <br/>    "stream": false, <br/>    "auto_save_history":true, <br/>    "additional_messages":[ <br/>        { <br/>            "role":"user", <br/>            "content":"丽江旅游", <br/>            "content_type":"text" <br/>        } <br/>    ] <br/>}</code></pre></td></tr></tbody></table>

**PS：大佬们不要用我的Token和BotId测试哈，标黄的部分要换成你们的**

## 最新的V3异步接口

首先打开这个网址：[HTTP接口测试工具-在线模拟HTTP请求 - 站长工具](https://tool.chinaz.com/tools/httptest.aspx?jdfwkey=14snq2)

> [!abstract]- 🖼 图片展示了在ChinaZ在线调试工具中测试Coze API的界面。关键信
> 图片展示了在ChinaZ在线调试工具中测试Coze API的界面。关键信息有：请求地址为https://api.coze.cn/v3/chat，需注意HTTPS；请求方式为POST；Header设置有Content-Type和Authorization；入参为JSON字符串设置；返回值位于下方区域。该图与上文介绍的调用Coze API查看消息的步骤相关，直观呈现了操作界面及参数设置，帮助用户在实际操作中参考。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ZPmlb2zeqoW2uCxSflScRQaknTh) · `ZPmlb2zeqoW2uCxSflScRQaknTh`

如果返回如下格式，代表请求成功啦，你会发现没有返回值，**只有一个status：in_progress**

这个的意思是，这个请求已经在处理中了，你需要调用另一个接口去查询消息：

这里你需要获取两个返回值：

**"conversation_id": "7393010358887284777",**

**"id":"7393010358887301161"**

```Shell
{
    "data": {
        "id": "7393010358887301161",
        "conversation_id": "7393010358887284777",
        "bot_id": "7393008672953679913",
        "created_at": 1721319366,
        "last_error": {
            "code": 0,
            "msg": ""
        },
        "status": "in_progress"
    },
    "code": 0,
    "msg": ""
}
```

PS：这种请求方式叫做异步处理：

也就是说，你调用我一个API发起了一次对话，但是这个对话可能耗时比较长，我先给你返回处理中，并且告诉你一些标识，过一会儿请你带着标识过来再来问我要结果

上面这个接口返回的标识有两个：

**"conversation_id": "7393010358887284777",**

**"id":"7393010358887301161"**

**接下来我们就要带着这些标识调用另一个API去查看返回结果啦**

---

接下来我们要用另一个API查看刚才的消息，API文档如下：

PS：这里正好给大家留个作业，自己看懂这个API文档

https://www.coze.cn/docs/developer_guides/list_chat_messages

| 请求地址 |  https://api.coze.cn/v3/chat/message/list  |
|-|-|
| Header | Content-Type: application/json  <br/>Authorization: **Bearer** **pat_etmxdA4eeGB4pKJZR0uyR89c7VWyc5J4rG7x3F3lf4fox11hcYZ2QyXnIYhP2jea** |
| 入参 | conversation_id = **7393010358887284777**  <br/>chat_id = **7393010358887301161** |

注意：这里面的conversation_id和chat_id请用你自己的值，不要复制文档中的，没有用

另外，当调用完https://api.coze.cn/v3/chat这个接口后，不要等太久再调用 https://api.coze.cn/v3/chat/message/list ，这里好像有bug，等太久，就出不来结果了

> [!abstract]- 🖼 图片展示了HTTPie测试工具界面中调用https://api.coze
> 图片展示了HTTPie测试工具界面中调用https://api.coze.cn/v3/chat/message/list接口的设置情况。关键信息有：请求地址为HTTPS链接；请求方式为GET；Header设置有Content-Type和Authorization；参数设置为Query形式，包含conversation_id和chat_id；返回值为JSON格式，显示了对话内容等信息。该图片与上文介绍的调用查看消息的API相关，直观呈现了API调用的参数设置及返回结果。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/N9xYbN1QFoiT3HxbUb1cTWwznfe) · `N9xYbN1QFoiT3HxbUb1cTWwznfe`

以下是返回的结果

```JSON
{
    "code": 0,
    "data": [
        {
            "bot_id": "7393008672953679913",
            "chat_id": "7393020334787559487",
            "content": "{\"msg_type\":\"generate_answer_finish\",\"data\":\"{\\\"finish_reason\\\":0}\",\"from_module\":null,\"from_unit\":null}",
            "content_type": "text",
            "conversation_id": "7393020334787543103",
            "id": "7393020465872175145",
            "role": "assistant",
            "type": "verbose"
        },
        {
            "bot_id": "7393008672953679913",
            "chat_id": "7393020334787559487",
            "content": "以下是为您生成的 10 个标题：\n1. 👀请大数据把我推荐给丽江旅游党！\n2. 🌄永远可以相信丽江旅游！\n3. 😜丽江旅游！真的好用到哭！\n4. 👋我不允许有人错过丽江旅游！\n5. 🏞️再也不怕！丽江旅游正确姿势！\n6. 🔥吹爆丽江旅游！都给我冲！\n7. 🤩丽江旅游！宝藏之地啊啊啊啊啊啊啊！\n8. 💖被夸爆的丽江旅游！你还不来？\n9. 👣丽江旅游！打开了新世界的大门！\n10. 🌟教科书般的丽江旅游！建议收藏！\n\n以下是对应的正文：\n\n🎈引用名言开篇：“世界是一本书，不旅行的人只看到其中的一页。”朋友们，丽江就是那让你想要翻遍整本书的神奇地方！\n\n💖丽江，简直是人间仙境！这里的风景美到让人窒息！🌄\n\n先来说说丽江古城，古色古香的建筑，充满了浓厚的历史气息，走在石板路上，仿佛穿越回了过去！😜\n\n还有玉龙雪山，那洁白的雪顶，在阳光下闪耀着神圣的光芒，啊啊啊啊啊啊啊！！！！！看到的那一刻，真的被震撼到破防了！！🌅\n\n拉市海也是不能错过的，湖水清澈如镜，周围是大片的草原和湿地，骑马漫步其间，感受着微风拂面，那种惬意真的无法形容！🐎\n\n而且，丽江的美食也让人欲罢不能！腊排骨、纳西烤鱼，每一口都是满满的幸福！！😋\n\n总之，丽江旅游，绝对是一场治愈心灵的旅程，不来会后悔一辈子的！！💖\n\n大家都给我冲啊！！！ ",
            "content_type": "text",
            "conversation_id": "7393020334787543103",
            "id": "7393020334787723327",
            "role": "assistant",
            "type": "answer"
        },
        {
            "bot_id": "7393008672953679913",
            "chat_id": "7393020334787559487",
            "content": "推荐一些丽江旅游的好去处",
            "content_type": "text",
            "conversation_id": "7393020334787543103",
            "id": "7393020465872207913",
            "role": "assistant",
            "type": "follow_up"
        },
        {
            "bot_id": "7393008672953679913",
            "chat_id": "7393020334787559487",
            "content": "制定一份丽江旅游的攻略",
            "content_type": "text",
            "conversation_id": "7393020334787543103",
            "id": "7393020465872224297",
            "role": "assistant",
            "type": "follow_up"
        },
        {
            "bot_id": "7393008672953679913",
            "chat_id": "7393020334787559487",
            "content": "在丽江旅游需要注意哪些事项？",
            "content_type": "text",
            "conversation_id": "7393020334787543103",
            "id": "7393020465872240681",
            "role": "assistant",
            "type": "follow_up"
        }
    ],
    "msg": ""
}
```

## 比较旧的V2同步接口

上面的那个例子需要调用两次才能获取结果，好麻烦，Coze有没有一次调用可以搞定的接口？

有的，那是之前的老接口，这里也分享给大家

<table><colgroup><col/><col/></colgroup><tbody><tr><td>请求地址</td><td>https://api.coze.cn/open_api/v2/chat</td></tr><tr><td>Header</td><td>Content-Type: application/json<br/>Authorization: <b>Bearer</b> <b>pat_etmxdA4eeGB4pKJZR0uyR89c7VWyc5J4rG7x3F3lf4fox11hcYZ2QyXnIYhP2jea</b></td></tr><tr><td>入参</td><td><pre lang="JSON"><code>{ <br/>    "bot_id": "<b>7393008672953679913</b>", <br/>    "user": "123456789", <br/>    "stream": false, <br/>    "query": "丽江旅游"<br/>}</code></pre></td></tr></tbody></table>

> [!abstract]- 🖼 图片展示的是HTTP接口测试工具中在线API请求的设置界面。请求地址为h
> 图片展示的是HTTP接口测试工具中在线API请求的设置界面。请求地址为https://api.coze.cn/open_api/v2/chat，Header设置有Content-Type和Authorization，Content-Type为application/json，Authorization为Bearer pat_etmxdA4eeGB4pKJZR0uyR89c7VWyc5J4rG7x3F3lf4fox11hcYZ2QyXnIYhP2jea。参数设置为JSON参数设置，入参为{"chat_id":"77393005829953679913","user":"1234567890","stream":false,"query":"去旅游"}。该图片与上文介绍的Coze API测试内容相关，直观呈现了API请求的设置情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ZIbVborKsobhyuxVW02cI17UnBd) · `ZIbVborKsobhyuxVW02cI17UnBd`

**PS：请注意，这个接口因为是同步的，所以耗时较长，而且容易失败，请多试几次**

# 写在最后

这篇文章终于写完了，我非常后悔选择Coze的例子，因为这个例子太复杂了。

这篇教程里，我不仅希望你可以真正的懂API的概念，也手把手带你调用了Coze的API，授人以渔，又授人以鱼！
