import tempfile
import unittest
import json
import sqlite3
from pathlib import Path

from knowledge_assets.cli import main
from knowledge_assets.ledger import Ledger


class CliTest(unittest.TestCase):
    def test_initializes_workspace_and_creates_frozen_local_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            workspace = root / "workspace"
            personal_root = root / "personal"
            personal_root.mkdir()
            (personal_root / "valuable-note.txt").write_text("完整内容", encoding="utf-8")
            generated_root = personal_root / "knowledge-system"
            generated_root.mkdir()
            (generated_root / "generated.sqlite3").write_text("系统生成", encoding="utf-8")
            inventory_path = workspace / "data" / "inventories" / "mac-current-local-2026-07-14.json"

            self.assertEqual(main(["init", "--workspace", str(workspace)]), 0)
            self.assertEqual(
                main(
                    [
                        "scan-local",
                        "--workspace",
                        str(workspace),
                        "--device-id",
                        "mac-current",
                        "--baseline-at",
                        "2026-07-14T00:00:00+08:00",
                        "--root",
                        str(personal_root),
                        "--exclude",
                        str(generated_root),
                        "--output",
                        str(inventory_path),
                    ]
                ),
                0,
            )

            self.assertTrue((workspace / "data" / "knowledge-assets.sqlite3").exists())
            self.assertTrue((workspace / "data" / "search-index.sqlite3").exists())
            self.assertTrue(inventory_path.exists())
            inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
            self.assertEqual(inventory["scanned_total"], 1)

    def test_creates_chromium_profile_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            bookmarks = root / "Bookmarks"
            bookmarks.write_text(
                json.dumps(
                    {
                        "roots": {
                            "bookmark_bar": {
                                "type": "folder",
                                "name": "收藏栏",
                                "children": [
                                    {"type": "url", "name": "文章", "url": "https://example.com/a"}
                                ],
                            }
                        }
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            history = root / "History"
            connection = sqlite3.connect(history)
            connection.execute(
                "CREATE TABLE urls (id INTEGER PRIMARY KEY, url TEXT, title TEXT, visit_count INTEGER, last_visit_time INTEGER)"
            )
            connection.execute(
                "INSERT INTO urls (url, title, visit_count, last_visit_time) VALUES (?, ?, ?, ?)",
                ("https://example.com/a", "文章", 2, 100),
            )
            connection.commit()
            connection.close()
            output = root / "workspace" / "data" / "inventories" / "chrome-default.json"

            exit_code = main(
                [
                    "scan-chromium",
                    "--workspace",
                    str(root / "workspace"),
                    "--profile-id",
                    "chrome-default",
                    "--baseline-at",
                    "2026-07-14T00:00:00+08:00",
                    "--bookmarks",
                    str(bookmarks),
                    "--history",
                    str(history),
                    "--output",
                    str(output),
                ]
            )

            self.assertEqual(exit_code, 0)
            self.assertTrue(output.exists())

    def test_registers_device_and_frozen_inventory_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            workspace = Path(temporary_directory) / "workspace"
            inventory = workspace / "data" / "inventories" / "local.json"
            inventory.parent.mkdir(parents=True)
            inventory.write_text(
                json.dumps(
                    {
                        "device_id": "mac-current",
                        "baseline_at": "2026-07-14T00:00:00+08:00",
                        "scanned_total": 3,
                    }
                ),
                encoding="utf-8",
            )
            main(["init", "--workspace", str(workspace)])

            self.assertEqual(
                main(
                    [
                        "register-device",
                        "--workspace",
                        str(workspace),
                        "--device-id",
                        "mac-current",
                        "--platform",
                        "macos",
                        "--device-name",
                        "Current Mac",
                        "--browser-profile",
                        "chrome-default",
                        "--personal-root",
                        "~/Documents",
                        "--sync-service",
                        "onedrive",
                        "--status",
                        "verified",
                    ]
                ),
                0,
            )
            self.assertEqual(
                main(
                    [
                        "register-inventory-source",
                        "--workspace",
                        str(workspace),
                        "--source-id",
                        "mac-current-local",
                        "--platform",
                        "local-files",
                        "--collection",
                        "personal-roots",
                        "--inventory",
                        str(inventory),
                    ]
                ),
                0,
            )

            with Ledger(workspace / "data" / "knowledge-assets.sqlite3") as ledger:
                self.assertEqual(ledger.get_device("mac-current")["verification_status"], "verified")
                source = ledger.get_source("mac-current-local")
                self.assertEqual(source["scanned_total"], 3)
                self.assertEqual(source["blocked_total"], 3)

    def test_registers_browser_bookmarks_and_history_with_separate_accounting(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            workspace = Path(temporary_directory) / "workspace"
            inventory = workspace / "data" / "inventories" / "browser.json"
            inventory.parent.mkdir(parents=True)
            inventory.write_text(
                json.dumps(
                    {
                        "profile_id": "chrome-default",
                        "baseline_at": "2026-07-14T00:00:00+08:00",
                        "bookmarks_total": 2,
                        "history_total": 5,
                        "content_candidates_total": 4,
                    }
                ),
                encoding="utf-8",
            )
            main(["init", "--workspace", str(workspace)])

            exit_code = main(
                [
                    "register-browser-inventory",
                    "--workspace",
                    str(workspace),
                    "--inventory",
                    str(inventory),
                ]
            )

            self.assertEqual(exit_code, 0)
            with Ledger(workspace / "data" / "knowledge-assets.sqlite3") as ledger:
                bookmarks = ledger.get_source("chrome-default-bookmarks")
                history = ledger.get_source("chrome-default-history")
                self.assertEqual(bookmarks["included_total"], 2)
                self.assertEqual(bookmarks["verification_status"], "verified")
                self.assertEqual(history["excluded_total"], 1)
                self.assertEqual(history["blocked_total"], 4)

    def test_seeds_candidates_from_a_frozen_browser_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            workspace = Path(temporary_directory) / "workspace"
            inventory = workspace / "data" / "inventories" / "browser.json"
            inventory.parent.mkdir(parents=True)
            inventory.write_text(
                json.dumps(
                    {
                        "profile_id": "chrome-default",
                        "baseline_at": "2026-07-14T00:00:00+08:00",
                        "bookmarks": [
                            {
                                "title": "文章",
                                "url": "https://example.com/article",
                                "folder_path": ["书签栏"],
                                "date_added": "1",
                            }
                        ],
                        "history": [],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            main(["init", "--workspace", str(workspace)])
            with Ledger(workspace / "data" / "knowledge-assets.sqlite3") as ledger:
                ledger.register_source(
                    source_id="chrome-default-bookmarks",
                    platform="browser",
                    collection="bookmarks",
                    baseline_at="2026-07-14T00:00:00+08:00",
                    scanned_total=1,
                )
                ledger.reconcile_source(
                    "chrome-default-bookmarks", included_total=1, excluded_total=0, blocked_total=0
                )

            self.assertEqual(
                main(
                    [
                        "seed-candidates",
                        "--workspace",
                        str(workspace),
                        "--inventory",
                        str(inventory),
                    ]
                ),
                0,
            )
            self.assertEqual(
                main(
                    [
                        "seed-candidates",
                        "--workspace",
                        str(workspace),
                        "--inventory",
                        str(inventory),
                    ]
                ),
                0,
            )
            with Ledger(workspace / "data" / "knowledge-assets.sqlite3") as ledger:
                self.assertEqual(ledger.connection.execute("SELECT COUNT(*) FROM candidates").fetchone()[0], 1)


if __name__ == "__main__":
    unittest.main()
