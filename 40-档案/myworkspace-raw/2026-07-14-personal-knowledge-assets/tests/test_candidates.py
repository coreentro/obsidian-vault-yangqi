import unittest

from knowledge_assets.candidates import build_browser_candidates, build_local_file_candidates


class CandidateBuilderTest(unittest.TestCase):
    def test_bookmarks_are_included_and_history_is_split_by_frozen_boundary(self) -> None:
        inventory = {
            "profile_id": "chrome-default",
            "bookmarks": [
                {
                    "title": "精华文章",
                    "url": "https://example.com/article",
                    "folder_path": ["书签栏", "研究"],
                    "date_added": "123",
                }
            ],
            "history": [
                {
                    "title": "可复用内容",
                    "url": "https://example.com/knowledge",
                    "visit_count": 3,
                    "last_visit_time": 456,
                    "is_content_candidate": True,
                },
                {
                    "title": "登录页",
                    "url": "https://example.com/login",
                    "visit_count": 1,
                    "last_visit_time": 789,
                    "is_content_candidate": False,
                },
            ],
        }

        candidates = build_browser_candidates(inventory)
        self.assertEqual(len(candidates), 3)
        self.assertEqual(candidates[0]["decision"], "included")
        self.assertIn("folder_path:['书签栏', '研究']", candidates[0]["preservation_signals"])
        self.assertEqual(candidates[1]["decision"], "review")
        self.assertEqual(candidates[1]["value_score"], 55)
        self.assertEqual(candidates[2]["decision"], "excluded")
        self.assertIn("冻结扫描规则", candidates[2]["decision_reason"])

    def test_local_file_candidate_keeps_path_and_checksum_as_signals(self) -> None:
        inventory = {
            "device_id": "mac-current",
            "candidates": [
                {
                    "path": "/Users/test/精华.md",
                    "mime_type": "text/markdown",
                    "byte_length": 12,
                    "modified_at_ns": 34,
                    "sha256": "abc123",
                }
            ],
        }
        candidates = build_local_file_candidates(inventory)
        self.assertEqual(candidates[0]["decision"], "blocked")
        self.assertIn("path:/Users/test/精华.md", candidates[0]["preservation_signals"])
        self.assertIn("sha256:abc123", candidates[0]["preservation_signals"])


if __name__ == "__main__":
    unittest.main()
