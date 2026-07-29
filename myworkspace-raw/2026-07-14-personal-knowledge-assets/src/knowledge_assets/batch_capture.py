from __future__ import annotations

import hashlib
import json
import multiprocessing
import os
import re
import tempfile
import threading
import time
from collections import OrderedDict
from concurrent.futures import Future, ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
from urllib.parse import urlparse

from .ledger import Ledger
from .public_capture import (
    FetchResult,
    UnsafePublicURLError,
    deterministic_asset_id,
    fetch_public_page,
    validate_public_url,
    write_public_capture,
)


MAX_WORKERS = 16
MAX_CACHE_BYTES = 256 * 1024 * 1024
MAX_RESPONSE_BYTES = 50 * 1024 * 1024
MAX_TIMEOUT_SECONDS = 120.0
MAX_BATCH_TIMEOUT_SECONDS = 3600.0


class BatchValidationError(ValueError):
    """Raised when an input is not an explicit, frozen public capture batch."""


class BatchConflictError(RuntimeError):
    """Raised when frozen input, evidence, or ledger state conflicts."""


Fetcher = Callable[..., FetchResult]


def _isolated_fetch_child(
    send_connection: object,
    fetcher: Fetcher,
    url: str,
    timeout_seconds: float,
    max_response_bytes: int,
) -> None:
    try:
        result = fetcher(
            url, timeout_seconds=timeout_seconds, max_bytes=max_response_bytes
        )
        send_connection.send(("ok", result))  # type: ignore[attr-defined]
    except BaseException as exc:
        try:
            send_connection.send(  # type: ignore[attr-defined]
                ("error", f"{type(exc).__name__}: {exc}")
            )
        except BaseException:
            pass
    finally:
        send_connection.close()  # type: ignore[attr-defined]


def _terminate_and_reap(process: multiprocessing.Process) -> None:
    if process.is_alive():
        process.terminate()
        process.join(0.2)
    if process.is_alive():
        process.kill()
        process.join()
    elif process.exitcode is None:
        process.join()


def _call_untrusted_fetcher_isolated(
    fetcher: Fetcher,
    url: str,
    *,
    timeout_seconds: float,
    max_response_bytes: int,
) -> FetchResult:
    """Run an untrusted injected fetcher behind a terminable POSIX process."""
    if os.name == "nt":
        raise RuntimeError(
            "untrusted-custom-fetcher-disabled-on-windows; use the default fetcher "
            "or an explicitly cooperative adapter"
        )
    # spawn never clones the caller's live threads or SQLite state and leaves
    # no persistent fork-server helper behind after the item finishes.
    # An unpicklable adapter is rejected and recorded as blocked instead of
    # falling back to an unsafe in-process call.
    context = multiprocessing.get_context("spawn")
    receive_connection, send_connection = context.Pipe(duplex=False)
    process = context.Process(
        target=_isolated_fetch_child,
        args=(send_connection, fetcher, url, timeout_seconds, max_response_bytes),
        name="isolated-public-fetch",
    )
    try:
        process.start()
    except BaseException:
        receive_connection.close()
        send_connection.close()
        process.close()
        raise
    send_connection.close()
    try:
        if not receive_connection.poll(timeout_seconds):
            raise TimeoutError(
                f"isolated-fetch-wall-clock-timeout-exceeded-{timeout_seconds}-seconds"
            )
        status, payload = receive_connection.recv()
        if status != "ok":
            raise RuntimeError(str(payload))
        if not isinstance(payload, FetchResult):
            raise TypeError("isolated fetcher must return FetchResult")
        return payload
    finally:
        receive_connection.close()
        _terminate_and_reap(process)


