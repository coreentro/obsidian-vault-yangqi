from __future__ import annotations

import hashlib
import http.client
import ipaddress
import json
import mimetypes
import socket
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .evidence import EvidencePackage


@dataclass
class FetchResult:
    requested_url: str
    final_url: str | None = None
    status_code: int | None = None
    content_type: str | None = None
    body: bytes = b""
    complete: bool = False
    error: str | None = None
    redirects: list[str] = field(default_factory=list)


class UnsafePublicURLError(ValueError):
    """Raised when a URL could reach credentials or a non-public network target."""


_DNS_HELPER_CODE = (
    "import json,socket,sys;"
    "a=socket.getaddrinfo(sys.argv[1],int(sys.argv[2]),type=socket.SOCK_STREAM);"
    "print(json.dumps([x[4][0] for x in a]))"
)


@dataclass(frozen=True)
class ResolvedPublicURL:
    url: str
    scheme: str
    hostname: str
    port: int
    request_target: str
    ips: tuple[str, ...]


def _resolve_hostname_with_deadline(hostname: str, port: int, deadline: float) -> list[str]:
    """Resolve in a terminable helper so OS DNS cannot outlive the request deadline."""
    try:
        completed = subprocess.run(
            [sys.executable, "-c", _DNS_HELPER_CODE, hostname, str(port)],
            check=True,
            capture_output=True,
            text=True,
            timeout=_remaining(deadline),
        )
        values = json.loads(completed.stdout)
    except subprocess.TimeoutExpired as exc:
        raise TimeoutError("dns-wall-clock-deadline-exceeded") from exc
    except (subprocess.SubprocessError, json.JSONDecodeError) as exc:
        raise UnsafePublicURLError(f"dns-resolution-failed: {exc}") from exc
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        raise UnsafePublicURLError("invalid-dns-address")
    return values


def resolve_public_url(
    url: str, *, resolve: bool = True, deadline: float | None = None
) -> ResolvedPublicURL:
    """Validate a URL and freeze the exact public IPs permitted for connection."""
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc or parsed.hostname is None:
        raise UnsafePublicURLError("unsupported-or-missing-http-url")
    if parsed.username is not None or parsed.password is not None:
        raise UnsafePublicURLError("url-credentials-are-forbidden")
    try:
        port = parsed.port
    except ValueError as exc:
        raise UnsafePublicURLError("invalid-url-port") from exc
    hostname = parsed.hostname.rstrip(".").lower()
    if hostname == "localhost" or hostname.endswith(".localhost") or hostname.endswith(".local"):
        raise UnsafePublicURLError("local-hostname-is-forbidden")
    if hostname in {"metadata.google.internal", "metadata.aws.internal"}:
        raise UnsafePublicURLError("metadata-host-is-forbidden")
    try:
        literal = ipaddress.ip_address(hostname)
        addresses = [literal]
    except ValueError:
        if not resolve:
            addresses = []
            request_target = parsed.path or "/"
            if parsed.query:
                request_target += f"?{parsed.query}"
            return ResolvedPublicURL(
                url=url, scheme=parsed.scheme, hostname=hostname,
                port=port or (443 if parsed.scheme == "https" else 80),
                request_target=request_target, ips=(),
            )
        resolved_port = port or (443 if parsed.scheme == "https" else 80)
        if deadline is not None:
            answer_addresses = _resolve_hostname_with_deadline(hostname, resolved_port, deadline)
            answers = [(None, None, None, None, (address, resolved_port)) for address in answer_addresses]
        else:
            try:
                answers = socket.getaddrinfo(
                    hostname, resolved_port, type=socket.SOCK_STREAM,
                )
            except socket.gaierror as exc:
                raise UnsafePublicURLError(f"dns-resolution-failed: {exc}") from exc
        addresses = []
        for answer in answers:
            try:
                addresses.append(ipaddress.ip_address(answer[4][0]))
            except (ValueError, IndexError):
                raise UnsafePublicURLError("invalid-dns-address") from None
    if not addresses or any(not address.is_global for address in addresses):
        raise UnsafePublicURLError("non-public-network-target")
    request_target = parsed.path or "/"
    if parsed.query:
        request_target += f"?{parsed.query}"
    return ResolvedPublicURL(
        url=url,
        scheme=parsed.scheme,
        hostname=hostname,
        port=port or (443 if parsed.scheme == "https" else 80),
        request_target=request_target,
        ips=tuple(dict.fromkeys(str(address) for address in addresses)),
    )


