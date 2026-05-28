"""Command-line interface for the task manager."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import List, Optional

from tasks.errors import TaskError
from tasks.manager import TaskManager


def _default_path() -> Path:
    override = os.environ.get("TASKS_FILE")
    if override:
        return Path(override)
    return Path.home() / ".local" / "share" / "tasks" / "tasks.json"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A tiny task manager.")
    parser.add_argument("--file", help="path to the tasks JSON file")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a task")
    add.add_argument("title", help="task description")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    path = Path(args.file) if args.file else _default_path()
    manager = TaskManager(path)

    try:
        if args.command == "add":
            task = manager.add(args.title)
            print(f"added #{task.id}: {task.title}")
    except TaskError as error:
        print(f"error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
