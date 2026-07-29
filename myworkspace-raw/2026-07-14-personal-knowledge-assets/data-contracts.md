# Data Contracts

## DeviceRecord

- `device_id`: stable ASCII identifier.
- `platform`: `macos`, `windows`, `ios`, `ipados`, or `android`.
- `device_name`: user-recognizable name.
- `browser_profiles`: discovered browser/profile identifiers.
- `personal_roots`: approved user-content roots only.
- `sync_services`: cloud or application sync services.
- `verification_status`: `pending`, `verified`, or `blocked`.
- `verified_at`: ISO 8601 timestamp or null.
- `blocker`: explicit reason or null.

## SourceRecord

- `source_id`: stable identifier unique to platform, account, and collection area.
- `device_id`: discovery device, if device-local.
- `platform`: platform or application name.
- `account_ref`: privacy-safe account reference.
- `collection`: collection, likes, bookmarks, history, folder, or other source area.
- `baseline_at`: frozen baseline timestamp.
- `scanned_total`, `included_total`, `excluded_total`, `blocked_total`: non-negative integers.
- `verification_status`: `pending`, `verified`, or `blocked`.
- `evidence_ref`: audit evidence location.

## CandidateRecord

- `candidate_id`: stable identifier.
- `source_id`: owning source.
- `title`, `original_url`, `observed_at`: discovery metadata.
- `preservation_signals`: explicit save/like/bookmark/download signals.
- `value_score`: integer 0-100.
- `decision`: `included`, `excluded`, `review`, or `blocked`.
- `decision_reason`: mandatory, including exclusions.
- `asset_id`: populated only after inclusion.

## AssetRecord

- `asset_id`: stable archive identifier.
- `candidate_id` and `source_id`: provenance.
- `author`, `published_at`, `captured_at`, `content_type`, `original_url`.
- `evidence_package_ref`: Google Drive or staging package location.
- `hot_evidence_ref`: optional Feishu hot copy.
- `completeness`: `complete`, `limited`, or `blocked`.
- `limitation`: explicit missing-content explanation.
- `duplicate_of`: related canonical asset or null; never deletes this record.
- `review_status`: `automatic`, `review_required`, or `reviewed`.

## EvidencePackageManifest

- `schema_version`, `asset_id`, `created_at`, `source_id`.
- `immutable_files`: path, byte length, SHA-256, MIME type, and role.
- `derived_files`: path, parent immutable file, transformation type, and SHA-256.
- `completeness`, `limitations`, and `capture_events`.

## ReviewRecord

- `review_id`, `candidate_id` or `asset_id`.
- `reason`: missing, conflict, sensitive, high-risk, low-confidence, or user decision.
- `status`: open or resolved.
- `resolution`, `resolved_at`.

## AnswerRecord

- `question`, `answer`, `evidence_asset_ids`.
- `coverage_statement`, `conflicting_evidence`, `confidence_boundary`.
- `action_steps`, `verification_needed`, `created_at`.

