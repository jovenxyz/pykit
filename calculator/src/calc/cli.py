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


def run_repl() -> None:
    print("calc REPL - type 'quit' to exit")
    while True:
        try:
            line = input("> ")
        except EOFError:
            print()
            break
        command = line.strip()
        if command in ("quit", "exit"):
            break
        if not command:
            continue
        try:
            print(_format(evaluate(command)))
        except CalcError as error:
            print(f"error: {error}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate an arithmetic expression."
    )
    parser.add_argument(
        "expression", nargs="?", help="expression to evaluate (omit for a REPL)"
    )
    args = parser.parse_args(argv)

    if args.expression is None:
        run_repl()
        return 0

    try:
        print(_format(evaluate(args.expression)))
    except CalcError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
