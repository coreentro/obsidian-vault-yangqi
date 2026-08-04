# Audit Report — 2026-07-14

## Audit status

**Partial implementation; not full historical completion.** The current Mac discovery baseline and control plane are reconciled. Evidence capture from platform accounts, other devices, and weak-signal classification remain incomplete and visibly blocked.

## Resolution note added after the initial environment audit

- The earlier Google Drive sign-in and Feishu upload blockers were resolved after the user completed the required local authorization steps. The original blocker notes below are retained as historical audit evidence; the current state is the resolved state recorded in the later bullets.
- Candidate registration is now complete for the frozen Mac baseline: 43,176 append-only candidate rows were seeded from the seven inventory manifests. Reconciliation remains `43,176 = 237 + 747 + 42,192`, delta `0`.
- Candidate decisions are deliberately not equivalent to asset capture: bookmarks are included for the first capture queue, history candidates remain review items, and all local files remain blocked pending value classification.

## Verified facts

- Current Mac device records: 1.
- Registered sources: 13.
- Total discovered source rows: 43,176.
- Candidate rows seeded from frozen inventories: 43,176; every source has one candidate row per scanned item.
- Candidate summary SHA-256: `c0fa9b318aade8faaea01fe764b6191fda301c1626ae824803c9cb018ea6d802`.
- Candidate ledger snapshot SHA-256: `38f68eb7e88d5392ecd58b690c5e0cc36f38902c64b108eb91d59aa026942bc4`; the matching Google Drive copy is versioned as `00-indexes/knowledge-assets-candidates-2026-07-14.sqlite3`.
- Strong-save rows provisionally included: 237 browser bookmarks.
- Non-content browser-history rows excluded with audit accounting: 747.
- Rows blocked for classification or complete capture: 42,192.
- Reconciliation delta: 0.
- Feishu source records independently reproduce the same totals and satisfy `scanned = included + excluded + blocked` for every source.
- Current local-file baseline contains 36,138 files and was created read-only with SHA-256 metadata; the active conversation directory was explicitly excluded.
- Six Chromium-family profile manifests are frozen: 237 bookmarks, 6,801 history rows, and 6,054 readable history candidates.
- Automated preservation and ledger test suite: 21 passed, 0 failed, with `ResourceWarning` treated as an error.
- The Google Drive download record was obtained from Google's official endpoint. The first saved body was HTTP-compressed and was not treated as an installer. Its XAR tail was extracted locally; the XAR table of contents contains Apple Developer ID Installer certificates for Google LLC and includes `GoogleDrive_arm64.pkg` version `127.0.1.0`. Staged distribution package SHA-256: `da3a260744cf0fdd4c62e72d00b7fb8e53147cad3a623ef7a925fde7da48e7aa`.
- Isolated media tools are installed and runnable: `yt-dlp 2026.07.04`, `openai-whisper 20250625`, and `ffmpeg 8.1.2`.
- Media virtual environment and package cache occupy about 1.48 GB in total; no Whisper model weights have been downloaded.

## Preservation checks

- Immutable evidence-package creation rejects silent overwrite.
- Full visible source text and raw transcript artifacts are separate from cleaned and summarized derivatives.
- Lossless transcript validation rejects cleaned text that removes source words.
- Duplicate content remains represented by distinct source records and may only be linked.
- Frozen inventory manifests reject silent replacement.
- Browser-history databases are copied with WAL state before read-only inspection; the source browser databases are not edited.

## Frozen manifest checksums

| Manifest | SHA-256 |
|---|---|
| `chrome-default-2026-07-14.json` | `1b9ed949d4d8544e7ea5897f0595e471d2174898614080f48d72708d1809aadd` |
| `chrome-guest-2026-07-14.json` | `676924c867237c87e358266067d23d9fb226838a9f89c628179b742e378eb35a` |
| `chrome-profile-1-2026-07-14.json` | `ce22a8ebdce38c853408492dc5ed7ab7d0018e5a0b85d5c55ee4e546477b2a67` |
| `chrome-profile-2-2026-07-14.json` | `3c8ffbd894e7502a9845d330edb3c08fa4ca865cbff66d133c08f75828d76be5` |
| `chrome-profile-3-2026-07-14.json` | `523a213291854b3bf9b1c4289d99700ccd8f4989c08eeb1a43cc817bc255473d` |
| `edge-default-2026-07-14.json` | `5b22be10a5fa51a5502402fc5920a9064649a0723145740aa45d0f207f4f9d18` |
| `mac-current-local-2026-07-14.json` | `291d8630003c08a4dff25498ac4e098a9184c59d7decef031ff706cffa226890` |

## Explicit blockers and historical resolution record

