# Xiao Mo v2 Upgrade

- Created: 2026-07-14
- Topic: Upgrade Xiao Mo to the latest Codex pet format
- Purpose: Preserve the existing pet identity and standard animations, add 16 looking directions, validate the 8x11 atlas, and package sprite version 2.

## Result

- Upgraded pet: `/Users/yangqi/.codex/pets/xiao-mo`
- Sprite contract: 8 columns × 11 rows, 192 × 208 cells, `spriteVersionNumber: 2`
- Added directions: 16 clockwise poses from 000° through 337.5°
- QA outcome: deterministic validation, three-reviewer blind direction validation, and independent final visual QA passed
- Audit artifacts: `xiao-mo-v2-run/qa/`
