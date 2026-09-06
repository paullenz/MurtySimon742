"""Tests of byte-recovery checking only; these are not SAT-proof tests."""
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('check_intake', Path(__file__).resolve().parents[1] / 'tools/check_intake.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class IntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.payloads = self.root / 'payloads'
        self.payloads.mkdir()
        self.item = {'path': 'a.txt', 'bytes': 4, 'sha256': hashlib.sha256(b'abc\n').hexdigest()}
        (self.payloads / 'a.txt').write_bytes(b'abc\n')
        self.manifest = self.root / 'manifest.json'
        self.write([self.item])

    def write(self, rows):
        self.manifest.write_text(json.dumps({'files': rows}))

    def check(self):
        return checker.inspect(self.manifest, self.payloads)

    def test_complete(self):
        self.assertEqual(self.check()['status'], 'COMPLETE')

    def test_missing(self):
        (self.payloads / 'a.txt').unlink()
        result = self.check()
        self.assertEqual(result['status'], 'PARTIAL')
        self.assertEqual(result['missing_declared_bytes'], 4)

    def test_altered_same_size(self):
        (self.payloads / 'a.txt').write_bytes(b'xyz\n')
        self.assertEqual(self.check()['status'], 'INVALID')

    def test_wrong_size(self):
        self.write([{**self.item, 'bytes': 5}])
        self.assertEqual(self.check()['status'], 'INVALID')

    def test_duplicate(self):
        self.write([self.item, self.item])
        with self.assertRaises(ValueError):
            self.check()

    def test_unsafe_paths(self):
        for name in ('../escape', '/absolute', 'a/../b', 'C:/escape', 'a\\b', './a.txt', 'a//b', '.'):
            with self.subTest(name=name):
                self.write([{**self.item, 'path': name}])
                with self.assertRaises(ValueError):
                    self.check()

    def test_symlink(self):
        (self.payloads / 'a.txt').unlink()
        (self.root / 'target').write_bytes(b'abc\n')
        (self.payloads / 'a.txt').symlink_to(self.root / 'target')
        with self.assertRaises(ValueError):
            self.check()

    def test_empty_manifest(self):
        self.write([])
        with self.assertRaises(ValueError):
            self.check()

    def test_malformed_metadata(self):
        for row in ({**self.item, 'bytes': True}, {**self.item, 'sha256': 'bad'}):
            with self.subTest(row=row):
                self.write([row])
                with self.assertRaises(ValueError):
                    self.check()


if __name__ == '__main__':
    unittest.main()
