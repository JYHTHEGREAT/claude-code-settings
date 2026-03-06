#!/bin/bash
# SessionStart Hook: 세션 시작 시 환경 체크 및 인사
# 현재 작업 환경 정보를 출력하여 컨텍스트를 빠르게 파악한다.

echo "=== Claude Code 세션 시작 ==="
echo "시간: $(date '+%Y-%m-%d %H:%M:%S')"
echo "디렉토리: $(pwd)"

if command -v git &> /dev/null && git rev-parse --is-inside-work-tree &> /dev/null 2>&1; then
    BRANCH=$(git branch --show-current 2>/dev/null)
    echo "Git 브랜치: $BRANCH"
fi

if command -v node &> /dev/null; then
    echo "Node.js: $(node -v)"
fi

if command -v python &> /dev/null; then
    echo "Python: $(python --version 2>&1)"
fi

echo "=============================="
exit 0
