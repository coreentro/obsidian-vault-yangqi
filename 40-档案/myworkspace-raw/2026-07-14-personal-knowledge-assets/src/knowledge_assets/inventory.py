from __future__ import annotations

import hashlib
import json
import mimetypes
import os
from dataclasses import dataclass
from pathlib import Path


EXCLUDED_DIRECTORY_NAMES = {
    ".git",
    ".Trash",
    "Caches",
    "Cache",
    "cache",
    "node_modules",
    "__pycache__",
}
EXCLUDED_FILE_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}


class InventoryConflictError(RuntimeError):
    """Raised when an existing frozen inventory would be replaced."""


@dataclass(frozen=True)
class FileCandidate:
    candidate_id: str
    device_id: str
    path: Path
    byte_length: int
    modified_at_ns: int
    sha256: str
    mime_type: str
    preservation_signals: tuple[str, ...]


def scan_personal_roots(
    roots: list[Path],
    *,
    device_id: str,
    exclude_roots: list[Path] | None = None,
) -> list[FileCandidate]:
    candidates: list[FileCandidate] = []
    excluded_paths = [Path(path).expanduser().resolve() for path in (exclude_roots or [])]
    for root_value in roots:
        root = Path(root_value).expanduser().resolve()
        if not root.exists() or any(_is_within(root, excluded) for excluded in excluded_paths):
            continue
        for directory, child_directories, file_names in os.walk(root, followlinks=False):
            directory_path = Path(directory)
            child_directories[:] = [
                name
                for name in child_directories
                if name not in EXCLUDED_DIRECTORY_NAMES
                and not any(
                    _is_within((directory_path / name).resolve(), excluded)
                    for excluded in excluded_paths
                )
            ]
            for file_name in file_names:
                if file_name in EXCLUDED_FILE_NAMES:
                    continue
                path = directory_path / file_name
                if path.is_symlink() or not path.is_file():
                    continue
                stat = path.stat()
                digest = _sha256(path)
                identity = hashlib.sha256(
                    f"{device_id}\0{path}\0{stat.st_size}\0{stat.st_mtime_ns}".encode("utf-8")
                ).hexdigest()
                candidates.append(
                    FileCandidate(
                        candidate_id=f"file-{identity[:24]}",
                        device_id=device_id,
                        path=path,
                        byte_length=stat.st_size,
                        modified_at_ns=stat.st_mtime_ns,
                        sha256=digest,
                        mime_type=mimetypes.guess_type(path.name)[0] or "application/octet-stream",
                        preservation_signals=_signals_for_path(path),
                    )
                )
    return sorted(candidates, key=lambda candidate: candidate.path.as_posix())


def write_inventory_manifest(
    output_path: Path,
    *,
    device_id: str,
    baseline_at: str,
    roots: list[Path],
    candidates: list[FileCandidate],
    exclude_roots: list[Path] | None = None,
) -> Path:
    payload = {
        "schema_version": 1,
        "device_id": device_id,
        "baseline_at": baseline_at,
        "roots": [str(Path(root).expanduser().resolve()) for root in roots],
        "excluded_roots": [
            str(Path(root).expanduser().resolve()) for root in (exclude_roots or [])
        ],
        "scanned_total": len(candidates),
        "candidates": [
            {
                "candidate_id": candidate.candidate_id,
                "path": str(candidate.path),
                "byte_length": candidate.byte_length,
                "modified_at_ns": candidate.modified_at_ns,
                "sha256": candidate.sha256,
                "mime_type": candidate.mime_type,
                "preservation_signals": list(candidate.preservation_signals),
            }
            for candidate in candidates
        ],
    }
    content = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise InventoryConflictError(f"Refusing to replace frozen inventory: {path}")
        return path
    with path.open("xb") as handle:
        handle.write(content)
    return path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _signals_for_path(path: Path) -> tuple[str, ...]:
    names = {part.lower() for part in path.parts}
    signals = []
    if "downloads" in names or "下载" in names:
        signals.append("download")
    if "screenshots" in names or "screenshot" in path.name.lower() or "截图" in path.name:
        signals.append("screenshot")
    return tuple(signals)


def _is_within(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents
