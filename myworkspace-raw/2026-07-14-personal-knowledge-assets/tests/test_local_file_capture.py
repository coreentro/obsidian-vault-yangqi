import hashlib
import json
import tempfile
import unittest
from io import BytesIO
from pathlib import Path

from pypdf import PdfWriter

from knowledge_assets.local_file_capture import (
    FrozenFileChangedError,
    LocalFileCapture,
    UnsafeLocalFileError,
)


class LocalFileCaptureTest(unittest.TestCase):
    def test_preserves_exact_original_and_complete_plain_text(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "note.md"
            raw = "# 原始笔记\n\n重复的话不能删。重复的话不能删。\n".encode("utf-8")
            source.write_bytes(raw)
            frozen_hash = hashlib.sha256(raw).hexdigest()

            result = LocalFileCapture(root / "evidence").capture_plain_text(
                candidate_id="local:item:1",
                source_id="local-files",
                source_path=source,
                frozen_sha256=frozen_hash,
                frozen_byte_length=len(raw),
                title="原始笔记",
            )

            package = result.package_path
            self.assertEqual((package / "source-original.md").read_bytes(), raw)
            self.assertEqual((package / "source.md").read_bytes(), raw)
            manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["completeness"], "complete")
            self.assertIn("source-original.md", {x["path"] for x in manifest["immutable_files"]})
            self.assertIn("source.md", {x["path"] for x in manifest["derived_files"]})
            self.assertEqual(result.source_sha256, frozen_hash)

    def test_rejects_changed_file_before_creating_package(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "note.md"
            source.write_text("changed", encoding="utf-8")

            with self.assertRaises(FrozenFileChangedError):
                LocalFileCapture(root / "evidence").capture_plain_text(
                    candidate_id="local:item:1",
                    source_id="local-files",
                    source_path=source,
                    frozen_sha256=hashlib.sha256(b"original").hexdigest(),
                    frozen_byte_length=len(b"original"),
                    title="note",
                )
            self.assertEqual(list((root / "evidence").glob("asset-*")), [])

    def test_rejects_symlink_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            target = root / "target.md"
            target.write_text("safe", encoding="utf-8")
            link = root / "link.md"
            link.symlink_to(target)

            with self.assertRaises(UnsafeLocalFileError):
                LocalFileCapture(root / "evidence").capture_plain_text(
                    candidate_id="local:item:1",
                    source_id="local-files",
                    source_path=link,
                    frozen_sha256=hashlib.sha256(b"safe").hexdigest(),
                    frozen_byte_length=4,
                    title="note",
                )

    def test_replay_is_idempotent_but_conflicting_package_is_not_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "note.txt"
            source.write_text("same", encoding="utf-8")
            digest = hashlib.sha256(b"same").hexdigest()
            capture = LocalFileCapture(root / "evidence")
            kwargs = dict(
                candidate_id="local:item:1",
                source_id="local-files",
                source_path=source,
                frozen_sha256=digest,
                frozen_byte_length=4,
                title="note",
            )
            first = capture.capture_plain_text(**kwargs)
            second = capture.capture_plain_text(**kwargs)
            self.assertEqual(first, second)
            with self.assertRaises(Exception):
                capture.capture_plain_text(**(kwargs | {"title": "different"}))

    def test_pdf_capture_preserves_original_and_records_every_page_extraction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "paper.pdf"
            writer = PdfWriter()
            writer.add_blank_page(width=612, height=792)
            writer.add_blank_page(width=612, height=792)
            buffer = BytesIO()
            writer.write(buffer)
            raw = buffer.getvalue()
            source.write_bytes(raw)

            result = LocalFileCapture(root / "evidence").capture_pdf(
                candidate_id="local:item:pdf",
                source_id="local-files",
                source_path=source,
                frozen_sha256=hashlib.sha256(raw).hexdigest(),
                frozen_byte_length=len(raw),
                title="paper",
                visually_reviewed_pages=[1, 2],
                additional_limitations=["Embedded font extraction is incomplete; original PDF is authoritative."],
            )

            self.assertEqual((result.package_path / "source-original.pdf").read_bytes(), raw)
            extracted = (result.package_path / "transcript-raw.txt").read_text(encoding="utf-8")
            self.assertIn("===== PAGE 1 OF 2 =====", extracted)
            self.assertIn("===== PAGE 2 OF 2 =====", extracted)
            extraction = json.loads(
                (result.package_path / "extraction.json").read_text(encoding="utf-8")
            )
            self.assertEqual(extraction["page_count"], 2)
            self.assertEqual(extraction["empty_text_pages"], [1, 2])
            self.assertEqual(extraction["visually_reviewed_pages"], [1, 2])
            capture_log = json.loads(
                (result.package_path / "capture-log.json").read_text(encoding="utf-8")
            )
            self.assertIn(
                "Embedded font extraction is incomplete; original PDF is authoritative.",
                capture_log["limitations"],
            )
            manifest = json.loads(
                (result.package_path / "manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(manifest["completeness"], "limited")


if __name__ == "__main__":
    unittest.main()
