from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any
from urllib.parse import urlparse


_GENERIC_TITLES = {"", "首页", "主页", "home", "index", "welcome"}
_KNOWLEDGE_TERMS = (
    "教程",
    "指南",
    "方法",
    "入门",
    "实践",
    "研究",
    "知识",
    "文献",
    "实验",
    "数据",
    "tutorial",
    "guide",
    "how to",
    "research",
)
_PRACTICE_TERMS = (
    "教程",
    "指南",
    "方法",
    "入门",
    "实践",
    "操作",
    "实验",
    "数据处理",
    "tutorial",
    "guide",
    "how to",
)
_SENSITIVE_HOSTS = {
    "accounts.google.com",
    "mail.google.com",
    "outlook.live.com",
    "web.telegram.org",
}
_SENSITIVE_URL_MARKERS = (
    "/login",
    "/signin",
    "/account",
    "/dashboard",
    "/checkout",
    "/payment",
    "/billing",
    "/admin",
    "/console",
    "#inbox",
)
_CREDIBLE_HOSTS = {
    "github.com",
    "zotero-chinese.com",
    "docs.python.org",
    "developer.mozilla.org",
}


def score_history_candidate(
    record: Mapping[str, Any],
    *,
    themes: Sequence[str] = (),
) -> dict[str, Any]:
    """Return an explainable recommendation without changing frozen evidence.

    The score is a deterministic first-pass ordering aid. It never mutates the
    candidate ledger and never silently turns a recommendation into a final
    inclusion or exclusion decision.
    """
    title = str(record.get("title") or "").strip()
    url = str(record.get("url") or "").strip()
    visit_count = max(0, int(record.get("visit_count") or 0))
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    haystack = f"{title} {url}".lower()
    flags: list[str] = []
    reasons: list[str] = []

    sensitive = (
        host in _SENSITIVE_HOSTS
        or host in {"localhost", "127.0.0.1"}
        or any(marker in haystack for marker in _SENSITIVE_URL_MARKERS)
    )
    if sensitive:
        flags.append("non-knowledge-or-sensitive")
        reasons.append("链接指向登录、支付、账户、后台、邮箱或本地控制页面。")
        return {
            "factors": {
                "reusability": 0,
                "uniqueness": 0,
                "credibility": 0,
                "theme_relation": 0,
                "practice_value": 0,
            },
            "total_score": 0,
            "confidence": 1.0,
            "recommended_decision": "excluded",
            "review_required": True,
            "flags": flags,
            "reasons": reasons,
        }

    normalized_title = title.lower()
    knowledge_hits = [term for term in _KNOWLEDGE_TERMS if term in haystack]
    practice_hits = [term for term in _PRACTICE_TERMS if term in haystack]
    theme_hits = [theme for theme in themes if str(theme).strip().lower() in haystack]

    reusability = min(
        20,
        (14 if knowledge_hits else 0)
        + (3 if len(title) >= 8 else 0)
        + (3 if visit_count >= 3 else 0),
    )
    path_segments = [segment for segment in parsed.path.split("/") if segment]
    uniqueness = min(
        20,
        (8 if len(path_segments) >= 2 else 0)
        + (6 if len(title) >= 12 else 0)
        + (4 if knowledge_hits else 0)
        + (2 if normalized_title not in _GENERIC_TITLES else 0),
    )
    credible_domain = (
        host in _CREDIBLE_HOSTS
        or host.endswith(".edu")
        or ".edu." in host
        or host.endswith(".gov")
        or ".gov." in host
    )
    credibility = min(20, (16 if credible_domain else 0) + (2 if parsed.scheme == "https" else 0))
    theme_relation = 20 if theme_hits else (8 if knowledge_hits else 0)
    practice_value = min(
        20,
        (16 if practice_hits else 0) + (4 if visit_count >= 3 else 0),
    )
    factors = {
        "reusability": reusability,
        "uniqueness": uniqueness,
        "credibility": credibility,
        "theme_relation": theme_relation,
        "practice_value": practice_value,
    }
    total_score = sum(factors.values())

    confidence_signals = sum(
        (
            bool(title and normalized_title not in _GENERIC_TITLES),
            bool(len(path_segments) >= 2),
            bool(knowledge_hits),
            bool(theme_hits),
            bool(credible_domain),
            bool(visit_count >= 3),
        )
    )
    confidence = round(min(1.0, 0.2 + confidence_signals * 0.13), 2)
    if confidence < 0.7:
        flags.append("low-confidence")
    if knowledge_hits:
        reasons.append(f"知识型标题或链接命中：{', '.join(knowledge_hits[:3])}。")
    if theme_hits:
        reasons.append(f"与已知主题相关：{', '.join(map(str, theme_hits[:3]))}。")
    if credible_domain:
        reasons.append("来源域名具有官方、教育、政府或公共技术文档信号。")
    if visit_count >= 3:
        reasons.append(f"历史访问次数为 {visit_count}，具有重复使用信号。")
    if not reasons:
        reasons.append("仅有弱浏览信号，尚无足够材料证明可复用价值。")

    recommended_decision = (
        "included" if total_score >= 75 and confidence >= 0.7 and not flags else "review"
    )
    return {
        "factors": factors,
        "total_score": total_score,
        "confidence": confidence,
        "recommended_decision": recommended_decision,
        "review_required": recommended_decision != "included",
        "flags": flags,
        "reasons": reasons,
    }
