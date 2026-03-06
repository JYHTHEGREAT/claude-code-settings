import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.summarizer import extract_action_items, extract_decisions, generate_summary

SAMPLE_TEXT = """[논의]
이영희: Redis 캐싱 도입을 검토할 필요가 있습니다. 담당: 이영희
박민수: 디자인 시안은 이번 주 금요일까지 전달할 것입니다.

[결정]
- 대시보드 MVP 마감일: 3월 31일
- API 캐싱 레이어 도입 확정

[액션 아이템]
- 박민수: 디자인 시안 금요일까지 전달할 것
- 이영희: Redis 캐싱 PoC 다음 주 수요일까지 완료할 것
- 김철수: 스프린트 백로그 정리 필요
"""


class TestExtractActionItems(unittest.TestCase):
    def test_extract_items(self):
        items = extract_action_items(SAMPLE_TEXT)
        self.assertGreaterEqual(len(items), 3)
        owners = [item["owner"] for item in items]
        self.assertIn("박민수", owners)
        self.assertIn("이영희", owners)

    def test_empty_text(self):
        items = extract_action_items("")
        self.assertEqual(items, [])

    def test_no_action_items(self):
        items = extract_action_items("[논의]\n일반적인 내용입니다.")
        self.assertEqual(items, [])


class TestExtractDecisions(unittest.TestCase):
    def test_extract(self):
        decisions = extract_decisions(SAMPLE_TEXT)
        self.assertGreaterEqual(len(decisions), 2)
        self.assertTrue(any("MVP" in d for d in decisions))

    def test_empty(self):
        decisions = extract_decisions("")
        self.assertEqual(decisions, [])


class TestGenerateSummary(unittest.TestCase):
    def test_contains_sections(self):
        sections = {
            "참석자": "김철수, 이영희",
            "안건": "1. 대시보드\n2. API",
            "논의": SAMPLE_TEXT,
            "결정": "- MVP 마감\n- 캐싱 도입",
        }
        summary = generate_summary(sections)
        self.assertIn("#", summary)
        self.assertIn("참석자", summary)
        self.assertIn("액션 아이템", summary)

    def test_empty_sections(self):
        summary = generate_summary({})
        self.assertIn("데이터 없음", summary)


if __name__ == "__main__":
    unittest.main()