- Google Drive for desktop is now installed at `/Applications/Google Drive.app`, signed by Google LLC Developer ID, version 127.0.1.0, and running. DriveFS logs still show no authenticated account (`user_email: ""`, `current_account_token: ""`, `no_user`), so sign-in, File Provider mount, and streaming mode remain unverified.
- Feishu user authorization is now valid for `space:folder:create` and `drive:drive`. The private hot-storage root and three child folders were created successfully; their tokens are recorded in `data/feishu-control-plane.json`.
- Feishu upload authorization is now valid for `drive:file:upload` and `drive:drive.metadata:readonly`. Seven index/control files and seven frozen inventory manifests were uploaded and re-listed successfully; no source files were moved or deleted.
- Google Drive is now signed in as `yangqihello@gmail.com`. The File Provider domain is `com.google.drivefs.fpext/gdrive-111465258891193642050`; `fileproviderctl` reports the domain as writable and all 14 staged files as `ul:uploaded`. Source and Google Drive copies match byte-for-byte by SHA-256 for all 14 files.
- Google Drive evidence root created: `我的云端硬盘/personal-knowledge-assets/`, with `00-indexes`, `01-raw-evidence`, `02-media`, `03-transcripts`, `04-manifests`, `05-capture-logs`, and `06-recovery-tests`.
- The latest audit and implementation records are versioned in the cloud as `audit-report-2026-07-14-verified.md` and `implementation-log-2026-07-14-verified.md`; earlier copies remain unchanged for audit history.
- Candidate queue artifacts were additionally synchronized without overwrite: Feishu tokens `PFesb8qqdoH5gLxaIuecQRwOnme` (summary), `RbORbDxrLo2BJVxinX0cF1L5nAb` (ledger), and `IjKMbAQ55oKzQcxPUaich14Xngd` (control-plane snapshot). Google Drive copies are byte-identical to local sources.
- The first capture queue is frozen but not yet counted as captured: `data/capture-batch-001-2026-07-14.json` contains 20 public knowledge-page candidates. A redirect, login, paywall, dynamic omission, or inaccessible page will be recorded as a limitation rather than guessed or silently substituted.
- Other computers, phones, browser profiles, platform accounts, and local directories cannot be declared complete until the user provides or confirms access.
- Coze project creation failed because the account has insufficient credits. No Coze project or deployment was created.
- No source is marked fully captured merely because it was discovered. The 237 bookmarks are strong-save decisions but still require complete evidence packages before asset-level completion.

## Material interpretation

The system has established its production relations before scaling production: immutable source evidence is the base layer, while indexes, summaries, and model outputs are subordinate instruments. The main contradiction has now shifted from schema design to access and capture capacity—device/account availability, cloud permissions, and lawful platform extraction—not to a lack of classification ideas.

## Next acceptance gates

1. Sign in to the running Google Drive app, confirm the intended Google account, enable streaming mode, and verify the File Provider mount before uploading evidence.
2. Upload the local index and manifest artifacts to `01-indexes` and `03-evidence-manifests` only after checksum verification; original evidence remains primary in Google Drive.
3. Capture complete evidence packages for the 237 bookmark records in bounded batches.
4. Register and freeze every remaining device and account source.
5. Run batch anomaly review plus the required random sample, then perform ten-package cloud recovery tests and ten-question blind evaluation.

## Continuation audit — 2026-07-15

- Trial batch `capture-batch-001-2026-07-14` was attempted without credentials and without disabling TLS verification. Of 20 public bookmark candidates, 12 yielded complete raw HTML packages, 2 yielded limited application shells, and 6 were blocked by HTTP errors or network/TLS limits.
- Each attempted item has a separate immutable package under `data/evidence/<asset_id>/`. The package manifest and `checksums.sha256` were verified; no package checksum mismatch, missing file, or extra untracked file was found.
- The trial produced 20 ledger assets with the same completeness distribution (12/2/6). A blocked or limited package is not counted as a complete historical capture and remains review-required in Feishu.
- Google Drive `01-raw-evidence` contains 126 copied package files. Local and cloud SHA-256 values match for all 126 files. File Provider currently reports no authentication or indexing blocker and zero pending indexable items.
- Feishu Assets now has 20 review-required records. The source URL, package completeness, original-state limitation, and a valid Drive search link are retained as index metadata; the local package and cloud copy remain the evidence authority.
- Verification artifact: `data/capture-verification-001-2026-07-15.json`, SHA-256 `2a1efcae503e47af256df893ba4fba55af0fc24658edeedd343d3a875fa03a3d`. Capture result artifact: `data/capture-results-001-2026-07-15.json`, SHA-256 `a5d946db463643fa9d7b6422aa2c4e94bbd5e0f9e93f57f2332a10f0d4cc9e00`.
- Reconciliation remains exact: `43,176 = 237 + 747 + 42,192`, delta `0`. The 237 bookmark inclusion decision is not being reinterpreted as 237 complete assets; only 20 have been attempted, and 6 of those remain blocked.
- The complete automated preservation suite now reports 28 passed and 0 failed, with `ResourceWarning` treated as an error.
- A first Drive recovery sample restored 10 trial packages to a temporary directory and passed 10/10 checksum validations. This is evidence of recoverability for the trial only, not completion of the full required random recovery gate.
- A second public-page batch of 20 bookmarks was attempted: 13 complete, 4 limited, 3 blocked. Its 130 package files match the Google Drive copies byte-for-byte. The local ledger now has 40 attempted assets (25 complete, 6 limited, 9 blocked).
- Batch-002 result SHA-256 is `8d8fa4171b11553dbe455bfa8090340d95a0e860e5cee64b4b238939ecd1f7b1`; verification SHA-256 is `a64cb34e0420cb26f7eee3b24af15fbbab1b5a0ba5e80192f4c836b419716ddb`.
- A second recovery sample restored 10 batch-002 packages and passed 10/10 checksum validations; 20 trial packages have now been recovery-checked in total.

