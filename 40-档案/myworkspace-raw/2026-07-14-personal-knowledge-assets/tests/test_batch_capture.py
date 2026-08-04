import hashlib
import io
import json
import multiprocessing
import tempfile
import threading
import time
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from knowledge_assets.batch_capture import (
    BatchConflictError,
    BatchValidationError,
    run_public_capture_batch,
)
from knowledge_assets.cli import main
from knowledge_assets.ledger import Ledger
from knowledge_assets.public_capture import FetchResult, deterministic_asset_id


class RecordingFetcher:
    _knowledge_assets_cooperative_timeout = True
    def __init__(self, outcomes: dict[str, FetchResult | BaseException]) -> None:
        self.outcomes = outcomes
        self.calls: list[tuple[str, float, int]] = []
        self.active = 0
        self.max_active = 0
        self.lock = threading.Lock()

    def __call__(self, url: str, *, timeout_seconds: float, max_bytes: int) -> FetchResult:
        with self.lock:
            self.calls.append((url, timeout_seconds, max_bytes))
            self.active += 1
            self.max_active = max(self.max_active, self.active)
        try:
            time.sleep(0.01)
            outcome = self.outcomes[url]
            if isinstance(outcome, BaseException):
                raise outcome
            return outcome
        finally:
            with self.lock:
                self.active -= 1


class SlowFetcher:
    _knowledge_assets_cooperative_timeout = True
    def __call__(self, url: str, *, timeout_seconds: float, max_bytes: int) -> FetchResult:
        time.sleep(timeout_seconds)
        return FetchResult(
            requested_url=url,
            final_url=url,
            complete=False,
            error=f"wall-clock-timeout-exceeded-{timeout_seconds}-seconds",
        )


class BudgetAwareFetcher:
    _knowledge_assets_cooperative_timeout = True
    def __init__(self) -> None:
        self.timeouts: list[float] = []

    def __call__(self, url: str, *, timeout_seconds: float, max_bytes: int) -> FetchResult:
        self.timeouts.append(timeout_seconds)
        duration = min(0.04, timeout_seconds)
        time.sleep(duration)
        if timeout_seconds < 0.04:
            return FetchResult(
                requested_url=url, complete=False, error="wall-clock-deadline-exceeded"
            )
        return FetchResult(
            requested_url=url, final_url=url, status_code=200,
            content_type="text/html", body=b"<html><body>ok</body></html>", complete=True,
        )


class HungFetcher:
    def __call__(self, url: str, *, timeout_seconds: float, max_bytes: int) -> FetchResult:
        while True:
            time.sleep(1)


class PublicCaptureBatchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.workspace = self.root / "workspace"
        self.batch_path = self.root / "frozen-batch.json"
        self.items = [
            {
                "candidate_id": "candidate-001",
                "source_id": "source-001",
                "title": "第一篇",
                "url": "https://example.com/one",
                "capture_status": "pending",
            },
            {
                "candidate_id": "candidate-002",
                "source_id": "source-001",
                "title": "第二篇",
                "url": "https://example.com/two",
                "capture_status": "pending",
            },
        ]
        self._write_batch(self.items)
        self._seed_ledger(self.items)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _write_batch(self, items: list[dict[str, object]]) -> None:
        self.batch_path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "batch_id": "capture-batch-test-2026-07-15",
                    "created_at": "2026-07-15T00:00:00+00:00",
                    "selection_rule": "public HTTP(S) pages only",
                    "capture_status": "pending",
                    "items": items,
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    def _seed_ledger(self, items: list[dict[str, object]]) -> None:
        database = self.workspace / "data" / "knowledge-assets.sqlite3"
        with Ledger(database) as ledger:
            ledger.register_source(
                source_id="source-001",
                platform="browser",
                collection="bookmarks",
                baseline_at="2026-07-15T00:00:00+00:00",
                scanned_total=len(items),
            )
            ledger.reconcile_source(
                "source-001", included_total=len(items), excluded_total=0, blocked_total=0
            )
            ledger.register_candidates_batch(
                [
                    {
                        "candidate_id": item["candidate_id"],
                        "source_id": item["source_id"],
                        "title": item["title"],
                        "original_url": item["url"],
                        "preservation_signals": ["bookmark"],
                        "value_score": 80,
                        "decision": "included",
                        "decision_reason": "explicit bookmark",
                    }
                    for item in items
                ]
            )

    def test_continues_after_fetch_exception_and_writes_versioned_result(self) -> None:
        fetcher = RecordingFetcher(
            {
                "https://example.com/one": FetchResult(
                    requested_url="https://example.com/one",
                    final_url="https://example.com/one",
                    status_code=200,
                    content_type="text/html",
                    body=b"<html><body>complete article</body></html>",
                    complete=True,
                ),
                "https://example.com/two": RuntimeError("simulated fetch failure"),
            }
        )

        first = run_public_capture_batch(
            self.batch_path,
            workspace=self.workspace,
            fetcher=fetcher,
            max_workers=2,
            max_cache_bytes=1024,
            max_response_bytes=512,
        )
        second = run_public_capture_batch(
            self.batch_path,
            workspace=self.workspace,
            fetcher=RecordingFetcher({}),
            max_workers=1,
            max_cache_bytes=0,
            max_response_bytes=512,
        )

        self.assertNotEqual(first, second)
        self.assertEqual(first.name, "capture-results-capture-batch-test-2026-07-15-v001.json")
        self.assertEqual(second.name, "capture-results-capture-batch-test-2026-07-15-v002.json")
        first_result = json.loads(first.read_text(encoding="utf-8"))
        self.assertEqual([item["completeness"] for item in first_result["items"]], ["complete", "blocked"])
        self.assertEqual(
            first_result["items"][0]["package_ref"],
            f"data/evidence/{deterministic_asset_id('candidate-001')}",
        )
        self.assertIn("RuntimeError", first_result["items"][1]["error"])
        self.assertEqual(first_result["source_batch_sha256"], hashlib.sha256(self.batch_path.read_bytes()).hexdigest())
        self.assertEqual(fetcher.max_active, 2)
        self.assertTrue(all(call[2] == 512 for call in fetcher.calls))
        with Ledger(self.workspace / "data" / "knowledge-assets.sqlite3") as ledger:
            self.assertEqual(len(ledger.list_assets()), 2)

    def test_replay_skips_identical_finalized_packages_without_fetching(self) -> None:
        fetcher = RecordingFetcher(
            {
                item["url"]: FetchResult(
                    requested_url=str(item["url"]),
                    final_url=str(item["url"]),
                    status_code=200,
                    content_type="text/html",
                    body=f"<html><body>{item['title']}</body></html>".encode(),
                    complete=True,
                )
                for item in self.items
            }
        )
        run_public_capture_batch(self.batch_path, workspace=self.workspace, fetcher=fetcher)
        metadata_path = (
            self.workspace
            / "data"
            / "evidence"
            / deterministic_asset_id("candidate-001")
            / "metadata.json"
        )
        original_metadata = metadata_path.read_bytes()
        replay_fetcher = RecordingFetcher({})

        result_path = run_public_capture_batch(
            self.batch_path, workspace=self.workspace, fetcher=replay_fetcher
        )

        result = json.loads(result_path.read_text(encoding="utf-8"))
        self.assertEqual(replay_fetcher.calls, [])
        self.assertEqual([item["run_status"] for item in result["items"]], ["replayed", "replayed"])
        self.assertEqual(metadata_path.read_bytes(), original_metadata)

    def test_rejects_conflicting_finalized_package(self) -> None:
        asset_root = (
            self.workspace
            / "data"
            / "evidence"
            / deterministic_asset_id("candidate-001")
        )
        asset_root.mkdir(parents=True)
        (asset_root / "manifest.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "asset_id": deterministic_asset_id("candidate-001"),
                    "source_id": "different-source",
                    "created_at": "2026-07-15T00:00:00+00:00",
                    "completeness": "complete",
                    "immutable_files": [],
                    "derived_files": [],
                }
            ),
            encoding="utf-8",
        )

        with self.assertRaises(BatchConflictError):
            run_public_capture_batch(
                self.batch_path, workspace=self.workspace, fetcher=RecordingFetcher({})
            )

    def test_dry_run_validates_but_does_not_fetch_or_write(self) -> None:
        fetcher = RecordingFetcher({})

        plan = run_public_capture_batch(
            self.batch_path, workspace=self.workspace, fetcher=fetcher, dry_run=True
        )

        self.assertEqual(plan["status"], "dry-run")
        self.assertEqual(plan["item_total"], 2)
        self.assertEqual(fetcher.calls, [])
        self.assertFalse((self.workspace / "data" / "evidence").exists())
        self.assertFalse((self.workspace / "data" / "capture-results-capture-batch-test-2026-07-15-v001.json").exists())

    def test_dry_run_does_not_change_database_or_create_sidecars(self) -> None:
        database = self.workspace / "data" / "knowledge-assets.sqlite3"
        before = database.read_bytes()
        before_names = sorted(path.name for path in database.parent.iterdir())
        run_public_capture_batch(
            self.batch_path,
            workspace=self.workspace,
            fetcher=RecordingFetcher({}),
            dry_run=True,
        )
        self.assertEqual(database.read_bytes(), before)
        self.assertEqual(sorted(path.name for path in database.parent.iterdir()), before_names)

    def test_replay_rejects_empty_checksum_list_unlisted_extra_and_symlink(self) -> None:
        fetcher = RecordingFetcher(
            {
                item["url"]: FetchResult(
                    requested_url=str(item["url"]), final_url=str(item["url"]),
                    status_code=200, content_type="text/html", body=b"<html><body>x</body></html>", complete=True,
                )
                for item in self.items
            }
        )
        run_public_capture_batch(self.batch_path, workspace=self.workspace, fetcher=fetcher)
        package = self.workspace / "data" / "evidence" / deterministic_asset_id("candidate-001")
        (package / "checksums.sha256").write_text("", encoding="utf-8")
        with self.assertRaises(BatchConflictError):
            run_public_capture_batch(self.batch_path, workspace=self.workspace, fetcher=RecordingFetcher({}))

        # Restore by using the untouched second package, then prove extra files are rejected.
        package = self.workspace / "data" / "evidence" / deterministic_asset_id("candidate-002")
        (package / "unlisted.txt").write_text("extra", encoding="utf-8")
        with self.assertRaises(BatchConflictError):
            run_public_capture_batch(self.batch_path, workspace=self.workspace, fetcher=RecordingFetcher({}))

    def test_asset_registration_batch_is_atomic_on_late_conflict(self) -> None:
        database = self.workspace / "data" / "knowledge-assets.sqlite3"
        with Ledger(database) as ledger:
            records = [
                {
                    "asset_id": deterministic_asset_id(str(item["candidate_id"])),
                    "candidate_id": str(item["candidate_id"]),
                    "source_id": str(item["source_id"]),
                    "content_type": "text/html",
                    "original_url": str(item["url"]),
                    "evidence_package_ref": f"data/evidence/{deterministic_asset_id(str(item['candidate_id']))}",
                    "completeness": "complete",
                    "duplicate_of": None,
                }
                for item in self.items
            ]
            records[1]["source_id"] = "wrong-source"
            with self.assertRaises(ValueError):
                ledger.register_assets_batch_idempotent(records)
            self.assertEqual(ledger.list_assets(), [])
            self.assertTrue(all(ledger.get_candidate(str(item["candidate_id"]))["asset_id"] is None for item in self.items))

    def test_rejects_non_frozen_or_unsafe_batch_before_fetching(self) -> None:
        unsafe_items = [dict(self.items[0], url="file:///etc/passwd")]
        self._write_batch(unsafe_items)
        fetcher = RecordingFetcher({})

        with self.assertRaises(BatchValidationError):
            run_public_capture_batch(self.batch_path, workspace=self.workspace, fetcher=fetcher)

        self.assertEqual(fetcher.calls, [])

    def test_bounded_cache_reuses_duplicate_public_response(self) -> None:
        duplicate_items = [dict(item, url="https://example.com/shared") for item in self.items]
        self._write_batch(duplicate_items)
        (self.workspace / "data" / "knowledge-assets.sqlite3").unlink()
        self._seed_ledger(duplicate_items)
        fetcher = RecordingFetcher(
            {
                "https://example.com/shared": FetchResult(
                    requested_url="https://example.com/shared",
                    final_url="https://example.com/shared",
                    status_code=200,
                    content_type="text/html",
                    body=b"<html><body>shared</body></html>",
                    complete=True,
                )
            }
        )

        run_public_capture_batch(
            self.batch_path,
            workspace=self.workspace,
            fetcher=fetcher,
            max_workers=2,
            max_cache_bytes=1024,
        )

        self.assertEqual(len(fetcher.calls), 1)

    def test_wall_clock_timeout_returns_blocked_without_waiting_for_slow_fetcher(self) -> None:
        started = time.monotonic()
        result_path = run_public_capture_batch(
            self.batch_path,
            workspace=self.workspace,
            fetcher=SlowFetcher(),
            max_workers=2,
            timeout_seconds=0.05,
        )
        elapsed = time.monotonic() - started
        result = json.loads(result_path.read_text(encoding="utf-8"))
        self.assertLess(elapsed, 0.2)
        self.assertEqual(result["counts"]["blocked"], 2)
        self.assertTrue(all("wall-clock" in str(item["error"]) for item in result["items"]))
        self.assertFalse(any(thread.name == "bounded-public-fetch" for thread in threading.enumerate()))

    def test_replay_rejects_package_root_symlink(self) -> None:
        evidence = self.workspace / "data" / "evidence"
        evidence.mkdir(parents=True)
        real = self.root / "outside-package"
        real.mkdir()
        (evidence / deterministic_asset_id("candidate-001")).symlink_to(real, target_is_directory=True)
        with self.assertRaises(BatchConflictError):
            run_public_capture_batch(
                self.batch_path, workspace=self.workspace, fetcher=RecordingFetcher({})
            )

    def test_rejects_invalid_batch_total_deadline(self) -> None:
        with self.assertRaises(BatchValidationError):
            run_public_capture_batch(
                self.batch_path,
                workspace=self.workspace,
                fetcher=RecordingFetcher({}),
                batch_timeout_seconds=0,
            )

    def test_batch_deadline_bounds_sequential_item_timeouts(self) -> None:
        third = {
            "candidate_id": "candidate-003", "source_id": "source-001",
            "title": "第三篇", "url": "https://example.com/three", "capture_status": "pending",
        }
        items = self.items + [third]
        self._write_batch(items)
        database = self.workspace / "data" / "knowledge-assets.sqlite3"
        database.unlink()
        self._seed_ledger(items)
        fetcher = BudgetAwareFetcher()
        started = time.monotonic()
        result_path = run_public_capture_batch(
            self.batch_path, workspace=self.workspace, fetcher=fetcher,
            max_workers=1, timeout_seconds=0.1, batch_timeout_seconds=0.06,
        )
        elapsed = time.monotonic() - started
        result = json.loads(result_path.read_text(encoding="utf-8"))
        self.assertLess(elapsed, 0.16)
        self.assertGreaterEqual(result["counts"]["blocked"], 1)
        self.assertTrue(all(timeout <= 0.06 for timeout in fetcher.timeouts))
        self.assertTrue(all(
            later <= earlier for earlier, later in zip(fetcher.timeouts, fetcher.timeouts[1:])
        ))

    @unittest.skipIf(__import__("os").name == "nt", "POSIX isolation test")
    def test_uncooperative_custom_fetcher_is_terminated_without_residual_workers(self) -> None:
        children_before = {child.pid for child in multiprocessing.active_children()}
        started = time.monotonic()
        result_path = run_public_capture_batch(
            self.batch_path, workspace=self.workspace, fetcher=HungFetcher(),
            max_workers=2, timeout_seconds=0.05, batch_timeout_seconds=0.08,
        )
        elapsed = time.monotonic() - started
        result = json.loads(result_path.read_text(encoding="utf-8"))
        self.assertLess(elapsed, 0.3)
        self.assertEqual(result["counts"]["blocked"], 2)
        self.assertTrue(all(
            "wall-clock" in str(item["error"]) for item in result["items"]
        ))
        self.assertTrue(any(
            "isolated-fetch-wall-clock" in str(item["error"]) for item in result["items"]
        ))
        self.assertEqual(
            {child.pid for child in multiprocessing.active_children()}, children_before
        )
        self.assertFalse(any(thread.name == "bounded-public-fetch" for thread in threading.enumerate()))

    def test_cli_exposes_bounded_dry_run_without_network_or_evidence_writes(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main(
                [
                    "capture-public-batch",
                    "--workspace",
                    str(self.workspace),
                    "--batch",
                    str(self.batch_path),
                    "--dry-run",
                    "--max-workers",
                    "2",
                    "--max-cache-bytes",
                    "2048",
                    "--max-response-bytes",
                    "4096",
                    "--timeout-seconds",
                    "5",
                ]
            )

        self.assertEqual(exit_code, 0)
        self.assertEqual(json.loads(output.getvalue())["status"], "dry-run")
        self.assertFalse((self.workspace / "data" / "evidence").exists())


if __name__ == "__main__":
    unittest.main()
