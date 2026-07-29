---
title: 个人知识资产系统设计
aliases: 跨设备知识资产,知识归档,证据包,来源保全,append-only
tags:
  - 知识管理
  - 系统设计
  - 数据契约
  - 实操笔记
created: 2026-07-29
source-dirs:
  - 2026-07-14-personal-knowledge-assets
related:
  - "[[05-feishu-knowledge-base-blueprint]]"
---

# 个人知识资产系统设计

> 这是一套跨设备、跨平台、把个人在高价值来源里看到的内容**保全、审计、检索、再用**的私有系统设计。核心矛盾是：既要让分散在各处的有价值内容能被找回来用，又不能在"整理"过程中悄悄篡改或丢失来源。

## 一、最高不变式（决定了整套系统的形态）

> **一旦内容被接受进归档，它的来源保全层不可变、完整。清洗稿、摘要、分类、行动笔记都是派生产物，可以提升可读性，但永远不能代替、截断、或静默改写来源。**

这句话不是口号，它决定了后面所有的设计：为什么是 append-only、为什么清洗稿要单独存、为什么去重只链接不删源、为什么"容量不够"不能成为删内容的理由。

从唯物辩证法看：这里处理的是"来源的客观性与派生解释的主观性"这对矛盾。系统保护来源的客观性不被主观改写侵蚀，同时允许派生解释作为辅助层存在。两者分层，不互相侵占。

## 二、三层架构

```
┌─ 发现层 (Discovery)
│   设备界 + 账号/收藏集合界
│   强信号自动接受：收藏、点赞、稍后读、下载、截图、收藏消息、自转发
│   弱信号打分：浏览历史、散落文件
│   被排除的候选保留可审计的元数据记录（不静默丢弃）
│
├─ 证据层 (Evidence)
│   每个 accepted 资产得到一个不可变证据包：
│   manifest + 元数据 + 完整可见源文 + 允许的媒体 + 可见评论
│   + 原始转写/OCR + 派生清洗稿 + 抓取日志 + SHA-256 校验
│
│   Google Drive = 全量证据归档
│   Feishu       = 运营索引 + 精选知识文档 + 热证据
│   本机         = 有界暂存缓存,永远不移动/编辑被清点的源文件
│
└─ 控制与检索层 (Control & Retrieval)
    设备/来源/候选/资产/复审异常/问答答案
    本地可重建索引做过滤 + 全文搜索
    模型可重排和综合检索证据,但答案必须披露:
    出处、覆盖、冲突、不确定性、下一步
```

## 三、完成语义：一个数学等式（防"差不多就标完成"）

```
scanned_total = included_total + excluded_total + blocked_total
```

- 每个 frozen 源基线都要对得上这个等式
- 一个源被 block 不挡其他源，但**只要还有基线项没交代，整个归档不能标"完全完成"**
- block 的要记录"为什么 block"，不能静默

> 这个等式是系统的客观性兜底。它强制每个来源都被交代：要么纳入、要么排除（带理由）、要么 block（带原因），没有"忘了"或"差不多"。

## 四、数据契约（写了就照着实现的字段）

### DeviceRecord
`device_id`、`platform` (macos/windows/ios/ipados/android)、`device_name`、`browser_profiles`、`personal_roots`（只批准的用户内容根）、`sync_services`、`verification_status`、`verified_at`、`blocker`

### SourceRecord
`source_id`（平台+账号+集合唯一）、`device_id`、`platform`、`account_ref`（隐私安全引用）、`collection`、`baseline_at`、`scanned_total`/`included_total`/`excluded_total`/`blocked_total`、`verification_status`、`evidence_ref`

### CandidateRecord
`candidate_id`、`source_id`、`title`/`original_url`/`observed_at`、`preservation_signals`、`value_score` (0–100)、`decision` (included/excluded/review/blocked)、`decision_reason`（必填，排除也要写理由）、`asset_id`（纳入后才填）

### AssetRecord
`asset_id`、`candidate_id`+`source_id`、`author`/`published_at`/`captured_at`/`content_type`/`original_url`、`evidence_package_ref`、`hot_evidence_ref`、`completeness` (complete/limited/blocked)、`limitation`（明确写缺什么）、`duplicate_of`（**链接不删源**）、`review_status`

### EvidencePackageManifest
`schema_version`、`asset_id`、`created_at`、`immutable_files` (path+长+SHA-256+MIME+角色)、`derived_files` (path+父文件+变换类型+SHA-256)、`completeness`/`limitations`/`capture_events`

### ReviewRecord / AnswerRecord
- ReviewRecord：`review_id`、`candidate_id`/`asset_id`、`reason` (missing/conflict/sensitive/high-risk/low-confidence/user decision)、`status`、`resolution`、`resolved_at`
- AnswerRecord：`question`/`answer`/`evidence_asset_ids`、`coverage_statement`/`conflicting_evidence`/`confidence_boundary`、`action_steps`/`verification_needed`/`created_at`

> AnswerRecord 里的 `coverage_statement` 和 `confidence_boundary` 是关键：强制答案承认"我覆盖了哪些、哪些没覆盖、信心边界在哪"。防止模型给出没有边界的断言。

## 五、实施进度（截至 2026-07-15 v008）

- 本机基线冻结：36,138 本地文件、237 书签、6,801 浏览器历史行
- 候选队列 append-only 填充：43,176 行完整复现基线（237 纳入/747 排除/6,054 弱信号审/36,138 本地文件 block）
- 候选导入幂等且冲突安全：同一冻结清单重放是 no-op，同 id 但内容变化被拒
- 资产 78 个（55 complete / 10 limited / 13 blocked），sidecar 证据 41,539 行
- 双语别名层：中文问题能检出英文化学论文和工作流文档，**不改写来源文本**
- 同步到飞书 `01-indexes` 和 Google Drive `00-indexes`（带版本号，旧快照不删）
- 20 篇学术 PDF、216 页全量遍历文本抽取，60 页代表页人工视觉核验
- 一个 SEM 文章有显式嵌入字体抽取限制——**保留原 PDF 权威，不猜缺字**

## 六、范围与安全边界

- 采集在来源侧**只读**
- 不绕登录、付费墙、访问控制、DRM
- 视频若不能合法保留，保留官方字幕或从合法可访问音频生成的完整转写，并记录限制
- 第一期私有个人：公开再发布、商业化、分享完整第三方源包**都不在范围**

## 七、可复用设计教训

1. **来源保全与派生解释必须分层**：混在一起迟早派生层会悄悄蚕食来源层。物理上分目录 + SHA-256 校验是最低保障。
2. **完成语义要数学化**：模糊的"差不多完成"会逐步退化为"忘了哪些没做"。`scanned = included + excluded + blocked` 是不可退让的。
3. **排除也要带理由**：`decision_reason` 对所有 decision 必填。否则"排除"会变成静默丢失。
4. **去重链接不删源**：重复是关系，不是删除依据。删了就回不来了。
5. **答案要有边界**：知识库不是搜索引擎返回链接列表，也不是模型的断言。答案要自带覆盖、冲突、信心边界、下一步——让使用者知道能用它做到什么程度。
6. **容量不够就暂停扩充，不是删内容**：这是归档系统的立身之本，一行字也不能让步。
