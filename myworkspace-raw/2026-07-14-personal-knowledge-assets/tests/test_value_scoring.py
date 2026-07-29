import unittest

from knowledge_assets.value_scoring import score_history_candidate


class HistoryValueScoringTest(unittest.TestCase):
    def test_explainable_high_value_article_can_be_recommended_for_inclusion(self) -> None:
        result = score_history_candidate(
            {
                "title": "Zotero 文献管理完整教程与实践指南",
                "url": "https://zotero-chinese.com/user-guide/quick-start",
                "visit_count": 8,
            },
            themes=("文献管理", "学习方法"),
        )

        self.assertGreaterEqual(result["total_score"], 75)
        self.assertEqual(result["recommended_decision"], "included")
        self.assertFalse(result["review_required"])
        self.assertEqual(
            set(result["factors"]),
            {"reusability", "uniqueness", "credibility", "theme_relation", "practice_value"},
        )
        self.assertTrue(result["reasons"])

    def test_ambiguous_homepage_is_kept_for_human_review(self) -> None:
        result = score_history_candidate(
            {"title": "首页", "url": "https://example.com/", "visit_count": 1}
        )

        self.assertEqual(result["recommended_decision"], "review")
        self.assertTrue(result["review_required"])
        self.assertIn("low-confidence", result["flags"])

    def test_login_payment_and_account_pages_are_auditable_exclusion_recommendations(self) -> None:
        for url in (
            "https://mail.google.com/mail/u/0/#inbox",
            "https://example.com/account/dashboard",
            "https://example.com/payment/checkout",
        ):
            with self.subTest(url=url):
                result = score_history_candidate(
                    {"title": "个人页面", "url": url, "visit_count": 20}
                )
                self.assertEqual(result["recommended_decision"], "excluded")
                self.assertTrue(result["review_required"])
                self.assertIn("non-knowledge-or-sensitive", result["flags"])

    def test_scoring_does_not_mutate_the_frozen_input_record(self) -> None:
        record = {
            "title": "化学实验数据处理教程",
            "url": "https://university.example.edu/chemistry/tutorial",
            "visit_count": 3,
        }
        original = dict(record)

        score_history_candidate(record, themes=("化学",))

        self.assertEqual(record, original)


if __name__ == "__main__":
    unittest.main()
