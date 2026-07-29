from __future__ import annotations

import argparse
import json
from pathlib import Path

from .batch_capture import run_public_capture_batch
from .browser import write_chromium_inventory
from .candidates import build_browser_candidates, build_local_file_candidates, load_inventory
from .inventory import scan_personal_roots, write_inventory_manifest
from .ledger import Ledger
from .search import SearchIndex


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="knowledge-assets")
    commands = parser.add_subparsers(dest="command", required=True)

    initialize = commands.add_parser("init", help="Initialize local control and search databases")
    initialize.add_argument("--workspace", type=Path, required=True)

    scan = commands.add_parser("scan-local", help="Create a read-only frozen local file inventory")
    scan.add_argument("--workspace", type=Path, required=True)
    scan.add_argument("--device-id", required=True)
    scan.add_argument("--baseline-at", required=True)
    scan.add_argument("--root", type=Path, action="append", required=True)
    scan.add_argument("--exclude", type=Path, action="append", default=[])
    scan.add_argument("--output", type=Path, required=True)

    browser = commands.add_parser(
        "scan-chromium", help="Create a read-only frozen Chromium bookmark and history inventory"
    )
    browser.add_argument("--workspace", type=Path, required=True)
    browser.add_argument("--profile-id", required=True)
    browser.add_argument("--baseline-at", required=True)
    browser.add_argument("--bookmarks", type=Path, required=True)
    browser.add_argument("--history", type=Path, required=True)
    browser.add_argument("--output", type=Path, required=True)

    device = commands.add_parser("register-device", help="Register a verified or blocked device boundary")
    device.add_argument("--workspace", type=Path, required=True)
    device.add_argument("--device-id", required=True)
    device.add_argument("--platform", choices=["macos", "windows", "ios", "ipados", "android"], required=True)
    device.add_argument("--device-name", required=True)
    device.add_argument("--browser-profile", action="append", default=[])
    device.add_argument("--personal-root", action="append", default=[])
    device.add_argument("--sync-service", action="append", default=[])
    device.add_argument("--status", choices=["pending", "verified", "blocked"], required=True)
    device.add_argument("--blocker")

    source = commands.add_parser(
        "register-inventory-source",
        help="Register a frozen inventory as a source with all undecided items blocked",
    )
    source.add_argument("--workspace", type=Path, required=True)
    source.add_argument("--source-id", required=True)
    source.add_argument("--platform", required=True)
    source.add_argument("--collection", required=True)
    source.add_argument("--inventory", type=Path, required=True)

    browser_source = commands.add_parser(
        "register-browser-inventory",
        help="Register bookmark and history source counts from a frozen browser inventory",
    )
    browser_source.add_argument("--workspace", type=Path, required=True)
    browser_source.add_argument("--inventory", type=Path, required=True)

    seed = commands.add_parser(
        "seed-candidates",
        help="Register immutable candidate records from a frozen inventory",
    )
    seed.add_argument("--workspace", type=Path, required=True)
    seed.add_argument("--inventory", type=Path, required=True)

    capture = commands.add_parser(
        "capture-public-batch",
        help="Capture one explicit frozen batch of public HTTP(S) bookmarks",
    )
    capture.add_argument("--workspace", type=Path, required=True)
    capture.add_argument("--batch", type=Path, required=True)
    capture.add_argument("--dry-run", action="store_true")
    capture.add_argument("--max-workers", type=int, default=4)
    capture.add_argument("--max-cache-bytes", type=int, default=32 * 1024 * 1024)
    capture.add_argument("--max-response-bytes", type=int, default=10 * 1024 * 1024)
    capture.add_argument("--timeout-seconds", type=float, default=45.0)
    capture.add_argument(
        "--batch-timeout-seconds", type=float, default=900.0,
        help="Network-capture budget only; excludes replay, hashing, ledger, and local writes",
    )
    return parser