class _BoundedFetchCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.cache: OrderedDict[str, FetchResult] = OrderedDict()
        self.inflight: dict[str, Future[FetchResult]] = {}
        self.lock = threading.Lock()

    def get(
        self,
        url: str,
        *,
        fetcher: Fetcher,
        timeout_seconds: float,
        max_response_bytes: int,
    ) -> FetchResult:
        with self.lock:
            cached = self.cache.pop(url, None)
            if cached is not None:
                self.cache[url] = cached
                return cached
            future = self.inflight.get(url)
            owner = future is None
            if owner:
                future = Future()
                self.inflight[url] = future
        assert future is not None
        if not owner:
            return future.result()

        try:
            result = fetcher(
                url,
                timeout_seconds=timeout_seconds,
                max_bytes=max_response_bytes,
            )
            if not isinstance(result, FetchResult):
                raise TypeError("fetcher must return FetchResult")
            future.set_result(result)
            with self.lock:
                body_size = len(result.body)
                if self.capacity and body_size <= self.capacity:
                    while self.cache and self.size + body_size > self.capacity:
                        _, removed = self.cache.popitem(last=False)
                        self.size -= len(removed.body)
                    self.cache[url] = result
                    self.size += body_size
            return result
        except BaseException as exc:
            future.set_exception(exc)
            # Retrieve the exception here as well, avoiding an unobserved-Future warning
            # when there are no duplicate waiters.
            try:
                future.exception()
            finally:
                pass
            raise
        finally:
            with self.lock:
                self.inflight.pop(url, None)


def _validate_limits(
    *, max_workers: int, max_cache_bytes: int, max_response_bytes: int,
    timeout_seconds: float, batch_timeout_seconds: float,
) -> None:
    if not 1 <= max_workers <= MAX_WORKERS:
        raise BatchValidationError(f"max_workers must be between 1 and {MAX_WORKERS}")
    if not 0 <= max_cache_bytes <= MAX_CACHE_BYTES:
        raise BatchValidationError(f"max_cache_bytes must be between 0 and {MAX_CACHE_BYTES}")
    if not 1 <= max_response_bytes <= MAX_RESPONSE_BYTES:
        raise BatchValidationError(
            f"max_response_bytes must be between 1 and {MAX_RESPONSE_BYTES}"
        )
    if not 0 < timeout_seconds <= MAX_TIMEOUT_SECONDS:
        raise BatchValidationError(
            f"timeout_seconds must be greater than 0 and at most {MAX_TIMEOUT_SECONDS}"
        )
    if not 0 < batch_timeout_seconds <= MAX_BATCH_TIMEOUT_SECONDS:
        raise BatchValidationError(
            f"batch_timeout_seconds must be greater than 0 and at most {MAX_BATCH_TIMEOUT_SECONDS}"
        )


def _load_frozen_batch(batch_path: Path) -> tuple[dict[str, object], str]:
    path = Path(batch_path)
    if not path.is_file() or path.suffix.lower() != ".json":
        raise BatchValidationError("An explicit frozen batch JSON file is required")
    raw = path.read_bytes()
    try:
        batch = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise BatchValidationError(f"Invalid batch JSON: {exc}") from exc
    if not isinstance(batch, dict) or batch.get("schema_version") != 1:
        raise BatchValidationError("Unsupported or missing batch schema_version")
    batch_id = batch.get("batch_id")
    if not isinstance(batch_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,127}", batch_id):
        raise BatchValidationError("batch_id must be stable lowercase ASCII kebab-case")
    if batch.get("capture_status") != "pending":
        raise BatchValidationError("Frozen batch capture_status must be pending")
    if not isinstance(batch.get("created_at"), str) or not isinstance(
        batch.get("selection_rule"), str
    ):
        raise BatchValidationError("Frozen batch must record created_at and selection_rule")
    items = batch.get("items")
    if not isinstance(items, list) or not items:
        raise BatchValidationError("Frozen batch items must be a non-empty list")

    identities: dict[str, tuple[str, str, str]] = {}
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise BatchValidationError(f"Batch item {index} must be an object")
        required = {"candidate_id", "source_id", "title", "url", "capture_status"}
        missing = required.difference(item)
        if missing:
            raise BatchValidationError(f"Batch item {index} is missing {sorted(missing)}")
        if item["capture_status"] != "pending":
            raise BatchValidationError(f"Batch item {index} capture_status must be pending")
        if not all(isinstance(item[key], str) and item[key] for key in ("candidate_id", "source_id", "title", "url")):
            raise BatchValidationError(f"Batch item {index} contains an empty or non-string identity")
        try:
            validate_public_url(item["url"], resolve=False)
        except UnsafePublicURLError as exc:
            raise BatchValidationError(f"Batch item {index} URL is unsafe: {exc}") from exc
        identity = (item["source_id"], item["title"], item["url"])
        previous = identities.get(item["candidate_id"])
        if previous is not None:
            if previous != identity:
                raise BatchValidationError(
                    f"Conflicting duplicate candidate in batch: {item['candidate_id']}"
                )
            raise BatchValidationError(f"Duplicate candidate in batch: {item['candidate_id']}")
        identities[item["candidate_id"]] = identity
    return batch, hashlib.sha256(raw).hexdigest()


