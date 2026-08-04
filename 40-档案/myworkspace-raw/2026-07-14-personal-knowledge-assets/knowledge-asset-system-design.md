# Cross-Device Personal Knowledge Asset System Design

## Goal

Build a private system that discovers valuable content across macOS, Windows, iPhone/iPad, Android, browsers, local personal directories, Xiaohongshu, Bilibili, Zhihu, X, Reddit, Telegram, forums, and newly discovered sources.

## Non-negotiable preservation rules

1. Accepted source content is append-only and immutable.
2. Original text, images, media, subtitles, OCR, and raw transcripts are never overwritten by cleaned or summarized versions.
3. A cleaned transcript may add punctuation, paragraphs, speaker labels, timestamps, and explicit corrections, but it may not omit words, repetitions, or ideas.
4. Summaries and knowledge cards are derived aids. They never stand in for the source.
5. Deduplication links records; it does not delete source records or their source-specific context.
6. Missing material is reported as missing. Models must not invent it.
7. Capacity pressure pauses ingestion and triggers expansion. It never justifies deleting accepted content.

## Architecture

### Discovery plane

- Devices define the inspection boundary.
- Accounts and platform collections define logical sources.
- The same account is ingested once; other devices contribute only device-local material.
- Strong preservation signals are accepted automatically: collections, likes, bookmarks, read-later queues, downloads, screenshots, saved messages, and self-forwarded material.
- Weak signals such as browsing history and scattered files are scored. Excluded candidates retain an auditable metadata record.

### Evidence plane

Each accepted asset receives an immutable evidence package with a manifest, metadata, full visible source text, permitted media, captured visible comments, raw transcripts or OCR, derived cleaned text, capture logs, and SHA-256 checksums.

Google Drive is the full evidence archive. Feishu holds operational indexes, selected knowledge documents, and hot evidence. The current Mac uses a bounded staging cache and never moves or edits the source files being inventoried.

### Control and retrieval plane

The operational model contains devices, sources, candidates, assets, review exceptions, and question answers. A local rebuildable index supports filters and full-text search. A model may rerank and synthesize retrieved evidence, but answers must disclose citations, coverage, conflicts, uncertainty, and practical next steps.

## Completion semantics

For every frozen source baseline:

`scanned_total = included_total + excluded_total + blocked_total`

A blocked source does not stop other sources, but the overall archive cannot be labeled fully complete while any baseline item remains unaccounted for.

## Safety and scope

- Collection is read-only at the source.
- No login, paywall, access control, or DRM bypass.
- If original video cannot lawfully be retained, preserve available official subtitles or a complete transcript generated from lawfully accessible audio and record the limitation.
- Phase one is private and personal. Public republishing, commercialization, and sharing complete third-party source packages are out of scope.

