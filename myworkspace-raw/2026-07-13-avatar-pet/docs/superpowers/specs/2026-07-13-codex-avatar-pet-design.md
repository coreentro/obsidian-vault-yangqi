# Codex Avatar Pet Design

## Summary

Create a Codex-compatible local custom pet named “小墨” (`xiao-mo`) from the user's avatar. The pet is a miniature human avatar rendered in a hand-drawn sticker style, preserving the reference's tousled black hair, playful wink, silver accessories, tattoo linework, and warm personality.

The deliverable is a native Codex pet package installed without overwriting any existing pet or settings.

## Goals

- Produce a recognizable miniature-human companion based on the supplied avatar.
- Support all nine Codex pet states with readable, distinct animation loops.
- Incorporate personal actions: cheek-resting wink, typing code, and completion celebration.
- Pass visual, geometry, transparency, and animation validation.
- Install the package locally so it appears in Codex pet settings.

## Non-goals

- Building a separate macOS application.
- Reproducing the source photograph as a pasted or photorealistic face.
- Adding sound, speech, network access, or a hosted installation service.
- Modifying or deleting existing Codex pets or user settings.

## Package Architecture

The local package will be placed under `${CODEX_HOME:-$HOME/.codex}/pets/xiao-mo/` and contain:

```text
xiao-mo/
├── pet.json
└── spritesheet.webp
```

The manifest will use this shape:

```json
{
  "id": "xiao-mo",
  "displayName": "小墨",
  "description": "A playful miniature companion with tousled black hair and warm, mischievous energy.",
  "spritesheetPath": "spritesheet.webp"
}
```

The sprite atlas must be `1536x1872`, arranged as 8 columns by 9 rows, with `192x208` cells and fully transparent unused cells.

## Visual Identity

- Form: compact full-body miniature human, approximately 1:1.5 head-to-body proportion.
- Style: hand-drawn sticker illustration with a bold, clean silhouette.
- Hair: voluminous tousled black hair as the primary identifying feature.
- Face: playful wink and warm, mischievous expression; illustrated rather than photographic.
- Accessories: simplified silver ear jewelry, rings, or bracelet details that remain readable at pet size.
- Markings: simplified black tattoo linework on the visible arm; no literal high-detail copying.
- Palette: charcoal black, warm skin and amber accents, muted silver, and restrained cream highlights.
- Clothing: one stable dark patterned outfit across all states.
- Exclusions: text, code glyphs, visible grids, scenery, cast shadows, detached effects, and details too fine to survive at 80–224 px display size.

## State and Action Mapping

| Codex state | Designed action |
| --- | --- |
| `idle` | Quiet breathing, blink, subtle head movement, occasional light cheek-resting pose. |
| `running-right` | Compact right-facing run used during directional dragging. |
| `running-left` | Compact left-facing run used during directional dragging. |
| `waving` | Friendly hand wave with a playful expression. |
| `jumping` | Upward celebratory jump using body position only. |
| `failed` | Brief slump and lowered gaze; disappointed but not distressed. |
| `waiting` | Two hands supporting the cheeks in an expectant pose. |
| `running` | Focused seated or standing typing motion that reads as active Codex work. |
| `review` | Forward lean, narrowed eyes, and attentive head movement while checking results. |

The personal completion celebration is expressed through `jumping` and `waving`. The wink and cheek-resting behavior are distributed between `idle` and `waiting`. Typing is assigned to the Codex active-work state, `running`.

## Production Flow

1. Prepare a run folder using the avatar reference, pet name, description, sticker-style notes, and stable character constraints.
2. Generate and approve a canonical full-body base image for 小墨.
3. Generate `idle` and `running-right` first to confirm identity stability and movement readability.
4. Mirror `running-right` into `running-left` only if asymmetrical jewelry and tattoo placement remain semantically acceptable; otherwise generate `running-left` independently.
5. Generate the remaining state strips with the canonical base and the correct layout guide attached.
6. Extract frames, remove the chroma-key background, normalize transparency, and inspect connected components.
7. Compose PNG and WebP atlases, validate the final geometry, and render contact-sheet and animation previews.
8. Create `pet.json`, preserve the complete validated run in the conversation directory, and install a copy under the Codex pets directory.
9. Refresh the Codex custom-pet list and select 小墨 only after successful installation.

## Error Handling

- If one row fails identity or motion QA, regenerate or repair only that row.
- If identity drift affects several rows, return to the canonical base instead of normalizing inconsistent artwork downstream.
- If chroma-key removal leaves halos or disconnected pixels, rerun extraction with stricter cleanup and validate again.
- If frame extraction causes scale popping or baseline jumps, use stable-slot extraction and rebuild all QA artifacts.
- If the target installation directory already exists, preserve it and install to a meaningfully versioned sibling directory rather than overwrite it.
- If final validation fails, do not install or present the pet as complete.

## Validation and Acceptance Criteria

The pet is complete only when all of these conditions hold:

- The final atlas is exactly `1536x1872` with the fixed 8-by-9 layout.
- Every populated cell stays within its `192x208` boundary.
- Unused cells and background pixels are fully transparent without hidden RGB residue.
- All nine states are present, distinct, correctly directed, and semantically readable.
- Face, hairstyle, clothing, palette, jewelry, tattoos, body proportions, and line style remain consistent.
- Preview loops show no unintended scale popping, baseline jumping, clipping, duplicated frames, or cross-cell artifacts.
- `pet.json` references the packaged WebP and the package loads in Codex pet settings.
- Existing pets and user settings remain untouched.

## Deliverables

- `pet.json`
- `spritesheet.webp`
- lossless `spritesheet.png`
- atlas validation report
- contact sheet
- per-state animation previews
- canonical base image and generated row sources retained in the conversation directory

