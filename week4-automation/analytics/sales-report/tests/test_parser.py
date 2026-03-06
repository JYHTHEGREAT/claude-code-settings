import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.parser import load_csv, validate_row


class TestValidateRow(unittest.TestCase):
    def test_valid_row(self):
        row = {"date": "2024-01-05", "category": "Electronics", "amount": "150000"}
        self.assertTrue(validate_row(row))

    def test_missing_date(self):
        row = {"category": "Electronics", "amount": "150000"}
        self.assertFalse(validate_row(row))

    def test_missing_category(self):
        row = {"date": "2024-01-05", "amount": "150000"}
        self.assertFalse(validate_row(row))

    def test_missing_amount(self):
        row = {"date": "2024-01-05", "category": "Electronics"}
        self.assertFalse(validate_row(row))

    def test_invalid_amount(self):
        row = {"date": "2024-01-05", "category": "Electronics", "amount": "abc"}
        self.assertFalse(validate_row(row))

    def test_invalid_date_format(self):
        row = {"date": "01-05-2024", "category": "Electronics", "amount": "150000"}
        self.assertFalse(validate_row(row))


class TestLoadCsv(unittest.TestCase):
    def test_load_sample_csv(self):
        csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_sales.csv")
        data = load_csv(csv_path)
        self.assertEqual(len(data), 24)
        self.assertEqual(data[0]["category"], "Electronics")
        self.assertIsInstance(data[0]["amount"], float)

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("")
            tmp_path = f.name
        try:
            data = load_csv(tmp_path)
            self.assertEqual(data, [])
        finally:
            os.unlink(tmp_path)

    def test_skip_invalid_rows(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("date,category,amount\n")
            f.write("2024-01-05,Electronics,150000\n")
            f.write("bad-date,Food,abc\n")
            f.write("2024-02-10,Clothing,85000\n")
            tmp_path = f.name
        try:
            data = load_csv(tmp_path)
            self.assertEqual(len(data), 2)
        finally:
            os.unlink(tmp_path)

    def test_missing_columns(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("date,category\n")
            f.write("2024-01-05,Electronics\n")
            tmp_path = f.name
        try:
            data = load_csv(tmp_path)
            self.assertEqual(data, [])
        finally:
            os.unlink(tmp_path)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_csv("/nonexistent/path.csv")


if __name__ == "__main__":
    unittest.main()
