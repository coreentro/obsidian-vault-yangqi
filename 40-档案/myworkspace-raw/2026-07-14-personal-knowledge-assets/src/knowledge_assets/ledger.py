from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class ReconciliationError(ValueError):
    """Raised when source counts do not account for the full baseline."""


class Ledger:
    def __init__(self, database_path: Path, *, readonly: bool = False) -> None:
        self.database_path = Path(database_path)
        self.readonly = readonly
        if readonly:
            if not self.database_path.is_file():
                raise FileNotFoundError(self.database_path)
            self.connection = sqlite3.connect(
                f"file:{self.database_path.as_posix()}?mode=ro&immutable=1", uri=True
            )
        else:
            self.database_path.parent.mkdir(parents=True, exist_ok=True)
            self.connection = sqlite3.connect(self.database_path)
        self.connection.row_factory = sqlite3.Row
        if readonly:
            self.connection.execute("PRAGMA query_only = ON")
            return
        self.connection.executescript(
            """
            PRAGMA journal_mode = WAL;
            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS devices (
                device_id TEXT PRIMARY KEY,
                platform TEXT NOT NULL CHECK (platform IN ('macos', 'windows', 'ios', 'ipados', 'android')),
                device_name TEXT NOT NULL,
                browser_profiles_json TEXT NOT NULL,
                personal_roots_json TEXT NOT NULL,
                sync_services_json TEXT NOT NULL,
                verification_status TEXT NOT NULL CHECK (verification_status IN ('pending', 'verified', 'blocked')),
                verified_at TEXT,
                blocker TEXT
            );

            CREATE TABLE IF NOT EXISTS sources (
                source_id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                collection_name TEXT NOT NULL,
                baseline_at TEXT NOT NULL,
                scanned_total INTEGER NOT NULL CHECK (scanned_total >= 0),
                included_total INTEGER NOT NULL DEFAULT 0 CHECK (included_total >= 0),
                excluded_total INTEGER NOT NULL DEFAULT 0 CHECK (excluded_total >= 0),
                blocked_total INTEGER NOT NULL DEFAULT 0 CHECK (blocked_total >= 0),
                verification_status TEXT NOT NULL DEFAULT 'pending'
                    CHECK (verification_status IN ('pending', 'verified', 'blocked'))
            );

            CREATE TABLE IF NOT EXISTS audit_events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                entity_type TEXT NOT NULL,
                entity_id TEXT NOT NULL,
                event_type TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS candidates (
                candidate_id TEXT PRIMARY KEY,
                source_id TEXT NOT NULL REFERENCES sources(source_id),
                title TEXT NOT NULL,
                original_url TEXT,
                preservation_signals_json TEXT NOT NULL,
                value_score INTEGER NOT NULL CHECK (value_score BETWEEN 0 AND 100),
                decision TEXT NOT NULL CHECK (decision IN ('included', 'excluded', 'review', 'blocked')),
                decision_reason TEXT NOT NULL,
                asset_id TEXT
            );

            CREATE TABLE IF NOT EXISTS assets (
                asset_id TEXT PRIMARY KEY,
                candidate_id TEXT NOT NULL UNIQUE REFERENCES candidates(candidate_id),
                source_id TEXT NOT NULL REFERENCES sources(source_id),
                content_type TEXT NOT NULL,
                original_url TEXT,
                evidence_package_ref TEXT NOT NULL,
                completeness TEXT NOT NULL CHECK (completeness IN ('complete', 'limited', 'blocked')),
                duplicate_of TEXT REFERENCES assets(asset_id),
                captured_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS review_queue (
                review_id TEXT PRIMARY KEY,
                candidate_id TEXT REFERENCES candidates(candidate_id),
                asset_id TEXT REFERENCES assets(asset_id),
                reasons_json TEXT NOT NULL,
                flags_json TEXT NOT NULL,
                evidence_refs_json TEXT NOT NULL,
                status TEXT NOT NULL CHECK (status IN ('pending', 'reviewed', 'blocked')),
                owner TEXT,
                created_at TEXT NOT NULL,
                CHECK (candidate_id IS NOT NULL OR asset_id IS NOT NULL)
            );

            CREATE TABLE IF NOT EXISTS question_answers (
                answer_id TEXT PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                evidence_asset_ids_json TEXT NOT NULL,
                coverage_statement TEXT NOT NULL,
                conflicting_evidence_json TEXT NOT NULL,
                confidence_boundary TEXT NOT NULL,
                action_recommendations_json TEXT NOT NULL,
                current_source_checks_json TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
            """
        )

    def __enter__(self) -> "Ledger":
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        self.close()

    def close(self) -> None:
        self.connection.close()

    def register_device(
        self,
        *,
        device_id: str,
        platform: str,
        device_name: str,
        browser_profiles: list[str],
        personal_roots: list[str],
        sync_services: list[str],
        verification_status: str,
        blocker: str | None = None,
    ) -> None:
        verified_at = (
            datetime.now(timezone.utc).isoformat() if verification_status == "verified" else None
        )
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO devices (
                    device_id, platform, device_name, browser_profiles_json,
                    personal_roots_json, sync_services_json, verification_status,
                    verified_at, blocker
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    device_id,
                    platform,
                    device_name,
                    json.dumps(browser_profiles, ensure_ascii=False),
                    json.dumps(personal_roots, ensure_ascii=False),
                    json.dumps(sync_services, ensure_ascii=False),
                    verification_status,
                    verified_at,
                    blocker,
                ),
            )
            self._record_event(
                "device",
                device_id,
                "registered",
                {"platform": platform, "verification_status": verification_status},
            )

    def get_device(self, device_id: str) -> dict[str, Any]:
        row = self.connection.execute(
            "SELECT * FROM devices WHERE device_id = ?", (device_id,)
        ).fetchone()
        if row is None:
            raise KeyError(device_id)
        return dict(row)

    def register_source(
        self,
        *,
        source_id: str,
        platform: str,
        collection: str,
        baseline_at: str,
        scanned_total: int,
    ) -> None:
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO sources (
                    source_id, platform, collection_name, baseline_at, scanned_total
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (source_id, platform, collection, baseline_at, scanned_total),
            )
            self._record_event(
                "source",
                source_id,
                "registered",
                {"scanned_total": scanned_total, "baseline_at": baseline_at},
            )

    def reconcile_source(
        self,
        source_id: str,
        *,
        included_total: int,
        excluded_total: int,
        blocked_total: int,
    ) -> None:
        source = self.get_source(source_id)
        accounted = included_total + excluded_total + blocked_total
        if accounted != source["scanned_total"]:
            raise ReconciliationError(
                f"Source {source_id!r} scanned {source['scanned_total']} items but accounted for {accounted}"
            )
        status = "blocked" if blocked_total else "verified"
        with self.connection:
            self.connection.execute(
                """
                UPDATE sources
                SET included_total = ?, excluded_total = ?, blocked_total = ?, verification_status = ?
                WHERE source_id = ?
                """,
                (included_total, excluded_total, blocked_total, status, source_id),
            )
            self._record_event(
                "source",
                source_id,
                "reconciled",
                {
                    "included_total": included_total,
                    "excluded_total": excluded_total,
                    "blocked_total": blocked_total,
                    "verification_status": status,
                },
            )

    def get_source(self, source_id: str) -> dict[str, Any]:
        row = self.connection.execute(
            "SELECT * FROM sources WHERE source_id = ?", (source_id,)
        ).fetchone()
        if row is None:
            raise KeyError(source_id)
        return dict(row)

    def register_candidate(
        self,
        *,
        candidate_id: str,
        source_id: str,
        title: str,
        original_url: str | None,
        preservation_signals: list[str],
        value_score: int,
        decision: str,
        decision_reason: str,
    ) -> None:
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO candidates (
                    candidate_id, source_id, title, original_url,
                    preservation_signals_json, value_score, decision, decision_reason
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    candidate_id,
                    source_id,
                    title,
                    original_url,
                    json.dumps(preservation_signals, ensure_ascii=False),
                    value_score,
                    decision,
                    decision_reason,
                ),
            )
            self._record_event("candidate", candidate_id, "registered", {"decision": decision})

    def register_candidates_batch(self, candidates: list[dict[str, Any]]) -> int:
        """Register candidates without overwriting frozen records.

        Re-running an import with byte-for-byte equivalent records is a no-op. Any
        mismatch for an existing candidate id is treated as a conflict and aborts
        the whole batch, preserving the append-only audit boundary.
        """
        if not candidates:
            return 0

        normalized: dict[str, dict[str, Any]] = {}
        for candidate in candidates:
            required = {
                "candidate_id",
                "source_id",
                "title",
                "original_url",
                "preservation_signals",
                "value_score",
                "decision",
                "decision_reason",
            }
            missing = required.difference(candidate)
            if missing:
                raise ValueError(f"Candidate is missing fields: {sorted(missing)}")
            candidate_id = str(candidate["candidate_id"])
            record = {
                "candidate_id": candidate_id,
                "source_id": str(candidate["source_id"]),
                "title": str(candidate["title"]),
                "original_url": candidate["original_url"],
                "preservation_signals": list(candidate["preservation_signals"]),
                "value_score": int(candidate["value_score"]),
                "decision": str(candidate["decision"]),
                "decision_reason": str(candidate["decision_reason"]),
            }
            previous = normalized.get(candidate_id)
            if previous is not None and previous != record:
                raise ValueError(f"Conflicting candidate records in batch: {candidate_id}")
            normalized[candidate_id] = record

        source_ids = {record["source_id"] for record in normalized.values()}
        known_sources = {
            row["source_id"]
            for row in self.connection.execute(
                "SELECT source_id FROM sources WHERE source_id IN ({})".format(
                    ",".join("?" for _ in source_ids)
                ),
                tuple(source_ids),
            ).fetchall()
        } if source_ids else set()
        missing_sources = source_ids.difference(known_sources)
        if missing_sources:
            raise KeyError(f"Unknown candidate source(s): {sorted(missing_sources)}")

        existing: dict[str, sqlite3.Row] = {}
        candidate_ids = list(normalized)
        # SQLite builds have a finite bound-parameter limit (often 999). Query
        # in chunks so a large local-file inventory remains one logical batch.
        for start in range(0, len(candidate_ids), 500):
            chunk = candidate_ids[start : start + 500]
            placeholders = ",".join("?" for _ in chunk)
            rows = self.connection.execute(
                f"SELECT * FROM candidates WHERE candidate_id IN ({placeholders})",
                tuple(chunk),
            ).fetchall()
            existing.update({row["candidate_id"]: row for row in rows})

        def equivalent(row: sqlite3.Row, record: dict[str, Any]) -> bool:
            return (
                row["source_id"] == record["source_id"]
                and row["title"] == record["title"]
                and row["original_url"] == record["original_url"]
                and json.loads(row["preservation_signals_json"]) == record["preservation_signals"]
                and row["value_score"] == record["value_score"]
                and row["decision"] == record["decision"]
                and row["decision_reason"] == record["decision_reason"]
            )

        for candidate_id, record in normalized.items():
            row = existing.get(candidate_id)
            if row is not None and not equivalent(row, record):
                raise ValueError(f"Refusing to overwrite frozen candidate: {candidate_id}")

        new_records = [record for candidate_id, record in normalized.items() if candidate_id not in existing]
        with self.connection:
            for record in new_records:
                self.connection.execute(
                    """
                    INSERT INTO candidates (
                        candidate_id, source_id, title, original_url,
                        preservation_signals_json, value_score, decision, decision_reason
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        record["candidate_id"],
                        record["source_id"],
                        record["title"],
                        record["original_url"],
                        json.dumps(record["preservation_signals"], ensure_ascii=False),
                        record["value_score"],
                        record["decision"],
                        record["decision_reason"],
                    ),
                )
                self._record_event(
                    "candidate",
                    record["candidate_id"],
                    "registered",
                    {"decision": record["decision"], "batch": True},
                )
        return len(new_records)

    def register_asset(
        self,
        *,
        asset_id: str,
        candidate_id: str,
        source_id: str,
        content_type: str,
        original_url: str | None,
        evidence_package_ref: str,
        completeness: str,
        duplicate_of: str | None = None,
    ) -> None:
        captured_at = datetime.now(timezone.utc).isoformat()
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO assets (
                    asset_id, candidate_id, source_id, content_type, original_url,
                    evidence_package_ref, completeness, duplicate_of, captured_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    asset_id,
                    candidate_id,
                    source_id,
                    content_type,
                    original_url,
                    evidence_package_ref,
                    completeness,
                    duplicate_of,
                    captured_at,
                ),
            )
            self.connection.execute(
                "UPDATE candidates SET asset_id = ? WHERE candidate_id = ?",
                (asset_id, candidate_id),
            )
            self._record_event(
                "asset",
                asset_id,
                "registered",
                {"duplicate_of": duplicate_of, "completeness": completeness},
            )

    def get_candidate(self, candidate_id: str) -> dict[str, Any]:
        row = self.connection.execute(
            "SELECT * FROM candidates WHERE candidate_id = ?", (candidate_id,)
        ).fetchone()
        if row is None:
            raise KeyError(candidate_id)
        return dict(row)

    def register_asset_idempotent(
        self,
        *,
        asset_id: str,
        candidate_id: str,
        source_id: str,
        content_type: str,
        original_url: str | None,
        evidence_package_ref: str,
        completeness: str,
        duplicate_of: str | None = None,
    ) -> bool:
        """Register an immutable asset, replaying only an equivalent record.

        Returns ``True`` for a new record and ``False`` for an identical replay.
        Any reuse of the asset or candidate identity with different provenance is
        rejected before the candidate row is changed.
        """
        candidate = self.get_candidate(candidate_id)
        expected = {
            "asset_id": asset_id,
            "candidate_id": candidate_id,
            "source_id": source_id,
            "content_type": content_type,
            "original_url": original_url,
            "evidence_package_ref": evidence_package_ref,
            "completeness": completeness,
            "duplicate_of": duplicate_of,
        }
        if candidate["source_id"] != source_id or candidate["original_url"] != original_url:
            raise ValueError(f"Asset provenance conflicts with candidate: {candidate_id}")

        rows = self.connection.execute(
            "SELECT * FROM assets WHERE asset_id = ? OR candidate_id = ?",
            (asset_id, candidate_id),
        ).fetchall()
        if rows:
            if len(rows) != 1:
                raise ValueError(f"Conflicting asset identities for candidate: {candidate_id}")
            existing = dict(rows[0])
            if any(existing[key] != value for key, value in expected.items()):
                raise ValueError(f"Refusing conflicting asset registration: {asset_id}")
            if candidate["asset_id"] not in {None, asset_id}:
                raise ValueError(f"Candidate already references another asset: {candidate_id}")
            if candidate["asset_id"] is None:
                with self.connection:
                    self.connection.execute(
                        "UPDATE candidates SET asset_id = ? WHERE candidate_id = ?",
                        (asset_id, candidate_id),
                    )
            return False

        if candidate["asset_id"] not in {None, asset_id}:
            raise ValueError(f"Candidate already references another asset: {candidate_id}")
        self.register_asset(**expected)
        return True

    def register_assets_batch_idempotent(self, assets: list[dict[str, Any]]) -> int:
        """Preflight and register a whole asset batch in one SQLite transaction."""
        if not assets:
            return 0
        required = {
            "asset_id", "candidate_id", "source_id", "content_type", "original_url",
            "evidence_package_ref", "completeness", "duplicate_of",
        }
        normalized: dict[str, dict[str, Any]] = {}
        candidate_to_asset: dict[str, str] = {}
        for asset in assets:
            missing = required.difference(asset)
            if missing:
                raise ValueError(f"Asset is missing fields: {sorted(missing)}")
            record = {key: asset[key] for key in required}
            asset_id = str(record["asset_id"])
            candidate_id = str(record["candidate_id"])
            record.update(asset_id=asset_id, candidate_id=candidate_id)
            previous = normalized.get(asset_id)
            if previous is not None and previous != record:
                raise ValueError(f"Conflicting asset records in batch: {asset_id}")
            previous_asset = candidate_to_asset.get(candidate_id)
            if previous_asset is not None and previous_asset != asset_id:
                raise ValueError(f"Candidate appears with multiple assets: {candidate_id}")
            normalized[asset_id] = record
            candidate_to_asset[candidate_id] = asset_id

        candidate_rows: dict[str, sqlite3.Row] = {}
        candidate_ids = list(candidate_to_asset)
        for start in range(0, len(candidate_ids), 500):
            chunk = candidate_ids[start : start + 500]
            placeholders = ",".join("?" for _ in chunk)
            rows = self.connection.execute(
                f"SELECT * FROM candidates WHERE candidate_id IN ({placeholders})", tuple(chunk)
            ).fetchall()
            candidate_rows.update({row["candidate_id"]: row for row in rows})
        missing_candidates = set(candidate_ids).difference(candidate_rows)
        if missing_candidates:
            raise KeyError(f"Unknown asset candidate(s): {sorted(missing_candidates)}")

        asset_rows: dict[str, sqlite3.Row] = {}
        query_ids = list(normalized)
        for start in range(0, len(query_ids), 500):
            chunk = query_ids[start : start + 500]
            placeholders = ",".join("?" for _ in chunk)
            rows = self.connection.execute(
                f"SELECT * FROM assets WHERE asset_id IN ({placeholders})", tuple(chunk)
            ).fetchall()
            for row in rows:
                asset_rows[row["asset_id"]] = row
        for start in range(0, len(candidate_ids), 500):
            chunk = candidate_ids[start : start + 500]
            placeholders = ",".join("?" for _ in chunk)
            rows = self.connection.execute(
                f"SELECT * FROM assets WHERE candidate_id IN ({placeholders})", tuple(chunk)
            ).fetchall()
            for row in rows:
                asset_rows[row["asset_id"]] = row

        new_records: list[dict[str, Any]] = []
        for asset_id, record in normalized.items():
            candidate = candidate_rows[str(record["candidate_id"])]
            if candidate["source_id"] != record["source_id"] or candidate["original_url"] != record["original_url"]:
                raise ValueError(f"Asset provenance conflicts with candidate: {record['candidate_id']}")
            matching = [row for row in asset_rows.values() if row["asset_id"] == asset_id or row["candidate_id"] == record["candidate_id"]]
            if matching:
                if len(matching) != 1:
                    raise ValueError(f"Conflicting asset identities for candidate: {record['candidate_id']}")
                existing = matching[0]
                if any(existing[key] != value for key, value in record.items()):
                    raise ValueError(f"Refusing conflicting asset registration: {asset_id}")
            else:
                new_records.append(record)
            if candidate["asset_id"] not in {None, asset_id}:
                raise ValueError(f"Candidate already references another asset: {record['candidate_id']}")

        with self.connection:
            for record in new_records:
                captured_at = datetime.now(timezone.utc).isoformat()
                self.connection.execute(
                    """
                    INSERT INTO assets (
                        asset_id, candidate_id, source_id, content_type, original_url,
                        evidence_package_ref, completeness, duplicate_of, captured_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        record["asset_id"], record["candidate_id"], record["source_id"],
                        record["content_type"], record["original_url"], record["evidence_package_ref"],
                        record["completeness"], record["duplicate_of"], captured_at,
                    ),
                )
                self.connection.execute(
                    "UPDATE candidates SET asset_id = ? WHERE candidate_id = ?",
                    (record["asset_id"], record["candidate_id"]),
                )
                self._record_event(
                    "asset", str(record["asset_id"]), "registered",
                    {"duplicate_of": record["duplicate_of"], "completeness": record["completeness"], "batch": True},
                )
            for asset_id, record in normalized.items():
                if candidate_rows[str(record["candidate_id"])]["asset_id"] is None:
                    self.connection.execute(
                        "UPDATE candidates SET asset_id = ? WHERE candidate_id = ?",
                        (asset_id, record["candidate_id"]),
                    )
        return len(new_records)

    def list_assets(self) -> list[dict[str, Any]]:
        rows = self.connection.execute("SELECT * FROM assets ORDER BY asset_id").fetchall()
        return [dict(row) for row in rows]

    def register_review_record(
        self,
        *,
        review_id: str,
        candidate_id: str | None,
        asset_id: str | None,
        reasons: list[str],
        flags: list[str],
        evidence_refs: list[str],
        status: str,
        owner: str | None,
    ) -> bool:
        if candidate_id is None and asset_id is None:
            raise ValueError("Review record requires a candidate_id or asset_id")
        if candidate_id is not None:
            self.get_candidate(candidate_id)
        if asset_id is not None and self.connection.execute(
            "SELECT 1 FROM assets WHERE asset_id = ?", (asset_id,)
        ).fetchone() is None:
            raise KeyError(asset_id)
        record = {
            "candidate_id": candidate_id,
            "asset_id": asset_id,
            "reasons": list(reasons),
            "flags": list(flags),
            "evidence_refs": list(evidence_refs),
            "status": status,
            "owner": owner,
        }
        existing = self.connection.execute(
            "SELECT * FROM review_queue WHERE review_id = ?", (review_id,)
        ).fetchone()
        if existing is not None:
            equivalent = (
                existing["candidate_id"] == record["candidate_id"]
                and existing["asset_id"] == record["asset_id"]
                and json.loads(existing["reasons_json"]) == record["reasons"]
                and json.loads(existing["flags_json"]) == record["flags"]
                and json.loads(existing["evidence_refs_json"]) == record["evidence_refs"]
                and existing["status"] == record["status"]
                and existing["owner"] == record["owner"]
            )
            if not equivalent:
                raise ValueError(f"Refusing to overwrite review record: {review_id}")
            return False
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO review_queue (
                    review_id, candidate_id, asset_id, reasons_json, flags_json,
                    evidence_refs_json, status, owner, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    review_id,
                    candidate_id,
                    asset_id,
                    json.dumps(reasons, ensure_ascii=False),
                    json.dumps(flags, ensure_ascii=False),
                    json.dumps(evidence_refs, ensure_ascii=False),
                    status,
                    owner,
                    datetime.now(timezone.utc).isoformat(),
                ),
            )
            self._record_event(
                "review",
                review_id,
                "registered",
                {"candidate_id": candidate_id, "asset_id": asset_id, "status": status},
            )
        return True

    def list_review_records(self) -> list[dict[str, Any]]:
        rows = self.connection.execute(
            "SELECT * FROM review_queue ORDER BY review_id"
        ).fetchall()
        return [dict(row) for row in rows]

    def register_answer_record(
        self,
        *,
        answer_id: str,
        question: str,
        answer: str,
        evidence_asset_ids: list[str],
        coverage_statement: str,
        conflicting_evidence: list[str],
        confidence_boundary: str,
        action_recommendations: list[str],
        current_source_checks: list[str],
    ) -> bool:
        if not evidence_asset_ids:
            raise ValueError("Answer record requires at least one evidence asset")
        known_assets = {
            row["asset_id"]
            for row in self.connection.execute(
                "SELECT asset_id FROM assets WHERE asset_id IN ({})".format(
                    ",".join("?" for _ in evidence_asset_ids)
                ),
                tuple(evidence_asset_ids),
            ).fetchall()
        }
        missing = set(evidence_asset_ids).difference(known_assets)
        if missing:
            raise KeyError(f"Unknown evidence asset(s): {sorted(missing)}")
        record = {
            "question": question,
            "answer": answer,
            "evidence_asset_ids": list(evidence_asset_ids),
            "coverage_statement": coverage_statement,
            "conflicting_evidence": list(conflicting_evidence),
            "confidence_boundary": confidence_boundary,
            "action_recommendations": list(action_recommendations),
            "current_source_checks": list(current_source_checks),
        }
        existing = self.connection.execute(
            "SELECT * FROM question_answers WHERE answer_id = ?", (answer_id,)
        ).fetchone()
        if existing is not None:
            equivalent = (
                existing["question"] == question
                and existing["answer"] == answer
                and json.loads(existing["evidence_asset_ids_json"]) == evidence_asset_ids
                and existing["coverage_statement"] == coverage_statement
                and json.loads(existing["conflicting_evidence_json"]) == conflicting_evidence
                and existing["confidence_boundary"] == confidence_boundary
                and json.loads(existing["action_recommendations_json"]) == action_recommendations
                and json.loads(existing["current_source_checks_json"]) == current_source_checks
            )
            if not equivalent:
                raise ValueError(f"Refusing to overwrite answer record: {answer_id}")
            return False
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO question_answers (
                    answer_id, question, answer, evidence_asset_ids_json,
                    coverage_statement, conflicting_evidence_json,
                    confidence_boundary, action_recommendations_json,
                    current_source_checks_json, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    answer_id,
                    question,
                    answer,
                    json.dumps(evidence_asset_ids, ensure_ascii=False),
                    coverage_statement,
                    json.dumps(conflicting_evidence, ensure_ascii=False),
                    confidence_boundary,
                    json.dumps(action_recommendations, ensure_ascii=False),
                    json.dumps(current_source_checks, ensure_ascii=False),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )
            self._record_event(
                "answer",
                answer_id,
                "registered",
                {"evidence_asset_ids": evidence_asset_ids},
            )
        return True

    def list_answer_records(self) -> list[dict[str, Any]]:
        rows = self.connection.execute(
            "SELECT * FROM question_answers ORDER BY answer_id"
        ).fetchall()
        return [dict(row) for row in rows]

    def _record_event(
        self,
        entity_type: str,
        entity_id: str,
        event_type: str,
        payload: dict[str, Any],
    ) -> None:
        self.connection.execute(
            """
            INSERT INTO audit_events (
                entity_type, entity_id, event_type, payload_json, created_at
            ) VALUES (?, ?, ?, ?, ?)
            """,
            (
                entity_type,
                entity_id,
                event_type,
                json.dumps(payload, ensure_ascii=False, sort_keys=True),
                datetime.now(timezone.utc).isoformat(),
            ),
        )
