from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any


class IndexConflictError(RuntimeError):
    """Raised when an indexed source would be silently replaced."""


class SearchIndex:
    def __init__(self, database_path: Path) -> None:
        self.database_path = Path(database_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.database_path)
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(
            """
            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS documents (
                asset_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                source_text TEXT NOT NULL,
                author TEXT,
                platform TEXT NOT NULL,
                topics_json TEXT NOT NULL,
                evidence_ref TEXT NOT NULL,
                content_hash TEXT NOT NULL
            );

            CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(
                asset_id UNINDEXED,
                title,
                source_text,
                author,
                platform,
                topics,
                tokenize='trigram'
            );

            CREATE TABLE IF NOT EXISTS document_aliases (
                asset_id TEXT PRIMARY KEY REFERENCES documents(asset_id),
                aliases_json TEXT NOT NULL,
                content_hash TEXT NOT NULL
            );

            CREATE VIRTUAL TABLE IF NOT EXISTS document_aliases_fts USING fts5(
                asset_id UNINDEXED,
                aliases,
                tokenize='trigram'
            );

            CREATE TABLE IF NOT EXISTS document_alias_additions (
                asset_id TEXT NOT NULL REFERENCES documents(asset_id),
                alias TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                PRIMARY KEY (asset_id, alias)
            );

            CREATE VIRTUAL TABLE IF NOT EXISTS document_alias_additions_fts USING fts5(
                asset_id UNINDEXED,
                alias,
                tokenize='trigram'
            );
            """
        )

    def __enter__(self) -> "SearchIndex":
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        self.close()

    def close(self) -> None:
        self.connection.close()

    def add_asset(
        self,
        *,
        asset_id: str,
        title: str,
        source_text: str,
        author: str | None,
        platform: str,
        topics: list[str],
        evidence_ref: str,
    ) -> None:
        topics_json = json.dumps(topics, ensure_ascii=False)
        fingerprint_payload = json.dumps(
            {
                "title": title,
                "source_text": source_text,
                "author": author,
                "platform": platform,
                "topics": topics,
                "evidence_ref": evidence_ref,
            },
            ensure_ascii=False,
            sort_keys=True,
        ).encode("utf-8")
        content_hash = hashlib.sha256(fingerprint_payload).hexdigest()
        existing = self.connection.execute(
            "SELECT content_hash FROM documents WHERE asset_id = ?", (asset_id,)
        ).fetchone()
        if existing is not None:
            if existing["content_hash"] != content_hash:
                raise IndexConflictError(f"Refusing to replace indexed source for {asset_id}")
            return
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO documents (
                    asset_id, title, source_text, author, platform,
                    topics_json, evidence_ref, content_hash
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    asset_id,
                    title,
                    source_text,
                    author,
                    platform,
                    topics_json,
                    evidence_ref,
                    content_hash,
                ),
            )
            self.connection.execute(
                """
                INSERT INTO documents_fts (
                    asset_id, title, source_text, author, platform, topics
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (asset_id, title, source_text, author or "", platform, " ".join(topics)),
            )

    def add_aliases(self, *, asset_id: str, aliases: list[str]) -> None:
        if not aliases or any(not isinstance(alias, str) or not alias.strip() for alias in aliases):
            raise ValueError("Aliases must contain at least one non-empty string")
        if self.connection.execute(
            "SELECT 1 FROM documents WHERE asset_id = ?", (asset_id,)
        ).fetchone() is None:
            raise KeyError(asset_id)
        normalized = list(dict.fromkeys(alias.strip() for alias in aliases))
        aliases_json = json.dumps(normalized, ensure_ascii=False)
        content_hash = hashlib.sha256(aliases_json.encode("utf-8")).hexdigest()
        existing = self.connection.execute(
            "SELECT content_hash FROM document_aliases WHERE asset_id = ?", (asset_id,)
        ).fetchone()
        if existing is not None:
            if existing["content_hash"] != content_hash:
                raise IndexConflictError(f"Refusing to replace aliases for {asset_id}")
            return
        with self.connection:
            self.connection.execute(
                "INSERT INTO document_aliases (asset_id, aliases_json, content_hash) VALUES (?, ?, ?)",
                (asset_id, aliases_json, content_hash),
            )
            self.connection.execute(
                "INSERT INTO document_aliases_fts (asset_id, aliases) VALUES (?, ?)",
                (asset_id, " ".join(normalized)),
            )

    def extend_aliases(self, *, asset_id: str, aliases: list[str]) -> None:
        """Append new retrieval aliases without changing the frozen base alias set."""
        if not aliases or any(not isinstance(alias, str) or not alias.strip() for alias in aliases):
            raise ValueError("Aliases must contain at least one non-empty string")
        if self.connection.execute(
            "SELECT 1 FROM documents WHERE asset_id = ?", (asset_id,)
        ).fetchone() is None:
            raise KeyError(asset_id)
        normalized = list(dict.fromkeys(alias.strip() for alias in aliases))
        with self.connection:
            for alias in normalized:
                content_hash = hashlib.sha256(alias.encode("utf-8")).hexdigest()
                inserted = self.connection.execute(
                    """
                    INSERT OR IGNORE INTO document_alias_additions (asset_id, alias, content_hash)
                    VALUES (?, ?, ?)
                    """,
                    (asset_id, alias, content_hash),
                ).rowcount
                if inserted:
                    self.connection.execute(
                        "INSERT INTO document_alias_additions_fts (asset_id, alias) VALUES (?, ?)",
                        (asset_id, alias),
                    )

    def search(self, query: str, *, limit: int = 20) -> list[dict[str, Any]]:
        terms = _trigram_terms(query)
        rows: list[sqlite3.Row] = []
        if terms:
            match_query = " OR ".join(f'"{term}"' for term in terms)
            rows = self.connection.execute(
                """
                SELECT d.*, bm25(documents_fts) AS rank
                FROM documents_fts
                JOIN documents AS d ON d.asset_id = documents_fts.asset_id
                WHERE documents_fts MATCH ?
                ORDER BY rank, d.asset_id
                LIMIT ?
                """,
                (match_query, limit),
            ).fetchall()
        if not rows:
            recall_terms = _recall_terms(query)
            if not recall_terms:
                return []
            clauses = []
            score_parts = []
            score_parameters: list[str] = []
            where_parameters: list[str] = []
            for term in recall_terms:
                clauses.append(
                    "(title LIKE ? ESCAPE '\\' OR source_text LIKE ? ESCAPE '\\' "
                    "OR topics_json LIKE ? ESCAPE '\\')"
                )
                score_parts.append(
                    "(CASE WHEN title LIKE ? ESCAPE '\\' THEN 3 ELSE 0 END + "
                    "CASE WHEN source_text LIKE ? ESCAPE '\\' THEN 1 ELSE 0 END + "
                    "CASE WHEN topics_json LIKE ? ESCAPE '\\' THEN 2 ELSE 0 END)"
                )
                pattern = f"%{_escape_like(term)}%"
                score_parameters.extend((pattern, pattern, pattern))
                where_parameters.extend((pattern, pattern, pattern))
            parameters: list[str | int] = score_parameters + where_parameters + [limit]
            rows = self.connection.execute(
                f"""
                SELECT ranked.*, -ranked.recall_score AS rank
                FROM (
                    SELECT documents.*, ({' + '.join(score_parts)}) AS recall_score
                    FROM documents
                    WHERE {' OR '.join(clauses)}
                ) AS ranked
                ORDER BY recall_score DESC, asset_id
                LIMIT ?
                """,
                parameters,
            ).fetchall()
        alias_rows = self._search_aliases(query, limit=limit)
        combined: list[dict[str, Any]] = []
        seen: set[str] = set()
        for row in alias_rows + rows:
            record = dict(row)
            if record["asset_id"] in seen:
                continue
            seen.add(record["asset_id"])
            combined.append(record)
            if len(combined) == limit:
                break
        return combined

    def _search_aliases(self, query: str, *, limit: int) -> list[sqlite3.Row]:
        addition_rows = self._search_alias_additions(query, limit=limit)
        if addition_rows:
            return addition_rows
        terms = _trigram_terms(query)
        rows: list[sqlite3.Row] = []
        if terms:
            match_query = " OR ".join(f'"{term}"' for term in terms)
            rows = self.connection.execute(
                """
                SELECT d.*, bm25(document_aliases_fts) - 100 AS rank
                FROM document_aliases_fts
                JOIN documents AS d ON d.asset_id = document_aliases_fts.asset_id
                WHERE document_aliases_fts MATCH ?
                ORDER BY rank, d.asset_id
                LIMIT ?
                """,
                (match_query, limit),
            ).fetchall()
        if rows:
            return rows
        recall_terms = _recall_terms(query)
        if not recall_terms:
            return []
        clauses = []
        score_parts = []
        score_parameters: list[str] = []
        where_parameters: list[str] = []
        for term in recall_terms:
            clauses.append("a.aliases_json LIKE ? ESCAPE '\\'")
            score_parts.append("CASE WHEN a.aliases_json LIKE ? ESCAPE '\\' THEN 2 ELSE 0 END")
            pattern = f"%{_escape_like(term)}%"
            score_parameters.append(pattern)
            where_parameters.append(pattern)
        parameters: list[str | int] = score_parameters + where_parameters + [limit]
        return self.connection.execute(
            f"""
            SELECT d.*, -100 - ({' + '.join(score_parts)}) AS rank
            FROM document_aliases AS a
            JOIN documents AS d ON d.asset_id = a.asset_id
            WHERE {' OR '.join(clauses)}
            ORDER BY rank, d.asset_id
            LIMIT ?
            """,
            parameters,
        ).fetchall()

    def _search_alias_additions(self, query: str, *, limit: int) -> list[sqlite3.Row]:
        terms = _trigram_terms(query)
        if terms:
            match_query = " OR ".join(f'"{term}"' for term in terms)
            rows = self.connection.execute(
                """
                SELECT d.*, bm25(document_alias_additions_fts) - 200 AS rank
                FROM document_alias_additions_fts
                JOIN documents AS d ON d.asset_id = document_alias_additions_fts.asset_id
                WHERE document_alias_additions_fts MATCH ?
                ORDER BY rank, d.asset_id
                LIMIT ?
                """,
                (match_query, limit),
            ).fetchall()
            if rows:
                return rows
        recall_terms = _recall_terms(query)
        if not recall_terms:
            return []
        clauses = []
        score_parts = []
        score_parameters: list[str] = []
        where_parameters: list[str] = []
        for term in recall_terms:
            clauses.append("a.alias LIKE ? ESCAPE '\\'")
            score_parts.append("CASE WHEN a.alias LIKE ? ESCAPE '\\' THEN 2 ELSE 0 END")
            pattern = f"%{_escape_like(term)}%"
            score_parameters.append(pattern)
            where_parameters.append(pattern)
        parameters: list[str | int] = score_parameters + where_parameters + [limit]
        return self.connection.execute(
            f"""
            SELECT d.*, -200 - ({' + '.join(score_parts)}) AS rank
            FROM document_alias_additions AS a
            JOIN documents AS d ON d.asset_id = a.asset_id
            WHERE {' OR '.join(clauses)}
            ORDER BY rank, d.asset_id
            LIMIT ?
            """,
            parameters,
        ).fetchall()


def _trigram_terms(query: str) -> list[str]:
    compact = "".join(query.split())
    if len(compact) < 3:
        return []
    return list(dict.fromkeys(compact[index : index + 3] for index in range(len(compact) - 2)))


def _recall_terms(query: str) -> list[str]:
    compact = "".join(query.split())
    if not compact:
        return []
    if len(compact) <= 2:
        return [compact]
    return list(dict.fromkeys(compact[index : index + 2] for index in range(len(compact) - 1)))


def _escape_like(value: str) -> str:
    return value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
