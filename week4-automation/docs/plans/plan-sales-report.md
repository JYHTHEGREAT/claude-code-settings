# Plan: 4차시 과제 — 자동화 시스템 개발 (가산점 풀 커버)

## 목표
2개의 자동화 시스템(매출 리포트 생성기 + 회의록 정리기)을 개발 파이프라인으로 구현하고, GitHub에 PR/Merge까지 완료하여 **100점 + 가산점 15점** 확보.

## 접근 전략
Python 표준 라이브러리 중심으로 2개 시스템을 `week4-automation/analytics/` 하위에 구현한다.
- **시스템 A**: 매출 리포트 생성기 (CSV → 분석 → 마크다운 리포트) — "분석" 분야
- **시스템 B**: 회의록 정리기 (텍스트 → 요약 + 액션 아이템 추출) — "업무" 분야
- 두 시스템 모두 순수 Python + CLI. TDD 친화적, 설치 간편, 결과물 명확.
- 외부 의존성 없음 (pandas, numpy, AI API 미사용)

## 가산점 전략
| 가산점 항목 | 점수 | 달성 방법 |
|-------------|------|-----------|
| 2개 이상 시스템 개발 | +5점 | 매출 리포트 + 회의록 정리기 |
| Verify Loop 활용 | +5점 | 시스템 B에서 `/verify-loop` 실행 |
| 상세 스크린샷 | +5점 | /plan, /tdd, /code-review, /handoff-verify, /verify-loop, /commit-push-pr 총 6장+ |

## 선행 조건
- [x] JYH-forge 설치 및 MCP 세팅 확인 완료
- [ ] 현재 브랜치에서 분기: `feature/automation-systems`
- [ ] 기존 테스트 없음 (신규 개발)

## Phase 의존성
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5
- Phase 2 진행 조건: Phase 1 테스트 전부 통과
- Phase 3 진행 조건: Phase 2 테스트 전부 통과 (시스템 A 완성)
- Phase 4 진행 조건: Phase 3 테스트 전부 통과
- Phase 5 진행 조건: Phase 4 테스트 전부 통과 (시스템 B 완성)

---

## 시스템 A: 매출 리포트 생성기

### Phase 1: 데이터 파싱
- [ ] `week4-automation/analytics/sales-report/` — 폴더 구조 생성
- [ ] `week4-automation/analytics/sales-report/src/__init__.py` — 패키지 초기화
- [ ] `week4-automation/analytics/sales-report/src/parser.py` — CSV 파싱 모듈
  - `load_csv(filepath: str) -> list[dict]`: CSV 파일 읽기
  - `validate_row(row: dict) -> bool`: 필수 컬럼 검증 (date, category, amount)
  - 잘못된 행은 건너뛰고 경고 로그 출력
- [ ] `week4-automation/analytics/sales-report/data/sample_sales.csv` — 샘플 데이터 (20~30행)
- [ ] `week4-automation/analytics/sales-report/tests/test_parser.py` — 파서 테스트 (TDD: 먼저 작성)
  - 정상 CSV 파싱 / 빈 파일 / 잘못된 행 건너뛰기 / 필수 컬럼 누락
- 근거: 데이터 입력 계층을 먼저 확립해야 분석 로직 구현 가능
- 검증: `python -m pytest week4-automation/analytics/sales-report/tests/test_parser.py` 전부 통과

### Phase 2: 분석 로직 + 리포트 + CLI
- [ ] `week4-automation/analytics/sales-report/src/analyzer.py` — 분석 모듈
  - `total_sales(data) -> float`: 총 매출
  - `sales_by_category(data) -> dict[str, float]`: 카테고리별 매출
  - `sales_by_month(data) -> dict[str, float]`: 월별 매출
  - `top_category(data) -> str`: 최고 매출 카테고리
  - `summary_stats(data) -> dict`: 평균/최대/최소 거래 금액
- [ ] `week4-automation/analytics/sales-report/src/reporter.py` — 마크다운 리포트 생성
  - `generate_report(data) -> str`: 요약, 카테고리별, 월별, 인사이트 섹션
- [ ] `week4-automation/analytics/sales-report/main.py` — CLI 진입점 (argparse)
  - `python main.py data/sample_sales.csv` → 터미널 출력
  - `python main.py data/sample_sales.csv -o report.md` → 파일 저장
- [ ] `week4-automation/analytics/sales-report/tests/test_analyzer.py` — 분석 테스트 (TDD)
  - 총 매출 / 카테고리별 / 월별 / 빈 데이터
- [ ] `week4-automation/analytics/sales-report/tests/test_reporter.py` — 리포트 테스트 (TDD)
  - 필수 섹션 포함 / 마크다운 형식
- 검증: 전체 테스트 통과 + CLI 실행 결과 확인

---

## 시스템 B: 회의록 정리기

### Phase 3: 텍스트 파싱 & 요약
- [ ] `week4-automation/analytics/meeting-notes/` — 폴더 구조 생성
- [ ] `week4-automation/analytics/meeting-notes/src/__init__.py` — 패키지 초기화
- [ ] `week4-automation/analytics/meeting-notes/src/parser.py` — 회의록 텍스트 파싱
  - `load_text(filepath: str) -> str`: 텍스트 파일 읽기
  - `split_sections(text: str) -> dict[str, str]`: 섹션 분리 (참석자, 안건, 논의, 결정)
- [ ] `week4-automation/analytics/meeting-notes/data/sample_meeting.txt` — 샘플 회의록
- [ ] `week4-automation/analytics/meeting-notes/tests/test_parser.py` — 파서 테스트 (TDD)
  - 정상 파싱 / 빈 파일 / 섹션 누락 처리
