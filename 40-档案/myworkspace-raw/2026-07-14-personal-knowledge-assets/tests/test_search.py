import tempfile
import unittest
import sqlite3
from pathlib import Path

from knowledge_assets.search import IndexConflictError, SearchIndex


class SearchIndexTest(unittest.TestCase):
    def test_context_manager_closes_database_connection(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            with SearchIndex(Path(temporary_directory) / "search.sqlite3") as index:
                index.connection.execute("SELECT 1").fetchone()

            with self.assertRaises(sqlite3.ProgrammingError):
                index.connection.execute("SELECT 1").fetchone()

    def test_indexes_full_source_text_and_refuses_silent_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            index = SearchIndex(Path(temporary_directory) / "search.sqlite3")
            self.addCleanup(index.close)
            full_text = "第一段完整内容。第二段讨论知识库如何服务实践，不能删减。"
            index.add_asset(
                asset_id="asset-001",
                title="个人知识库",
                source_text=full_text,
                author="作者甲",
                platform="forum",
                topics=["知识管理", "实践"],
                evidence_ref="gdrive://evidence/asset-001",
            )

            results = index.search("知识库服务实践")
            self.assertEqual(results[0]["asset_id"], "asset-001")
            self.assertEqual(results[0]["source_text"], full_text)

            with self.assertRaises(IndexConflictError):
                index.add_asset(
                    asset_id="asset-001",
                    title="个人知识库",
                    source_text="被删减的内容",
                    author="作者甲",
                    platform="forum",
                    topics=["知识管理"],
                    evidence_ref="gdrive://evidence/asset-001",
                )

    def test_short_chinese_query_and_separated_concepts_use_a_recall_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            with SearchIndex(Path(temporary_directory) / "search.sqlite3") as index:
                index.add_asset(
                    asset_id="asset-noise",
                    title="资源导航",
                    source_text="提供站内搜索入口。",
                    author=None,
                    platform="forum",
                    topics=[],
                    evidence_ref="evidence/asset-noise",
                )
                index.add_asset(
                    asset_id="asset-search",
                    title="如何增强自己搜索的能力",
                    source_text="本文讨论检索方法与信息判断。",
                    author=None,
                    platform="forum",
                    topics=["学习方法"],
                    evidence_ref="evidence/asset-search",
                )

                self.assertEqual(index.search("搜索")[0]["asset_id"], "asset-search")
                self.assertEqual(index.search("搜索能力")[0]["asset_id"], "asset-search")

    def test_bilingual_aliases_add_recall_without_rewriting_indexed_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            index = SearchIndex(Path(temporary_directory) / "search.sqlite3")
            self.addCleanup(index.close)
            index.add_asset(
                asset_id="asset-paper",
                title="Sulfur vacancies and photocatalytic hydrogen evolution",
                source_text="An English-only research article about charge transfer.",
                author="Researcher",
                platform="local-pdf",
                topics=["photocatalysis", "sulfur-vacancies"],
                evidence_ref="evidence/asset-paper",
            )

            self.assertEqual(index.search("硫空位 光催化制氢"), [])
            index.add_aliases(
                asset_id="asset-paper",
                aliases=["硫空位", "电子转移", "光催化制氢"],
            )
            self.assertEqual(index.search("硫空位 光催化制氢")[0]["asset_id"], "asset-paper")
            index.add_aliases(
                asset_id="asset-paper",
                aliases=["硫空位", "电子转移", "光催化制氢"],
            )
            with self.assertRaises(IndexConflictError):
                index.add_aliases(asset_id="asset-paper", aliases=["被静默替换"])

    def test_extends_aliases_append_only_without_replacing_frozen_alias_set(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            index = SearchIndex(Path(temporary_directory) / "search.sqlite3")
            self.addCleanup(index.close)
            index.add_asset(
                asset_id="asset-paper",
                title="微波辐射相转移催化下水相合成查尔酮",
                source_text="完整论文正文",
                author="作者",
                platform="local-pdf",
                topics=["chemistry"],
                evidence_ref="evidence/asset-paper",
            )
            index.add_aliases(asset_id="asset-paper", aliases=["TBAB catalyst"])
            frozen = index.connection.execute(
                "SELECT aliases_json, content_hash FROM document_aliases WHERE asset_id = ?",
                ("asset-paper",),
            ).fetchone()

            index.extend_aliases(asset_id="asset-paper", aliases=["水相微波查尔酮"])
            index.extend_aliases(asset_id="asset-paper", aliases=["水相微波查尔酮"])

            current = index.connection.execute(
                "SELECT aliases_json, content_hash FROM document_aliases WHERE asset_id = ?",
                ("asset-paper",),
            ).fetchone()
            self.assertEqual(tuple(current), tuple(frozen))
            self.assertEqual(index.search("水相微波查尔酮")[0]["asset_id"], "asset-paper")
            self.assertEqual(
                index.connection.execute(
                    "SELECT COUNT(*) FROM document_alias_additions WHERE asset_id = ?",
                    ("asset-paper",),
                ).fetchone()[0],
                1,
            )


if __name__ == "__main__":
    unittest.main()
