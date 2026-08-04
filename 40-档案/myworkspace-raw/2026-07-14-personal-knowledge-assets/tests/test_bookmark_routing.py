import unittest

from knowledge_assets.bookmark_routing import route_bookmark


class BookmarkRoutingTests(unittest.TestCase):
    def test_account_and_local_pages_require_manual_access(self) -> None:
        for url in ("https://example.com/account", "http://localhost:8080/admin"):
            self.assertEqual(route_bookmark(url, "Account")["route"], "manual-private-or-account")

    def test_social_and_ai_sessions_are_not_anonymous_batch_targets(self) -> None:
        for url in ("https://x.com/user/status/1", "https://claude.ai/chat/abc"):
            self.assertEqual(route_bookmark(url, "saved")["route"], "manual-platform-or-session")

    def test_proxy_and_download_resources_are_conservative_manual_reviews(self) -> None:
        result = route_bookmark("https://example.com/vpn-nodes", "免费节点下载")
        self.assertEqual(result["route"], "manual-sensitive-resource")

    def test_plain_public_article_can_enter_public_review(self) -> None:
        result = route_bookmark("https://example.edu/article/chemistry", "Chemistry article")
        self.assertEqual(result["route"], "public-anonymous-review")
        self.assertFalse(result["capture_approved"])


if __name__ == "__main__":
    unittest.main()
