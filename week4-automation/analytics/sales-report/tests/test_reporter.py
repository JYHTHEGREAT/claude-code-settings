import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.reporter import generate_report

SAMPLE_DATA = [
    {"date": "2024-01-05", "category": "Electronics", "amount": 100000.0},
    {"date": "2024-01-12", "category": "Clothing", "amount": 50000.0},
    {"date": "2024-02-03", "category": "Electronics", "amount": 200000.0},
]


class TestGenerateReport(unittest.TestCase):
    def test_contains_title(self):
        report = generate_report(SAMPLE_DATA)
        self.assertIn("#", report)

    def test_contains_total(self):
        report = generate_report(SAMPLE_DATA)
        self.assertIn("350,000", report)

    def test_contains_category_section(self):
        report = generate_report(SAMPLE_DATA)
        self.assertIn("Electronics", report)
        self.assertIn("Clothing", report)

    def test_contains_monthly_section(self):
        report = generate_report(SAMPLE_DATA)
        self.assertIn("2024-01", report)
        self.assertIn("2024-02", report)

    def test_empty_data(self):
        report = generate_report([])
        self.assertIn("데이터 없음", report)

    def test_markdown_format(self):
        report = generate_report(SAMPLE_DATA)
        self.assertTrue(report.startswith("#"))


if __name__ == "__main__":
    unittest.main()
