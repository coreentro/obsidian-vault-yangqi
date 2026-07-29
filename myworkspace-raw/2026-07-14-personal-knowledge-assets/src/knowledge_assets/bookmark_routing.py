from __future__ import annotations

import ipaddress
from typing import Any
from urllib.parse import unquote, urlsplit


_ACCOUNT_TERMS = {
    "account", "admin", "auth", "billing", "checkout", "console", "dashboard",
    "inbox", "login", "mail", "mycourse", "notebook", "payment", "profile",
    "settings", "signin", "upload", "wallet",
}
_PLATFORM_HOSTS = {
    "bilibili.com", "chatgpt.com", "claude.ai", "discord.com", "douban.com",
    "facebook.com", "gemini.google.com", "instagram.com", "openai.com", "quora.com",
    "reddit.com", "t.me", "telegram.org", "weibo.com", "x.com", "xiaohongshu.com",
    "youtube.com", "zhihu.com",
}
_SENSITIVE_TERMS = {
    "black card", "crack", "download", "fanqiang", "gift card", "node", "nodes",
    "ping", "proxy", "quantumult", "torrent", "vpn", "vps", "代理", "机场",
    "节点", "破解", "礼品卡", "网盘", "翻墙", "下载",
}


def _matches_host(host: str, boundary: str) -> bool:
    return host == boundary or host.endswith("." + boundary)


def route_bookmark(url: str, title: str) -> dict[str, Any]:
    """Route bookmark metadata conservatively; never authorizes capture by itself."""
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower().rstrip(".")
    combined = unquote(f"{title} {url}").lower()
    path_terms = {term for term in parsed.path.lower().replace("-", "/").split("/") if term}

    try:
        literal_ip = ipaddress.ip_address(host.strip("[]"))
    except ValueError:
        literal_ip = None

    if (
        parsed.scheme.lower() not in {"http", "https"}
        or parsed.username is not None
        or parsed.password is not None
        or host in {"", "localhost"}
        or literal_ip is not None
        or path_terms.intersection(_ACCOUNT_TERMS)
    ):
        route = "manual-private-or-account"
        reason = "本地、账户、后台、支付、上传或带凭据页面，只能在用户明确访问时人工处理。"
    elif any(_matches_host(host, boundary) for boundary in _PLATFORM_HOSTS):
        route = "manual-platform-or-session"
        reason = "社交、视频、问答或AI会话平台可能依赖登录和动态上下文，不进入匿名批处理。"
    elif any(term in combined for term in _SENSITIVE_TERMS):
        route = "manual-sensitive-resource"
        reason = "代理、节点、下载、版权或支付型资源需人工判断合法性、隐私和实际价值。"
    else:
        route = "public-anonymous-review"
        reason = "仅通过离线元数据初筛；入批前仍需去重、来源价值和网络安全复核。"

    return {
        "route": route,
        "reason": reason,
        "capture_approved": False,
        "preservation_policy": "Routing is derived metadata; it does not alter or delete the frozen bookmark.",
    }