def _validate_candidates(batch: dict[str, object], ledger: Ledger) -> None:
    for item in batch["items"]:  # type: ignore[index]
        try:
            candidate = ledger.get_candidate(item["candidate_id"])
        except KeyError as exc:
            raise BatchConflictError(f"Unknown frozen candidate: {item['candidate_id']}") from exc
        if (
            candidate["source_id"] != item["source_id"]
            or candidate["title"] != item["title"]
            or candidate["original_url"] != item["url"]
            or candidate["decision"] != "included"
        ):
            raise BatchConflictError(
                f"Frozen batch conflicts with registered candidate: {item['candidate_id']}"
            )


def _verify_finalized_package(package_root: Path, item: dict[str, object]) -> dict[str, object] | None:
    if package_root.is_symlink():
        raise BatchConflictError(f"Evidence package root must not be a symbolic link: {package_root}")
    if not package_root.exists():
        return None
    manifest_path = package_root / "manifest.json"
    metadata_path = package_root / "metadata.json"
    checksum_path = package_root / "checksums.sha256"
    if not package_root.is_dir() or not all(path.is_file() for path in (manifest_path, metadata_path, checksum_path)):
        raise BatchConflictError(f"Evidence path is not a finalized package: {package_root}")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise BatchConflictError(f"Invalid finalized package: {package_root}") from exc
    asset_id = deterministic_asset_id(str(item["candidate_id"]))
    if (
        manifest.get("asset_id") != asset_id
        or manifest.get("source_id") != item["source_id"]
        or metadata.get("asset_id") != asset_id
        or metadata.get("candidate_id") != item["candidate_id"]
        or metadata.get("source_id") != item["source_id"]
        or metadata.get("title") != item["title"]
        or metadata.get("original_url") != item["url"]
    ):
        raise BatchConflictError(f"Finalized package identity conflict: {asset_id}")
    records = manifest.get("immutable_files")
    derived = manifest.get("derived_files")
    if not isinstance(records, list) or not isinstance(derived, list):
        raise BatchConflictError(f"Finalized package has no complete manifest file list: {asset_id}")
    for path in package_root.rglob("*"):
        if path.is_symlink():
            raise BatchConflictError(f"Finalized package contains symbolic links: {asset_id}")
    manifest_records: dict[str, dict[str, object]] = {}
    for record in records + derived:
        if not isinstance(record, dict) or not isinstance(record.get("path"), str):
            raise BatchConflictError(f"Malformed manifest file record: {asset_id}")
        relative = str(record["path"])
        path = Path(relative)
        if (
            path.is_absolute()
            or ".." in path.parts
            or "\\" in relative
            or path.as_posix() != relative
            or relative in manifest_records
        ):
            raise BatchConflictError(f"Unsafe or duplicate manifest path: {asset_id}/{relative}")
        target = package_root / path
        try:
            target.resolve(strict=True).relative_to(package_root.resolve(strict=True))
        except (OSError, ValueError) as exc:
            raise BatchConflictError(f"Manifest path escapes package: {asset_id}/{relative}") from exc
        if target.is_symlink() or not target.is_file():
            raise BatchConflictError(f"Manifest path is missing or symbolic: {asset_id}/{relative}")
        if not isinstance(record.get("sha256"), str) or not isinstance(record.get("byte_length"), int):
            raise BatchConflictError(f"Manifest lacks checksum metadata: {asset_id}/{relative}")
        manifest_records[relative] = record
    for record in derived:
        parent = record.get("parent")
        if not isinstance(parent, str) or parent not in manifest_records or parent == record["path"]:
            raise BatchConflictError(f"Derived-file parent conflict: {asset_id}/{record.get('path')}")
    required = {"metadata.json", "comments.json", "capture-log.json"}
    if manifest.get("completeness") in {"complete", "limited"}:
        required.add("source-response.bin")
    if not required.issubset(manifest_records):
        raise BatchConflictError(f"Finalized package lacks core files: {asset_id}")

    checksum_records: dict[str, str] = {}
    lines = checksum_path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise BatchConflictError(f"Empty checksum file in {asset_id}")
    for line in lines:
        try:
            expected, relative = line.split("  ", 1)
        except ValueError as exc:
            raise BatchConflictError(f"Malformed checksum record in {asset_id}") from exc
        if relative in checksum_records or not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise BatchConflictError(f"Duplicate or invalid checksum record in {asset_id}")
        checksum_records[relative] = expected
    if set(checksum_records) != set(manifest_records) | {"manifest.json"}:
        raise BatchConflictError(f"Manifest/checksum file-set conflict: {asset_id}")
    if hashlib.sha256(manifest_path.read_bytes()).hexdigest() != checksum_records["manifest.json"]:
        raise BatchConflictError(f"Finalized package manifest checksum conflict: {asset_id}")
    for relative, record in manifest_records.items():
        target = package_root / relative
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != checksum_records[relative] or actual != record["sha256"] or target.stat().st_size != record["byte_length"]:
            raise BatchConflictError(f"Finalized package checksum conflict: {asset_id}/{relative}")
    actual_files = {
        path.relative_to(package_root).as_posix()
        for path in package_root.rglob("*")
        if path.is_file()
    }
    expected_files = set(manifest_records) | {"manifest.json", "checksums.sha256"}
    if actual_files != expected_files:
        raise BatchConflictError(f"Finalized package contains unlisted or missing files: {asset_id}")
    return _result_item(item, package_root, manifest, metadata, run_status="replayed")


