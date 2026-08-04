# Avatar Pet

- Created: 2026-07-13
- Topic: Create a personalized pet based on the user's avatar
- Purpose: Store the generated pet image and related conversation artifacts.

## Artifacts

- `avatar-reference.jpg`: source avatar supplied by the user
- `avatar-pet.png`: generated black fox-cat companion portrait
- `docs/superpowers/specs/2026-07-13-codex-avatar-pet-design.md`: approved design specification for the Codex-compatible custom pet
- `docs/superpowers/plans/2026-07-13-codex-avatar-pet.md`: task-by-task production, QA, packaging, and installation plan
- `xiao-mo-run/qa/run-summary.json`: final artifact and installation index
- `xiao-mo-run/qa/contact-sheet.png`: contact sheet for all nine animation states
- `xiao-mo-run/final/spritesheet.webp`: validated 1536 x 1872 Codex pet atlas
- `xiao-mo-run/final/validation.json`: structural atlas validation report
- `xiao-mo-run/qa/review.json`: per-frame structural and edge inspection report
- `.superpowers/sdd/task-7-despill-report.md`: final visual QA and deterministic despill report
- `xiao-mo-run/qa/previews/`: animated GIF previews for all nine states

## Installation

- Display name: `小墨`
- Package: `/Users/yangqi/.codex/pets/xiao-mo`
- Versioned directory used: no; the base `xiao-mo` directory was available
- Package files: `pet.json`, `spritesheet.webp`
- Codex GUI selection was intentionally not performed as part of the packaging task.
