from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_legacy_correction(package: Path, corrections_root: Path) -> Path:
    """Create an external correction record without changing a legacy package."""
    package = Path(package)
    if not package.is_dir() or not (package / "manifest.json").is_file():
        raise ValueError(f"Not a legacy evidence package: {package}")
    asset_id = package.name
    output = Path(corrections_root) / asset_id
    output.mkdir(parents=True, exist_ok=False)

    files = []
    for path in sorted(package.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Legacy package contains a symbolic link: {path}")
        if path.is_file():
            files.append(
                {
                    "path": path.relative_to(package).as_posix(),
                    "byte_length": path.stat().st_size,
                    "sha256": _sha256(path),
                }
            )

    correction = {
        "schema_version": 2,
        "record_type": "external-legacy-correction",
        "asset_id": asset_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "legacy_package_ref": package.as_posix(),
        "legacy_package_files": files,
        "role_corrections": {
            "source.html": "decoded-or-normalized response representation; not guaranteed byte-identical to the HTTP body",
            "source.md": "derived visible-text reading layer; does not replace the captured response representation",
            "comments.json": "collection-scope record; an empty/not-collected value is not evidence that the source had no comments",
        },
        "limitations": [
            "The legacy package did not preserve separately verifiable raw HTTP response bytes.",
            "The historical response-body SHA recorded in metadata cannot always be recomputed from the legacy package.",
            "Comments, embedded media, dynamic state, login-only content, and inaccessible material may be absent as recorded in the legacy capture log.",
        ],
        "preservation_policy": "This correction is additive and external. No legacy package file was edited, deleted, renamed, or replaced.",
    }
    manifest = output / "manifest-v2.json"
    manifest.write_text(
        json.dumps(correction, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (output / "checksums.sha256").write_text(
        f"{_sha256(manifest)}  manifest-v2.json\n", encoding="utf-8"
    )
    return output
