# Feishu Knowledge Base Plan

- Creation date: 2026-07-13
- Topic: Personal Feishu knowledge base architecture and Xiaohongshu migration
- Purpose: Build and operate a practical personal knowledge system, beginning with structured ingestion of saved and liked Xiaohongshu content.

## Current progress

- Created the personal knowledge base and nine operating areas in Feishu.
- Created Xiaohongshu collection and like indexes with the first 20 visible items in each.
- Completed the first high-value video card: source link, creator caption, platform summary, comment evidence, critical analysis, action checklist, and keyframe.
- Created a four-table knowledge control Base with 40 pilot assets, linked themes, project actions, operational views, and a dashboard.
- Created a 32-node system map in Feishu Whiteboard and connected the operating entrances from the homepage.
- Set local extraction and transcription as the default video route; Feishu Minutes is optional and not a system dependency.
- Inventoried 134 owner-managed Feishu resources and lightly inspected 34 low-confidence items.
- Created 22 content-classification nodes and moved 49 high-confidence Wiki resources into the new knowledge system.
- Left two legacy Wiki-space root pages in place because Feishu does not allow them to be moved as ordinary child nodes.
- Started a separate quality-review stage for self-authored editable documents; source PDFs, quotations, and raw evidence remain unchanged.
- Optimized ten self-authored notes: nine structured rewrites and one boundary clarification appended without disturbing the original question image.
- Upgraded `lark-cli` and Feishu Skills from 1.0.48 to 1.0.68.
- Resumed the live Xiaohongshu pipeline with the logged-in account `氧气` (Red ID `1029040812`): the collection page reports 572 notes, 112 albums, and 1 file; the like page currently reports no visible liked content.
- Created a dedicated raw-ingestion Base under `01 收集箱 / 小红书收藏`, imported the first 10 current collection records, and fully distilled the first research item into a one-sentence takeaway plus a verified action checklist.
- Imported collection items 11-30 with value tiers and topic tags. Fully processed the 30-page NotebookLM tutorial, preserved every page, generated a local OCR transcript, and attached the complete evidence package to its Feishu Base record.
- Imported collection items 31-50. Fully processed the 98-second AI learning-path video without Feishu Minutes: preserved the original video, extracted 33 timed frames with macOS AVFoundation, recovered on-screen instructions with local Vision OCR, produced a reusable practice card, and attached the 86 MB evidence package to the verified Feishu Base record.
- Corrected the ingestion model after review: the Base now separates `原文正文（保真）`, `原文标签`, `作者与互动`, `原始媒体链接`, and `视频转写与画面文字`; the full page text and visible comment evidence for items 31-50 were backfilled. Summaries remain auxiliary fields and no longer stand in for source content.
- Switched the user-facing Xiaohongshu archive from Base to individual Feishu Docx pages. Twenty source-preserving documents for items 31-50 plus a directory page now sit directly under `小红书收藏`; Base is legacy staging only and is no longer the reading入口.

## Feishu links

- Personal knowledge base: https://larkcommunity.feishu.cn/wiki/Jhmxwyvoviej9zkVAx3c8b4In6c
- Knowledge control panel: https://larkcommunity.feishu.cn/wiki/MVKBwHDDBiRefXknSfjc4hJDndc
- Personal knowledge system map: https://larkcommunity.feishu.cn/wiki/Jx9xwqh5LiGNl0ke3SIccv3Tn3D
- First video card: https://larkcommunity.feishu.cn/wiki/M6bMwQD4AivSKPkCNXGcuihJnxg
- Video ingestion standard: https://larkcommunity.feishu.cn/wiki/LVLcwW94qiVlmykNmmEcCxEOnfg
- Xiaohongshu raw-ingestion ledger: https://larkcommunity.feishu.cn/wiki/Io7iwxupwiRsC7k5ZYKcl2tlnlc
- Xiaohongshu source-document directory (items 31-50): https://larkcommunity.feishu.cn/docx/IBazdkjnqoxe4yxBLK6cl33EnSB

## Pilot artifacts

- `twitter-content-growth-video-card.xml`: structured source for the first video knowledge card.
- `twitter-content-growth-keyframe-2026-07-13.jpg`: captured source keyframe.
- `video-ingestion-standard.xml`: tiered operating standard for video evidence, transcription, and fallback processing.
- `knowledge-assets-seed-records.json`: first 40 Xiaohongshu assets imported into the control Base.
- `xiaohongshu-batch-2026-07-13-02.json`: normalized Base payload for collection items 11-30.
- `xiaohongshu-notebooklm-6982e2f9/`: 30-page NotebookLM source capture and local OCR transcript.
- `notebooklm-source-6982e2f9.zip`: evidence package attached to the corresponding Feishu Base record.
- `notebooklm-summary-6982e2f9.md`: cleaned extraction with workflow, use cases, and evidence boundaries.
- `xiaohongshu-batch-2026-07-13-03.json`: normalized Base payload for collection items 31-50.
- `xiaohongshu-ai-learning-683a935f/`: original 98-second video, 33 timed frames, local OCR evidence, and the cleaned learning-method card.
- `xiaohongshu-ai-learning-683a935f-evidence.zip`: complete evidence package attached to the corresponding Feishu Base record.
- `xiaohongshu-full-content-batch-2026-07-14-31-50.json`: full source-text, visible-comment, and media-link capture for items 31-50.
- `apply-full-content.py`: repeatable backfill script that writes source-preserving fields to the Feishu Base.
- `create-xiaohongshu-docs.py`: repeatable Docx creation script for the source-preserving Wiki archive.
- `xiaohongshu-docs-batch-2026-07-14-31-50.json`: item-to-Docx mapping for the first document archive batch.
- `xiaohongshu-full-content-standard.md`: long-term source-preservation rules.
- `knowledge-system-map.xml`: Feishu document wrapper for the knowledge-system whiteboard.
- `diagrams/2026-07-13T162100/diagram.mmd`: source for the 32-node system map.
- `migration-execution-summary-2026-07-13.md`: verified results and remaining boundaries from the first document-organization batch.
- `agent-collaboration-note.xml`, `practice-driven-change-note.xml`, and related XML sources: verified structured rewrites for the first ten self-authored notes.
