import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from src.parser import load_csv
from src.reporter import generate_report


def main():
    parser = argparse.ArgumentParser(description="CSV 매출 데이터 분석 리포트 생성기")
    parser.add_argument("csv_file", help="분석할 CSV 파일 경로")
    parser.add_argument("-o", "--output", help="리포트 저장 경로 (미지정 시 터미널 출력)")
    args = parser.parse_args()

    data = load_csv(args.csv_file)
    report = generate_report(data)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"리포트 저장 완료: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
