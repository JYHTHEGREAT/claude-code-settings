# Project CLAUDE.md — Claude Code Automation Settings

## Role & Context
- 나는 AI 자동화에 관심 있는 개발자이며, 반복 업무를 Claude Code로 효율화하는 것이 목표다.
- 주로 Python, JavaScript/TypeScript 기반 프로젝트를 다룬다.
- Git 기반 버전 관리와 GitHub 협업 워크플로우를 따른다.

## Core Principles
- 변경은 요청된 범위만. 관련 없는 코드, 주석, 포맷은 건드리지 않는다.
- 문제를 완전히 해결하는 최소한의 코드만 작성한다.
- 의도가 불확실하면 구현 전에 먼저 확인한다.
- 보안 취약점(인젝션, XSS 등)을 절대 도입하지 않는다.

## Coding Standards
- 들여쓰기: 스페이스 4칸 (Python), 스페이스 2칸 (JS/TS)
- 변수/함수명: snake_case (Python), camelCase (JS/TS)
- 파일 인코딩: UTF-8
- 줄바꿈: LF

## Communication
- 한국어로 응답한다.
- 기술 용어는 원어 그대로 사용한다 (예: commit, push, hook).
- 간결하고 핵심만 전달한다.

## Modular Rules
> 상세 규칙은 `.claude/rules/` 폴더의 개별 파일을 참조한다.

- `coding-style.md` — 코딩 컨벤션 상세
- `git-workflow.md` — Git 워크플로우 규칙
- `documentation.md` — 문서 작성 규칙
- `security.md` — 보안 관련 규칙
