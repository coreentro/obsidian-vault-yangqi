---
title: "Coze对话流：大模型为什么可以感知上下文"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/ItInw9qTHi63Y7kyHnrcKOoNnGg
node_token: ItInw9qTHi63Y7kyHnrcKOoNnGg
obj_token: S6R3dx4WTof4LgxyVymcN5vRn1f
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体中级课程"
  - "第八章：Coze对话流与会话功能讲解"
  - "Coze对话流：大模型为什么可以感知上下文"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 4
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# Coze对话流：大模型为什么可以感知上下文

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体中级课程 › 第八章：Coze对话流与会话功能讲解

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcn5k93xsd4m911uxyzd7gz?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，这节课我来给大家讲明白，**大模型为什么可以感知上下文？**

在我们使用ChatGPT、Kimi这种对话软件的时候，我们会发现这些软件是可以记住我们之前说了什么的。

这也是我们常说的上下文，你有没有想过大模型是怎么感知这个上下文的？

这个文章我们就来把这个事情讲明白。

# AI对话中的3个角色

在最早我们跟GPT大模型对话的过程中，这里面有3个角色的概念，分别是：

1. System
2. User
3. Assistant

听到这里，你可能会懵逼，我天天跟豆包，Kimi对话，我怎么感知不到三个角色呢？

不要担心，接下来让我们通过一个我专门做的教学案例来演示下这三个角色的不同

**-- 此处请观看教学视频 --**

**PS：由于ChatGPT是第一代的AI对话应用，他们定义了这三个角色，因此后来的对话应用基本都会沿用这个概念**

<callout emoji="💡">
### System角色
设定AI助手的行为和角色定位，用户不可见但会影响整个对话。
### User角色
用户输入的内容，是对话的主要驱动者。
### Assistant角色
AI助手的回复，会基于System角色设定和对话上下文来响应。
</callout>

# AI对话应用的框架

了解了AI对话应用中的三个角色之后，我们来看下，每一次的对话，为什么大模型可以给出符合语境的回答

就好像大模型“记住了”我们之前的对话一样？

我们可以通过Coze的调试来带大家看下整个过程

**-- 此处请观看教学视频--**

对于类似于豆包，ChatGPT这类对话应用来讲，他们的框架图其实非常简单。

<whiteboard token="DpFLwjmJlhZk4LbMdL8cIenHnMe"></whiteboard>

上面这个框图表示出了大模型可以感知上下文的原理

<callout emoji="💡">
我们每次跟大模型对话，只要把**System提示词**  + **之前对话的数据 + 本次用户的问题**都给到大模型，大模型就可以拿到所有的对话信息，然后再根据本次的问题，给出最合理的回答
所以并不是大模型记住了之前的内容，而是你每次都把之前的内容给他了，他自然而然就感知到了上下文
</callout>

# 附录

## 三个角色的演示代码

