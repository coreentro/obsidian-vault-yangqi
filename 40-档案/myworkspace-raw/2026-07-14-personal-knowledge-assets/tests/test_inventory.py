import tempfile
import unittest
import json
from pathlib import Path

from knowledge_assets.inventory import InventoryConflictError, scan_personal_roots, write_inventory_manifest


class InventoryTest(unittest.TestCase):
    def test_scan_is_read_only_and_excludes_cache_and_system_noise(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            document = root / "Documents" / "notes.txt"
            download = root / "Downloads" / "article.pdf"
            cache = root / "Library" / "Caches" / "noise.bin"
            system_file = root / ".DS_Store"
            for path, content in (
                (document, b"complete notes"),
                (download, b"complete article"),
                (cache, b"cache"),
                (system_file, b"system"),
            ):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)

            before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in (document, download, cache, system_file)}
            candidates = scan_personal_roots([root], device_id="mac-current")
            after = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in (document, download, cache, system_file)}

            self.assertEqual(before, after)
            self.assertEqual({candidate.path.name for candidate in candidates}, {"notes.txt", "article.pdf"})
            article = next(candidate for candidate in candidates if candidate.path.name == "article.pdf")
            self.assertIn("download", article.preservation_signals)
            self.assertEqual(len(article.sha256), 64)

    def test_inventory_manifest_is_auditable_and_not_silently_replaced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "source" / "note.txt"
            source.parent.mkdir(parents=True)
            source.write_text("完整资料", encoding="utf-8")
            candidates = scan_personal_roots([source.parent], device_id="mac-current")
            manifest_path = root / "inventory.json"

            write_inventory_manifest(
                manifest_path,
                device_id="mac-current",
                baseline_at="2026-07-14T00:00:00+08:00",
                roots=[source.parent],
                candidates=candidates,
            )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["scanned_total"], 1)
            self.assertEqual(manifest["candidates"][0]["sha256"], candidates[0].sha256)

            with self.assertRaises(InventoryConflictError):
                write_inventory_manifest(
                    manifest_path,
                    device_id="mac-current",
                    baseline_at="2026-07-15T00:00:00+08:00",
                    roots=[source.parent],
                    candidates=candidates,
                )

    def test_explicitly_excluded_workspace_is_not_scanned(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            kept = root / "Documents" / "kept.txt"
            excluded = root / "Documents" / "knowledge-system" / "generated.sqlite3"
            kept.parent.mkdir(parents=True)
            excluded.parent.mkdir(parents=True)
            kept.write_text("保留", encoding="utf-8")
            excluded.write_text("系统生成", encoding="utf-8")

            candidates = scan_personal_roots(
                [root / "Documents"],
                device_id="mac-current",
                exclude_roots=[excluded.parent],
            )

            self.assertEqual([candidate.path.name for candidate in candidates], ["kept.txt"])


if __name__ == "__main__":
    unittest.main()
