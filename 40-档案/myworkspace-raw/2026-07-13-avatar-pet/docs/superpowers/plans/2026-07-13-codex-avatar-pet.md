# Codex Avatar Pet Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create, validate, package, and locally install “小墨,” a Codex-compatible animated desktop pet based on the supplied avatar.

**Architecture:** Prepare an official hatch-pet run, generate one canonical hand-drawn sticker character, ground all nine animation rows in that reference, and use deterministic scripts to extract frames and build the fixed atlas. Install only after automated validation and visual QA both pass.

**Tech Stack:** Codex `$imagegen`, bundled hatch-pet Python scripts, Python 3, jq, PNG/WebP, Codex local pet manifest.

## Global Constraints

- Project root: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet`.
- Source avatar: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/avatar-reference.jpg`.
- Hatch-pet root: `/Users/yangqi/.codex/vendor_imports/skills/skills/.curated/hatch-pet`.
- Pet id: `xiao-mo`; display name: `小墨`; style: hand-drawn `sticker`.
- Preserve tousled black hair, playful wink, simplified silver accessories, tattoo linework, dark patterned clothing, and warm amber accents.
- Exclude text, code glyphs, scenery, cast shadows, detached effects, visible guides, and details unreadable at 80–224 px.
- Final atlas: exactly `1536x1872`, 8 columns by 9 rows, `192x208` cells, transparent unused cells.
- This project is not a Git repository. Do not initialize Git or claim commits; use file validation checkpoints.
- Keep at most two generation workers active at once.
- Do not install until deterministic validation and final visual QA pass.

## File Structure

