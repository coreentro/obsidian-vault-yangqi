---
title: "手搓一个 Dr. Know (Piece by Piece)"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/AEjtwy2Kpinc4bkNv0WcKWAUnl3
node_token: AEjtwy2Kpinc4bkNv0WcKWAUnl3
obj_token: VLrfdVoQYokWNgxjXZscZr2Mnbe
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 4
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - " Agent 搭建共学快闪 0523"
  - "5月23日 艾木分享 | 这也许是你一生中第一个Bot"
  - "手搓一个 Dr. Know (Piece by Piece)"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 157
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 手搓一个 Dr. Know (Piece by Piece)

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 ›  Agent 搭建共学快闪 0523 › 5月23日 艾木分享 | 这也许是你一生中第一个Bot

# 手搓一个 Dr. Know (Piece by Piece)

<callout emoji="🏖️">
原创: 艾木;  Dr. Know完整的实现在这里：[https://mp.weixin.qq.com/s/Ory8iVXXjjN3zSTcupPm6Q](https://mp.weixin.qq.com/s/Ory8iVXXjjN3zSTcupPm6Q)
</callout>

以下为教程中的提示词和代码段, 配合上面👆的完整教程, 大家可以直接复制:

## 大模型提示词

```Markdown
用户提问了一个问题: {{query}}

以下是一些跟用户问题相关的信息：

{{search_result}}

-----

请你根据以上信息对用户的问题做出回答，并在末尾列出参考链接。
```

输出的结果参考:

```Markdown
拾下拾下的意思是指傻乎乎、傻里傻气、糊糊涂涂的状态。这个词在广东话中常用来形容别人反应迟钝、思维迷糊。在一些文章和表演中，拾下拾下也可以指迷惘和不安定的状态。总之，这个词通常用来形容人的智商或反应速度较慢。

参考链接：
- [黄子华《拾下拾下》的解读 - 知乎专栏](https://zhuanlan.zhihu.com/p/24504766)
- [拾下拾下/ 煠下煠下- 廣東話解釋 - 粵典 words.hk](https://words.hk/zidin/%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B)
- [搜索结果_请问粤语“拾下拾下”是什么意思呢？ - 百度知道](https://zhidao.baidu.com/index/?word=%E8%AF%B7%E9%97%AE%E7%B2%A4%E8%AF%AD%E2%80%9C%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B%E2%80%9D%E6%98%AF%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D%E5%91%A2%EF%BC%9F&from=qb&ad_test=&wangm=1&uid=bd_1424654832_160&step=1)
- [拾下拾下 - SoLeisure](https://www.soleisure.com.hk/article/J60)
```

## 参考索引格式化代码

写代码来格式化的提示词:

```Markdown
输入参数`search_result`中包含`googleWebSearch`插件的结果，其中`organic_results`是具体的结果数据。请你从`search_result`中提取出所有的链接，并格式化成一个字符串，按照以下格式输出：

        [1] [`title`](`link`)
        [2] [`title`](`link`)
        [3] [`title`](`link`)
```

预期产生的代码: 如果ai写的代码不可用, 可以复制这段

```Python
async def main(args: Args) -> Output:
    params = args.params
    search_result = params['search_result']
    organic_results = search_result['organic_results']
    links = []
    for i, result in enumerate(organic_results):
        title = result['title']
        link = result['link']
        links.append(f"[{i+1}] [`{title}`](`{link}`)")
    formatted_links = "\n".join(links)
    ret: Output = {
        "references": formatted_links
    }
    return ret
```

输出的效果:

```Markdown
拾下拾下原意是指傻乎乎、傻里傻气、糊糊涂涂的意思。在广东话中，也可以用来形容别人傻乎乎、反应慢。这个词在黄子华的栋笃笑中被广泛使用。

[1] [`黄子华《拾下拾下》的解读`](https://zhuanlan.zhihu.com/p/24504766)
[2] [`拾下拾下/ 煠下煠下- 廣東話解釋`](https://words.hk/zidin/%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B)
[3] [`搜索结果_请问粤语“拾下拾下”是什么意思呢？`](https://zhidao.baidu.com/index/?word=%E8%AF%B7%E9%97%AE%E7%B2%A4%E8%AF%AD%E2%80%9C%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B%E2%80%9D%E6%98%AF%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D%E5%91%A2%EF%BC%9F&from=qb&ad_test=&wangm=1&uid=bd_1424654832_160&step=1)
[4] [`拾下拾下`](https://www.soleisure.com.hk/article/J60)
[5] [`泛湖(10) — 黃子華「拾下拾下」對儒學的反思`](https://medium.com/%E8%8F%AF%E7%94%B0%E5%A3%AB%E5%A4%9A/%E6%B3%9B%E6%B9%96-10-%E9%BB%83%E5%AD%90%E8%8F%AF-%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B-%E4%B8%AD%E5%B0%8D%E5%84%92%E5%AD%B8%E7%9A%84%E5%8F%8D%E6%87%89-87d1ba147f22)
[6] [`粤语拾下拾下什么意思`](https://www.douyin.com/zhuanti/7260550675141085195)
[7] [`假若下世纪没有了黄子华的栋笃笑，到底都是一件值得可惜 ...`](https://zhuanlan.zhihu.com/p/661087664)
[8] [`一次滿帶傷感的拾下拾下`](https://www.dayo-wong.com/column/%E4%B8%80%E6%AC%A1%E6%BB%BF%E5%B8%B6%E5%82%B7%E6%84%9F%E7%9A%84%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B/)
[9] [`黄子华- 1999年《拾下拾下》棟篤笑金句`](https://blog.sina.com.cn/s/blog_69731ed40102w9z3.html)
```

## 链接索引格式化代码

进阶版的代码提示词:

```Markdown
修改代码，增加以下功能：从`organic_results`的每一条结果中提取出`title`、`source`、`snippet`、`link`信息，并格式化成字符串。格式如下：

        [i]
        Title : {title}
        Source: {source}
        Snippet: {snippet}
        Link: {link}

然后，将每一条格式化后的结果拼接成一个长的字符串，输出为`retrieved_contexts`。
```

预期产生的代码: 如果ai写的代码不可用, 可以复制这段

```Python
async def main(args: Args) -> Output:
    params = args.params
    search_result = params['search_result']
    organic_results = search_result['organic_results']
    links = []
    contexts = []
    for i, result in enumerate(organic_results):
        title = result['title']
        source = result['source']
        snippet = result['snippet']
        link = result['link']
        links.append(f"[{i+1}] [`{title}`](`{link}`)")
        contexts.append(f"\n[{i+1}]\nTitle : {title}\nSource: {source}\nSnippet: {snippet}\nLink: {link}\n")
    formatted_links = "\n".join(links)
    retrieved_contexts = "\n".join(contexts)
    ret: Output = {
        "references": formatted_links,
        "retrieved_contexts": retrieved_contexts
    }
    return ret
```

预期效果:

```Markdown
{
  "references": "[1] [`黄子华《拾下拾下》的解读`](`https://zhuanlan.zhihu.com/p/24504766`)\n[2] [`拾下拾下/ 煠下煠下- 廣東話解釋`](`https://words.hk/zidin/%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B`)\n[3] [`拾下拾下`](`https://baike.baidu.com/item/%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B?noadapt=1`)\n[4] [`拾下拾下`](`https://www.soleisure.com.hk/article/J60`)\n[5] [`泛湖(10) — 黃子華「拾下拾下」對儒學的反思`](`https://medium.com/%E8%8F%AF%E7%94%B0%E5%A3%AB%E5%A4%9A/%E6%B3%9B%E6%B9%96-10-%E9%BB%83%E5%AD%90%E8%8F%AF-%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B-%E4%B8%AD%E5%B0%8D%E5%84%92%E5%AD%B8%E7%9A%84%E5%8F%8D%E6%87%89-87d1ba147f22`)\n[6] [`粤语拾下拾下什么意思`](`https://www.douyin.com/zhuanti/7260550675141085195`)\n[7] [`假若下世纪没有了黄子华的栋笃笑，到底都是一件值得可惜 ...`](`https://zhuanlan.zhihu.com/p/661087664`)\n[8] [`一次滿帶傷感的拾下拾下`](`https://www.dayo-wong.com/column/%E4%B8%80%E6%AC%A1%E6%BB%BF%E5%B8%B6%E5%82%B7%E6%84%9F%E7%9A%84%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B/`)\n[9] [`黄子华- 1999年《拾下拾下》棟篤笑金句`](`https://blog.sina.com.cn/s/blog_69731ed40102w9z3.html`)",
  "retrieved_contexts": "\n[1]\nTitle : 黄子华《拾下拾下》的解读\nSource: 知乎专栏\nSnippet: 拾下拾下原意是指傻乎乎、傻里傻气、糊糊涂涂的意思。子华说，可能在我们生存的时候，大家不要妄想我们会变得那么聪明，我们一天不死可能一天都是傻傻的，其实可能生存 ...\nLink: https://zhuanlan.zhihu.com/p/24504766\n\n\n[2]\nTitle : 拾下拾下/ 煠下煠下- 廣東話解釋\nSource: 粵典 words.hk\nSnippet: 例句：. (粵) 你 nei5 咪 mai5 拾 saap6 下 haa5 拾 saap6 下 haa5 噉 gam2 ， 快 faai3 啲 di1 過 gwo3 嚟 lai4 幫 bong1 手 sau2 啦 laa1 。 (英) Stop daydreaming and ...\nLink: https://words.hk/zidin/%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B\n\n\n[3]\nTitle : 拾下拾下\nSource: 百度百科\nSnippet: 关于主题 粤语：拾下拾下，原意是指傻乎乎、傻里傻气、糊糊涂涂的意思。 根本没人能想像到自己将来可以怎样，会怎样想啊。 如果我们很多人都迷信：哇 ...\nLink: https://baike.baidu.com/item/%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B?noadapt=1\n\n\n[4]\nTitle : 拾下拾下\nSource: SoLeisure\nSnippet: 在廣東話中，「拾下拾下」有傻乎乎、糊糊塗塗的意思。 沒有目標，沒有計劃，見步行步，「拾下拾下」地過活，一直不受推崇，會被視作白費人生。 充滿目標，事事計劃，步步為營，認認真真地過活，才是從小到大，被灌輸為對生活應有的態度。\nLink: https://www.soleisure.com.hk/article/J60\n\n\n[5]\nTitle : 泛湖(10) — 黃子華「拾下拾下」對儒學的反思\nSource: Medium · 華田 Watin\nSnippet: 子華神金盆𠺘口前夕，華田感傷之時，翻看了1999 年的「拾下拾下」，看畢好像更為神傷。 那年的棟篤笑創造了很多金句，例如：Number降、鑽石海景、負 ...\nLink: https://medium.com/%E8%8F%AF%E7%94%B0%E5%A3%AB%E5%A4%9A/%E6%B3%9B%E6%B9%96-10-%E9%BB%83%E5%AD%90%E8%8F%AF-%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B-%E4%B8%AD%E5%B0%8D%E5%84%92%E5%AD%B8%E7%9A%84%E5%8F%8D%E6%87%89-87d1ba147f22\n\n\n[6]\nTitle : 粤语拾下拾下什么意思\nSource: 抖音\nSnippet: 粤语拾下拾下什么意思. 【粤语骂人常用词汇】第二期教你不用脏嘴骂人#. 点赞数icon 911. 01:07 · 【粤语骂人常用词汇】第二期教你不用脏嘴骂人#学粤语# ...\nLink: https://www.douyin.com/zhuanti/7260550675141085195\n\n\n[7]\nTitle : 假若下世纪没有了黄子华的栋笃笑，到底都是一件值得可惜 ...\nSource: 知乎专栏\nSnippet: 另外，“拾下拾下”又有迷惘和不安定的意思，这又正是回归后香港人的普遍精神状态，子华这次栋笃笑之所以无题，正因为我们身处的地方已经再无可观的事情可以 ...\nLink: https://zhuanlan.zhihu.com/p/661087664\n\n\n[8]\nTitle : 一次滿帶傷感的拾下拾下\nSource: Dayo Wong Website\nSnippet: ... 拾下拾下」地上台，東拉西扯地開始了整場棟篤笑。 棟篤笑的精華專輯. 嘗試用兩個角度去閱讀今次「拾下拾下」棟篤笑，首先，題目中的「拾」有「十」的意思，今次是子華棟 ...\nLink: https://www.dayo-wong.com/column/%E4%B8%80%E6%AC%A1%E6%BB%BF%E5%B8%B6%E5%82%B7%E6%84%9F%E7%9A%84%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B/\n\n\n[9]\nTitle : 黄子华- 1999年《拾下拾下》棟篤笑金句\nSource: 手机新浪网\nSnippet: 所謂“負家產”嘅意思想就係你要背負著呢幢“冚家產”供佢一世。 7. 保險一個被岐視崇高嘅職業，賣保險係緊一份保障，但係呢一份保障唔係普通嘅保障，係 ...\nLink: https://blog.sina.com.cn/s/blog_69731ed40102w9z3.html\n"
}
```

## 升级版大模型提示词

```Markdown
来自：https://github.com/leptonai/search_with_lepton/blob/main/search_with_lepton.py

