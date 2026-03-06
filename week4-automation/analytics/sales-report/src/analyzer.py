from collections import defaultdict


def total_sales(data: list[dict]) -> float:
    """총 매출 합계를 반환한다."""
    return sum(row["amount"] for row in data)


def sales_by_category(data: list[dict]) -> dict[str, float]:
    """카테고리별 매출 합계를 반환한다."""
    result: dict[str, float] = defaultdict(float)
    for row in data:
        result[row["category"]] += row["amount"]
    return dict(result)


def sales_by_month(data: list[dict]) -> dict[str, float]:
    """월별(YYYY-MM) 매출 합계를 반환한다."""
    result: dict[str, float] = defaultdict(float)
    for row in data:
        month_key = row["date"][:7]
        result[month_key] += row["amount"]
    return dict(result)


def top_category(data: list[dict]) -> str:
    """최고 매출 카테고리명을 반환한다."""
    by_cat = sales_by_category(data)
    if not by_cat:
        return ""
    return max(by_cat, key=by_cat.get)


def summary_stats(data: list[dict]) -> dict:
    """거래 건수, 합계, 평균, 최대, 최소를 반환한다."""
    if not data:
        return {"count": 0, "total": 0.0, "average": 0.0, "max": 0.0, "min": 0.0}

    amounts = [row["amount"] for row in data]
    return {
        "count": len(amounts),
        "total": sum(amounts),
        "average": sum(amounts) / len(amounts),
        "max": max(amounts),
        "min": min(amounts),
    }
