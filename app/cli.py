import argparse
import sys

from app.reader import read_files
from app.services import build_report
from app.output import print_report


def main() -> None:
    parser = argparse.ArgumentParser(description="YouTube analytics CLI")

    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)

    args = parser.parse_args()

    try:
        data = read_files(args.files)
        report = build_report(args.report, data)
        print_report(report)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
