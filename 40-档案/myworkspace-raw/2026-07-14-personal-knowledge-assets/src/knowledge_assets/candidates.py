from __future__ import annotations

from pathlib import Path
from typing import Any


def build_browser_candidates(inventory: dict[str, Any]) -> list[dict[str, Any]]:
    """Turn a frozen browser inventory into auditable candidate records.

    Bookmarks are explicit preservation signals and therefore enter the included
    lane. History is only a weak signal: readable records enter review and
    records filtered by the frozen boundary remain excluded with a reason.
    """
    profile_id = str(inventory["profile_id"])
    output: list[dict[str, Any]] = []
    for index, bookmark in enumerate(inventory.get("bookmarks", [])):
        folder_path = list(bookmark.get("folder_path", []))
        signals = ["bookmark", f"folder_path:{folder_path}"]
        if bookmark.get("date_added") is not None:
            signals.append(f"date_added:{bookmark['date_added']}")
        output.append(
            {
                "candidate_id": f"{profile_id}-bookmarks:item:{index:08d}",
                "source_id": f"{profile_id}-bookmarks",
                "title": str(bookmark.get("title") or ""),
                "original_url": bookmark.get("url"),
                "preservation_signals": signals,
                "value_score": 100,
                "decision": "included",
                "decision_reason": "显式书签信号，进入不可删减证据采集队列。",
            }
        )

    for index, history in enumerate(inventory.get("history", [])):
        visit_count = int(history.get("visit_count") or 0)
        last_visit_time = int(history.get("last_visit_time") or 0)
        signals = [
            "history",
            f"visit_count:{visit_count}",
            f"last_visit_time:{last_visit_time}",
        ]
        if history.get("is_content_candidate"):
            # This is a provisional score for queue ordering, not a final AI
            # value judgment. Human review remains mandatory before capture.
            score = min(89, 40 + min(40, visit_count * 5))
            decision = "review"
            reason = "浏览历史弱保存信号；初始分仅用于排序，待AI评分和人工复核。"
        else:
            score = 0
            decision = "excluded"
            reason = "冻结扫描规则判定为不可直接作为知识内容的页面；保留候选审计记录，不采集正文。"
        output.append(
            {
                "candidate_id": f"{profile_id}-history:item:{index:08d}",
                "source_id": f"{profile_id}-history",
                "title": str(history.get("title") or ""),
                "original_url": history.get("url"),
                "preservation_signals": signals,
                "value_score": score,
                "decision": decision,
                "decision_reason": reason,
            }
        )
    return output


def build_local_file_candidates(inventory: dict[str, Any]) -> list[dict[str, Any]]:
    """Create blocked candidates for every scanned local file.

    The local scan has not yet undergone value classification. Keeping every
    record in the blocked lane preserves the exact baseline without implying
    that a file is valuable or disposable.
    """
    source_id = f"{inventory['device_id']}-local"
    output: list[dict[str, Any]] = []
    for index, item in enumerate(inventory.get("candidates", [])):
        path = str(item.get("path") or "")
        signals = [
            "local-file",
            f"path:{path}",
            f"mime_type:{item.get('mime_type', '')}",
            f"byte_length:{int(item.get('byte_length') or 0)}",
            f"modified_at_ns:{int(item.get('modified_at_ns') or 0)}",
            f"sha256:{item.get('sha256', '')}",
        ]
        output.append(
            {
                "candidate_id": f"{source_id}:item:{index:08d}",
                "source_id": source_id,
                "title": path or f"local-file-{index:08d}",
                "original_url": None,
                "preservation_signals": signals,
                "value_score": 0,
                "decision": "blocked",
                "decision_reason": "本机资料尚未完成AI价值判断；暂不采集正文，不推断文件内容。",
            }
        )
    return output


def load_inventory(path: Path) -> dict[str, Any]:
    import json

    return json.loads(Path(path).read_text(encoding="utf-8"))
