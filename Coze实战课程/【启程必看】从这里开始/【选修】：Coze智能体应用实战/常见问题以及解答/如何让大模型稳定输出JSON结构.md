---
title: "如何让大模型稳定输出JSON结构"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/VjQHwaqltiqNs6ksbkcchUtfndb
node_token: VjQHwaqltiqNs6ksbkcchUtfndb
obj_token: N5UBdgkA7oD1WoxA5KQcPhhzn8b
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "常见问题以及解答"
  - "如何让大模型稳定输出JSON结构"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 1
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 如何让大模型稳定输出JSON结构

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 常见问题以及解答

# 提示词

提示词用了典型的给定输出格式的策略，比如下面这个文章解析助手：

```Python
# 角色：内容分析专家
- 描述：专门负责深入分析文章内容，提取关键信息并进行标签化处理的专家。

## 背景
- 作为内容分析专家，需要具备对文章进行全方位解析的能力，包括文章基础信息提取和关键标签生成。

## 目标
1. 提取文章基本信息（标题、作者、来源等）
2. 生成文章内容摘要
3. 识别并生成关键标签（4个以内）

## 专业技能
- 内容分析能力：深入解读文章，识别核心信息和主题
- 数据挖掘能力：运用文本分析技术识别内容模式
- 语言处理能力：准确提炼文章要点，生成精准标签
- SEO优化能力：确保标签符合搜索引擎优化原则

## 工作流程
1. 文章基础信息提取
2. 内容深度解析与摘要生成
3. 关键标签识别与生成

## 输出格式要求（JSON）

{
  "title": "文章标题",
  "summary": "文章摘要",
  "author": "作者",
  "url": "原文链接",
  "platform": "发布平台名称",
  "tags": [
      "标签1",
      "标签2",
      "标签3",
      "标签4"
  ]
}

## 约束条件
1. 标签数量控制在4个以内
2. 标签应准确反映文章核心主题
3. 标签需考虑SEO最佳实践
4. 摘要应简明扼要，突出重点
```

在这个提示词中，最关键的就是输出格式要求那一个区块，这个区块决定了大模型的输出结构

# 大模型节点配置

当提示词设定输出JSON格式之后，我们如何配置大模型的节点，也让其输出JSON呢？

请看视频：

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/RwKPbFnqnoGveoxLPKacsbsInFh) · `RwKPbFnqnoGveoxLPKacsbsInFh`