def _capture_one(
    item: dict[str, object],
    *,
    evidence_root: Path,
    result: FetchResult,
) -> dict[str, object]:
    asset_id = deterministic_asset_id(str(item["candidate_id"]))
    try:
        with tempfile.TemporaryDirectory(prefix="capture-stage-", dir=evidence_root) as temporary:
            stage_root = Path(temporary)
            _, staged_package = write_public_capture(
                result,
                root=stage_root,
                candidate_id=str(item["candidate_id"]),
                source_id=str(item["source_id"]),
                original_url=str(item["url"]),
                title=str(item["title"]),
            )
            final_root = evidence_root / asset_id
            if final_root.exists():
                replay = _verify_finalized_package(final_root, item)
                if replay is None:
                    raise BatchConflictError(f"Evidence package appeared concurrently: {asset_id}")
                return replay
            os.replace(staged_package, final_root)
    except BatchConflictError:
        raise
    except Exception as exc:
        blocked = FetchResult(
            requested_url=str(item["url"]),
            complete=False,
            error=f"capture-{type(exc).__name__}: {exc}",
        )
        with tempfile.TemporaryDirectory(prefix="capture-blocked-stage-", dir=evidence_root) as temporary:
            _, staged_package = write_public_capture(
                blocked,
                root=Path(temporary),
                candidate_id=str(item["candidate_id"]),
                source_id=str(item["source_id"]),
                original_url=str(item["url"]),
                title=str(item["title"]),
            )
            final_root = evidence_root / asset_id
            if final_root.exists():
                raise BatchConflictError(f"Refusing to replace existing evidence package: {asset_id}")
            os.replace(staged_package, final_root)

    manifest = json.loads((final_root / "manifest.json").read_text(encoding="utf-8"))
    metadata = json.loads((final_root / "metadata.json").read_text(encoding="utf-8"))
    return _result_item(item, final_root, manifest, metadata, run_status="captured")


