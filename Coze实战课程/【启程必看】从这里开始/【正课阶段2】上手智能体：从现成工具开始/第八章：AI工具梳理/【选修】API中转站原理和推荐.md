---
title: "【选修】API中转站原理和推荐"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/EU4PwKZFHiElayk249lcrhwgnag
node_token: EU4PwKZFHiElayk249lcrhwgnag
obj_token: PE9pdRzjeoAnCExH9TtcM3N6nCg
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段2】上手智能体：从现成工具开始"
  - "第八章：AI工具梳理"
  - "【选修】API中转站原理和推荐"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 2
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 【选修】API中转站原理和推荐

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段2】上手智能体：从现成工具开始 › 第八章：AI工具梳理

# 写在前面

你好，我是大圣

我们的目的是在国内使用上海外大模型

在了解了开源套壳软件之后，我相信你已经明白，要使用海外大模型，依靠的就是API中转站

我们只要能找到稳定靠谱的AP中转，并且把它配置到Cherry Studio里面，我们就可以使用上海外模型

这节课我就给大家讲明白API中转站的原理、类型，以及给大家推荐1-2个

> [!abstract]- 🖼 图片展示了API中转站的工作原理。左侧“开源套壳”向右侧多个API（Ge
> 图片展示了API中转站的工作原理。左侧“开源套壳”向右侧多个API（Gemini、GPT、Deepseek、Calude）发送请求，这些API再将请求转发给API中转站。右侧API中转站将请求转发给Google、OpenAI、深度求索、Anthropic等公司，这些公司是API中转站的上游服务提供商。该图直观呈现了API中转站作为桥梁，连接开源套壳与上游大模型服务提供商的功能，与上下文介绍API中转站原理的内容相契合。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Bd0pbSEk6oZ5Jpx5cNWckjIUnyh) · `Bd0pbSEk6oZ5Jpx5cNWckjIUnyh`

# 一、API中转站的原理

API中转站，我按照它的原理分为两种

第一种叫官方中转

第二种叫做薅羊毛中转

## 1）官方中转

官方中转很好理解，**它背后连接的仍然是官方正儿八经的官方API**

他给用户解决的是：**网络访问问题**、**付款的问题**，**还有因为量大可能能得到一些优惠**

但这个优惠一般来讲，8折顶天了

如果有厂商告诉你，他能够拿到5折的官方API优惠，基本就是假的

## 2）薅羊毛中转

越到后面，你越发现想要使用官方API，不仅有网络问题、付款问题，还有最重要的一个问题：**太贵了**

而薅羊毛中转解决的就是这个痛点  
  
它降低成本的方式有很多，涉及到一些技术原理。我们这里只给大家举几类，你有个概念

第一种：批量注册官方账号，然后通过技术的手段给用户去调用

比如100个用户共享10个账号，那么成本就降下来了

第二种：一些像Cursor这样的正规软件，他们拥有Claude Code、Gemini这些能力，然后API中转站服务商会批量注册扣子的账号去薅取他的羊毛

---

**这种薅羊毛中转最大的优点就是便宜。当然它有一些缺点（你必须了解）**

**缺点一：容易不稳定**；API中转商批量注册账号，会导致官方算力不足。因此官方会严格封禁这波账号

**缺点二：如果他们薅的第三方的软件的羊毛，那么会额外注入大量的提示词**

比如Cursor，它是一款编程IDE。那么你跟这个API对话的时候，不是直接跟官方API对话，而是会经过一道Cursor，提前注入一些编程相关的提示词

这类提示词会导致你在使用的时候出现一些不符合预期的回答

**缺点三：速度慢**；中间经过了多道网络就是会导致速度变慢，而且API中转商为了降低成本，部署少量服务器，也会导致网络拥挤

**缺点四：掺水降智；降智一般有三种**

第一种是API服务商刻意为之，这种就属于欺骗

第二种就是因为薅羊毛或者批量注册账号，导致官方检测到账号异常，从而选择给你降智

第三种就是薅第三方软件羊毛，注入大量无关提示词，让用户感觉降智

# 二、正规API中转

给大家推荐一个业内正规的中转站，它跟硅基流动原理是一致的，大家自行去了解即可

地址：https://openrouter.ai/

这上边你能够访问Claude、GPT、Gemini等等任何的API，但它的缺点就一个：贵

# 三、国内API中转

这是我们这节课的重点，也是国内用户在一定的性价比内使用国外模型的手段

**这里我一定要提前叠个甲，请务必仔细阅读下面这段话**

<callout emoji="✨">
我会给大家推荐国内API中转：但我没有办法保证它不掺水，不降智，我也没有办法保证它的稳定性
因为现在全球算力不足，Calude、GPT、Gemini的封号越来越严重
所以这些中转站他们要不断地和平台做对抗，不稳定、不可用，是常有的事儿
如果你使用的中转站速度变慢了，回复质量变差了，或者直接不可用了，可以找他们客服，不要问我
我会给大家留意靠谱的中转站，但没有办法做到实时
**也不要一直问我说，大圣有没有便宜又好用的中转**
**任何中转都不要一次性充太多钱，少量多充，按需充值**
</callout>

如果你认可上面这段话，请继续往下看

# 四、中转一：aigocode

<callout emoji="✨">
不要着急为这个中转充钱，先把我推荐的几个中转看完
</callout>

地址：https://aigocode.com/invite/WB3DJX6W

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/NDFzb7uPKolOeAxeJMIcCI3ongc) · `NDFzb7uPKolOeAxeJMIcCI3ongc`

> [!abstract]- 🖼 图片展示了2026年3月30日的对话内容。一位用户提到cherry st
> 图片展示了2026年3月30日的对话内容。一位用户提到cherry studio最近2.2的ClaudeMax封号严重，用3.9肯定可以，1.8可以但不够稳定。大圣回复称在写教程，最终确认一下，如果让其接入Cherry Studio，就选择Claude Max。用户表示2.2的我们把cherry studio关了，不然死号更快，文档里写3.9。大圣回复价格贵但稳定，是专门给企业用的。该图片与文档中介绍国内API中转的内容相关，用于说明ClaudeMax封号情况及用户建议。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/NftWbiq67obEEUxRkkZcf3qhn8b) · `NftWbiq67obEEUxRkkZcf3qhn8b`

# 五、中转二：ClaudeCN

地址：https://claudecn.top/register?aff=UyTK

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/Tns5bMRA9o4rzvx1C0uc8Ba7nEd) · `Tns5bMRA9o4rzvx1C0uc8Ba7nEd`

# 六、中转三：云雾

地址：https://yunwu.ai/register?aff=OUcT

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/MAkRbzbqYoizlZxznrwc3N3inad) · `MAkRbzbqYoizlZxznrwc3N3inad`

# 七、如何自己寻找中转API

1. 时刻关注我的社群，我如果找到了比较靠谱的好用的，我会给大家分享
2. 可以问一下你身边比较懂AI的朋友，看看他们有哪些比较好用的
3. 看我下面这个视频

网址：https://relaypulse.top

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/TYJubhsFEolVjAxCIkdcCaCHnGQ) · `TYJubhsFEolVjAxCIkdcCaCHnGQ`

# 写在最后

使用中转API不要一次性充太多钱，少量多次

如果你选择了使用中转API，就要接受它的不完美

如果你日常处理的任务并不多，但是你对质量要求非常高，可以选择使用官方API

你要思考你的任务是否一定需要用Claude，前面给大家讲了ChatGPT的官方订阅方式，一个月120块钱，已经是非常顶级的模型了