- 검증: 파서 테스트 전부 통과

### Phase 4: 요약 + 액션 아이템 추출 + CLI
- [ ] `week4-automation/analytics/meeting-notes/src/summarizer.py` — 요약 모듈
  - `extract_action_items(text: str) -> list[dict]`: 액션 아이템 추출 (패턴: "~ 할 것", "~ 필요", "담당: ~")
  - `extract_decisions(text: str) -> list[str]`: 결정 사항 추출
  - `generate_summary(sections: dict) -> str`: 마크다운 요약 리포트
- [ ] `week4-automation/analytics/meeting-notes/main.py` — CLI 진입점
  - `python main.py data/sample_meeting.txt` → 터미널 출력
  - `python main.py data/sample_meeting.txt -o summary.md` → 파일 저장
- [ ] `week4-automation/analytics/meeting-notes/tests/test_summarizer.py` — 요약 테스트 (TDD)
  - 액션 아이템 추출 정확성 / 결정 사항 추출 / 빈 입력 처리
- 검증: 전체 테스트 통과 + CLI 실행 결과 확인

---

## Phase 5: 검증 & 배포
- [ ] `/code-review` — 두 시스템 코드 품질/보안 검토
- [ ] `/handoff-verify` — 독립 컨텍스트 최종 검증
- [ ] `/verify-loop` — 자동 반복 검증 (**가산점 +5점**)
- [ ] README.md에 4차시 과제 섹션 추가
- [ ] `/commit-push-pr` — GitHub Push + PR + Merge

## 하지 않는 것 (Not Doing)
- **pandas/numpy/AI API 등 외부 라이브러리 사용하지 않음** — 표준 라이브러리로 충분
- **웹 UI, 그래프 시각화 만들지 않음** — CLI 텍스트 리포트로 충분
- **데이터베이스 연동하지 않음** — 파일 입력만 지원
- **자연어 처리(NLP) 라이브러리 사용하지 않음** — 정규식 + 패턴 매칭으로 구현
- **기존 3주차 파일(hooks/, .claude/rules/) 수정하지 않음**
- **README.md 전체 재작성하지 않음** — 새 섹션만 추가

## 롤백 계획
- 전체 작업은 `feature/automation-systems` 브랜치에서 수행
- Phase N 실패 시: `git stash` 또는 해당 Phase 커밋으로 `git reset --soft`
- 최악의 경우: 브랜치 삭제 후 master에서 재분기

## 리스크
| 리스크 | 확률 | 대응 |
|--------|------|------|
| CSV 인코딩 이슈 (cp949 등) | 중 | encoding 파라미터 지원, UTF-8 기본값 |
| 날짜 형식 불일치 | 중 | YYYY-MM-DD 형식 강제, 파싱 실패 시 행 건너뛰기 |
| 회의록 패턴 매칭 부정확 | 중 | 샘플 데이터에 맞춘 패턴 + 폴백 처리 |
| 테스트 환경 (pytest 미설치) | 저 | unittest 표준 라이브러리 사용으로 회피 |

## 커밋 계획
- Phase 1: `feat(analytics): 매출 리포트 CSV 파서 구현`
- Phase 2: `feat(analytics): 매출 리포트 분석기 및 CLI 구현`
- Phase 3: `feat(analytics): 회의록 정리기 파서 구현`
- Phase 4: `feat(analytics): 회의록 요약 및 CLI 구현`
- Phase 5: `docs: README 업데이트 및 최종 검증`
- 최종: `/commit-push-pr`로 PR 생성 및 Merge

## 파이프라인 실행 순서 & 스크린샷 계획
| 단계 | 명령어 | 스크린샷 | 비고 |
|------|--------|----------|------|
| 1 | `/plan` | SS-1: plan 결과 | 현재 문서 |
| 2 | `/tdd` (시스템 A) | SS-2: TDD RED→GREEN | 테스트 실행 결과 |
| 3 | `/tdd` (시스템 B) | SS-3: TDD RED→GREEN | 테스트 실행 결과 |
| 4 | `/code-review` | SS-4: 리뷰 결과 | 품질/보안 |
| 5 | `/handoff-verify` | SS-5: 검증 통과 | 독립 검증 |
| 6 | `/verify-loop` | SS-6: 반복 검증 | **가산점** |
| 7 | `/commit-push-pr` | SS-7: PR/Merge | GitHub |

> 총 7장 스크린샷 → 가산점 조건(5장+) 충족

## 폴더 구조 (최종)
```
qjc_practice/
├── week4-automation/              # 4차시 과제
│   ├── analytics/
│   │   ├── sales-report/          # 시스템 A: 매출 리포트 생성기
│   │   │   ├── main.py
│   │   │   ├── data/
│   │   │   │   └── sample_sales.csv
│   │   │   ├── src/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── parser.py
│   │   │   │   ├── analyzer.py
│   │   │   │   └── reporter.py
│   │   │   └── tests/
│   │   │       ├── __init__.py
│   │   │       ├── test_parser.py
│   │   │       ├── test_analyzer.py
│   │   │       └── test_reporter.py
│   │   └── meeting-notes/         # 시스템 B: 회의록 정리기
│   │       ├── main.py
│   │       ├── data/
│   │       │   └── sample_meeting.txt
│   │       ├── src/
│   │       │   ├── __init__.py
│   │       │   ├── parser.py
│   │       │   └── summarizer.py
│   │       └── tests/
│   │           ├── __init__.py
│   │           ├── test_parser.py
│   │           └── test_summarizer.py
│   └── docs/plans/
│       └── plan-sales-report.md
├── .claude/          # (3주차 기존 유지)
├── hooks/            # (3주차 기존 유지)
└── README.md         # (섹션 추가만)
```
