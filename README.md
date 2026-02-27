# Claude Code Automation Settings

특이점 빌더스 3주차 과제 — Claude Code 자동화 시스템 세팅

## 프로젝트 구조

```
qjc_practice/
├── .claude/
│   ├── CLAUDE.md              # 프로젝트 핵심 규칙
│   ├── settings.json          # Hooks & MCP 설정
│   └── rules/
│       ├── coding-style.md    # 코딩 컨벤션
│       ├── git-workflow.md    # Git 워크플로우
│       ├── documentation.md   # 문서 작성 규칙
│       └── security.md        # 보안 규칙
├── hooks/
│   ├── pre-tool-use-guard.sh      # 위험 명령어 차단 Hook
│   ├── post-tool-use-logger.sh    # 파일 수정 로그 기록 Hook
│   └── session-start-greeting.sh  # 세션 시작 환경 체크 Hook
├── .gitignore
└── README.md
```

## 설정 내용

### CLAUDE.md + Rules
- **CLAUDE.md**: 역할, 핵심 원칙, 코딩 표준, 커뮤니케이션 규칙 정의
- **Rules 모듈화**: 코딩 스타일, Git 워크플로우, 문서화, 보안 규칙을 개별 파일로 분리

### Hooks (3개)
| Hook | 이벤트 | 기능 |
|------|--------|------|
| `pre-tool-use-guard.sh` | PreToolUse | `rm -rf`, `git push --force` 등 위험 명령어 자동 차단 |
| `post-tool-use-logger.sh` | PostToolUse | 파일 수정(Write/Edit) 시 변경 로그 자동 기록 |
| `session-start-greeting.sh` | SessionStart | 세션 시작 시 환경 정보(Git 브랜치, 런타임 버전) 출력 |

### MCP 연동
- `@anthropic-ai/mcp-filesystem` 서버 설정 포함
