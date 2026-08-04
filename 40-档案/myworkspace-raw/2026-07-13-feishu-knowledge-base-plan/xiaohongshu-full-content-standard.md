# Xiaohongshu full-content ingestion standard

## Core rule

Every saved or liked note enters Feishu in two layers:

1. **Source-preserving layer**: original title, full caption/body, original hashtags, author, date, source URL, visible comments/interaction evidence, media URLs, and local attachments where available.
2. **Working layer**: topic tags, value tier, one-sentence takeaway, action points, risks, and review status.

The working layer may interpret the source, but must never replace or silently rewrite it.

## Media rules

- Image notes: retain every page-observed image URL and attach a local evidence package when the asset can be downloaded reliably.
- Video notes: retain the original video URL and attach the original video when possible; add speech transcription and/or keyframe OCR in a separate field.
- If transcription is incomplete, write an explicit status such as “原片已保留；转写待复核”，never invent missing content.

## Comment rules

Visible comment text is stored as evidence, clearly labeled as a page-visible capture. It is not treated as a representative sample of all comments unless the page exposes a complete list.

## Quality gates

- A record cannot be marked “已提炼” unless the source-preserving layer is present.
- A video cannot be marked “视频已转写” unless the transcript or OCR has been checked against the source.
- The Base is the index and retrieval surface; the attachment package is the evidence surface; the Wiki/Docx layer is for durable synthesis.
