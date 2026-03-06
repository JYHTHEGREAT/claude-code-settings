import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from src.parser import load_text, split_sections
from src.summarizer import generate_summary


def main():
    parser = argparse.ArgumentParser(description="회의록 자동 정리기")
    parser.add_argument("text_file", help="회의록 텍스트 파일 경로")
    parser.add_argument("-o", "--output", help="요약 저장 경로 (미지정 시 터미널 출력)")
    args = parser.parse_args()

    text = load_text(args.text_file)
    sections = split_sections(text)
    summary = generate_summary(sections)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"요약 저장 완료: {args.output}")
    else:
        print(summary)


if __name__ == "__main__":
    main()