The next contradiction is now capture quality and access boundaries, not the existence of an index: complete the remaining bookmark batches only when each source can be legally and reproducibly read, then perform the required anomaly review, 5% random sample, ten-package recovery test, and ten-question blind evaluation.

### Local-document batch 001 — 2026-07-15

- Five non-sensitive Markdown files were selected from the frozen local inventory through an explicit metadata-only allowlist. Only those five contents were opened; their combined size was 15,433 bytes.
- Each source was revalidated against its frozen byte length and SHA-256 before capture and checked again after the read. All five original files remained unchanged.
- The evidence layer preserves exact original bytes plus a separately labelled exact UTF-8 decoding; it does not replace the original with a summary or cleaned version. All 35 package files pass their checksum lists and match the Google Drive copies.
- The batch is idempotent: the first run registered five assets, and an immediate replay registered zero. Current verified totals are 51 assets (30 complete, 8 limited, 13 blocked), 41,512 reviews, and 30 full-text index documents.
- Feishu boundary reads at asset offset 46 and review offset 41,507 returned exactly the five new records with `has_more=false`; all five candidate rows independently show the expected asset IDs. This proves the local and Feishu counts for this batch rather than inferring them from upload intent.

### Chemistry PDF batch 001 — 2026-07-15

- Five scholarly chemistry PDFs were selected using a frozen metadata-only allowlist totaling 44,450,227 bytes. The selected topics cover mechanochemistry, condensation catalysis, ceria oxygen vacancies, sulfur-vacancy electron bridges, S-scheme heterojunctions, and photocatalytic hydrogen evolution.
- All 62 pages were traversed for text extraction; no page was empty. First, middle, and last pages were rendered for every article, producing 15 visual checks with no clipping, rotation, missing page body, or unreadable layout defect.
- Every evidence package retains the exact original PDF as the authority. Page-delimited extracted text is additive and does not replace figures or the original layout; the capture log explicitly states that raster figure text may not be represented in extraction.
- All five source hashes, 45 package files, package checksum lists, and Google Drive copies match. Immediate replay registered zero assets.
- Feishu boundary reads at asset offset 51 and review offset 41,512 returned the five expected rows with `has_more=false`; the five candidate records show the exact expected asset IDs. Verified totals are 56 assets, 41,517 reviews, and 35 full-text search documents.

### Chemistry PDF batch 002 — 2026-07-15

- Five additional scholarly PDFs were selected through a frozen metadata-only allowlist totaling 17,089,318 bytes. Sensitive personal documents and non-allowlisted files remained unopened.
- All 64 pages were traversed for text extraction with zero empty pages. First, middle, and last pages were rendered for each article, producing 15 legible and unclipped visual checks.
- All five packages passed frozen-source hash checks, exact source-to-`source-original.pdf` byte comparison, package checksum verification, and an idempotent replay that added zero assets. Google Drive contains matching 45-file package copies.
- Feishu boundary reads at asset offset 56 and review offset 41,517 returned exactly the five expected rows with `has_more=false`; all five candidates point to their expected asset IDs. Verified totals are 61 assets, 41,522 reviews, 40 full-text search documents, and 15 bilingual alias records.
- The append-only timestamp correction `data/local-pdf-batch-002-timestamp-correction-2026-07-15.json` documents four planned timestamp labels that postdated their actual filesystem writes. The derived files were preserved unchanged, and no source evidence, asset content, or index content was affected.

### Chemistry PDF batch 003 — 2026-07-15

