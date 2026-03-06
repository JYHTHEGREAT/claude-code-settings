import csv
import logging
import re
from typing import Any

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED_COLUMNS = {"date", "category", "amount"}


def validate_row(row: dict[str, Any]) -> bool:
    """필수 컬럼 검증: date(YYYY-MM-DD), category, amount(숫자)."""
    if not REQUIRED_COLUMNS.issubset(row.keys()):
        return False

    if not DATE_PATTERN.match(row["date"]):
        return False

    try:
        float(row["amount"])
    except (ValueError, TypeError):
        return False

    return True


def load_csv(filepath: str, encoding: str = "utf-8") -> list[dict]:
    """CSV 파일을 읽어 유효한 행만 dict 리스트로 반환한다."""
    with open(filepath, "r", encoding=encoding) as f:
        reader = csv.DictReader(f)
        results = []
        for i, row in enumerate(reader, start=2):
            if validate_row(row):
                results.append({
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"]),
                })
            else:
                logger.warning("행 %d 건너뜀: %s", i, row)
        return results
