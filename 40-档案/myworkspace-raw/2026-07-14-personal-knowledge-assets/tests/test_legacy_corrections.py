import json
import tempfile
import unittest
from pathlib import Path

from knowledge_assets.legacy_corrections import write_legacy_correction


class LegacyCorrectionTests(unittest.TestCase):
    def test_writes_external_append_only_correction_without_touching_package(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            package = root / "evidence" / "asset-one"
            package.mkdir(parents=True)
            (package / "manifest.json").write_text('{"asset_id":"asset-one"}\n')
            (package / "source.html").write_bytes(b"legacy-decoded-html")
            before = {p.name: p.read_bytes() for p in package.iterdir()}

            output = write_legacy_correction(package, root / "corrections")

            self.assertEqual(before, {p.name: p.read_bytes() for p in package.iterdir()})
            correction = json.loads((output / "manifest-v2.json").read_text())
            self.assertEqual(correction["asset_id"], "asset-one")
            self.assertEqual({item["path"] for item in correction["legacy_package_files"]}, set(before))
            self.assertIn("raw HTTP response bytes", " ".join(correction["limitations"]))

    def test_refuses_to_replace_an_existing_correction(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            package = root / "evidence" / "asset-one"
            package.mkdir(parents=True)
            (package / "manifest.json").write_text('{"asset_id":"asset-one"}\n')
            output = write_legacy_correction(package, root / "corrections")
            with self.assertRaises(FileExistsError):
                write_legacy_correction(package, root / "corrections")
            self.assertTrue((output / "checksums.sha256").is_file())


if __name__ == "__main__":
    unittest.main()