You are a large language AI assistant built by Lepton AI. You are given a user question, and please write clean, concise and accurate answer to the question. You will be given a set of related contexts to the question, each starting with a reference number like [[citation:x]], where x is a number. Please use the context and cite the context at the end of each sentence if applicable.
你是由Lepton AI构建的大型语言AI助手。你将得到一个用户的问题，请为这个问题写出简洁、准确的答案。你将得到一组与问题相关的上下文，每个上下文都以一个像[[citation:x]]这样的引用号开始，其中x是一个数字。如果适用，请在每个句子的结尾引用上下文。

Your answer must be correct, accurate and written by an expert using an unbiased and professional tone. Please limit to 1024 tokens. Do not give any information that is not related to the question, and do not repeat. Say "information is missing on" followed by the related topic, if the given context do not provide sufficient information.
你的答案必须是正确的、准确的，并由专家以公正、专业的语气撰写。请限制在1024个标记之内。不要提供与问题无关的信息，也不要重复。如果给定的上下文没有提供足够的信息，就说“缺少关于......的信息”。

Please cite the contexts with the reference numbers, in the format [citation:x]. If a sentence comes from multiple contexts, please list all applicable citations, like [citation:3][citation:5]. Other than code and specific names and citations, your answer must be written in the same language as the question.
请用引用号引用上下文，格式为[citation:x]。如果一个句子来自多个上下文，请列出所有适用的引用，例如[citation:3][citation:5]。除了代码和特定的名称和引用，你的答案必须用与问题相同的语言写出。

