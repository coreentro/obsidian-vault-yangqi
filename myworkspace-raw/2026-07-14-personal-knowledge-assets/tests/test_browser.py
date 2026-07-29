import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from knowledge_assets.browser import (
    BrowserInventoryConflictError,
    is_readable_content_url,
    read_chromium_bookmarks,
    read_chromium_history,
    write_chromium_inventory,
)


class BrowserInventoryTest(unittest.TestCase):
    def test_reads_nested_http_bookmarks_without_shortening_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            bookmark_path = Path(temporary_directory) / "Bookmarks"
            bookmark_path.write_text(
                json.dumps(
                    {
                        "roots": {
                            "bookmark_bar": {
                                "type": "folder",
                                "name": "收藏栏",
                                "children": [
                                    {
                                        "type": "url",
                                        "name": "完整标题",
                                        "url": "https://example.com/article?id=1",
                                        "date_added": "13300000000000000",
                                    },
                                    {
                                        "type": "folder",
                                        "name": "研究",
                                        "children": [
                                            {
                                                "type": "url",
                                                "name": "第二篇",
                                                "url": "https://forum.example.com/topic/2",
                                            }
                                        ],
                                    },
                                    {"type": "url", "name": "脚本", "url": "javascript:void(0)"},
                                ],
                            }
                        }
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            bookmarks = read_chromium_bookmarks(bookmark_path, profile_id="chrome-default")

            self.assertEqual([bookmark.title for bookmark in bookmarks], ["完整标题", "第二篇"])
            self.assertEqual(bookmarks[1].folder_path, ("收藏栏", "研究"))
            self.assertEqual(bookmarks[0].url, "https://example.com/article?id=1")

    def test_content_url_filter_excludes_navigation_and_sensitive_utility_pages(self) -> None:
        self.assertTrue(is_readable_content_url("https://example.com/articles/knowledge-system"))
        self.assertFalse(is_readable_content_url("https://example.com/login"))
        self.assertFalse(is_readable_content_url("https://www.google.com/search?q=knowledge"))
        self.assertFalse(is_readable_content_url("chrome://settings"))

    def test_history_scan_accounts_for_every_row_and_marks_content_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            history_path = Path(temporary_directory) / "History"
            connection = sqlite3.connect(history_path)
            connection.execute(
                "CREATE TABLE urls (id INTEGER PRIMARY KEY, url TEXT, title TEXT, visit_count INTEGER, last_visit_time INTEGER)"
            )
            connection.executemany(
                "INSERT INTO urls (url, title, visit_count, last_visit_time) VALUES (?, ?, ?, ?)",
                [
                    ("https://example.com/article", "文章", 3, 100),
                    ("https://example.com/login", "登录", 2, 90),
                    ("https://www.google.com/search?q=test", "搜索", 1, 80),
                ],
            )
            connection.commit()
            connection.close()
            modified_before = history_path.stat().st_mtime_ns

            records = read_chromium_history(history_path, profile_id="chrome-default")

            self.assertEqual(len(records), 3)
            self.assertEqual(sum(record.is_content_candidate for record in records), 1)
            self.assertEqual(records[0].title, "文章")
            self.assertEqual(history_path.stat().st_mtime_ns, modified_before)

    def test_frozen_browser_inventory_cannot_be_silently_replaced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            bookmark_path = root / "Bookmarks"
            bookmark_path.write_text(
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
            history_path = root / "History"
            connection = sqlite3.connect(history_path)
            connection.execute(
                "CREATE TABLE urls (id INTEGER PRIMARY KEY, url TEXT, title TEXT, visit_count INTEGER, last_visit_time INTEGER)"
            )
            connection.execute(
                "INSERT INTO urls (url, title, visit_count, last_visit_time) VALUES (?, ?, ?, ?)",
                ("https://example.com/a", "文章", 2, 100),
            )
            connection.commit()
            connection.close()
            output = root / "browser-inventory.json"

            write_chromium_inventory(
                output,
                profile_id="chrome-default",
                baseline_at="2026-07-14T00:00:00+08:00",
                bookmarks_path=bookmark_path,
                history_path=history_path,
            )
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(payload["bookmarks_total"], 1)
            self.assertEqual(payload["history_total"], 1)

            with self.assertRaises(BrowserInventoryConflictError):
                write_chromium_inventory(
                    output,
                    profile_id="chrome-default",
                    baseline_at="2026-07-15T00:00:00+08:00",
                    bookmarks_path=bookmark_path,
                    history_path=history_path,
                )

    def test_history_scan_includes_committed_wal_rows_without_modifying_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            history_path = Path(temporary_directory) / "History"
            connection = sqlite3.connect(history_path)
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute(
                "CREATE TABLE urls (id INTEGER PRIMARY KEY, url TEXT, title TEXT, visit_count INTEGER, last_visit_time INTEGER)"
            )
            connection.commit()
            connection.execute(
                "INSERT INTO urls (url, title, visit_count, last_visit_time) VALUES (?, ?, ?, ?)",
                ("https://example.com/wal-article", "WAL文章", 1, 101),
            )
            connection.commit()
            source_bytes_before = history_path.read_bytes()
            modified_before = history_path.stat().st_mtime_ns

            records = read_chromium_history(history_path, profile_id="chrome-default")

            self.assertEqual([record.title for record in records], ["WAL文章"])
            self.assertEqual(history_path.read_bytes(), source_bytes_before)
            self.assertEqual(history_path.stat().st_mtime_ns, modified_before)
            connection.close()


if __name__ == "__main__":
    unittest.main()
