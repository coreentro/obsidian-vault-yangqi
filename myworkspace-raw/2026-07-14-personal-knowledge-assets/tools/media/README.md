# Media Tools

This directory contains an isolated, version-locked environment for subtitle extraction and multilingual transcription.

## Preservation boundary

- Prefer platform-provided subtitles before generating a transcript.
- Do not bypass login, payment, access control, or DRM.
- Keep platform subtitles, OCR, and machine transcripts as separate immutable raw artifacts.
- A cleaned transcript may only improve punctuation, paragraphs, speaker labels, and explicit recognition errors. It may not remove filler words, repetition, or opinions.
- Missing media or transcript segments must remain explicitly marked as missing; models may not invent them.

## Storage boundary

- Processing cache is capped at 10 GB.
- Upload and checksum verification must finish before generated cache files are eligible for cleanup.
- Original user files and accepted evidence packages are never cleanup targets.

## Locked tools

- `yt-dlp==2026.7.4`
- `openai-whisper==20250625`
- Homebrew `ffmpeg==8.1.2`
