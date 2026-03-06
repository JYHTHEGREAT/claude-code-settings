import re


def load_text(filepath: str, encoding: str = "utf-8") -> str:
    """텍스트 파일을 읽어 문자열로 반환한다."""
    with open(filepath, "r", encoding=encoding) as f:
        return f.read()


def split_sections(text: str) -> dict[str, str]:
    """[섹션명] 패턴으로 텍스트를 분리하여 dict로 반환한다."""
    if not text.strip():
        return {}

    pattern = re.compile(r"\[(.+?)\]")
    sections: dict[str, str] = {}
    matches = list(pattern.finditer(text))

    for i, match in enumerate(matches):
        section_name = match.group(1)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()
        sections[section_name] = content

    return sections
