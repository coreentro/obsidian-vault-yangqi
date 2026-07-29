from __future__ import annotations

import hashlib
import json
import mimetypes
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


class EvidenceConflictError(RuntimeError):
    """Raised when an immutable evidence path would be changed."""


class LosslessCleaningError(ValueError):
    """Raised when a cleaned text omits source characters."""


def validate_lossless_cleaning(
    raw_text: str,
    cleaned_text: str,
    *,
    corrections: tuple[tuple[str, str], ...] = (),
) -> None:
    corrected_raw = raw_text
    for original, replacement in corrections:
        corrected_raw = corrected_raw.replace(original, replacement)
    source_characters = _semantic_characters(corrected_raw)
    cleaned_characters = _semantic_characters(cleaned_text)
    position = 0
    for character in cleaned_characters:
        if position < len(source_characters) and character == source_characters[position]:
            position += 1
    if position != len(source_characters):
        missing = source_characters[position : position + 20]
        raise LosslessCleaningError(f"Cleaned text omits source content near: {missing!r}")


def _semantic_characters(text: str) -> str:
    normalized = unicodedata.normalize("NFKC", text)
    return "".join(character for character in normalized if unicodedata.category(character)[0] in {"L", "N"})


class EvidencePackage:
    def __init__(self, root: Path, *, asset_id: str, source_id: str) -> None:
        self.root = Path(root)
        self.asset_id = asset_id
        self.source_id = source_id
        self.root.mkdir(parents=True, exist_ok=True)
        self._derived: dict[str, dict[str, str]] = {}
        manifest_path = self.root / "manifest.json"
        if manifest_path.exists():
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
            if existing["asset_id"] != asset_id or existing["source_id"] != source_id:
                raise EvidenceConflictError("Evidence package identity does not match its manifest")
            self.created_at = existing["created_at"]
            self._derived = {
                item["path"]: {
                    "parent": item["parent"],
                    "transformation": item["transformation"],
                }
                for item in existing.get("derived_files", [])
            }
        else:
            self.created_at = datetime.now(timezone.utc).isoformat()

    def write_immutable_text(self, relative_path: str, content: str) -> Path:
        return self.write_immutable_bytes(relative_path, content.encode("utf-8"))

    def write_immutable_bytes(self, relative_path: str, content: bytes) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            if path.read_bytes() != content:
                raise EvidenceConflictError(f"Refusing to overwrite immutable evidence: {relative_path}")
            return path
        with path.open("xb") as handle:
            handle.write(content)
        return path

    def write_derived_text(
        self,
        relative_path: str,
        content: str,
        *,
        parent: str,
        transformation: str,
    ) -> Path:
        if not (self.root / parent).is_file():
            raise FileNotFoundError(f"Derived text parent does not exist: {parent}")
        path = self.write_immutable_text(relative_path, content)
        self._derived[relative_path] = {
            "parent": parent,
            "transformation": transformation,
        }
        return path

    def write_lossless_cleaned_text(
        self,
        relative_path: str,
        content: str,
        *,
        parent: str,
        corrections: tuple[tuple[str, str], ...] = (),
    ) -> Path:
        parent_path = self.root / parent
        if not parent_path.exists():
            raise FileNotFoundError(f"Derived text parent does not exist: {parent}")
        raw_text = parent_path.read_text(encoding="utf-8")
        validate_lossless_cleaning(raw_text, content, corrections=corrections)
        path = self.write_immutable_text(relative_path, content)
        self._derived[relative_path] = {
            "parent": parent,
            "transformation": "lossless-cleaning",
        }
        return path

    def finalize(self, *, completeness: str) -> Path:
        immutable_files = []
        derived_files = []
        checksum_lines = []
        excluded = {"manifest.json", "checksums.sha256"}
        for path in sorted(item for item in self.root.rglob("*") if item.is_file()):
            relative_path = path.relative_to(self.root).as_posix()
            if relative_path in excluded:
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            file_record = {
                "path": relative_path,
                "byte_length": path.stat().st_size,
                "sha256": digest,
                "mime_type": mimetypes.guess_type(relative_path)[0] or "application/octet-stream",
            }
            if relative_path in self._derived:
                derived_files.append(file_record | self._derived[relative_path])
            else:
                immutable_files.append(file_record | {"role": "source"})
            checksum_lines.append(f"{digest}  {relative_path}")

        manifest = {
            "schema_version": 1,
            "asset_id": self.asset_id,
            "source_id": self.source_id,
            "created_at": self.created_at,
            "completeness": completeness,
            "immutable_files": immutable_files,
            "derived_files": derived_files,
            "limitations": [],
            "capture_events": [],
        }
        self._write_control_file("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        manifest_digest = hashlib.sha256((self.root / "manifest.json").read_bytes()).hexdigest()
        checksum_lines.append(f"{manifest_digest}  manifest.json")
        self._write_control_file("checksums.sha256", "\n".join(checksum_lines) + "\n")
        return self.root / "manifest.json"

    def _write_control_file(self, relative_path: str, content: str) -> None:
        path = self.root / relative_path
        encoded = content.encode("utf-8")
        if path.exists() and path.read_bytes() != encoded:
            raise EvidenceConflictError(f"Refusing to rewrite finalized control file: {relative_path}")
        if not path.exists():
            with path.open("xb") as handle:
                handle.write(encoded)
