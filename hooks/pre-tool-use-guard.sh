#!/bin/bash
# PreToolUse Hook: 위험 명령어 차단
# rm -rf, git push --force 등 파괴적 명령어를 자동 차단한다.

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if [ "$TOOL_NAME" = "Bash" ] && [ -n "$COMMAND" ]; then
    # 위험 명령어 패턴 목록
    DANGEROUS_PATTERNS=(
        "rm -rf /"
        "rm -rf ~"
        "rm -rf \."
        "git push --force"
        "git push -f"
        "git reset --hard"
        "git clean -fd"
        "DROP TABLE"
        "DROP DATABASE"
        ":(){ :|:& };:"
    )

    for pattern in "${DANGEROUS_PATTERNS[@]}"; do
        if echo "$COMMAND" | grep -qi "$pattern"; then
            echo "BLOCKED: 위험 명령어가 감지되었습니다 → $pattern"
            echo "이 명령은 시스템에 돌이킬 수 없는 손상을 줄 수 있습니다."
            exit 2
        fi
    done
fi

exit 0
