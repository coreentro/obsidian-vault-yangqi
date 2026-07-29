import unittest

from knowledge_assets.local_file_scoring import classify_local_file


class LocalFileScoringTests(unittest.TestCase):
    def test_excludes_obvious_metadata_without_deleting_record(self) -> None:
        result = classify_local_file(
            path="/Users/me/Documents/.localized",
            mime_type="application/octet-stream",
            byte_length=0,
        )
        self.assertEqual(result["recommendation"], "excluded")
        self.assertEqual(result["record_policy"], "retain-audit-record")

    def test_sensitive_secret_like_file_requires_manual_review(self) -> None:
        result = classify_local_file(
            path="/Users/me/project/.env",
            mime_type="text/plain",
            byte_length=120,
        )
        self.assertEqual(result["recommendation"], "review")
        self.assertTrue(result["sensitive"])
        self.assertFalse(result["auto_capture_allowed"])

    def test_personal_document_is_reviewed_not_auto_excluded(self) -> None:
        result = classify_local_file(
            path="/Users/me/Documents/chemistry-notes.pdf",
            mime_type="application/pdf",
            byte_length=2048,
        )
        self.assertEqual(result["recommendation"], "review")
        self.assertIn("document", result["signals"])

    def test_generated_dependency_file_is_excluded_from_knowledge_capture(self) -> None:
        result = classify_local_file(
            path="/Users/me/project/node_modules/pkg/index.js",
            mime_type="text/javascript",
            byte_length=900,
        )
        self.assertEqual(result["recommendation"], "excluded")
        self.assertIn("generated-or-dependency", result["flags"])


if __name__ == "__main__":
    unittest.main()
