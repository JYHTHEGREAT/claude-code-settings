#!/bin/bash
# PostToolUse Hook: 파일 수정 로그 기록
# Write, Edit 도구 사용 시 변경 내역을 자동으로 로그 파일에 기록한다.

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

LOG_DIR="$HOME/.claude/logs"
LOG_FILE="$LOG_DIR/file-changes.log"

# 로그 디렉토리 생성
mkdir -p "$LOG_DIR"

if [ "$TOOL_NAME" = "Write" ] || [ "$TOOL_NAME" = "Edit" ]; then
    echo "[$TIMESTAMP] $TOOL_NAME → $FILE_PATH" >> "$LOG_FILE"
fi

exit 0
