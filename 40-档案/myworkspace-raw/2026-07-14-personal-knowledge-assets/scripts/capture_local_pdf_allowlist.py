from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from knowledge_assets.ledger import Ledger
from knowledge_assets.local_file_capture import LocalFileCapture
from knowledge_assets.search import SearchIndex


def build_review_id(candidate_id: str, review_version: str) -> str:
    if re.fullmatch(r"v[0-9]{3}", review_version) is None:
        raise ValueError("review_version must use the form v001")
    return f"review-{candidate_id.replace(':', '-')}-pdf-{review_version}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allowlist", type=Path, required=True)
    parser.add_argument("--assessment", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--search-index", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--review-version", default="v002")
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
    extracted_for_index: dict[str, str] = {}
    with Ledger(args.ledger) as ledger, SearchIndex(args.search_index) as search:
        for candidate_id in sorted(allowed):
            frozen = allowed[candidate_id]
            decision = assessed[candidate_id]
            candidate = ledger.get_candidate(candidate_id)
            result = capturer.capture_pdf(
                candidate_id=candidate_id,
                source_id=candidate["source_id"],
                source_path=Path(frozen["path"]),
                frozen_sha256=frozen["sha256"],
                frozen_byte_length=frozen["byte_length"],
                title=decision["title"],
                visually_reviewed_pages=decision["visually_reviewed_pages"],
                additional_limitations=decision.get("additional_limitations", []),
            )
            evidence_ref = result.package_path.as_posix()
            manifest = json.loads((result.package_path / "manifest.json").read_text(encoding="utf-8"))
            completeness = manifest["completeness"]
            assets.append(
                {
                    "asset_id": result.asset_id,
                    "candidate_id": candidate_id,
                    "source_id": candidate["source_id"],
                    "content_type": "local-scholarly-pdf",
                    "original_url": candidate["original_url"],
                    "evidence_package_ref": evidence_ref,
                    "completeness": completeness,
                    "duplicate_of": None,
                }
            )
            extracted_for_index[result.asset_id] = result.source_text
            results.append(
                {
                    "asset_id": result.asset_id,
                    "candidate_id": candidate_id,
                    "title": decision["title"],
                    "authors": decision["authors"],
                    "source_path": frozen["path"],
                    "source_sha256": result.source_sha256,
                    "source_byte_length": result.source_byte_length,
                    "page_count": decision["page_count"],
                    "extracted_text_characters": decision["extracted_text_characters"],
                    "visually_reviewed_pages": decision["visually_reviewed_pages"],
                    "value_score": decision["value_score"],
                    "topics": decision["topics"],
                    "completeness": completeness,
                    "evidence_package_ref": evidence_ref,
                }
            )

        inserted = ledger.register_assets_batch_idempotent(assets)
        for item in results:
            search.add_asset(
                asset_id=item["asset_id"],
                title=item["title"],
                source_text=extracted_for_index[item["asset_id"]],
                author=item["authors"],
                platform="local-pdf",
                topics=item["topics"],
                evidence_ref=item["evidence_package_ref"],
            )
            ledger.register_review_record(
                review_id=build_review_id(item["candidate_id"], args.review_version),
                candidate_id=item["candidate_id"],
                asset_id=item["asset_id"],
                reasons=["complete-pdf-reviewed", "accepted-as-reusable-chemistry-knowledge"],
                flags=["non-sensitive", "frozen-hash-verified", "source-pdf-preserved-completely", "visual-sample-verified"],
                evidence_refs=[args.allowlist.as_posix(), args.assessment.as_posix(), item["evidence_package_ref"]],
                status="reviewed",
                owner="ai-pdf-content-review",
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
