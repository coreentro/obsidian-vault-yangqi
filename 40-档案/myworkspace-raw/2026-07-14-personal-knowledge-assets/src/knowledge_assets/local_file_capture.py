from __future__ import annotations

import hashlib
import json
import os
import stat
from io import BytesIO
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader

from .evidence import EvidencePackage


class FrozenFileChangedError(RuntimeError):
    """Raised when the current file differs from its frozen inventory record."""


class UnsafeLocalFileError(RuntimeError):
    """Raised when a local path is not safe for read-only evidence capture."""


@dataclass(frozen=True)
class LocalCaptureResult:
    asset_id: str
    candidate_id: str
    package_path: Path
    source_sha256: str
    source_byte_length: int
    source_text: str


class LocalFileCapture:
    """Copy a frozen plain-text file into an immutable evidence package.

    The source is opened read-only with symlink following disabled where the
    platform supports it. Its identity, size, and digest are checked before any
    evidence directory is created, and checked again after the read.
    """

    def __init__(self, evidence_root: Path, *, max_file_bytes: int = 25 * 1024 * 1024) -> None:
        self.evidence_root = Path(evidence_root)
        self.max_file_bytes = max_file_bytes

    def capture_plain_text(
        self,
        *,
        candidate_id: str,
        source_id: str,
        source_path: Path,
        frozen_sha256: str,
        frozen_byte_length: int,
        title: str,
    ) -> LocalCaptureResult:
        path = Path(source_path)
        raw, before = self._read_frozen_bytes(
            path,
            frozen_sha256=frozen_sha256,
            frozen_byte_length=frozen_byte_length,
        )
        digest = frozen_sha256
        try:
            source_text = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            raise UnsafeLocalFileError(f"Plain-text source is not valid UTF-8: {path}") from error

        asset_id = "asset-" + hashlib.sha256(
            f"local-file\0{candidate_id}\0{frozen_sha256}".encode("utf-8")
        ).hexdigest()[:24]
        package_path = self.evidence_root / asset_id
        package = EvidencePackage(package_path, asset_id=asset_id, source_id=source_id)
        suffix = path.suffix.lower()
        if suffix not in {".md", ".txt"}:
            raise UnsafeLocalFileError(f"Unsupported plain-text suffix: {suffix or '<none>'}")
        original_name = f"source-original{suffix}"
        package.write_immutable_bytes(original_name, raw)
        package.write_derived_text(
            "source.md",
            source_text,
            parent=original_name,
            transformation="exact UTF-8 decoding; no characters added, removed, or reordered",
        )
        package.write_immutable_text(
            "metadata.json",
            _json_text(
                {
                    "candidate_id": candidate_id,
                    "source_id": source_id,
                    "title": title,
                    "original_path": str(path),
                    "original_filename": path.name,
                    "original_suffix": suffix,
                    "frozen_sha256": frozen_sha256,
                    "frozen_byte_length": frozen_byte_length,
                    "source_mtime_ns": before.st_mtime_ns,
                }
            ),
        )
        package.write_immutable_text(
            "comments.json",
            _json_text(
                {
                    "applicable": False,
                    "captured": [],
                    "scope": "Local standalone document; no platform comment surface applies.",
                }
            ),
        )
        package.write_immutable_text(
            "capture-log.json",
            _json_text(
                {
                    "method": "read-only local file capture",
                    "source_mutated": False,
                    "pre_read_frozen_hash_verified": True,
                    "post_read_identity_verified": True,
                    "post_read_hash_verified": True,
                    "text_decoding": "utf-8 strict",
                    "transcript": "not applicable to a native text document",
                    "limitations": [],
                }
            ),
        )
        package.finalize(completeness="complete")
        return LocalCaptureResult(
            asset_id=asset_id,
            candidate_id=candidate_id,
            package_path=package_path,
            source_sha256=digest,
            source_byte_length=len(raw),
            source_text=source_text,
        )

    def capture_pdf(
        self,
        *,
        candidate_id: str,
        source_id: str,
        source_path: Path,
        frozen_sha256: str,
        frozen_byte_length: int,
        title: str,
        visually_reviewed_pages: list[int],
        additional_limitations: list[str] | None = None,
    ) -> LocalCaptureResult:
        path = Path(source_path)
        if path.suffix.lower() != ".pdf":
            raise UnsafeLocalFileError(f"PDF source must use the .pdf suffix: {path}")
        raw, before = self._read_frozen_bytes(
            path,
            frozen_sha256=frozen_sha256,
            frozen_byte_length=frozen_byte_length,
        )
        try:
            reader = PdfReader(BytesIO(raw))
        except Exception as error:
            raise UnsafeLocalFileError(f"Unable to parse PDF source: {path}") from error
        if reader.is_encrypted:
            raise UnsafeLocalFileError(f"Encrypted PDF requires manual review: {path}")

        page_count = len(reader.pages)
        reviewed_pages = sorted(set(int(page) for page in visually_reviewed_pages))
        if not reviewed_pages or any(page < 1 or page > page_count for page in reviewed_pages):
            raise ValueError("Visually reviewed pages must be valid one-based PDF page numbers")
        extra_limitations = list(
            dict.fromkeys(
                limitation.strip()
                for limitation in (additional_limitations or [])
                if isinstance(limitation, str) and limitation.strip()
            )
        )
        page_texts: list[str] = []
        empty_pages: list[int] = []
        for index, page in enumerate(reader.pages, start=1):
            try:
                page_text = page.extract_text() or ""
            except Exception as error:
                raise UnsafeLocalFileError(f"PDF text extraction failed on page {index}: {path}") from error
            page_texts.append(page_text)
            if not page_text.strip():
                empty_pages.append(index)
        extracted_text = "\n\n".join(
            f"===== PAGE {index} OF {page_count} =====\n{text}"
            for index, text in enumerate(page_texts, start=1)
        )

        asset_id = "asset-" + hashlib.sha256(
            f"local-pdf\0{candidate_id}\0{frozen_sha256}".encode("utf-8")
        ).hexdigest()[:24]
        package_path = self.evidence_root / asset_id
        package = EvidencePackage(package_path, asset_id=asset_id, source_id=source_id)
        package.write_immutable_bytes("source-original.pdf", raw)
        package.write_derived_text(
            "transcript-raw.txt",
            extracted_text,
            parent="source-original.pdf",
            transformation="pypdf page-by-page text extraction with explicit page boundaries; no extracted page text omitted",
        )
        package.write_derived_text(
            "source.md",
            extracted_text,
            parent="transcript-raw.txt",
            transformation="exact UTF-8 copy of transcript-raw.txt; no characters added, removed, or reordered",
        )
        package.write_immutable_text(
            "metadata.json",
            _json_text(
                {
                    "candidate_id": candidate_id,
                    "source_id": source_id,
                    "title": title,
                    "original_path": str(path),
                    "original_filename": path.name,
                    "frozen_sha256": frozen_sha256,
                    "frozen_byte_length": frozen_byte_length,
                    "source_mtime_ns": before.st_mtime_ns,
                    "page_count": page_count,
                }
            ),
        )
        package.write_immutable_text(
            "extraction.json",
            _json_text(
                {
                    "tool": "pypdf",
                    "page_count": page_count,
                    "pages_traversed": page_count,
                    "empty_text_pages": empty_pages,
                    "extracted_character_count": len(extracted_text),
                    "visually_reviewed_pages": reviewed_pages,
                    "visual_review_scope": "Rendered first, middle, and last pages when distinct; checked for legibility, clipping, and missing page content.",
                }
            ),
        )
        package.write_immutable_text(
            "comments.json",
            _json_text(
                {
                    "applicable": False,
                    "captured": [],
                    "scope": "Standalone scholarly PDF; no platform comment surface applies.",
                }
            ),
        )
        package.write_immutable_text(
            "capture-log.json",
            _json_text(
                {
                    "method": "read-only local PDF capture",
                    "source_mutated": False,
                    "pre_read_frozen_hash_verified": True,
                    "post_read_identity_verified": True,
                    "post_read_hash_verified": True,
                    "all_pdf_pages_traversed": True,
                    "text_extraction": "pypdf page-by-page",
                    "limitations": [
                        "Text embedded inside raster figures may not appear in the extracted transcript; the exact original PDF preserves every figure and page."
                    ] + extra_limitations,
                }
            ),
        )
        completeness = "complete" if not empty_pages else "limited"
        package.finalize(completeness=completeness)
        return LocalCaptureResult(
            asset_id=asset_id,
            candidate_id=candidate_id,
            package_path=package_path,
            source_sha256=frozen_sha256,
            source_byte_length=len(raw),
            source_text=extracted_text,
        )

    def _read_frozen_bytes(
        self,
        path: Path,
        *,
        frozen_sha256: str,
        frozen_byte_length: int,
    ) -> tuple[bytes, os.stat_result]:
        before = path.lstat()
        if stat.S_ISLNK(before.st_mode) or not stat.S_ISREG(before.st_mode):
            raise UnsafeLocalFileError(f"Source is not a regular non-symlink file: {path}")
        if before.st_size > self.max_file_bytes:
            raise UnsafeLocalFileError(f"Source exceeds capture limit: {path}")
        if before.st_size != frozen_byte_length:
            raise FrozenFileChangedError(f"Frozen byte length no longer matches: {path}")

        flags = os.O_RDONLY
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(path, flags)
        try:
            opened = os.fstat(descriptor)
            if (opened.st_dev, opened.st_ino) != (before.st_dev, before.st_ino):
                raise FrozenFileChangedError(f"Source identity changed while opening: {path}")
            chunks: list[bytes] = []
            total = 0
            while True:
                chunk = os.read(descriptor, min(1024 * 1024, self.max_file_bytes + 1 - total))
                if not chunk:
                    break
                chunks.append(chunk)
                total += len(chunk)
                if total > self.max_file_bytes:
                    raise UnsafeLocalFileError(f"Source exceeds capture limit: {path}")
            after_open = os.fstat(descriptor)
        finally:
            os.close(descriptor)

        after_path = path.lstat()
        identity = (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
        if identity != (after_open.st_dev, after_open.st_ino, after_open.st_size, after_open.st_mtime_ns):
            raise FrozenFileChangedError(f"Source changed during read: {path}")
        if identity != (after_path.st_dev, after_path.st_ino, after_path.st_size, after_path.st_mtime_ns):
            raise FrozenFileChangedError(f"Source path changed during read: {path}")

        raw = b"".join(chunks)
        digest = hashlib.sha256(raw).hexdigest()
        if len(raw) != frozen_byte_length or digest != frozen_sha256:
            raise FrozenFileChangedError(f"Frozen SHA-256 no longer matches: {path}")
        return raw, before


def _json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