- Five non-sensitive scholarly PDFs totaling 5,739,907 bytes were frozen by path, size, and SHA-256 before content access. Personal identity, examination, application, and credential-like files remained excluded from automatic reading.
- All 45 pages were traversed with zero empty extraction pages; 15 first/middle/last renders were visually reviewed. One publisher copyright-only final page was preserved as present rather than treated as missing or guessed.
- All five packages passed exact source-to-`source-original.pdf` byte comparison, package checksum verification, and idempotent replay with zero new assets. Their 45 Google Drive package files match the local file sets and hashes.
- Feishu reads at asset offset 61 and review offset 41,522 returned exactly five expected rows with `has_more=false`; all five candidate rows are `included` and reference the expected asset. Verified totals are 66 assets and 41,527 reviews.
- Search now contains 45 full-text documents, 20 immutable base alias sets, and five append-only alias additions. Five representative bilingual queries return the intended new assets first. The complete automated suite passes 75 tests.

### Scholarly PDF batch 004 — 2026-07-15

- Five non-sensitive PDFs totaling 10,169,065 bytes were frozen before reading. All 45 pages were traversed and 15 pages visually sampled; no empty extraction page or sensitive-pattern hit was found.
- Four articles rendered and extracted normally. The SEM article contains an embedded Traditional Chinese font defect: diagrams and structure remain readable, but some glyphs are absent from derived text and sampled rendering. This limitation is written inside the evidence package; author text and missing glyphs were not guessed, and `source-original.pdf` remains authoritative.
- All five packages passed source-to-original byte comparison, checksum verification, and idempotent replay with zero new assets. Their 45 Google Drive files match the local packages.
- Feishu reads at asset offset 66 and review offset 41,527 returned exactly five expected rows with `has_more=false`; candidate links are correct. Totals are 71 assets and 41,532 reviews.
- Search contains 50 documents, 25 immutable base alias sets, and ten append-only alias additions. Five representative queries return the intended assets first; the full suite passes 75 tests.
- A conflict-safe bilingual alias layer was added for the ten local assets after testing showed that English-only articles were weakly recalled by Chinese questions. Alias rows are additive, separately hashed, idempotent, and forbidden from replacing the indexed source. Representative Chinese queries now rank the intended chemistry and workflow assets first.

### Statistical correction — 2026-07-15

The earlier aggregate text `26 complete, 6 limited, 8 blocked` was an arithmetic transcription error. The authoritative batch results are `12/2/6` and `13/4/3`, so the correct aggregate is `25 complete, 6 limited, 9 blocked`. No asset, evidence package, manifest, or source file changed; only the derived aggregate description was corrected.

### Google Drive version follow-up — 2026-07-15

The currently installed `/Applications/Google Drive.app` reports version `128.0`. References to `127.0.1.0` above describe the originally inspected installer and the earlier installation state; they are retained as historical evidence rather than silently rewritten. The active File Provider mount is available under the authenticated `yangqihello@gmail.com` account.

### Control-plane, classification, and batch-003 follow-up — 2026-07-15

- Feishu Base now contains all 43,176 candidate rows, 44 asset rows, and 41,314 review rows. First/last boundary records were read back from Feishu and match the local append-only ledger; the answer table remains at zero.
- All 6,054 history candidates received a derived, explainable value score. All 36,138 local-file candidates received a metadata-only classification without opening or modifying source files: 875 are auditable exclusion recommendations and 35,263 remain review-required, including 242 sensitive-name records that cannot be auto-captured.
- The final public batch runner review found no Critical or Important issue after DNS pinning, redirect validation, exact raw-byte preservation, strict replay verification, dry-run isolation, atomic registration, and timeout-process cleanup were tested. The suite reports 63 passed.
- Batch 003 attempted four anonymous public URLs. The current resolver mapped every hostname to `198.18.0.x`; because that range is not public, all four items are blocked. No source body was fetched or inferred. The result distribution is now 44 total assets: 25 complete, 6 limited, 13 blocked.
- A second execution replayed all four finalized blocked packages without fetching, overwriting, or adding assets. All 20 batch-003 package files match their Google Drive copies. Verification artifact: `data/capture-verification-003-2026-07-15.json`, SHA-256 `572652b9a578fb60b4b5f9b2395e40bee86537e4a10d7ef93b37f5abacfd85e0`.
- Two further bookmark sources had exact URLs already represented by complete assets. Separate limited duplicate-reference packages preserve their frozen bookmark metadata and point to the prior complete evidence; no source record was deleted and no page was re-downloaded. The current distribution is 46 assets: 25 complete, 8 limited, 13 blocked.
- The required random anomaly/recovery sample selected 20 of 46 packages without replacement and restored them from Google Drive. All 20 passed file-set, size, SHA-256, and package-checksum validation; artifact SHA-256: `82c9e8b90b8150023fa9ca2e59fafac58b032d740cc1ad31d877eef55dc9623d`.
- Ten personal-question blind tests produced nine actionable improvements and one evidence-insufficient refusal. Every answer names evidence assets, coverage, conflicts, confidence limits, actions, and current-source checks; fabricated-source count is zero. The acceptance threshold of eight improvements is passed.
