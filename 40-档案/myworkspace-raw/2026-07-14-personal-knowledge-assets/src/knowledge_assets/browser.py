from __future__ import annotations

import json
import shutil
import sqlite3
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse


@dataclass(frozen=True)
class BrowserBookmark:
    profile_id: str
    title: str
    url: str
    folder_path: tuple[str, ...]
    date_added: str | None


class BrowserInventoryConflictError(RuntimeError):
    """Raised when a frozen browser inventory would be replaced."""


@dataclass(frozen=True)
class BrowserHistoryRecord:
    profile_id: str
    url: str
    title: str
    visit_count: int
    last_visit_time: int
    is_content_candidate: bool


def read_chromium_bookmarks(path: Path, *, profile_id: str) -> list[BrowserBookmark]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    bookmarks: list[BrowserBookmark] = []
    for root in payload.get("roots", {}).values():
        _walk_bookmark_node(root, profile_id=profile_id, folders=(), output=bookmarks)
    return bookmarks


def read_chromium_history(path: Path, *, profile_id: str) -> list[BrowserHistoryRecord]:
    database_path = Path(path).expanduser().resolve()
    with tempfile.TemporaryDirectory(prefix="knowledge-assets-history-") as temporary_directory:
        copy_path = Path(temporary_directory) / "History"
        shutil.copy2(database_path, copy_path)
        for suffix in ("-wal", "-shm"):
            companion = Path(f"{database_path}{suffix}")
            if companion.exists():
                shutil.copy2(companion, Path(f"{copy_path}{suffix}"))
        connection = sqlite3.connect(copy_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA query_only = ON")
        try:
            rows = connection.execute(
                """
                SELECT url, COALESCE(title, '') AS title,
                       COALESCE(visit_count, 0) AS visit_count,
                       COALESCE(last_visit_time, 0) AS last_visit_time
                FROM urls
                ORDER BY last_visit_time DESC, id
                """
            ).fetchall()
        finally:
            connection.close()
    return [
        BrowserHistoryRecord(
            profile_id=profile_id,
            url=row["url"],
            title=row["title"],
            visit_count=row["visit_count"],
            last_visit_time=row["last_visit_time"],
            is_content_candidate=is_readable_content_url(row["url"]),
        )
        for row in rows
    ]


def write_chromium_inventory(
    output_path: Path,
    *,
    profile_id: str,
    baseline_at: str,
    bookmarks_path: Path,
    history_path: Path,
) -> Path:
    bookmarks = read_chromium_bookmarks(bookmarks_path, profile_id=profile_id)
    history = read_chromium_history(history_path, profile_id=profile_id)
    payload = {
        "schema_version": 1,
        "profile_id": profile_id,
        "baseline_at": baseline_at,
        "bookmarks_total": len(bookmarks),
        "history_total": len(history),
        "content_candidates_total": sum(item.is_content_candidate for item in history),
        "bookmarks": [
            {
                "title": item.title,
                "url": item.url,
                "folder_path": list(item.folder_path),
                "date_added": item.date_added,
            }
            for item in bookmarks
        ],
        "history": [
            {
                "title": item.title,
                "url": item.url,
                "visit_count": item.visit_count,
                "last_visit_time": item.last_visit_time,
                "is_content_candidate": item.is_content_candidate,
            }
            for item in history
        ],
    }
    content = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise BrowserInventoryConflictError(f"Refusing to replace frozen browser inventory: {path}")
        return path
    with path.open("xb") as handle:
        handle.write(content)
    return path


def _walk_bookmark_node(
    node: dict[str, object],
    *,
    profile_id: str,
    folders: tuple[str, ...],
    output: list[BrowserBookmark],
) -> None:
    node_type = node.get("type")
    if node_type == "folder":
        name = str(node.get("name") or "")
        child_folders = folders + ((name,) if name else ())
        for child in node.get("children", []):
            if isinstance(child, dict):
                _walk_bookmark_node(
                    child,
                    profile_id=profile_id,
                    folders=child_folders,
                    output=output,
                )
        return
    if node_type != "url":
        return
    url = str(node.get("url") or "")
    if urlparse(url).scheme not in {"http", "https"}:
        return
    output.append(
        BrowserBookmark(
            profile_id=profile_id,
            title=str(node.get("name") or ""),
            url=url,
            folder_path=folders,
            date_added=str(node["date_added"]) if node.get("date_added") else None,
        )
    )


def is_readable_content_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return False
    path = parsed.path.lower()
    blocked_segments = {"login", "signin", "signup", "checkout", "payment", "pay"}
    if any(segment in blocked_segments for segment in path.split("/") if segment):
        return False
    host = parsed.netloc.lower().split(":", 1)[0]
    search_hosts = {
        "google.com",
        "www.google.com",
        "bing.com",
        "www.bing.com",
        "baidu.com",
        "www.baidu.com",
    }
    if host in search_hosts and path.startswith("/search"):
        return False
    return True