- Create: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run/` — complete run.
- Create: `xiao-mo-run/pet_request.json` — normalized identity and chroma key.
- Create: `xiao-mo-run/imagegen-jobs.json` — job dependencies and state.
- Create: `xiao-mo-run/references/canonical-base.png` — identity source of truth.
- Create: `xiao-mo-run/decoded/*.png` — base and nine row strips.
- Create: `xiao-mo-run/frames/` — extracted cells.
- Create: `xiao-mo-run/final/spritesheet.webp` — installable atlas.
- Create: `xiao-mo-run/qa/` — validation, contact sheet, GIFs, and summary.
- Create: `${CODEX_HOME:-$HOME/.codex}/pets/xiao-mo/` or a versioned sibling — installed package.
- Modify: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/README.md` — artifact index.

---

### Task 1: Prepare the Production Run

**Files:**
- Create: `xiao-mo-run/pet_request.json`
- Create: `xiao-mo-run/imagegen-jobs.json`
- Create: `xiao-mo-run/prompts/`
- Create: `xiao-mo-run/references/layout-guides/`

**Interfaces:**
- Consumes: approved design and avatar reference.
- Produces: ten jobs, prompts, guides, copied references, and selected chroma key.

- [ ] **Step 1: Verify prerequisites**

```bash
test -f '/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/avatar-reference.jpg'
test -f '/Users/yangqi/.codex/vendor_imports/skills/skills/.curated/hatch-pet/scripts/prepare_pet_run.py'
command -v python3
command -v jq
```

Expected: every command exits `0`.

- [ ] **Step 2: Generate the run**

```bash
python3 '/Users/yangqi/.codex/vendor_imports/skills/skills/.curated/hatch-pet/scripts/prepare_pet_run.py' \
  --pet-name '小墨' \
  --pet-id 'xiao-mo' \
  --display-name '小墨' \
  --description 'A playful miniature companion with tousled black hair and warm, mischievous energy.' \
  --reference '/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/avatar-reference.jpg' \
  --output-dir '/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run' \
  --pet-notes 'Compact full-body miniature human, approximately 1:1.5 head-to-body proportion, voluminous tousled black hair, playful wink, warm skin, simplified silver ear jewelry and rings, simplified black tattoo linework on the visible arm, one stable dark patterned outfit, warm amber accents.' \
  --style-preset sticker \
  --style-notes 'Hand-drawn sticker illustration with bold clean dark outlines, readable expression, stable proportions, no photographic face, text, scenery, shadows, or detached effects.' \
  --chroma-key auto \
  --force
```

Expected: request, manifest, prompts, and nine guides are created.

- [ ] **Step 3: Validate preparation**

```bash
RUN_DIR='/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run'
jq -e '.pet_id == "xiao-mo" and .display_name == "小墨"' "$RUN_DIR/pet_request.json"
jq -e '.jobs | length == 10 and any(.id == "base") and any(.id == "review")' "$RUN_DIR/imagegen-jobs.json"
test "$(find "$RUN_DIR/references/layout-guides" -type f -name '*.png' | wc -l | tr -d ' ')" = '9'
```

Expected: jq prints `true`; guide count is nine.

### Task 2: Generate and Lock the Canonical Base

**Files:**
- Create: `xiao-mo-run/decoded/base.png`
- Create: `xiao-mo-run/references/canonical-base.png`
- Modify: `xiao-mo-run/imagegen-jobs.json`

**Interfaces:**
- Consumes: base prompt and all base-job references.
- Produces: canonical identity used by every row.

- [ ] **Step 1: Confirm the base job is ready**

```bash
RUN_DIR='/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run'
jq -e '.jobs[] | select(.id == "base" and .status == "pending" and (.depends_on | length == 0))' "$RUN_DIR/imagegen-jobs.json"
jq '.jobs[] | select(.id == "base") | {prompt_file,input_images,output_path}' "$RUN_DIR/imagegen-jobs.json"
```

Expected: one pending job with output `decoded/base.png`.

- [ ] **Step 2: Generate the base**

Dispatch one lightweight worker using the hatch-pet base-worker contract. It must read `prompts/base-pet.md`, attach every listed reference, use `$imagegen` only, and return exactly `selected_source=` and `qa_note=`.

Expected: one centered full-body miniature-human sticker on a flat chroma background.

- [ ] **Step 3: Copy and record the approved source**

Assign the worker's complete two-line response to the shell variable `BASE_WORKER_RESULT`, then run:

```bash
SOURCE_PATH=$(printf '%s' "$BASE_WORKER_RESULT" | sed -n 's/^selected_source=//p')
test -f "$SOURCE_PATH"
cp "$SOURCE_PATH" "$RUN_DIR/decoded/base.png"
cp "$RUN_DIR/decoded/base.png" "$RUN_DIR/references/canonical-base.png"
UPDATED_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)
TMP_MANIFEST=$(mktemp)
jq --arg source "$SOURCE_PATH" --arg at "$UPDATED_AT" '(.jobs[] | select(.id == "base")) += {status:"complete",source_path:$source,completed_at:$at}' "$RUN_DIR/imagegen-jobs.json" > "$TMP_MANIFEST"
mv "$TMP_MANIFEST" "$RUN_DIR/imagegen-jobs.json"
```

Expected: both base files exist and the base job is complete.

- [ ] **Step 4: Review the identity lock**

Reject and repeat Task 2 if the character is not compact and full-body, the face is photographic or unrecognizable, or the approved hair, wink, jewelry, tattoo linework, outfit, and palette are missing.

Expected: one QA note approves all stable identity traits.

### Task 3: Generate Idle and Directional Rows

**Files:**
- Create: `xiao-mo-run/decoded/idle.png`
- Create: `xiao-mo-run/decoded/running-right.png`
- Create: `xiao-mo-run/decoded/running-left.png`
- Modify: `xiao-mo-run/imagegen-jobs.json`

**Interfaces:**
- Consumes: canonical base, avatar reference, guides, and row prompts.
- Produces: identity and gait checkpoints.

- [ ] **Step 1: Generate and record `idle`**

Dispatch one row worker with all manifest-listed inputs. Require exactly six calm frames with breathing, blink, or small head motion; no large gesture. Copy to `decoded/idle.png` and update only that job with `status`, `source_path`, and UTC `completed_at`.

Expected: visible micro-variation, stable identity, flat chroma background.

- [ ] **Step 2: Generate and record `running-right`**

Dispatch one row worker with all listed inputs. Require exactly eight right-facing alternating gait frames without speed lines, dust, shadows, or detached effects. Copy to `decoded/running-right.png` and update that job.

Expected: readable rightward gait with stable scale and baseline.

- [ ] **Step 3: Decide the leftward strategy**

Mirror only if jewelry, tattoo placement, rings, bracelet, and hair sweep remain meaningful when sides change. Prefer independent generation for this asymmetrical design unless the approved base deliberately simplified those traits symmetrically.

Expected: one explicit mirror or generate decision.

- [ ] **Step 4: Produce and record `running-left`**

If mirroring is approved:

```bash
python3 '/Users/yangqi/.codex/vendor_imports/skills/skills/.curated/hatch-pet/scripts/derive_running_left_from_running_right.py' \
  --run-dir '/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run' \
  --confirm-appropriate-mirror \
  --decision-note 'The simplified sticker design is symmetric enough that mirroring preserves identity and meaning.'
```

Otherwise dispatch a `running-left` worker with all listed inputs, including the rightward gait reference, then copy and record the result.

Expected: eight left-facing frames with preserved temporal order.

### Task 4: Generate Reaction Rows

**Files:**
- Create: `xiao-mo-run/decoded/waving.png`
- Create: `xiao-mo-run/decoded/jumping.png`
- Create: `xiao-mo-run/decoded/failed.png`
- Modify: `xiao-mo-run/imagegen-jobs.json`

**Interfaces:**
- Consumes: canonical identity and each row's production inputs.
- Produces: greeting, celebration, and failure loops.

- [ ] **Step 1: Generate `waving`**

Use one row worker. Require exactly four hand-wave frames without wave marks or floating effects. Copy and record `decoded/waving.png`.

Expected: clear start, raised gesture, and return.

- [ ] **Step 2: Generate `jumping`**

Use one row worker. Require exactly five frames: anticipation, lift, peak, descent, settle. Copy and record `decoded/jumping.png`.

Expected: no floor shadow, dust, impact mark, or detached celebration symbol.

- [ ] **Step 3: Generate `failed`**

Use one row worker. Require exactly eight frames of a brief slump and lowered gaze. Copy and record `decoded/failed.png`.

Expected: distinct from idle; no red X, detached tear, or smoke.

### Task 5: Generate Codex Work-State Rows

**Files:**
- Create: `xiao-mo-run/decoded/waiting.png`
- Create: `xiao-mo-run/decoded/running.png`
- Create: `xiao-mo-run/decoded/review.png`
- Modify: `xiao-mo-run/imagegen-jobs.json`

**Interfaces:**
- Consumes: canonical identity and each row's production inputs.
- Produces: user-input, active-work, and inspection loops.

- [ ] **Step 1: Generate `waiting`**

Use one row worker. Require exactly six frames centered on the two-hands-on-cheeks expectant pose. Copy and record `decoded/waiting.png`.

Expected: clearly waiting for user input and distinct from idle.

- [ ] **Step 2: Generate `running`**

Use one row worker. Require exactly six focused typing or compact active-work frames. Do not depict foot-running, directional travel, readable code, or a new UI panel. Copy and record `decoded/running.png`.

Expected: active Codex work is readable at pet size.

- [ ] **Step 3: Generate `review`**

Use one row worker. Require exactly six frames using lean, eyes, head tilt, and hand position only. Copy and record `decoded/review.png`.

Expected: no magnifying glass, paper, code, punctuation, or new prop.

- [ ] **Step 4: Confirm all jobs are complete**

```bash
jq -e '.jobs | length == 10 and all(.status == "complete")' '/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run/imagegen-jobs.json'
```

Expected: jq prints `true`.

### Task 6: Build and Validate the Atlas

**Files:**
- Create: `xiao-mo-run/frames/frames-manifest.json`
- Create: `xiao-mo-run/qa/review.json`
- Create: `xiao-mo-run/final/spritesheet.png`
- Create: `xiao-mo-run/final/spritesheet.webp`
- Create: `xiao-mo-run/final/validation.json`
- Create: `xiao-mo-run/qa/contact-sheet.png`
- Create: `xiao-mo-run/qa/previews/*.gif`

**Interfaces:**
- Consumes: all nine completed row strips.
- Produces: installable atlas and QA evidence.

- [ ] **Step 1: Extract transparent frames**

```bash
RUN_DIR='/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run'
SKILL_DIR='/Users/yangqi/.codex/vendor_imports/skills/skills/.curated/hatch-pet'
python3 "$SKILL_DIR/scripts/extract_strip_frames.py" \
  --decoded-dir "$RUN_DIR/decoded" \
  --output-dir "$RUN_DIR/frames" \
  --states all \
  --method auto
```

Expected: cells and `frames-manifest.json` are created.

- [ ] **Step 2: Inspect geometry and components**

```bash
python3 "$SKILL_DIR/scripts/inspect_frames.py" \
  --frames-root "$RUN_DIR/frames" \
  --json-out "$RUN_DIR/qa/review.json" \
  --require-components
jq -e '(.errors | length) == 0' "$RUN_DIR/qa/review.json"
```

Expected: jq prints `true`; warnings remain subject to visual review.

- [ ] **Step 3: Compose and validate**

```bash
mkdir -p "$RUN_DIR/final" "$RUN_DIR/qa"
python3 "$SKILL_DIR/scripts/compose_atlas.py" \
  --frames-root "$RUN_DIR/frames" \
  --output "$RUN_DIR/final/spritesheet.png" \
  --webp-output "$RUN_DIR/final/spritesheet.webp"
python3 "$SKILL_DIR/scripts/validate_atlas.py" \
  "$RUN_DIR/final/spritesheet.webp" \
  --json-out "$RUN_DIR/final/validation.json"
jq -e '.ok == true' "$RUN_DIR/final/validation.json"
```

Expected: atlas is `1536x1872`; unused cells are transparent.

- [ ] **Step 4: Produce visual QA media**

```bash
python3 "$SKILL_DIR/scripts/make_contact_sheet.py" \
  "$RUN_DIR/final/spritesheet.webp" \
  --output "$RUN_DIR/qa/contact-sheet.png"
python3 "$SKILL_DIR/scripts/render_animation_previews.py" \
  --frames-root "$RUN_DIR/frames" \
  --output-dir "$RUN_DIR/qa/previews"
test "$(find "$RUN_DIR/qa/previews" -type f -name '*.gif' | wc -l | tr -d ' ')" = '9'
```

Expected: one contact sheet and nine GIFs exist.

- [ ] **Step 5: Run final visual QA**

Dispatch one lightweight visual worker with the contact sheet, GIFs, `review.json`, and `validation.json`, using the hatch-pet final-QA contract.

Expected: `visual_qa=pass`, `repair_rows=none`, `repair_notes=none`.

### Task 7: Repair the Smallest Failing Scope

**Files:**
- Modify: only failing `xiao-mo-run/decoded/*.png` rows and downstream QA files.

**Interfaces:**
- Consumes: automated errors, warnings, and row-specific visual-QA notes.
- Produces: a clean Task 6 result without replacing approved rows.

- [ ] **Step 1: Classify the failure**

Map chroma residue, clipping, identity drift, semantic mismatch, wrong facing, inert idle, reversed gait, and source instability to one row. Map size popping or baseline jumps absent from the source strip to extraction.

Expected: one row id or extraction method is selected; full regeneration occurs only if the canonical identity is wrong.

- [ ] **Step 2: Correct extraction-only instability**

```bash
RUN_DIR='/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run'
SKILL_DIR='/Users/yangqi/.codex/vendor_imports/skills/skills/.curated/hatch-pet'
rm -rf "$RUN_DIR/frames"
python3 "$SKILL_DIR/scripts/extract_strip_frames.py" \
  --decoded-dir "$RUN_DIR/decoded" \
  --output-dir "$RUN_DIR/frames" \
  --states all \
  --method stable-slots
python3 "$SKILL_DIR/scripts/inspect_frames.py" \
  --frames-root "$RUN_DIR/frames" \
  --json-out "$RUN_DIR/qa/review.json" \
  --require-components \
  --allow-stable-slots
```

Expected: use only when source strips already have stable scale and placement; rerun Task 6 Steps 3–5.

- [ ] **Step 3: Regenerate one failing row**

Dispatch one worker with the original prompt, retry prompt, canonical base, avatar reference, guide, and exact failure note. Replace only that row, update its manifest metadata, then rerun Task 6.

Expected: the repaired row passes without changing approved rows.

- [ ] **Step 4: Enforce the final gate**

```bash
jq -e '(.errors | length) == 0' '/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run/qa/review.json'
jq -e '.ok == true' '/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run/final/validation.json'
```

Expected: both checks pass and visual QA is `pass`.

### Task 8: Package, Install, and Record

**Files:**
- Create: `${CODEX_HOME:-$HOME/.codex}/pets/xiao-mo/pet.json` or a versioned sibling.
- Create: `${CODEX_HOME:-$HOME/.codex}/pets/xiao-mo/spritesheet.webp` or a versioned sibling.
- Create: `xiao-mo-run/qa/run-summary.json`
- Modify: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/README.md`

**Interfaces:**
- Consumes: QA-approved atlas and pet metadata.
- Produces: installed Codex pet and durable artifact index.

- [ ] **Step 1: Select a non-destructive directory**

```bash
RUN_DIR='/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-13-avatar-pet/xiao-mo-run'
PETS_ROOT="${CODEX_HOME:-$HOME/.codex}/pets"
PET_DIR="$PETS_ROOT/xiao-mo"
if test -e "$PET_DIR"; then
  VERSION=2
  while test -e "$PETS_ROOT/xiao-mo-v$VERSION"; do VERSION=$((VERSION + 1)); done
  PET_DIR="$PETS_ROOT/xiao-mo-v$VERSION"
fi
mkdir -p "$PET_DIR"
```

Expected: no existing pet is overwritten.

- [ ] **Step 2: Copy the atlas and create `pet.json`**

```bash
PET_ID=$(basename "$PET_DIR")
DISPLAY_NAME=$(jq -r '.display_name' "$RUN_DIR/pet_request.json")
DESCRIPTION=$(jq -r '.description' "$RUN_DIR/pet_request.json")
cp "$RUN_DIR/final/spritesheet.webp" "$PET_DIR/spritesheet.webp"
jq -n \
  --arg id "$PET_ID" \
  --arg displayName "$DISPLAY_NAME" \
  --arg description "$DESCRIPTION" \
  '{id:$id,displayName:$displayName,description:$description,spritesheetPath:"spritesheet.webp"}' \
  > "$PET_DIR/pet.json"
```

Expected: package contains `pet.json` and `spritesheet.webp`.

- [ ] **Step 3: Verify bytes and write the summary**

```bash
jq -e '.id != "" and .displayName == "小墨" and .spritesheetPath == "spritesheet.webp"' "$PET_DIR/pet.json"
cmp "$RUN_DIR/final/spritesheet.webp" "$PET_DIR/spritesheet.webp"
jq -n \
  --arg run_dir "$RUN_DIR" \
  --arg spritesheet "$RUN_DIR/final/spritesheet.webp" \
  --arg validation "$RUN_DIR/final/validation.json" \
  --arg contact_sheet "$RUN_DIR/qa/contact-sheet.png" \
  --arg review "$RUN_DIR/qa/review.json" \
  --arg package "$PET_DIR" \
  '{ok:true,run_dir:$run_dir,spritesheet:$spritesheet,validation:$validation,contact_sheet:$contact_sheet,review:$review,package:$package}' \
  > "$RUN_DIR/qa/run-summary.json"
jq -e '.ok == true' "$RUN_DIR/qa/run-summary.json"
```

Expected: jq prints `true`; `cmp` exits `0`.

- [ ] **Step 4: Refresh Codex and select 小墨**

Open Codex Settings → Pets, refresh local manifests, select `小墨`, and wake it only after all prior gates pass.

Expected: 小墨 appears in the floating overlay and reacts to all nine states.

- [ ] **Step 5: Update the conversation README**

Record the run summary, contact sheet, final atlas, validation report, preview directory, installed package, and whether a versioned directory was used.

Expected: README matches `qa/run-summary.json` and contains no stale status.
