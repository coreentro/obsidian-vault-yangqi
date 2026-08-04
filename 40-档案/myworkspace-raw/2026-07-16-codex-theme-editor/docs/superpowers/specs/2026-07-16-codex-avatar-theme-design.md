# Codex Avatar Theme Design

- Date: 2026-07-16
- Source image: `/Users/yangqi/Desktop/微信图片_2026-07-16_152228_462.jpg`
- Delivery engine: extracted `Codex Dream Skin Studio` from the user-provided ZIP

## Goal

Apply a durable macOS Codex theme based on the user's warm, intimate avatar photo while preserving Codex's native UI and providing a verified one-click restore path.

## Visual direction

Use the photo as the single image asset for the home banner and restrained task-page background. Build the palette from the image's dark surroundings and warm candlelight:

- background `#120b09`
- panel `#241511`
- panelAlt `#3b2119`
- accent `#ff9a52`
- accentAlt `#ffd08a`
- secondary `#d7643e`
- highlight `#6c2e24`
- text `#fff4e8`
- muted `#caa998`
- line `rgba(255,154,82,.28)`

Theme copy:

- name: `橙色凝视`
- tagline: `在温暖的光里，把想法写成可运行的代码。`
- quote: `STAY CURIOUS · KEEP BUILDING`

## Architecture and safety

Use the ZIP's official install/customize/start/verify scripts. Do not modify the official Codex `.app`, `app.asar`, code signature, or system security settings. The engine injects through loopback CDP and keeps decoration non-interactive. The user's explicit approval authorizes one Codex restart during deployment.

## Acceptance criteria

1. Engine static tests pass.
2. Installer completes and creates the user-level engine plus four desktop launchers.
3. Theme config points to the converted avatar image and exact palette/copy above.
4. `doctor-macos.sh --require-live` passes.
5. `verify-dream-skin-macos.sh --reload --screenshot ...` returns `pass: true`.
6. A task-route screenshot is captured and the native sidebar, composer, content, menus, and project controls remain usable.
7. Official Codex signature verification passes and no official app payload is modified.
8. Restore entry remains available.
