# Male Avatar Variants Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate three original square black-and-white male avatar PNGs representing Scholar, Fighter, and Thinker-Actor personalities.

**Architecture:** Use the supplied `logo.png` only as a style and composition reference. Generate each personality as a separate image so its prompt can control expression, silhouette, hair, collar geometry, and visual weight independently; then inspect each output and save the accepted images in the conversation directory.

**Tech Stack:** Built-in image generation tool, local image inspection, PNG files.

## Global Constraints

- Young East Asian man in a head-and-shoulders three-quarter profile.
- Pure black and white, with no gray or color.
- Bold ink shapes, crisp negative space, sharp hair highlights, and a retro manga/logo aesthetic.
- Square icon composition legible at small sizes.
- Original character; no direct gender swap or close copy of the reference.
- No words, letters, watermark, gradients, photorealism, cluttered background, exaggerated aggression, or militaristic symbols.
- Save every accepted PNG in `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-17-hermesagent-official-image/`.

---

### Task 1: Generate Scholar Avatar

**Files:**
- Create: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-17-hermesagent-official-image/male-avatar-scholar.png`

**Interfaces:**
- Consumes: `/Users/yangqi/Desktop/logo.png` as a style/composition reference.
- Produces: One square PNG representing calm, historically aware analytical intelligence.

- [ ] **Step 1:** Generate an original male avatar with neat medium-short black hair, a clean high collar, a calm observant expression, restrained warmth, finer facial lines, and relatively open white negative space.
- [ ] **Step 2:** Inspect the generated image for monochrome purity, icon legibility, originality, and accidental text.
- [ ] **Step 3:** Copy the accepted generated PNG to the exact output path.

### Task 2: Generate Fighter Avatar

**Files:**
- Create: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-17-hermesagent-official-image/male-avatar-fighter.png`

**Interfaces:**
- Consumes: `/Users/yangqi/Desktop/logo.png` as a style/composition reference.
- Produces: One square PNG representing disciplined resolve and practical courage.

- [ ] **Step 1:** Generate an original male avatar with a firmer jaw, sharper gaze, subtly windswept short hair, structured high-collar jacket, angular geometry, bold black masses, and dynamic diagonal highlights.
- [ ] **Step 2:** Inspect the generated image for disciplined energy without hostility, monochrome purity, icon legibility, originality, and accidental text or symbols.
- [ ] **Step 3:** Copy the accepted generated PNG to the exact output path.

### Task 3: Generate Thinker-Actor Avatar

**Files:**
- Create: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-17-hermesagent-official-image/male-avatar-thinker-actor.png`

**Interfaces:**
- Consumes: `/Users/yangqi/Desktop/logo.png` as a style/composition reference.
- Produces: One square PNG balancing critical reason with practical action.

- [ ] **Step 1:** Generate an original male avatar with short slightly tousled hair, a calm determined expression, a focused gaze beyond the frame, and a small abstract collar emblem made only of intersecting geometric shapes suggesting contradiction and unity.
- [ ] **Step 2:** Inspect the generated image for a clear balance between openness and force, monochrome purity, icon legibility, originality, and accidental text.
- [ ] **Step 3:** Copy the accepted generated PNG to the exact output path.

### Task 4: Final Verification

**Files:**
- Verify: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-17-hermesagent-official-image/male-avatar-scholar.png`
- Verify: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-17-hermesagent-official-image/male-avatar-fighter.png`
- Verify: `/Users/yangqi/Documents/Codex/MyWorkspace/2026-07-17-hermesagent-official-image/male-avatar-thinker-actor.png`

**Interfaces:**
- Consumes: The three generated PNG files.
- Produces: A verified three-image avatar set ready for user comparison.

- [ ] **Step 1:** Confirm all three files exist and are valid square PNG images.
- [ ] **Step 2:** View all three images and confirm their personalities are visually distinct while sharing one coherent style.
- [ ] **Step 3:** Report the three absolute output paths and the final prompts used.
