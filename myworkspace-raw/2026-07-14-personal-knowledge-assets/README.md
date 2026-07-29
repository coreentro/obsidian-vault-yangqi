# Personal Knowledge Assets

- Creation date: 2026-07-14
- Topic: Cross-device personal high-value knowledge asset system
- Purpose: Preserve, audit, search, and reuse valuable content from the user's devices, browsers, local files, and online platforms without deleting or silently shortening any accepted source material.

## Highest-priority invariant

Once content is accepted into the archive, its source-preserving layer is immutable and complete. Cleaned transcripts, summaries, classifications, and action notes are separate derived artifacts. They may improve readability, but they must never replace, truncate, or silently rewrite the source.

## Current implementation status

- Conversation workspace created.
- Design and data contracts recorded locally.
- Local append-only archive, audit ledger, reconciliation, read-only inventory, Chromium discovery, and search core are implemented test-first.
- Current Mac baseline is frozen at 36,138 local files, 237 bookmarks, and 6,801 browser-history rows.
- Candidate queue is now seeded append-only: 43,176 candidate rows reproduce the source baseline exactly (237 included, 747 excluded, 6,054 weak-signal review, and 36,138 local-file blocked).
- Candidate imports are idempotent and conflict-safe; replaying the same frozen inventory is a no-op, while a changed record with the same id is rejected.
- Candidate summaries, the current ledger, the search database, history scoring, and local-file classifications are synchronized to Feishu `01-indexes` and Google Drive `00-indexes` under versioned names; prior snapshots remain untouched.
- Capture batches 001–003, two cross-device duplicate-reference packages, five local Markdown documents, and twenty scholarly PDFs currently contain 71 assets: 50 complete, 8 limited, and 13 blocked. Batch 003's four hosts resolved to the non-public `198.18.0.0/15` range in the current environment, so the safety boundary recorded blocked packages without guessing source content.
- Feishu control tables are live with 1 device, 13 sources, all 43,176 candidates, 71 assets, 41,532 review records, and 10 evidence-backed blind-test answers.
- Ten newly captured local assets also have a separate conflict-safe bilingual alias layer, allowing Chinese questions to retrieve English chemistry papers and workflow documents without rewriting their source text.
- Feishu private hot storage is live with index, selected-knowledge, and evidence-manifest folders; 14 index/audit/manifest files are uploaded and verified.
- Google Drive desktop 128.0 is currently installed, logged in as `yangqihello@gmail.com`, mounted through File Provider, and has a `personal-knowledge-assets` evidence-root directory tree. The earlier 127.0.1.0 installer record is retained as historical installation evidence.
- Media-tool isolation is complete. Forty-six bookmark-source assets, five complete local Markdown assets, and twenty complete scholarly PDFs are synced and checksum-verified; weak-signal scoring, local-file metadata classification, the 20-package random cloud recovery gate, and the ten-question blind evaluation are complete. The twenty PDFs cover 216 pages, all traversed for text extraction with 60 representative pages visually checked. Twenty-five accepted local assets have bilingual base aliases, with ten later retrieval phrases stored as append-only additions. One SEM article has an explicit embedded-font extraction limitation; its exact PDF remains authoritative and missing glyphs were not guessed. The local-content stage remains active with 35,238 metadata-routed files still awaiting safe review. All remaining 191 bookmarks have explicit manual routes in the local and Feishu review queues; completing them plus other devices/accounts requires user-visible logged-in access or manual decisions.

## Planned artifacts

- `knowledge-asset-system-design.md`: approved architecture and preservation rules.
- `data-contracts.md`: device, source, candidate, asset, review, and answer interfaces.
- `implementation-log.md`: dated implementation and verification evidence.
- `src/`: local knowledge asset core.
- `tests/`: automated behavioral tests.
- `data/`: generated manifests, indexes, inventories, and audit reports; never original user files.

## Latest verified boundary (append-only correction, 2026-07-15)

The earlier 71-asset paragraph is a historical snapshot from before PDF batch 005. The current authoritative boundary is recorded in `data/implementation-status-2026-07-15-v006.json`: 76 assets (54 complete, 9 limited, 13 blocked), 41,537 review records, 55 full-text documents, 30 base aliases, and 15 append-only alias additions. Batch 005 synchronization evidence is in `data/local-pdf-sync-verification-2026-07-15-v005.json`. No prior status or evidence snapshot was deleted or silently rewritten.

Batch 006 has since been completed. The newest authoritative boundary is in `data/implementation-status-2026-07-15-v007.json`: 78 assets (55 complete, 10 limited, 13 blocked) and 41,539 review records. Batch 006 synchronization evidence is in `data/local-pdf-sync-verification-2026-07-15-v006.json`; the earlier v006 status remains as a historical snapshot.

The post-batch search verification is recorded in `data/local-index-verification-2026-07-15-v003.json`: 57 searchable documents, 30 base aliases, 15 append-only aliases, SQLite integrity OK, and no empty source text or missing FTS rows. The corresponding current status snapshot is `data/implementation-status-2026-07-15-v008.json`.