```TypeScript
import React, { useState } from 'react';
import { MessageCircle, Settings, User, Bot, Trash2 } from 'lucide-react';

const ChatDemo = () => {
  const initialSystemMessage = {
    role: 'system',
    content: '你是一个基于大语言模型的AI助手，请使用与用户相同的语言进行交流，保持友善和专业。'
  };

  const [messages, setMessages] = useState([initialSystemMessage]);
  const [newMessage, setNewMessage] = useState('');
  const [showContext, setShowContext] = useState(false);
  
  const addMessage = (role, content) => {
    setMessages([...messages, { role, content }]);
    // 模拟Assistant的回复
    if (role === 'user') {
      setTimeout(() => {
        setMessages(prev => [...prev, {
          role: 'assistant',
          content: `我理解你的问题："${content}"。作为AI助手，我会基于系统指令和之前的对话来回答你。`
        }]);
      }, 1000);
    }
  };

  const clearMessages = () => {
    setMessages([initialSystemMessage]);
  };
  
  return (
    <div className="max-w-4xl mx-auto p-4">
      <div className="mb-6">
        <h1 className="text-2xl font-bold mb-4">对话系统演示</h1>
        
        {/* 角色说明 */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="bg-gray-50 p-4 rounded-lg">
            <div className="flex items-center gap-2 mb-2">
              <Settings className="w-5 h-5 text-gray-600" />
              <h2 className="font-semibold">System</h2>
            </div>
            <p className="text-sm">系统指令，定义AI助手的行为规则和角色设定，在对话开始时发送。</p>
          </div>
          <div className="bg-green-50 p-4 rounded-lg">
            <div className="flex items-center gap-2 mb-2">
              <User className="w-5 h-5 text-green-600" />
              <h2 className="font-semibold">User</h2>
            </div>
            <p className="text-sm">用户发送的消息，代表人类用户的输入内容，显示在对话右侧。</p>
          </div>
          <div className="bg-purple-50 p-4 rounded-lg">
            <div className="flex items-center gap-2 mb-2">
              <Bot className="w-5 h-5 text-purple-600" />
              <h2 className="font-semibold">Assistant</h2>
            </div>
            <p className="text-sm">AI助手的回复，基于系统指令和上下文生成的回应，显示在对话左侧。</p>
          </div>
        </div>
      </div>
      
      {/* 对话区域 */}
      <div className="border rounded-lg mb-4">
        <div className="p-4 border-b">
          <div className="flex justify-between items-center mb-2">
            <h3 className="font-semibold">对话内容</h3>
            <div className="flex gap-2">
              <button
                onClick={() => setShowContext(!showContext)}
                className="text-sm text-blue-600 hover:text-blue-800"
              >
                {showContext ? '隐藏上下文' : '显示上下文'}
              </button>
              <button
                onClick={clearMessages}
                className="flex items-center gap-1 text-sm text-red-600 hover:text-red-800"
              >
                <Trash2 className="w-4 h-4" />
                清空对话
              </button>
            </div>
          </div>
          {showContext && (
            <div className="bg-gray-50 p-2 rounded text-sm mb-2">
              <pre className="whitespace-pre-wrap">
                {JSON.stringify(messages, null, 2)}
              </pre>
            </div>
          )}
        </div>
        
        <div className="h-80 overflow-y-auto p-4">
          {messages.map((msg, index) => (
            <div key={index} className={`mb-4 ${
              msg.role === 'user' ? 'text-right' : 'text-left'
            }`}>
              <div className="flex items-center gap-2 mb-1">
                {msg.role === 'assistant' ? (
                  <Bot className="w-4 h-4 text-purple-600" />
                ) : msg.role === 'user' ? (
                  <User className="w-4 h-4 text-green-600 ml-auto" />
                ) : (
                  <Settings className="w-4 h-4 text-gray-600" />
                )}
                <span className="text-xs text-gray-500">
                  {msg.role === 'user' ? 'User' : msg.role === 'assistant' ? 'Assistant' : 'System'}
                </span>
              </div>
              <div className={`inline-block max-w-[70%] p-3 rounded-lg ${
                msg.role === 'user' 
                  ? 'bg-blue-500 text-white'
                  : msg.role === 'system'
                  ? 'bg-gray-200'
                  : 'bg-gray-100'
              }`}>
                {msg.content}
              </div>
            </div>
          ))}
        </div>
        
        <div className="p-4 border-t">
          <div className="flex gap-2">
            <input
              type="text"
              value={newMessage}
              onChange={(e) => setNewMessage(e.target.value)}
              placeholder="输入消息..."
              className="flex-1 p-2 border rounded"
              onKeyPress={(e) => {
                if (e.key === 'Enter' && newMessage.trim()) {
                  addMessage('user', newMessage.trim());
                  setNewMessage('');
                }
              }}
            />
            <button
              onClick={() => {
                if (newMessage.trim()) {
                  addMessage('user', newMessage.trim());
                  setNewMessage('');
                }
              }}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              发送
            </button>
          </div>
        </div>
      </div>
      
      <div className="text-sm text-gray-600">
        <h3 className="font-semibold mb-2">说明：</h3>
        <ul className="list-disc pl-5">
          <li>在输入框中输入消息并发送，可以看到对话如何进行</li>
          <li>点击"显示上下文"可以查看完整的对话历史，包括系统指令</li>
          <li>点击"清空消息"可以清除所有对话记录（系统指令会保留）</li>
          <li>每次Assistant的回复都会考虑之前的所有对话内容</li>
        </ul>
      </div>
    </div>
  );
};

export default ChatDemo;
```
