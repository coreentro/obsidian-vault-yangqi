#!/usr/bin/env python3
"""Read-only health check for the rebuildable local search index.

The checker never mutates the index or evidence packages.  It records counts,
SQLite integrity, source-text preservation checks, and a few deterministic
recall probes in a new JSON report.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=Path, default=Path("data/search-index.sqlite3"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    index = args.index
    if not index.is_file():
        raise SystemExit(f"index not found: {index}")

    # URI mode read-only connection prevents accidental writes, including WAL setup.
    uri = f"file:{index.resolve()}?mode=ro"
    with sqlite3.connect(uri, uri=True) as db:
        db.row_factory = sqlite3.Row
        integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
        documents = db.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        aliases = db.execute("SELECT COUNT(*) FROM document_aliases").fetchone()[0]
        additions = db.execute("SELECT COUNT(*) FROM document_alias_additions").fetchone()[0]
        empty_sources = db.execute(
            "SELECT COUNT(*) FROM documents WHERE length(source_text) = 0"
        ).fetchone()[0]
        missing_fts = db.execute(
            """SELECT COUNT(*) FROM documents d
               WHERE NOT EXISTS (SELECT 1 FROM documents_fts f WHERE f.asset_id = d.asset_id)"""
        ).fetchone()[0]
        probes = {}
        for query in ("知识库", "搜索能力", "硫空位 光催化制氢"):
            terms = [query[i : i + 3] for i in range(max(0, len(query) - 2))]
            match = " OR ".join(f'"{term}"' for term in terms if term.strip())
            rows = db.execute(
                "SELECT asset_id FROM documents_fts WHERE documents_fts MATCH ? LIMIT 5",
                (match or '"__empty__"',),
            ).fetchall()
            alias_rows = db.execute(
                "SELECT asset_id FROM document_aliases_fts WHERE document_aliases_fts MATCH ? LIMIT 5",
                (match or '"__empty__"',),
            ).fetchall()
            addition_rows = db.execute(
                "SELECT asset_id FROM document_alias_additions_fts WHERE document_alias_additions_fts MATCH ? LIMIT 5",
                (match or '"__empty__"',),
            ).fetchall()
            probes[query] = {
                "document_hits": [r[0] for r in rows],
                "alias_hits": [r[0] for r in alias_rows],
                "append_only_alias_hits": [r[0] for r in addition_rows],
            }

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "index": str(index),
        "index_sha256": hashlib.sha256(index.read_bytes()).hexdigest(),
        "read_only": True,
        "sqlite_integrity": integrity,
        "counts": {"documents": documents, "base_aliases": aliases, "alias_additions": additions},
        "preservation_checks": {"empty_source_text": empty_sources, "documents_missing_fts": missing_fts},
        "probes": probes,
        "status": "pass" if integrity == "ok" and empty_sources == 0 and missing_fts == 0 else "attention",
    }
    output = args.output or index.parent / f"local-index-verification-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
