---
title: 概念辨析日常记录
aliases: 概念澄清,model-vs-agent,model-identity,llm-wiki
tags:
  - 概念
  - 日志
created: 2026-07-29
source-dirs:
  - 2026-07-16-model-vs-agent-relationship
  - 2026-07-16-model-identity
  - 2026-07-16-llm-wiki-intro
  - 2026-07-16-google-account-region
  - 2026-07-16-ip-geolocation-difference
  - 2026-07-16-cpa-password
related: []
---

# 概念辨析日常记录

> 这几个目录是日常对话里对一些概念的当场澄清，没有独立产出文档，只有占位 README。在这里一句带过，不为凑数硬包装成笔记。

## 已发生过的概念澄清主题

| 主题 | 一句话 | 源目录 |
|---|---|---|
| 模型 vs Agent 关系 | 区分"模型是能力载体"与"agent是能力调用框架"——模型不是 agent，agent 不是模型 | 2026-07-16-model-vs-agent-relationship |
| 模型身份 | 一个模型 id 背后的真实上游可能被 alias 改写，显示名不等于实际请求的上游 | 2026-07-16-model-identity |
| LLM Wiki 速读 | 对 LLM 概念做的一次快速梳理摘要 | 2026-07-16-llm-wiki-intro |
| Google 账号地区 | 资格判定看 Google ToS 页显示的国家，不是设备网络位置 | 2026-07-16-google-account-region |
| IP 地理位置差异 | 不同地理服务可能对同一出口报不同国家，一次查询不能下定论 | 2026-07-16-ip-geolocation-difference |
| CPA 密码 | CPA 凭据管理的注意事项，无独立文档 | 2026-07-16-cpa-password |

> 这些都是**当场问答、无独立产出**的对话。涉及的技术细节已在 [[01-model-provider-access]]、[[02-network-proxy-troubleshooting]]、[[07-troubleshooting-decision-tree]] 各篇里以可复用形式重新组织。这里只留索引，不重复展开。
