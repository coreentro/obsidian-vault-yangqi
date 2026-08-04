---
title: "使用IDE创建插件"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/U4d1wqvSJiIlCBktxNMclSyrnrD
node_token: U4d1wqvSJiIlCBktxNMclSyrnrD
obj_token: HoK9ds1IAo4RYbxkoS8cR15ZnRd
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体高级课程"
  - "第十四章：Coze自定义插件功能讲解"
  - "使用IDE创建插件"
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

# 使用IDE创建插件

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体高级课程 › 第十四章：Coze自定义插件功能讲解

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnjxaf6o95lf8s1pv2w27y?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，这节课我们具体讲下如何使用IDE创建插件。

这节课我依然带着大家从0-1创建，并且我们验证下上节课那个写代码的提示词是否有效

由于Coze的插件不支持完整复制，所以大家请务必学习我的底层逻辑

# 需求

我们还是使用大家共性的一些案例，就是使用302.ai来接入Claude

这里我们通过自己写代码把之前API创建的插件改造的更加易用

这个案例有如下几步：

1. 定义好插件的输入和输出
2. 选择一个强大的模型
3. 学会向大模型进行提问（这个很关键，要能问出自己的问题）
4. 将大模型生成的代码复制进来，运行测试，看结果
5. 如果代码有问题，则需要修复

## 插件的输入

为了让插件更易用，我们定义的输入为：

**authorization 为什么没有Bearer，因为如果我们可以控制，我觉得这里可以不加，然后在代码中添加**

```JSON
{
  "authorization": "sk-2m9bVeBDJoV3qQ59CAzxfXClKRFJGbQpJjNo8oQbcG1Caxpb",
  "system_prompt": "你是一个小助手", // 这是系统提示词
  "user_prompt": "你好呀", // 这是用户提示词
  "model": "claude-3-5-sonnet-20241022" // 这是模型选择
}
```

## 插件的输出

插件的输出我就想定义一个值：

```JSON
{
    "message":"插件的输出"
}
```

## 如何向大模型提问

**这个文档不开放复制权限，我希望大家可以自己手打一遍**

```Markdown
我的输入：

{
  "authorization": "鉴权",
  "system_prompt": "系统提示词",
  "user_prompt": "用户提示词",
  "model": "模型"
}

我的输出：

{
"message":"大模型的输出"
}

我希望这个插件可以调用一个API，然后将插件的输入转换成API的真实输入，将API的输出转换成插件的输出

API的调用代码如下：

import http.client
import json

conn = http.client.HTTPSConnection("api.302.ai")
payload = json.dumps({
   "model": "claude-3-5-sonnet-20241022",
   "messages": [
      {
         "role": "user",
         "content": "Hello!"
      }
   ]
})
headers = {
   'Accept': 'application/json',
   'Authorization': 'Bearer ',
   'Content-Type': 'application/json'
}
conn.request("POST", "/v1/chat/completions", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

API输出的结构如下

{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "\n\nHello there, how may I assist you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```
