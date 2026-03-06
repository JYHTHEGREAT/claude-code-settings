from src.analyzer import (
    total_sales,
    sales_by_category,
    sales_by_month,
    top_category,
    summary_stats,
)


def generate_report(data: list[dict]) -> str:
    """매출 데이터를 분석하여 마크다운 리포트를 생성한다."""
    if not data:
        return "# 매출 리포트\n\n데이터 없음\n"

    stats = summary_stats(data)
    by_category = sales_by_category(data)
    by_month = sales_by_month(data)
    top_cat = top_category(data)

    lines = [
        f"# 매출 리포트",
        "",
        "## 요약",
        f"- 총 매출: {stats['total']:,.0f}원",
        f"- 거래 건수: {stats['count']}건",
        f"- 평균 거래 금액: {stats['average']:,.0f}원",
        f"- 최대 거래: {stats['max']:,.0f}원",
        f"- 최소 거래: {stats['min']:,.0f}원",
        "",
        "## 카테고리별 매출",
        "",
        "| 카테고리 | 매출 |",
        "|----------|------|",
    ]

    for cat, amount in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"| {cat} | {amount:,.0f}원 |")

    lines.extend([
        "",
        "## 월별 매출 추이",
        "",
        "| 월 | 매출 |",
        "|----|------|",
    ])

    for month, amount in sorted(by_month.items()):
        lines.append(f"| {month} | {amount:,.0f}원 |")

    lines.extend([
        "",
        "## 주요 인사이트",
        f"- 최고 매출 카테고리: **{top_cat}** ({by_category[top_cat]:,.0f}원)",
    ])

    best_month = max(by_month, key=by_month.get)
    lines.append(f"- 최고 매출 월: **{best_month}** ({by_month[best_month]:,.0f}원)")

    return "\n".join(lines) + "\n"