def validate_public_url(url: str, *, resolve: bool = True) -> str:
    resolve_public_url(url, resolve=resolve)
    return url


class _PinnedHTTPConnection(http.client.HTTPConnection):
    def __init__(self, host: str, port: int, pinned_ip: str, **kwargs) -> None:
        self.pinned_ip = pinned_ip
        super().__init__(host, port, **kwargs)

    def connect(self) -> None:
        self.sock = socket.create_connection(
            (self.pinned_ip, self.port), self.timeout, self.source_address
        )


class _PinnedHTTPSConnection(http.client.HTTPSConnection):
    def __init__(self, host: str, port: int, pinned_ip: str, **kwargs) -> None:
        self.pinned_ip = pinned_ip
        super().__init__(host, port, **kwargs)

    def connect(self) -> None:
        raw_socket = socket.create_connection(
            (self.pinned_ip, self.port), self.timeout, self.source_address
        )
        # Certificate verification and SNI deliberately use the original DNS
        # hostname while the TCP peer remains the already validated IP.
        self.sock = self._context.wrap_socket(raw_socket, server_hostname=self.host)


def _remaining(deadline: float) -> float:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise TimeoutError("wall-clock-deadline-exceeded")
    return remaining


def _request_once(
    target: ResolvedPublicURL,
    *,
    deadline: float,
) -> tuple[http.client.HTTPResponse, http.client.HTTPConnection]:
    last_error: OSError | http.client.HTTPException | None = None
    for pinned_ip in target.ips:
        timeout = _remaining(deadline)
        connection_type = _PinnedHTTPSConnection if target.scheme == "https" else _PinnedHTTPConnection
        kwargs = {"timeout": timeout}
        if target.scheme == "https":
            kwargs["context"] = ssl.create_default_context()
        connection = connection_type(target.hostname, target.port, pinned_ip, **kwargs)
        try:
            connection.request(
                "GET",
                target.request_target,
                headers={
                    "User-Agent": "personal-knowledge-assets/1.0 (read-only archival capture)",
                    "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.1",
                    "Connection": "close",
                },
            )
            return connection.getresponse(), connection
        except (OSError, http.client.HTTPException) as exc:
            connection.close()
            last_error = exc
    if last_error is not None:
        raise last_error
    raise UnsafePublicURLError("public-url-has-no-pinned-ip")


