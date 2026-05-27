"""Command-line interface for the calculator."""
from __future__ import annotations

import argparse
import sys
from typing import List, Optional

from calc.api import evaluate
from calc.errors import CalcError


def _format(result: float) -> str:
    if result == int(result):
        return str(int(result))
    return str(result)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate an arithmetic expression."
    )
    parser.add_argument("expression", help="expression to evaluate")
    args = parser.parse_args(argv)

    try:
        print(_format(evaluate(args.expression)))
    except CalcError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
