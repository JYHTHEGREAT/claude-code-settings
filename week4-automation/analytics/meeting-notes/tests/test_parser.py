import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.parser import load_text, split_sections


class TestLoadText(unittest.TestCase):
    def test_load_sample(self):
        path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_meeting.txt")
        text = load_text(path)
        self.assertIn("[참석자]", text)
        self.assertIn("[결정]", text)

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("")
            tmp_path = f.name
        try:
            text = load_text(tmp_path)
            self.assertEqual(text, "")
        finally:
            os.unlink(tmp_path)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_text("/nonexistent/path.txt")


class TestSplitSections(unittest.TestCase):
    def test_all_sections(self):
        path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_meeting.txt")
        text = load_text(path)
        sections = split_sections(text)
        self.assertIn("참석자", sections)
        self.assertIn("안건", sections)
        self.assertIn("논의", sections)
        self.assertIn("결정", sections)

    def test_missing_section(self):
        text = "[참석자]\n김철수\n\n[논의]\n내용"
        sections = split_sections(text)
        self.assertIn("참석자", sections)
        self.assertIn("논의", sections)
        self.assertNotIn("안건", sections)

    def test_empty_text(self):
        sections = split_sections("")
        self.assertEqual(sections, {})


if __name__ == "__main__":
    unittest.main()
