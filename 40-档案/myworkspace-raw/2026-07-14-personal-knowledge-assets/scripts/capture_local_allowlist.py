from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from knowledge_assets.ledger import Ledger
from knowledge_assets.local_file_capture import LocalFileCapture
from knowledge_assets.search import SearchIndex


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allowlist", type=Path, required=True)
    parser.add_argument("--assessment", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--search-index", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    allowlist = json.loads(args.allowlist.read_text(encoding="utf-8"))
    assessment = json.loads(args.assessment.read_text(encoding="utf-8"))
    allowed = {item["candidate_id"]: item for item in allowlist["items"]}
    assessed = {item["candidate_id"]: item for item in assessment["items"]}
    if set(allowed) != set(assessed):
        raise ValueError("Allowlist and assessment candidate sets differ")
    if any(item["decision"] != "accepted" or item["safety_hits"] for item in assessed.values()):
        raise ValueError("Only accepted items with no safety hits may be captured")

    capturer = LocalFileCapture(args.evidence_root, max_file_bytes=allowlist["limits"]["per_file_bytes"])
    results = []
    assets = []
    with Ledger(args.ledger) as ledger, SearchIndex(args.search_index) as search:
        for candidate_id in sorted(allowed):
            frozen = allowed[candidate_id]
            decision = assessed[candidate_id]
            candidate = ledger.get_candidate(candidate_id)
            result = capturer.capture_plain_text(
                candidate_id=candidate_id,
                source_id=candidate["source_id"],
                source_path=Path(frozen["path"]),
                frozen_sha256=frozen["sha256"],
                frozen_byte_length=frozen["byte_length"],
                title=decision["title"],
            )
            evidence_ref = result.package_path.as_posix()
            assets.append(
                {
                    "asset_id": result.asset_id,
                    "candidate_id": candidate_id,
                    "source_id": candidate["source_id"],
                    "content_type": "local-text-document",
                    "original_url": candidate["original_url"],
                    "evidence_package_ref": evidence_ref,
                    "completeness": "complete",
                    "duplicate_of": None,
                }
            )
            search.add_asset(
                asset_id=result.asset_id,
                title=decision["title"],
                source_text=result.source_text,
                author=None,
                platform="local-file",
                topics=decision["topics"],
                evidence_ref=evidence_ref,
            )
            results.append(
                {
                    "asset_id": result.asset_id,
                    "candidate_id": candidate_id,
                    "title": decision["title"],
                    "source_path": frozen["path"],
                    "source_sha256": result.source_sha256,
                    "source_byte_length": result.source_byte_length,
                    "value_score": decision["value_score"],
                    "topics": decision["topics"],
                    "completeness": "complete",
                    "evidence_package_ref": evidence_ref,
                }
            )
        inserted = ledger.register_assets_batch_idempotent(assets)
        for item in results:
            ledger.register_review_record(
                review_id=f"review-{item['candidate_id'].replace(':', '-')}-v002",
                candidate_id=item["candidate_id"],
                asset_id=item["asset_id"],
                reasons=["complete-content-reviewed", "accepted-as-reusable-knowledge"],
                flags=["non-sensitive", "frozen-hash-verified", "source-preserved-completely"],
                evidence_refs=[args.allowlist.as_posix(), args.assessment.as_posix(), item["evidence_package_ref"]],
                status="reviewed",
                owner="ai-content-review",
            )

    payload = {
        "schema_version": 1,
        "created_at": assessment["created_at"],
        "allowlist": args.allowlist.as_posix(),
        "assessment": args.assessment.as_posix(),
        "captured_total": len(results),
        "ledger_assets_in_batch": len(assets),
        "results": results,
    }
    encoded = (json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists() and args.output.read_bytes() != encoded:
        raise RuntimeError(f"Refusing to overwrite batch result: {args.output}")
    if not args.output.exists():
        args.output.write_bytes(encoded)
    print(json.dumps({"captured_total": len(results), "new_ledger_assets": inserted, "output_sha256": hashlib.sha256(encoded).hexdigest()}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
