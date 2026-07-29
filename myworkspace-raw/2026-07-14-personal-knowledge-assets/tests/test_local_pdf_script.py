import unittest

from scripts.capture_local_pdf_allowlist import build_review_id


class LocalPdfScriptTest(unittest.TestCase):
    def test_review_id_uses_explicit_batch_version(self) -> None:
        self.assertEqual(
            build_review_id("mac-current-local:item:00001420", "v003"),
            "review-mac-current-local-item-00001420-pdf-v003",
        )


if __name__ == "__main__":
    unittest.main()
