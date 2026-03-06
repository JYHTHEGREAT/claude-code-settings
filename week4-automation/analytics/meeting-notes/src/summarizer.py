import re

ACTION_PATTERN = re.compile(
    r"[-·]\s*(.+?)[:：]\s*(.+?)(?:할 것|필요|완료)",
)
DECISION_PATTERN = re.compile(r"[-·]\s*(.+)")


def extract_action_items(text: str) -> list[dict]:
    """액션 아이템을 추출한다. 패턴: '- 담당자: 내용 ~할 것/필요/완료'."""
    if not text.strip():
        return []

    section_match = re.search(r"\[액션 아이템\](.*?)(?:\[|$)", text, re.DOTALL)
    if not section_match:
        return []

    section_text = section_match.group(1)
    items = []
    for match in ACTION_PATTERN.finditer(section_text):
        owner = match.group(1).strip()
        task = match.group(2).strip()
        items.append({"owner": owner, "task": task})

    return items


def extract_decisions(text: str) -> list[str]:
    """결정 사항을 추출한다."""
    if not text.strip():
        return []

    section_match = re.search(r"\[결정\](.*?)(?:\[|$)", text, re.DOTALL)
    if not section_match:
        return []

    section_text = section_match.group(1)
    decisions = []
    for match in DECISION_PATTERN.finditer(section_text):
        decision = match.group(1).strip()
        if decision:
            decisions.append(decision)

    return decisions


def generate_summary(sections: dict[str, str]) -> str:
    """섹션 dict를 받아 마크다운 요약 리포트를 생성한다."""
    if not sections:
        return "# 회의록 요약\n\n데이터 없음\n"

    lines = ["# 회의록 요약", ""]

    if "참석자" in sections:
        lines.extend(["## 참석자", sections["참석자"], ""])

    if "안건" in sections:
        lines.extend(["## 안건", sections["안건"], ""])

    full_text = "\n".join(f"[{k}]\n{v}" for k, v in sections.items())

    decisions = extract_decisions(full_text)
    if decisions:
        lines.extend(["## 결정 사항", ""])
        for d in decisions:
            lines.append(f"- {d}")
        lines.append("")

    action_items = extract_action_items(full_text)
    if action_items:
        lines.extend(["## 액션 아이템", ""])
        lines.append("| 담당자 | 할 일 |")
        lines.append("|--------|-------|")
        for item in action_items:
            lines.append(f"| {item['owner']} | {item['task']} |")
        lines.append("")

    return "\n".join(lines) + "\n"
