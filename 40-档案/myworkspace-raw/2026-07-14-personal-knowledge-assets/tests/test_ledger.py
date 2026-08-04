import tempfile
import unittest
import sqlite3
from pathlib import Path

from knowledge_assets.ledger import Ledger, ReconciliationError


class LedgerTest(unittest.TestCase):
    def test_context_manager_closes_database_connection(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            with Ledger(Path(temporary_directory) / "knowledge-assets.sqlite3") as ledger:
                ledger.connection.execute("SELECT 1").fetchone()

            with self.assertRaises(sqlite3.ProgrammingError):
                ledger.connection.execute("SELECT 1").fetchone()

    def test_registers_a_verified_device_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            ledger = Ledger(Path(temporary_directory) / "knowledge-assets.sqlite3")
            self.addCleanup(ledger.close)
            ledger.register_device(
                device_id="mac-current",
                platform="macos",
                device_name="Current Mac",
                browser_profiles=["chrome-default", "safari-default"],
                personal_roots=["~/Desktop", "~/Documents", "~/Downloads"],
                sync_services=["onedrive"],
                verification_status="verified",
            )

            device = ledger.get_device("mac-current")
            self.assertEqual(device["platform"], "macos")
            self.assertEqual(device["verification_status"], "verified")

    def test_source_requires_exact_reconciliation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            ledger = Ledger(Path(temporary_directory) / "knowledge-assets.sqlite3")
            self.addCleanup(ledger.close)
            ledger.register_source(
                source_id="xiaohongshu-account-collections",
                platform="xiaohongshu",
                collection="collections",
                baseline_at="2026-07-14T00:00:00+08:00",
                scanned_total=10,
            )

            with self.assertRaises(ReconciliationError):
                ledger.reconcile_source(
                    "xiaohongshu-account-collections",
                    included_total=6,
                    excluded_total=2,
                    blocked_total=1,
                )

            ledger.reconcile_source(
                "xiaohongshu-account-collections",
                included_total=8,
                excluded_total=2,
                blocked_total=0,
            )

            source = ledger.get_source("xiaohongshu-account-collections")
            self.assertEqual(source["verification_status"], "verified")
            self.assertEqual(source["included_total"], 8)

    def test_duplicate_assets_remain_distinct_source_records(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            ledger = Ledger(Path(temporary_directory) / "knowledge-assets.sqlite3")
            self.addCleanup(ledger.close)
            ledger.register_source(
                source_id="browser-bookmarks",
                platform="browser",
                collection="bookmarks",
                baseline_at="2026-07-14T00:00:00+08:00",
                scanned_total=2,
            )
            ledger.register_candidate(
                candidate_id="candidate-001",
                source_id="browser-bookmarks",
                title="同一篇文章",
                original_url="https://example.com/article?a=1",
                preservation_signals=["bookmark"],
                value_score=90,
                decision="included",
                decision_reason="Explicit bookmark",
            )
            ledger.register_candidate(
                candidate_id="candidate-002",
                source_id="browser-bookmarks",
                title="同一篇文章的另一个入口",
                original_url="https://example.com/article?utm_source=test",
                preservation_signals=["bookmark"],
                value_score=88,
                decision="included",
                decision_reason="Explicit bookmark",
            )
            ledger.register_asset(
                asset_id="asset-001",
                candidate_id="candidate-001",
                source_id="browser-bookmarks",
                content_type="article",
                original_url="https://example.com/article?a=1",
                evidence_package_ref="gdrive://evidence/asset-001",
                completeness="complete",
            )
            ledger.register_asset(
                asset_id="asset-002",
                candidate_id="candidate-002",
                source_id="browser-bookmarks",
                content_type="article",
                original_url="https://example.com/article?utm_source=test",
                evidence_package_ref="gdrive://evidence/asset-002",
                completeness="complete",
                duplicate_of="asset-001",
            )

            assets = ledger.list_assets()
            self.assertEqual([asset["asset_id"] for asset in assets], ["asset-001", "asset-002"])
            self.assertEqual(assets[1]["duplicate_of"], "asset-001")

    def test_batch_candidates_are_idempotent_and_conflict_safe(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            ledger = Ledger(Path(temporary_directory) / "knowledge-assets.sqlite3")
            self.addCleanup(ledger.close)
            ledger.register_source(
                source_id="browser-bookmarks",
                platform="browser",
                collection="bookmarks",
                baseline_at="2026-07-14T00:00:00+08:00",
                scanned_total=2,
            )
            ledger.reconcile_source(
                "browser-bookmarks", included_total=2, excluded_total=0, blocked_total=0
            )
            candidates = [
                {
                    "candidate_id": "browser-bookmarks:item:000000",
                    "source_id": "browser-bookmarks",
                    "title": "第一篇",
                    "original_url": "https://example.com/1",
                    "preservation_signals": ["bookmark"],
                    "value_score": 100,
                    "decision": "included",
                    "decision_reason": "显式书签",
                },
                {
                    "candidate_id": "browser-bookmarks:item:000001",
                    "source_id": "browser-bookmarks",
                    "title": "第二篇",
                    "original_url": "https://example.com/2",
                    "preservation_signals": ["bookmark"],
                    "value_score": 100,
                    "decision": "included",
                    "decision_reason": "显式书签",
                },
            ]

            self.assertEqual(ledger.register_candidates_batch(candidates), 2)
            self.assertEqual(ledger.register_candidates_batch(candidates), 0)
            count = ledger.connection.execute("SELECT COUNT(*) FROM candidates").fetchone()[0]
            self.assertEqual(count, 2)

            conflicting = dict(candidates[0], title="不允许覆盖")
            with self.assertRaises(ValueError):
                ledger.register_candidates_batch([conflicting])

    def test_large_candidate_batch_uses_sqlite_safe_chunks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            ledger = Ledger(Path(temporary_directory) / "knowledge-assets.sqlite3")
            self.addCleanup(ledger.close)
            ledger.register_source(
                source_id="local-files",
                platform="local-files",
                collection="personal-roots",
                baseline_at="2026-07-14T00:00:00+08:00",
                scanned_total=1200,
            )
            ledger.reconcile_source(
                "local-files", included_total=0, excluded_total=0, blocked_total=1200
            )
            candidates = [
                {
                    "candidate_id": f"local-files:item:{index:08d}",
                    "source_id": "local-files",
                    "title": f"/tmp/file-{index}",
                    "original_url": None,
                    "preservation_signals": ["local-file", f"path:/tmp/file-{index}"],
                    "value_score": 0,
                    "decision": "blocked",
                    "decision_reason": "待价值判断",
                }
                for index in range(1200)
            ]
            self.assertEqual(ledger.register_candidates_batch(candidates), 1200)
            self.assertEqual(ledger.register_candidates_batch(candidates), 0)

    def test_review_queue_is_append_only_idempotent_and_auditable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            ledger = Ledger(Path(temporary_directory) / "knowledge-assets.sqlite3")
            self.addCleanup(ledger.close)
            ledger.register_source(
                source_id="browser-history",
                platform="browser",
                collection="history",
                baseline_at="2026-07-15T00:00:00+08:00",
                scanned_total=1,
            )
            ledger.register_candidate(
                candidate_id="history:item:000001",
                source_id="browser-history",
                title="可能有价值的页面",
                original_url="https://example.com/article",
                preservation_signals=["history"],
                value_score=55,
                decision="review",
                decision_reason="弱保存信号",
            )
            review = {
                "review_id": "review-history-000001-v001",
                "candidate_id": "history:item:000001",
                "asset_id": None,
                "reasons": ["low-confidence"],
                "flags": ["weak-signal"],
                "evidence_refs": ["data/history-value-scores.jsonl"],
                "status": "pending",
                "owner": None,
            }

            self.assertTrue(ledger.register_review_record(**review))
            self.assertFalse(ledger.register_review_record(**review))
            self.assertEqual(ledger.list_review_records()[0]["review_id"], review["review_id"])
            with self.assertRaises(ValueError):
                ledger.register_review_record(**(review | {"reasons": ["changed"]}))

    def test_answer_records_require_existing_evidence_assets_and_preserve_boundaries(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            ledger = Ledger(Path(temporary_directory) / "knowledge-assets.sqlite3")
            self.addCleanup(ledger.close)
            ledger.register_source(
                source_id="browser-bookmarks",
                platform="browser",
                collection="bookmarks",
                baseline_at="2026-07-15T00:00:00+08:00",
                scanned_total=1,
            )
            ledger.register_candidate(
                candidate_id="candidate-001",
                source_id="browser-bookmarks",
                title="证据文章",
                original_url="https://example.com/evidence",
                preservation_signals=["bookmark"],
                value_score=100,
                decision="included",
                decision_reason="显式书签",
            )
            ledger.register_asset(
                asset_id="asset-001",
                candidate_id="candidate-001",
                source_id="browser-bookmarks",
                content_type="article",
                original_url="https://example.com/evidence",
                evidence_package_ref="data/evidence/asset-001",
                completeness="complete",
            )
            answer = {
                "answer_id": "answer-001-v001",
                "question": "这条材料能支持什么结论？",
                "answer": "只能支持材料明确写出的范围。",
                "evidence_asset_ids": ["asset-001"],
                "coverage_statement": "只覆盖一个公开页面。",
                "conflicting_evidence": [],
                "confidence_boundary": "未覆盖其他来源。",
                "action_recommendations": ["补充独立来源"],
                "current_source_checks": [],
            }

            self.assertTrue(ledger.register_answer_record(**answer))
            self.assertFalse(ledger.register_answer_record(**answer))
            self.assertEqual(ledger.list_answer_records()[0]["coverage_statement"], answer["coverage_statement"])
            with self.assertRaises(KeyError):
                ledger.register_answer_record(
                    **(answer | {"answer_id": "answer-002-v001", "evidence_asset_ids": ["missing"]})
                )


if __name__ == "__main__":
    unittest.main()