def main(arguments: list[str] | None = None) -> int:
    options = build_parser().parse_args(arguments)
    workspace = options.workspace.expanduser().resolve()
    data_directory = workspace / "data"
    if options.command != "capture-public-batch":
        data_directory.mkdir(parents=True, exist_ok=True)
    if options.command == "init":
        with Ledger(data_directory / "knowledge-assets.sqlite3"):
            pass
        with SearchIndex(data_directory / "search-index.sqlite3"):
            pass
        print(json.dumps({"status": "initialized", "workspace": str(workspace)}, ensure_ascii=False))
        return 0
    if options.command == "scan-local":
        candidates = scan_personal_roots(
            options.root,
            device_id=options.device_id,
            exclude_roots=options.exclude,
        )
        output = write_inventory_manifest(
            options.output,
            device_id=options.device_id,
            baseline_at=options.baseline_at,
            roots=options.root,
            candidates=candidates,
            exclude_roots=options.exclude,
        )
        print(
            json.dumps(
                {
                    "status": "inventory-created",
                    "device_id": options.device_id,
                    "scanned_total": len(candidates),
                    "output": str(output),
                },
                ensure_ascii=False,
            )
        )
        return 0
    if options.command == "scan-chromium":
        output = write_chromium_inventory(
            options.output,
            profile_id=options.profile_id,
            baseline_at=options.baseline_at,
            bookmarks_path=options.bookmarks,
            history_path=options.history,
        )
        inventory = json.loads(output.read_text(encoding="utf-8"))
        print(
            json.dumps(
                {
                    "status": "browser-inventory-created",
                    "profile_id": options.profile_id,
                    "bookmarks_total": inventory["bookmarks_total"],
                    "history_total": inventory["history_total"],
                    "content_candidates_total": inventory["content_candidates_total"],
                    "output": str(output),
                },
                ensure_ascii=False,
            )
        )
        return 0
    if options.command == "register-device":
        with Ledger(data_directory / "knowledge-assets.sqlite3") as ledger:
            ledger.register_device(
                device_id=options.device_id,
                platform=options.platform,
                device_name=options.device_name,
                browser_profiles=options.browser_profile,
                personal_roots=options.personal_root,
                sync_services=options.sync_service,
                verification_status=options.status,
                blocker=options.blocker,
            )
        print(json.dumps({"status": "device-registered", "device_id": options.device_id}))
        return 0
    if options.command == "register-inventory-source":
        inventory = json.loads(options.inventory.read_text(encoding="utf-8"))
        scanned_total = int(inventory["scanned_total"])
        with Ledger(data_directory / "knowledge-assets.sqlite3") as ledger:
            ledger.register_source(
                source_id=options.source_id,
                platform=options.platform,
                collection=options.collection,
                baseline_at=inventory["baseline_at"],
                scanned_total=scanned_total,
            )
            ledger.reconcile_source(
                options.source_id,
                included_total=0,
                excluded_total=0,
                blocked_total=scanned_total,
            )
        print(
            json.dumps(
                {
                    "status": "source-registered",
                    "source_id": options.source_id,
                    "scanned_total": scanned_total,
                    "blocked_total": scanned_total,
                },
                ensure_ascii=False,
            )
        )
        return 0
    if options.command == "register-browser-inventory":
        inventory = json.loads(options.inventory.read_text(encoding="utf-8"))
        profile_id = inventory["profile_id"]
        platform = profile_id.split("-", 1)[0]
        bookmarks_total = int(inventory["bookmarks_total"])
        history_total = int(inventory["history_total"])
        history_candidates = int(inventory["content_candidates_total"])
        with Ledger(data_directory / "knowledge-assets.sqlite3") as ledger:
            bookmark_source_id = f"{profile_id}-bookmarks"
            ledger.register_source(
                source_id=bookmark_source_id,
                platform=platform,
                collection="bookmarks",
                baseline_at=inventory["baseline_at"],
                scanned_total=bookmarks_total,
            )
            ledger.reconcile_source(
                bookmark_source_id,
                included_total=bookmarks_total,
                excluded_total=0,
                blocked_total=0,
            )
            history_source_id = f"{profile_id}-history"
            ledger.register_source(
                source_id=history_source_id,
                platform=platform,
                collection="history",
                baseline_at=inventory["baseline_at"],
                scanned_total=history_total,
            )
            ledger.reconcile_source(
                history_source_id,
                included_total=0,
                excluded_total=history_total - history_candidates,
                blocked_total=history_candidates,
            )
        print(
            json.dumps(
                {
                    "status": "browser-sources-registered",
                    "profile_id": profile_id,
                    "bookmarks_total": bookmarks_total,
                    "history_total": history_total,
                    "history_candidates": history_candidates,
                },
                ensure_ascii=False,
            )
        )
        return 0
    if options.command == "seed-candidates":
        inventory = load_inventory(options.inventory)
        if "profile_id" in inventory:
            candidates = build_browser_candidates(inventory)
        elif "device_id" in inventory and "candidates" in inventory:
            candidates = build_local_file_candidates(inventory)
        else:
            raise ValueError(f"Unsupported inventory shape: {options.inventory}")
        with Ledger(data_directory / "knowledge-assets.sqlite3") as ledger:
            inserted = ledger.register_candidates_batch(candidates)
        print(
            json.dumps(
                {
                    "status": "candidates-seeded",
                    "inventory": str(options.inventory),
                    "candidate_total": len(candidates),
                    "inserted_total": inserted,
                    "replayed_total": len(candidates) - inserted,
                },
                ensure_ascii=False,
            )
        )
        return 0
    if options.command == "capture-public-batch":
        result = run_public_capture_batch(
            options.batch,
            workspace=workspace,
            dry_run=options.dry_run,
            max_workers=options.max_workers,
            max_cache_bytes=options.max_cache_bytes,
            max_response_bytes=options.max_response_bytes,
            timeout_seconds=options.timeout_seconds,
            batch_timeout_seconds=options.batch_timeout_seconds,
        )
        if isinstance(result, Path):
            payload = {"status": "capture-batch-completed", "result": str(result)}
        else:
            payload = result
        print(json.dumps(payload, ensure_ascii=False))
        return 0
    raise AssertionError(f"Unhandled command: {options.command}")