class _RedirectRecorder(urllib.request.HTTPRedirectHandler):
    def __init__(self, redirects: list[str]) -> None:
        super().__init__()
        self.redirects = redirects

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_public_url(newurl)
        self.redirects.append(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_public_page(
    url: str,
    *,
    timeout_seconds: float = 45.0,
    max_bytes: int = 10 * 1024 * 1024,
) -> FetchResult:
    """Fetch a public page without credentials and reject partial responses."""
    result = FetchResult(requested_url=url)
    try:
        deadline = time.monotonic() + timeout_seconds
        target = resolve_public_url(url, deadline=deadline)
    except UnsafePublicURLError as exc:
        result.error = f"unsafe-public-url: {exc}"
        return result

    redirects: list[str] = []
    try:
        current_url = url
        for _ in range(11):
            response, connection = _request_once(target, deadline=deadline)
            try:
                status = response.status
                location = response.headers.get("Location")
                if status in {301, 302, 303, 307, 308} and location:
                    if len(redirects) >= 10:
                        raise UnsafePublicURLError("too-many-redirects")
                    current_url = urljoin(current_url, location)
                    target = resolve_public_url(current_url, deadline=deadline)
                    redirects.append(current_url)
                    # A redirect is resolved once here; _request_once connects
                    # only to one of these frozen, validated addresses.
                    continue
                result.final_url = current_url
                result.status_code = status
                result.content_type = response.headers.get_content_type()
                chunks: list[bytes] = []
                total = 0
                while True:
                    timeout = _remaining(deadline)
                    sock = connection.sock
                    if sock is None:
                        sock = getattr(getattr(response.fp, "raw", None), "_sock", None)
                    if sock is not None:
                        sock.settimeout(timeout)
                    chunk = response.read(min(64 * 1024, max_bytes + 1 - total))
                    if not chunk:
                        break
                    chunks.append(chunk)
                    total += len(chunk)
                    if total > max_bytes:
                        result.error = f"response-exceeds-{max_bytes}-bytes"
                        result.redirects = redirects
                        return result
                result.body = b"".join(chunks)
                result.complete = True
                break
            finally:
                response.close()
                connection.close()
    except (
        urllib.error.URLError,
        TimeoutError,
        OSError,
        http.client.HTTPException,
        UnsafePublicURLError,
    ) as exc:
        result.error = f"{type(exc).__name__}: {exc}"
    result.redirects = redirects
    return result


def extract_visible_text(html: str) -> str:
    """Extract current HTML body text as a derived reading layer."""
    soup = BeautifulSoup(html, "lxml")
    for element in soup.find_all(["script", "style", "noscript", "template", "svg"]):
        element.decompose()
    body = soup.body or soup
    lines = [line.strip() for line in body.get_text("\n").splitlines()]
    return "\n".join(line for line in lines if line)


def deterministic_asset_id(candidate_id: str) -> str:
    digest = hashlib.sha256(candidate_id.encode("utf-8")).hexdigest()[:24]
    return f"asset-{digest}"


def write_public_capture(
    result: FetchResult,
    *,
    root: Path,
    candidate_id: str,
    source_id: str,
    original_url: str,
    title: str,
) -> tuple[str, Path]:
    """Write one immutable public-page package and return its asset id and path."""
    asset_id = deterministic_asset_id(candidate_id)
    package = EvidencePackage(Path(root) / asset_id, asset_id=asset_id, source_id=source_id)
    captured_at = datetime.now(timezone.utc).isoformat()
    final_url = result.final_url or original_url
    metadata = {
        "asset_id": asset_id,
        "candidate_id": candidate_id,
        "source_id": source_id,
        "title": title,
        "original_url": original_url,
        "requested_url": result.requested_url,
        "final_url": final_url,
        "redirects": result.redirects,
        "captured_at": captured_at,
        "status_code": result.status_code,
        "content_type": result.content_type,
        "body_byte_length": len(result.body),
        "body_sha256": hashlib.sha256(result.body).hexdigest() if result.body else None,
    }
    package.write_immutable_text("metadata.json", json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")

    capture_log = {
        "requested_url": original_url,
        "final_url": result.final_url,
        "redirects": result.redirects,
        "complete_response": result.complete,
        "error": result.error,
        "limitations": [],
    }
    if result.redirects:
        capture_log["limitations"].append("页面发生重定向；原始链接和重定向链分别保留。")
    if result.final_url and urlparse(result.final_url).netloc != urlparse(original_url).netloc:
        capture_log["limitations"].append("最终域名与原始域名不同，需人工确认，不把跳转目标当作原始来源。")
    if not result.complete:
        capture_log["limitations"].append("响应未完整取得；未写入 source.html 或 source.md，不猜测缺失内容。")
    package.write_immutable_text("comments.json", json.dumps({"status": "not-collected", "scope": "public-page trial"}, ensure_ascii=False, indent=2) + "\n")

    completeness = "complete"
    if result.complete and result.body:
        package.write_immutable_bytes("source-response.bin", result.body)
        content_type = result.content_type or mimetypes.guess_type(final_url)[0] or ""
        if "html" in content_type or result.body.lstrip().startswith((b"<!DOCTYPE", b"<html", b"<HTML")):
            html = result.body.decode("utf-8", errors="replace")
            package.write_derived_text(
                "source.html", html, parent="source-response.bin", transformation="decoded-text-utf8-replacement"
            )
            visible_text = extract_visible_text(html)
            if visible_text:
                package.write_derived_text(
                    "source.md", visible_text + "\n", parent="source-response.bin", transformation="visible-text-extraction"
                )
            else:
                completeness = "limited"
                capture_log["limitations"].append("HTML 中未提取到可见正文文本。")
        else:
            package.write_derived_text(
                "source.txt", result.body.decode("utf-8", errors="replace"),
                parent="source-response.bin", transformation="decoded-text-utf8-replacement",
            )
            completeness = "limited"
    else:
        completeness = "blocked"
    package.write_immutable_text("capture-log.json", json.dumps(capture_log, ensure_ascii=False, indent=2) + "\n")
    package.finalize(completeness=completeness)
    return asset_id, package.root
