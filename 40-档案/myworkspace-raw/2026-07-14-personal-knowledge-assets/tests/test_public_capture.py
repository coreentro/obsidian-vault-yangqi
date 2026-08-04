import json
import hashlib
import socket
import multiprocessing
import os
import subprocess
import time
import tempfile
import unittest
from unittest.mock import Mock, patch
from pathlib import Path

from knowledge_assets.public_capture import (
    FetchResult,
    UnsafePublicURLError,
    _RedirectRecorder,
    deterministic_asset_id,
    extract_visible_text,
    validate_public_url,
    write_public_capture,
    _PinnedHTTPConnection,
    _PinnedHTTPSConnection,
    resolve_public_url,
    _resolve_hostname_with_deadline,
)


class PublicCaptureTest(unittest.TestCase):
    @patch("knowledge_assets.public_capture.socket.getaddrinfo")
    def test_public_url_validation_rejects_credentials_and_non_global_targets(self, getaddrinfo) -> None:
        getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("127.0.0.1", 443))]
        with self.assertRaises(UnsafePublicURLError):
            validate_public_url("https://example.com/private")
        with self.assertRaises(UnsafePublicURLError):
            validate_public_url("https://user:secret@example.com/article")
        with self.assertRaises(UnsafePublicURLError):
            validate_public_url("http://169.254.169.254/latest/meta-data")

    @patch("knowledge_assets.public_capture.socket.getaddrinfo")
    def test_redirect_handler_revalidates_every_redirect_target(self, getaddrinfo) -> None:
        getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("10.0.0.5", 80))]
        handler = _RedirectRecorder([])
        with self.assertRaises(UnsafePublicURLError):
            handler.redirect_request(None, None, 302, "Found", {}, "http://internal.example/secret")

    @patch("knowledge_assets.public_capture.socket.create_connection")
    @patch("knowledge_assets.public_capture.socket.getaddrinfo")
    def test_validated_dns_ip_is_pinned_to_tcp_connection(self, getaddrinfo, create_connection) -> None:
        getaddrinfo.side_effect = [
            [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 80))],
            [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("127.0.0.1", 80))],
        ]
        target = resolve_public_url("http://example.com/article")
        connection = _PinnedHTTPConnection(target.hostname, target.port, target.ips[0], timeout=3)
        connection.connect()
        create_connection.assert_called_once_with(("93.184.216.34", 80), 3, None)
        self.assertEqual(getaddrinfo.call_count, 1)

    @patch("knowledge_assets.public_capture.socket.create_connection")
    def test_https_uses_original_hostname_for_sni_and_certificate_context(self, create_connection) -> None:
        raw_socket = object()
        create_connection.return_value = raw_socket
        context = Mock()
        secured_socket = Mock()
        context.wrap_socket.return_value = secured_socket
        connection = _PinnedHTTPSConnection(
            "example.com", 443, "93.184.216.34", timeout=3, context=context
        )
        connection.connect()
        context.wrap_socket.assert_called_once_with(raw_socket, server_hostname="example.com")
        self.assertIs(connection.sock, secured_socket)

    @patch("knowledge_assets.public_capture._DNS_HELPER_CODE", "import time; time.sleep(30)")
    def test_dns_timeout_reaps_helper_process(self) -> None:
        def direct_children() -> set[int]:
            output = subprocess.check_output(
                ["ps", "-axo", "pid=,ppid=,comm="], text=True
            )
            children: set[int] = set()
            for line in output.splitlines():
                pid_text, ppid_text, command = line.strip().split(maxsplit=2)
                if int(ppid_text) == os.getpid() and command != "ps":
                    children.add(int(pid_text))
            return children

        children_before = {child.pid for child in multiprocessing.active_children()}
        direct_before = direct_children()
        started = time.monotonic()
        with self.assertRaises(TimeoutError):
            _resolve_hostname_with_deadline("example.com", 443, time.monotonic() + 0.05)
        self.assertLess(time.monotonic() - started, 0.3)
        self.assertEqual(
            {child.pid for child in multiprocessing.active_children()}, children_before
        )
        self.assertEqual(direct_children(), direct_before)

    def test_visible_text_excludes_non_visible_script_content(self) -> None:
        html = """
        <html><head><title>标题</title><script>不能进入正文</script></head>
        <body><h1>完整标题</h1><p>第一段</p><p>第二段</p><style>隐藏</style></body></html>
        """
        text = extract_visible_text(html)
        self.assertIn("完整标题", text)
        self.assertIn("第一段", text)
        self.assertNotIn("不能进入正文", text)
        self.assertNotIn("隐藏", text)

    def test_incomplete_response_creates_blocked_package_without_source_guess(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            asset_id, package_root = write_public_capture(
                FetchResult(
                    requested_url="https://example.com/article",
                    final_url=None,
                    complete=False,
                    error="TimeoutError",
                ),
                root=Path(temporary_directory),
                candidate_id="candidate-001",
                source_id="source-001",
                original_url="https://example.com/article",
                title="文章",
            )
            self.assertEqual(asset_id, deterministic_asset_id("candidate-001"))
            manifest = json.loads((package_root / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["completeness"], "blocked")
            self.assertFalse((package_root / "source.md").exists())
            capture_log = json.loads((package_root / "capture-log.json").read_text(encoding="utf-8"))
            self.assertIn("未完整取得", "".join(capture_log["limitations"]))

    def test_complete_response_preserves_exact_raw_bytes_and_marks_text_derived(self) -> None:
        raw = b"<html><body>prefix\xffsuffix</body></html>"
        with tempfile.TemporaryDirectory() as temporary_directory:
            _, package_root = write_public_capture(
                FetchResult(
                    requested_url="https://example.com/article",
                    final_url="https://example.com/article",
                    status_code=200,
                    content_type="text/html",
                    body=raw,
                    complete=True,
                ),
                root=Path(temporary_directory),
                candidate_id="candidate-raw",
                source_id="source-001",
                original_url="https://example.com/article",
                title="文章",
            )
            self.assertEqual((package_root / "source-response.bin").read_bytes(), raw)
            metadata = json.loads((package_root / "metadata.json").read_text(encoding="utf-8"))
            self.assertEqual(metadata["body_sha256"], hashlib.sha256(raw).hexdigest())
            manifest = json.loads((package_root / "manifest.json").read_text(encoding="utf-8"))
            derived = {item["path"]: item for item in manifest["derived_files"]}
            self.assertEqual(derived["source.html"]["parent"], "source-response.bin")
            self.assertEqual(derived["source.md"]["parent"], "source-response.bin")


if __name__ == "__main__":
    unittest.main()
