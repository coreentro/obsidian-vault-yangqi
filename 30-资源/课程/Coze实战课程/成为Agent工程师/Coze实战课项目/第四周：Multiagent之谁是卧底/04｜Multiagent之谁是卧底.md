---
title: "04｜Multiagent之谁是卧底"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/RWN5wdpIBiDzyvkekEfcuCXxnbf
node_token: RWN5wdpIBiDzyvkekEfcuCXxnbf
obj_token: ZcaFdQ7NFo0bt3xGoPecXcczn8u
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 3
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "第四周：Multiagent之谁是卧底"
  - "04｜Multiagent之谁是卧底"
obj_create_time: 1720418542
obj_edit_time: 1726322331
creator: ou_4f9742f370819a3c899baacbc140aed2
owner: ou_4f9742f370819a3c899baacbc140aed2
revision_id: 514
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# 04｜Multiagent之谁是卧底

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 第四周：Multiagent之谁是卧底

# 04｜Multiagent之谁是卧底

<callout emoji="❗">
### 开场
《谁是卧底》
- 案例很经典，很有代表性； 

  - 系统性，Bot 结构；
  - Multiagent 模式应用；
  - 设计具有复杂交互、复杂流程的 Agent 应用；
- 案例复杂度有很大提升；进入高级阶段：系统性，修炼内功，工程思维；
- 课程和案例经过 3 次迭代，内容的密度和质量还是很高的；
所以，你至少要学三遍。
### 使用海外Coze平台的一些注意事项
1. 海外 Coze 跟国内的区分，主要是模型。
2. 需要🪜
3. 收费（调试工作流不扣额度，好像）；两种应对方式：1. 冲个 9 美元/月；2. 免费试用
### 本课内容答疑
### 讲一讲案例更新&循环
### 其他问题的答疑
</callout>

<callout emoji="❗">
案例更新（2024 年 9 月 11 日）：
我利用 Coze 的循环功能（Loop 节点）对《谁是卧底》中的两个冗长的工作流作了优化。
一个是组织 AI 玩家发言的工作流：
- 原始 - [ai_players_speak](https://www.coze.com/work_flow?space_id=7341627710785110018&workflow_id=7390062069615181830)
- 优化后 - [ai_players_speak_loop](https://www.coze.com/work_flow?space_id=7341627710785110018&workflow_id=7413309671185842182)
另一个是组织 AI 玩家投票的工作流：
原始 - [ai_players_vote](https://www.coze.com/work_flow?space_id=7341627710785110018&workflow_id=7390230559030804485)
优化后 - [ai_players_vote_loop](https://www.coze.com/work_flow?space_id=7341627710785110018&workflow_id=7413312665001279494)
同时，Bot 版本也作了更新：
原始版 - [谁是卧底（教学版）](https://www.coze.com/space/7341627710785110018/bot/7390769467972173829)
更新版 - [谁是卧底（教学版v2）](https://www.coze.com/space/7341627710785110018/bot/7413311205646794757)
原来 Coze 工作流不支持循环，所以只能用笨方法实现。大家可以对比一下新旧两个版本的工作流，可以明显感受到循环节点的作用。 
</callout>

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcnhyjrs88d1b7mpi26jfj1?from=ccm" type="iframe"></readonly-block>

> [!warning]- 📎 附件（`application/pdf`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/HAfTb83VEo68IWx1D82clYwgnnb) · `HAfTb83VEo68IWx1D82clYwgnnb`

## Part 1：理解 Coze Bot 的系统结构

1. 程序设计的基本元素（心法）
2. Multiagent Flow（一种多 Agent 实现）

## Part 2：《谁是卧底》的整体设计

1. 解析《谁是卧底》整体结构
2. 深度解析 Multiagent Flow 的实现机制
3. 如何在多个 Agent 之间实现可靠的跳转？

## Part 3：《谁是卧底》的核心业务模块

1. 如何用变量传递上下文数据？
2. 如何用 LLM 生成词对（题目）
3. AI 玩家的发言策略（LLM 推理）
4. AI 玩家的投票策略（LLM 推理）

## QA

---

延伸阅读：

- [为什么Workflow对Agent系统很重要？（在WaytoAGI社群的分享）](https://mp.weixin.qq.com/s/kobWUoZvqwnweo2xAwxN7w)

其他可延伸的主题：

- Coze 在多 Agent 跳转上的问题（产品设计和工程实现）
- 如何查阅 Coze 的 Debug 日志（LLM 调用）