def _result_item(
    item: dict[str, object],
    package_root: Path,
    manifest: dict[str, object],
    metadata: dict[str, object],
    *,
    run_status: str,
) -> dict[str, object]:
    capture_log = json.loads((package_root / "capture-log.json").read_text(encoding="utf-8"))
    package_ref = Path("data") / "evidence" / package_root.name
    return {
        "candidate_id": item["candidate_id"],
        "source_id": item["source_id"],
        "title": item["title"],
        "original_url": item["url"],
        "asset_id": manifest["asset_id"],
        "package_ref": package_ref.as_posix(),
        "completeness": manifest["completeness"],
        "run_status": run_status,
        "status_code": metadata.get("status_code"),
        "content_type": metadata.get("content_type"),
        "body_byte_length": metadata.get("body_byte_length", 0),
        "final_url": metadata.get("final_url"),
        "redirects": metadata.get("redirects", []),
        "complete_response": capture_log.get("complete_response", False),
        "error": capture_log.get("error"),
        "limitations": capture_log.get("limitations", []),
    }


def _write_versioned_result(data_directory: Path, batch_id: str, result: dict[str, object]) -> Path:
    for version in range(1, 10000):
        path = data_directory / f"capture-results-{batch_id}-v{version:03d}.json"
        result["result_id"] = path.stem
        encoded = (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        try:
            with path.open("xb") as handle:
                handle.write(encoded)
                handle.flush()
                os.fsync(handle.fileno())
            return path
        except FileExistsError:
            continue
    raise RuntimeError(f"No free result version for batch: {batch_id}")


def run_public_capture_batch(
    batch_path: Path,
    *,
    workspace: Path,
    fetcher: Fetcher = fetch_public_page,
    dry_run: bool = False,
    max_workers: int = 4,
    max_cache_bytes: int = 32 * 1024 * 1024,
    max_response_bytes: int = 10 * 1024 * 1024,
    timeout_seconds: float = 45.0,
    batch_timeout_seconds: float = 900.0,
) -> Path | dict[str, object]:
    """Capture one frozen public batch.

    ``batch_timeout_seconds`` is a network-capture budget only. Replay/hash
    verification, evidence packaging, ledger transactions, and result-file I/O
    are deliberately outside that budget and remain separately bounded by
    finite local inputs and atomic operations.
    """
    _validate_limits(
        max_workers=max_workers,
        max_cache_bytes=max_cache_bytes,
        max_response_bytes=max_response_bytes,
        timeout_seconds=timeout_seconds,
        batch_timeout_seconds=batch_timeout_seconds,
    )
    batch, batch_sha256 = _load_frozen_batch(Path(batch_path))
    workspace = Path(workspace).expanduser().resolve()
    data_directory = workspace / "data"
    database_path = data_directory / "knowledge-assets.sqlite3"
    if not database_path.is_file():
        raise BatchConflictError(f"Asset ledger does not exist: {database_path}")
    with Ledger(database_path, readonly=True) as ledger:
        _validate_candidates(batch, ledger)
    if dry_run:
        return {
            "status": "dry-run",
            "batch_id": batch["batch_id"],
            "source_batch_sha256": batch_sha256,
            "item_total": len(batch["items"]),
            "batch_timeout_seconds": batch_timeout_seconds,
            "batch_timeout_scope": "network-capture-only; excludes replay, hashing, evidence packaging, ledger, and result-file I/O",
        }

    evidence_root = data_directory / "evidence"
    evidence_root.mkdir(parents=True, exist_ok=True)
    items: list[dict[str, object]] = batch["items"]  # type: ignore[assignment]
    completed: dict[str, dict[str, object]] = {}
    pending: list[dict[str, object]] = []
    for item in items:
        asset_id = deterministic_asset_id(str(item["candidate_id"]))
        replay = _verify_finalized_package(evidence_root / asset_id, item)
        if replay is None:
            pending.append(item)
        else:
            completed[str(item["candidate_id"])] = replay

    cache = _BoundedFetchCache(max_cache_bytes)
    batch_deadline = time.monotonic() + batch_timeout_seconds
    untrusted_custom_fetcher = fetcher is not fetch_public_page and not getattr(
        fetcher, "_knowledge_assets_cooperative_timeout", False
    )

    def fetch_item(item: dict[str, object]) -> FetchResult:
        remaining = batch_deadline - time.monotonic()
        if remaining <= 0:
            return FetchResult(
                requested_url=str(item["url"]), complete=False,
                error=f"batch-wall-clock-deadline-exceeded-{batch_timeout_seconds}-seconds",
            )
        try:
            effective_fetcher = fetcher
            if untrusted_custom_fetcher:
                def effective_fetcher(
                    url: str, *, timeout_seconds: float, max_bytes: int
                ) -> FetchResult:
                    return _call_untrusted_fetcher_isolated(
                        fetcher,
                        url,
                        timeout_seconds=timeout_seconds,
                        max_response_bytes=max_bytes,
                    )
            return cache.get(
                str(item["url"]),
                fetcher=effective_fetcher,
                timeout_seconds=min(timeout_seconds, remaining),
                max_response_bytes=max_response_bytes,
            )
        except Exception as exc:
            return FetchResult(
                requested_url=str(item["url"]),
                complete=False,
                error=f"{type(exc).__name__}: {exc}",
            )

    if untrusted_custom_fetcher:
        # POSIX process creation happens on the caller's main thread, avoiding
        # unsafe fork-from-worker behavior. Untrusted adapters are intentionally
        # sequential; production/default capture retains bounded concurrency.
        for item in pending:
            completed[str(item["candidate_id"])] = _capture_one(
                item, evidence_root=evidence_root, result=fetch_item(item)
            )
    else:
        with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="public-capture") as executor:
            # Keep only one worker-sized response window alive. This bounds memory by
            # the response limit, worker count, and explicit cache budget rather than
            # by the total number of items in a large frozen batch.
            for start in range(0, len(pending), max_workers):
                window = pending[start : start + max_workers]
                futures = [(item, executor.submit(fetch_item, item)) for item in window]
                for item, future in futures:
                    completed[str(item["candidate_id"])] = _capture_one(
                        item,
                        evidence_root=evidence_root,
                        result=future.result(),
                    )

    ordered_results = [completed[str(item["candidate_id"])] for item in items]
    with Ledger(database_path) as ledger:
        try:
            ledger.register_assets_batch_idempotent(
                [
                    {
                        "asset_id": str(item["asset_id"]),
                        "candidate_id": str(item["candidate_id"]),
                        "source_id": str(item["source_id"]),
                        "content_type": str(item["content_type"] or "unknown"),
                        "original_url": str(item["original_url"]),
                        "evidence_package_ref": str(item["package_ref"]),
                        "completeness": str(item["completeness"]),
                        "duplicate_of": None,
                    }
                    for item in ordered_results
                ]
            )
        except (KeyError, ValueError) as exc:
            raise BatchConflictError(str(exc)) from exc

    counts = {name: 0 for name in ("complete", "limited", "blocked")}
    for item in ordered_results:
        counts[str(item["completeness"])] += 1
    result = {
        "schema_version": 1,
        "batch_id": batch["batch_id"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_batch_sha256": batch_sha256,
        "limits": {
            "max_workers": max_workers,
            "max_cache_bytes": max_cache_bytes,
            "max_response_bytes": max_response_bytes,
            "timeout_seconds": timeout_seconds,
            "batch_timeout_seconds": batch_timeout_seconds,
            "batch_timeout_scope": "network-capture-only; excludes replay, hashing, evidence packaging, ledger, and result-file I/O",
        },
        "counts": counts,
        "items": ordered_results,
    }
    return _write_versioned_result(data_directory, str(batch["batch_id"]), result)
