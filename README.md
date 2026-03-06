# Claude Code + JYH-forge 자동화 실습 프로젝트

Claude Code 자동화 시스템 세팅부터 개발 파이프라인 실습까지.

## 자동화 시스템 (2개)

### 1. 매출 리포트 생성기 (Sales Report Generator)
CSV 매출 데이터를 분석하여 마크다운 리포트를 자동 생성합니다.

```bash
cd week4-automation/analytics/sales-report
python main.py data/sample_sales.csv           # 터미널 출력
python main.py data/sample_sales.csv -o report.md  # 파일 저장
```

**기능**: 총 매출, 카테고리별/월별 분석, 최고 매출 카테고리, 인사이트 자동 생성

### 2. 회의록 정리기 (Meeting Notes Summarizer)
회의록 텍스트에서 액션 아이템과 결정 사항을 자동 추출합니다.

```bash
cd week4-automation/analytics/meeting-notes
python main.py data/sample_meeting.txt            # 터미널 출력
python main.py data/sample_meeting.txt -o summary.md  # 파일 저장
```

**기능**: 섹션 분리, 액션 아이템 추출 (담당자 + 할 일), 결정 사항 추출, 마크다운 요약

## 개발 파이프라인

| 단계 | 명령어 | 결과 |
|------|--------|------|
| 1 | /plan | 체크리스트형 구현 계획 수립 |
| 2 | /tdd | RED -> GREEN -> IMPROVE (40개 테스트) |
| 3 | /code-review | 보안 + 품질 ALL PASS |
| 4 | /handoff-verify | 독립 컨텍스트 검증 PASS |
| 5 | /verify-loop | 3회 반복 검증 ALL PASS |
| 6 | /commit-push-pr | PR 생성 + Merge 완료 |

## 테스트

```bash
# 매출 리포트 (27개 테스트)
cd week4-automation/analytics/sales-report
python -m unittest discover -s tests -v

# 회의록 정리기 (13개 테스트)
cd week4-automation/analytics/meeting-notes
python -m unittest discover -s tests -v
```

## 프로젝트 구조

```
qjc_practice/
├── week4-automation/              # 4차시: 자동화 시스템
│   ├── analytics/
│   │   ├── sales-report/          # 매출 리포트 생성기
│   │   │   ├── main.py            # CLI 진입점
│   │   │   ├── data/              # 샘플 CSV 데이터
│   │   │   ├── src/               # parser, analyzer, reporter
│   │   │   └── tests/             # 27개 유닛 테스트
│   │   └── meeting-notes/         # 회의록 정리기
│   │       ├── main.py            # CLI 진입점
│   │       ├── data/              # 샘플 회의록
│   │       ├── src/               # parser, summarizer
│   │       └── tests/             # 13개 유닛 테스트
│   ├── docs/plans/                # 개발 계획 문서
│   └── screenshots/               # 파이프라인 스크린샷
├── week3-settings/                # 3차시: Claude Code 자동화 세팅
│   ├── hooks/                     # Pre/Post Hook 스크립트
│   └── screenshots/               # 3차시 스크린샷
├── .claude/                       # 프로젝트 규칙 (CLAUDE.md, rules/)
└── README.md
```

## 기술 스택
- Python 3.13 (표준 라이브러리만 사용, 외부 의존성 없음)
- JYH-forge (Claude Code 자동화 시스템 — claude-forge 커스텀)
- unittest (TDD)
