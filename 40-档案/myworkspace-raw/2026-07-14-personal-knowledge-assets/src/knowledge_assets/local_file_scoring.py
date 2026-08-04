from __future__ import annotations

from pathlib import PurePosixPath
from typing import Any


_GENERATED_PARTS = {
    ".git",
    ".idea",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "bower_components",
    "build",
    "dist",
    "node_modules",
    "target",
    "vendor",
}
_METADATA_NAMES = {".DS_Store", ".localized", "Thumbs.db", "desktop.ini"}
_SENSITIVE_NAMES = {".env", ".npmrc", ".pypirc", ".netrc", "credentials", "credentials.json"}
_SENSITIVE_SUFFIXES = {".key", ".pem", ".p12", ".pfx"}
_DOCUMENT_SUFFIXES = {
    ".csv", ".doc", ".docx", ".epub", ".html", ".md", ".mobi", ".odp",
    ".ods", ".odt", ".pdf", ".ppt", ".pptx", ".rtf", ".tex", ".txt",
    ".xls", ".xlsx",
}
_MEDIA_SUFFIXES = {
    ".aac", ".avi", ".flac", ".gif", ".heic", ".jpeg", ".jpg", ".m4a",
    ".mkv", ".mov", ".mp3", ".mp4", ".ogg", ".png", ".wav", ".webm",
    ".webp",
}


def classify_local_file(*, path: str, mime_type: str, byte_length: int) -> dict[str, Any]:
    """Classify frozen inventory metadata without reading, moving, or deleting a file."""
    file_path = PurePosixPath(path)
    name = file_path.name
    suffix = file_path.suffix.lower()
    parts = set(file_path.parts)
    flags: list[str] = []
    signals: list[str] = []

    if name in _SENSITIVE_NAMES or suffix in _SENSITIVE_SUFFIXES or any(
        token in name.lower() for token in ("secret", "token", "password", "credential")
    ):
        flags.append("sensitive")
        return {
            "recommendation": "review",
            "reason": "文件名疑似包含凭据或敏感信息，禁止自动采集正文。",
            "flags": flags,
            "signals": signals,
            "sensitive": True,
            "auto_capture_allowed": False,
            "record_policy": "retain-audit-record",
        }

    if name in _METADATA_NAMES or name.startswith(".~") or byte_length == 0:
        flags.append("metadata-or-empty")
        recommendation = "excluded"
        reason = "明显的系统元数据、临时文件或空文件，不作为知识正文采集。"
    elif parts.intersection(_GENERATED_PARTS):
        flags.append("generated-or-dependency")
        recommendation = "excluded"
        reason = "依赖、构建或工具生成文件；只保留审计记录。"
    elif suffix in _DOCUMENT_SUFFIXES or mime_type.startswith("text/"):
        signals.append("document")
        recommendation = "review"
        reason = "可能包含可复用文本知识，需结合路径、内容和重复关系复核。"
    elif suffix in _MEDIA_SUFFIXES or mime_type.startswith(("image/", "audio/", "video/")):
        signals.append("media")
        recommendation = "review"
        reason = "可能是个人保存的图像、音频或视频资料，需人工确认价值与隐私。"
    else:
        flags.append("unknown-binary-or-format")
        recommendation = "review"
        reason = "仅凭冻结元数据无法安全判断价值，保留待复核。"

    return {
        "recommendation": recommendation,
        "reason": reason,
        "flags": flags,
        "signals": signals,
        "sensitive": False,
        "auto_capture_allowed": False,
        "record_policy": "retain-audit-record",
    }
