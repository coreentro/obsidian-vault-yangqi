# MyWorkspace - Obsidian Knowledge Notes

**Created:** 2026-07-29  
**Purpose:** Comprehensive knowledge base of all projects, experiments, and artifacts in MyWorkspace. Designed to be imported directly into Obsidian as a beautiful, linked note vault.

**Tags:** #myworkspace #obsidian #knowledge-base #hermes #grok #claude #experiments #feishu #personal-knowledge

---

## Table of Contents

- [Naming Conventions & AGENTS.md](#naming-conventions--agentsmd)
- [Recent Projects (2026-07-28)](#recent-projects-2026-07-28)
- [Hermes Core & Infrastructure](#hermes-core--infrastructure)
- [Model Experiments & Diagnostics](#model-experiments--diagnostics)
- [Knowledge Systems & Feishu Integration](#knowledge-systems--feishu-integration)
- [Avatar & UI Experiments](#avatar--ui-experiments)
- [Other Notable Experiments](#other-notable-experiments)
- [File Structure Overview](#file-structure-overview)

---

## Naming Conventions & AGENTS.md {#naming-conventions--agentsmd}

**File:** `AGENTS.md` (3.2KB)

This file establishes strict naming conventions for all future conversation directories and files:

- **Directories:** `YYYY-MM-DD-topic-name` (kebab-case)
- **Files:** Descriptive names with dates when relevant
- **Standard files:** Keep `README.md` unchanged
- **Rule:** Never rename existing content unless explicitly asked

**Key principles:**
- Concise, descriptive English names
- ISO 8601 dates in filenames
- Conversation directories created automatically in `MyWorkspace` root

---

## Recent Projects (2026-07-28) {#recent-projects-2026-07-28}

### 2026-07-28-hermes-handoff/ {#2026-07-28-hermes-handoff}

**Files:**
- `README.md` (1.8KB)
- `takeover-notes.md` (6.5KB)
- `official-refresh-verification-2026-07-28.md` (1.4KB)
- `grokreg-e2e` (17.9MB binary)
- Various Python scripts:
  - `official-browser-confirm.py`
  - `inspect-grok-onboarding.py`
  - `build-shadowrocket-proxy.py`
  - `official-device-confirm.py`
- Images: `grok-browser-oauth.png`, `grok-account-inspect.png`
- Subdirectory: `verified-cpa/` (JSON config)

**Summary:** Recent handoff and verification work for Grok browser authentication and device confirmations. Includes scripts for official refresh verification and proxy setup.

### 2026-07-28-hermes-interface-troubleshooting/ {#2026-07-28-hermes-interface-troubleshooting}

**Files:**
- `README.md` (1.1KB)
- `hermes-window-after-restart.png` (2.5MB)
- `hermes-after-restart.png` (1.7MB)

**Summary:** Interface troubleshooting after restart, with screenshots of window behavior.

### 2026-07-28-any-router-403/ {#2026-07-28-any-router-403}

**Files:**
- `README.md` (198B)

**Summary:** Any router 403 error handling.

---

## Hermes Core & Infrastructure {#hermes-core--infrastructure}

### 2026-07-26-hermes-permissions/ {#2026-07-26-hermes-permissions}

**Files:**
- `README.md` (2.0KB)
- `update-persistence-implementation-plan.md` (43.3KB)
- `update-persistence-audit.md` (23.7KB)
- `hermes-stable-signing.patch` (40.1KB)
- Subdirectories:
  - `hermes-app-backup/`
  - `hermes-stable-signing/` (contains `hermes_cli/`, `scripts/`, `tests/`, `apps/desktop/src/`, `ui-tui/`, `website/docs/` — appears to be the full Hermes source tree)

**Summary:** Deep work on Hermes persistence, signing, and desktop application infrastructure. Includes full source tree for `hermes-ink` and desktop UI components.

**Note:** This directory contains the core Hermes codebase with extensive substructure (skills, UI components, Docusaurus website).

---

## Model Experiments & Diagnostics {#model-experiments--diagnostics}

### Claude & Gemini Experiments {#claude--gemini-experiments}

- `2026-07-21-claude-f-zscc/`: Claude configuration, backups, STATUS.md
- `2026-07-16-gemini-subscription/`: Gemini CLI source, experiment JSONs, Google OAuth
- `2026-07-16-claude-keep-grok-only/`, `2026-07-16-hermes-claude-diagnosis/`: Model switching, diagnosis logs, change logs

**Summary:** Extensive experimentation with Claude, Gemini, and Grok model providers, including configuration files, OAuth setups, and provider switching scripts.

---

## Knowledge Systems & Feishu Integration {#knowledge-systems--feishu-integration}

### 2026-07-13-feishu-knowledge-base-plan/ {#2026-07-13-feishu-knowledge-base-plan}

**Files:**
- `README.md` (6.1KB)
- `feishu-knowledge-base-blueprint.md` (11.5KB)
- `xiaohongshu-ai-learning-683a935f/` (large subdirectory with 40+ files, including `xai-official-refresh-2026-07-28.json`, Python scripts for batch processing, evidence ZIPs)
- XML files for chapters (full-chapter-*-part-*.xml)

**Summary:** Comprehensive Feishu knowledge base plan, including xiaohongshu AI learning notes, batch content extraction, and chapter XMLs (likely for a book or tutorial on Linux/Feishu usage).

### 2026-07-14-personal-knowledge-assets/ {#2026-07-14-personal-knowledge-assets}

**Files:**
- `README.md` (5.4KB)
- `implementation-log.md` (25.3KB)
- `knowledge-asset-system-design.md` (3.1KB)
- Subdirectories: `data/`, `src/`, `tests/`, `tools/`, `tmp/`, `scripts/`

**Summary:** Personal knowledge asset system design and implementation. Core project for organizing personal knowledge.

---

## Avatar & UI Experiments {#avatar--ui-experiments}

### 2026-07-15-agi-explorer-avatar/ {#2026-07-15-agi-explorer-avatar}

**Files:**
- `README.md` (1.2KB)
- `avatar-generation-plan.md` (531B)
- Multiple avatar images (PNG/JPG up to 2.5MB)
- `avatar-design.md` (1.2KB)

**Summary:** Generation and design of AGI Explorer avatars with multiple versions and variants.

### 2026-07-13-avatar-pet/ {#2026-07-13-avatar-pet}

**Files:**
- `README.md` (1.4KB)
- `avatar-pet.png` (2.0MB)
- Subdirectory `docs/`

**Summary:** Avatar pet project with reference images.

---

## Other Notable Experiments {#other-notable-experiments}

- **2026-07-26-slow-internet-diagnosis/**: Storage analysis, cleanup scripts
- **2026-07-24-linux-do-feishu-document/**: Extensive XML chapter files (likely book content)
- **2026-07-16-codex-theme-editor/**: Theme customization logs and outputs
- **2026-07-15-browser-access-fix/**, **2026-07-15-fix-browser-ssl-access/**: Browser access and SSL troubleshooting
- **2026-07-16-ip-geolocation-difference/**, **2026-07-16-model-vs-agent-relationship/**: Model relationship analysis

**Summary:** Scattered experiments around browser access, model relationships, storage management, and technical troubleshooting.

---

## File Structure Overview {#file-structure-overview}

```
MyWorkspace/
├── AGENTS.md                          # Naming conventions
├── 2026-07-28-hermes-handoff/        # Recent Grok verification
├── 2026-07-28-hermes-interface-troubleshooting/
├── 2026-07-26-hermes-permissions/    # Core Hermes codebase
├── 2026-07-13-feishu-knowledge-base-plan/
├── 2026-07-14-personal-knowledge-assets/
├── 2026-07-15-agi-explorer-avatar/
├── 2026-07-24-linux-do-feishu-document/  # Book/XML content
├── 2026-07-16-*/                     # Model experiments
└── *.md files (READMEs, logs, plans)
```

**Total estimated size:** Large (hundreds of MB across binaries, images, and source trees)

---

## Next Steps for Obsidian Import

1. Copy this entire note into a new Obsidian vault
2. Use `Obsidian Import` → Markdown
3. Create a new folder `MyWorkspace` and place subdirectories as links
4. For large subdirs (e.g., `2026-07-26-hermes-permissions/hermes-stable-signing/`), create separate notes or use `[[Links]]`
5. Add backlinks to this main note

**Recommended Obsidian Settings:**
- Enable Dataview plugin for dynamic lists
- Use Templates for new conversation directories
- Set up Daily Notes

**Would you like me to:**
- Create individual sub-notes for specific projects?
- Generate a more detailed outline for any section?
- Create a version optimized for Dataview queries?
- Export specific README contents into structured sections?

---

*This note was generated automatically from MyWorkspace analysis. Update it as new conversations are added.*