Here are the set of contexts:
这是一组上下文：

{context}

Remember, don't blindly repeat the contexts verbatim. And here is the user question:
记住，不要盲目地逐字重复上下文。这是用户的问题：

```

```Markdown
用户提问了一个问题: {{query}}

请提供清晰、简洁且准确的回答。你的回答必须是正确无误、精确到位，并且由专业人士使用中立专业的语调撰写的。不要提供任何与查询无关的信息，同时避免重复信息。

你将从网络上获得一系列相关的上下文，每个上下文都以"[i]"开头，其中i是这个引用的索引号码。如果适用，请使用该上下文并在每个句子的末尾引用该上下文。请按照引文的编号格式引用上下文，例如[1]。如果一句话来自多个上下文，请列出所有适用的引用，例如[3][5]。

以下是检索到的上下文信息：

{{retrieved_contexts}}

-----

用户的问题是: {{query}}
```

预期输出效果:

```Markdown
“拾下拾下”是粤语中的一个词语，原意指傻乎乎、傻里傻气、糊里糊涂的意思[1][3][4]。此外，这个词也可以形容一种迷惘和不安定的状态[7]。

[1] [`黄子华《拾下拾下》的解读`](`https://zhuanlan.zhihu.com/p/24504766`)
[2] [`拾下拾下/ 煠下煠下- 廣東話解釋`](`https://words.hk/zidin/%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B`)
[3] [`拾下拾下`](`https://baike.baidu.com/item/%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B?noadapt=1`)
[4] [`拾下拾下`](`https://www.soleisure.com.hk/article/J60`)
[5] [`泛湖(10) — 黃子華「拾下拾下」對儒學的反思`](`https://medium.com/%E8%8F%AF%E7%94%B0%E5%A3%AB%E5%A4%9A/%E6%B3%9B%E6%B9%96-10-%E9%BB%83%E5%AD%90%E8%8F%AF-%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B-%E4%B8%AD%E5%B0%8D%E5%84%92%E5%AD%B8%E7%9A%84%E5%8F%8D%E6%87%89-87d1ba147f22`)
[6] [`粤语拾下拾下什么意思`](`https://www.douyin.com/zhuanti/7260550675141085195`)
[7] [`假若下世纪没有了黄子华的栋笃笑，到底都是一件值得可惜 ...`](`https://zhuanlan.zhihu.com/p/661087664`)
[8] [`一次滿帶傷感的拾下拾下`](`https://www.dayo-wong.com/column/%E4%B8%80%E6%AC%A1%E6%BB%BF%E5%B8%B6%E5%82%B7%E6%84%9F%E7%9A%84%E6%8B%BE%E4%B8%8B%E6%8B%BE%E4%B8%8B/`)
[9] [`黄子华- 1999年《拾下拾下》棟篤笑金句`](`https://blog.sina.com.cn/s/blog_69731ed40102w9z3.html`)
```

## Agent提示词

```Markdown
你的最重要能力是`search_and_answer`。当用户向你提问，或询问某些主题或概念，或用户只是输入一些关键词或短语时，你应该始终调用`search_and_answer`来生成响应。
```
