---
title: "一个简单的AI翻译应用"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/I8ApwfKlMi5Q86k1GwHcqkaOnrh
node_token: I8ApwfKlMi5Q86k1GwHcqkaOnrh
obj_token: LsUndA94jo5qBgxR9kQc2RCnnPd
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体中级课程"
  - "第九章：Coze 创建AI应用功能讲解"
  - "一个简单的AI翻译应用"
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

# 一个简单的AI翻译应用

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体中级课程 › 第九章：Coze 创建AI应用功能讲解

应用地址：https://www.coze.cn/space/7362748064240877602/project-ide/7462650039581130752

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnaezz7g7k5xf8lp21sih4?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，这节课带着大家手把手搭建一个非常简单的AI应用。

麻雀虽小，五脏俱全，我们通过这个AI应用的搭建，来了解下Coze应用的组成

这个AI应用主要包括：

1. 工作流
2. 页面
3. 组件
4. 事件

这节课的目的是让大家对一个Coze应用的组成有更进一步的认知，但并不会深入到细节中

# AI翻译应用

在构建应用之前，我们需要先梳理清楚这个应用长什么样子。

我们可以借助大模型来辅助我们给出这个AI翻译应用的原型图

这里我们使用国产的大模型：通义千问

使用地址：https://chat.qwenlm.ai/

> [!abstract]- 🖼 图片展示了通义千问大模型的界面，上方显示“Qwen2.5-Plus”及“
> 图片展示了通义千问大模型的界面，上方显示“Qwen2.5-Plus”及“成为默认”。界面中部有蓝色图标和文字“晚上好，刘梦浩”，下方有“预览模式”“联网搜索”“图像生成”“视频生成”四个选项，其中“预览模式”被红色框突出显示。图片中还有一条红色箭头指向“预览模式”选项，并标注“这里一定要选择预览模式”。该图片与上下文关系紧密，是使用通义千问大模型构建AI翻译应用时，选择预览模式的示例，用于辅助说明应用原型图的构建。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XjQMbvCOqoGfxixrN2hckBQOnsh) · `XjQMbvCOqoGfxixrN2hckBQOnsh`

然后如下提示词进行对话

```JSON
我想构建一个翻译的软件。
用户可以输入要翻译的原始文本
然后选择语言，
点击翻译按钮
然后可以在另一个展示框可以看到翻译后的语言
帮我画下原型图
```

下面就是一个基本的页面，然后我们就可以用来构建我们的AI应用了

> [!abstract]- 🖼 图片展示的是一个AI翻译应用的页面示例。上方标题为“翻译软件”，下方有“
> 图片展示的是一个AI翻译应用的页面示例。上方标题为“翻译软件”，下方有“请输入要翻译的文本...”的输入框，下方是“英语”的下拉选择框，再下方是“翻译”按钮，最下方是“翻译后的文本将显示在这里...”的显示区域。该图片与上下文的关系是，在构建AI翻译应用之前，通过此图帮助大家了解应用的原型图，以便后续借助通义千问大模型进行应用搭建。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MWtWbdvy7o7TSdxtgA1cg9TanHb) · `MWtWbdvy7o7TSdxtgA1cg9TanHb`
