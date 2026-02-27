# Git Workflow Rules

## Commit
- 커밋 메시지는 한국어 또는 영어로 작성하되, 프로젝트 내 일관성을 유지한다.
- 형식: `<type>: <설명>` (예: `feat: 사용자 인증 기능 추가`)
- type: feat, fix, refactor, docs, test, chore, style
- 커밋 단위는 하나의 논리적 변경에 대응한다.

## Branch
- main: 배포 가능한 안정 브랜치
- feature/*: 기능 개발
- fix/*: 버그 수정
- 브랜치명은 소문자 + 하이픈 구분 (예: feature/user-auth)

## Pull Request
- PR 제목은 70자 이내로 작성한다.
- 본문에 변경 요약과 테스트 계획을 포함한다.
- force push는 사전 확인 없이 절대 실행하지 않는다.

## Safety
- `.env`, 인증 키, 비밀번호가 포함된 파일은 커밋하지 않는다.
- `git add .` 대신 파일을 명시적으로 지정한다.
- `--no-verify` 옵션 사용을 금지한다.
