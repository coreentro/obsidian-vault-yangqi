import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from knowledge_assets.evidence import (
    EvidenceConflictError,
    EvidencePackage,
    LosslessCleaningError,
    validate_lossless_cleaning,
)


class EvidencePackageTest(unittest.TestCase):
    def test_writes_complete_immutable_source_and_rejects_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            package = EvidencePackage(root / "asset-001", asset_id="asset-001", source_id="source-001")

            package.write_immutable_text("source.md", "第一段\n\n第二段，不能删减。")
            package.finalize(completeness="complete")

            source_path = root / "asset-001" / "source.md"
            manifest_path = root / "asset-001" / "manifest.json"
            checksum_path = root / "asset-001" / "checksums.sha256"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            expected_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()

            self.assertEqual(source_path.read_text(encoding="utf-8"), "第一段\n\n第二段，不能删减。")
            self.assertEqual(manifest["asset_id"], "asset-001")
            self.assertEqual(manifest["immutable_files"][0]["sha256"], expected_hash)
            self.assertIn(f"{expected_hash}  source.md", checksum_path.read_text(encoding="utf-8"))

            with self.assertRaises(EvidenceConflictError):
                package.write_immutable_text("source.md", "被删减的版本")

    def test_cleaned_transcript_may_add_structure_but_may_not_delete_words(self) -> None:
        raw = "嗯今天我们说知识库知识库很重要"
        cleaned = "说话人 1：嗯，今天我们说：知识库，知识库很重要。"

        validate_lossless_cleaning(raw, cleaned)

        with self.assertRaises(LosslessCleaningError):
            validate_lossless_cleaning(raw, "今天我们说：知识库很重要。")

    def test_records_cleaned_transcript_as_derived_without_replacing_raw_text(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            package = EvidencePackage(root / "asset-002", asset_id="asset-002", source_id="source-001")
            raw = "嗯今天我们说知识库知识库很重要"
            cleaned = "说话人 1：嗯，今天我们说：知识库，知识库很重要。"

            package.write_immutable_text("transcript-raw.txt", raw)
            package.write_lossless_cleaned_text(
                "transcript-clean.md",
                cleaned,
                parent="transcript-raw.txt",
            )
            package.finalize(completeness="limited")

            manifest = json.loads((root / "asset-002" / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual((root / "asset-002" / "transcript-raw.txt").read_text(encoding="utf-8"), raw)
            self.assertEqual(manifest["derived_files"][0]["path"], "transcript-clean.md")
            self.assertEqual(manifest["derived_files"][0]["parent"], "transcript-raw.txt")
            self.assertNotIn(
                "transcript-clean.md",
                {item["path"] for item in manifest["immutable_files"]},
            )

    def test_writes_immutable_bytes_without_text_decoding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            package = EvidencePackage(root / "asset-bin", asset_id="asset-bin", source_id="source-001")
            raw = b"\x00\xff\x10raw"
            package.write_immutable_bytes("source-response.bin", raw)
            package.finalize(completeness="limited")
            self.assertEqual((root / "asset-bin" / "source-response.bin").read_bytes(), raw)
            with self.assertRaises(EvidenceConflictError):
                package.write_immutable_bytes("source-response.bin", b"changed")


if __name__ == "__main__":
    unittest.main()
