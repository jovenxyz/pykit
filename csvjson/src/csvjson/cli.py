"""CSV/JSON conversion command-line tool."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from csvjson.convert import csv_to_json, json_to_csv


def _infer(path: Path) -> str:
    return "csv" if path.suffix.lower() == ".json" else "json"


def _convert(path: Path, target: str) -> str:
    text = path.read_text(encoding="utf-8")
    if target == "json":
        return csv_to_json(text)
    return json_to_csv(text)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Convert between CSV and JSON.")
    parser.add_argument("path", help="input file (.csv or .json)")
    parser.add_argument(
        "--to", choices=("json", "csv"), help="output format (inferred if omitted)"
    )
    args = parser.parse_args(argv)

    path = Path(args.path)
    target = args.to or _infer(path)
    try:
        sys.stdout.write(_convert(path, target))
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
