import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.analyzer import (
    total_sales,
    sales_by_category,
    sales_by_month,
    top_category,
    summary_stats,
)

SAMPLE_DATA = [
    {"date": "2024-01-05", "category": "Electronics", "amount": 100000.0},
    {"date": "2024-01-12", "category": "Clothing", "amount": 50000.0},
    {"date": "2024-02-03", "category": "Electronics", "amount": 200000.0},
    {"date": "2024-02-10", "category": "Food", "amount": 30000.0},
    {"date": "2024-03-15", "category": "Clothing", "amount": 80000.0},
]


class TestTotalSales(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total_sales(SAMPLE_DATA), 460000.0)

    def test_empty(self):
        self.assertEqual(total_sales([]), 0.0)


class TestSalesByCategory(unittest.TestCase):
    def test_categories(self):
        result = sales_by_category(SAMPLE_DATA)
        self.assertEqual(result["Electronics"], 300000.0)
        self.assertEqual(result["Clothing"], 130000.0)
        self.assertEqual(result["Food"], 30000.0)

    def test_empty(self):
        self.assertEqual(sales_by_category([]), {})


class TestSalesByMonth(unittest.TestCase):
    def test_months(self):
        result = sales_by_month(SAMPLE_DATA)
        self.assertEqual(result["2024-01"], 150000.0)
        self.assertEqual(result["2024-02"], 230000.0)
        self.assertEqual(result["2024-03"], 80000.0)

    def test_empty(self):
        self.assertEqual(sales_by_month([]), {})


class TestTopCategory(unittest.TestCase):
    def test_top(self):
        self.assertEqual(top_category(SAMPLE_DATA), "Electronics")

    def test_empty(self):
        self.assertEqual(top_category([]), "")


class TestSummaryStats(unittest.TestCase):
    def test_stats(self):
        stats = summary_stats(SAMPLE_DATA)
        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["total"], 460000.0)
        self.assertEqual(stats["average"], 92000.0)
        self.assertEqual(stats["max"], 200000.0)
        self.assertEqual(stats["min"], 30000.0)

    def test_empty(self):
        stats = summary_stats([])
        self.assertEqual(stats["count"], 0)
        self.assertEqual(stats["total"], 0.0)


if __name__ == "__main__":
    unittest.main()
