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

    sub.add_parser("list", help="list tasks")

    done = sub.add_parser("done", help="mark a task complete")
    done.add_argument("id", type=int, help="task id")

    remove = sub.add_parser("remove", help="delete a task")
    remove.add_argument("id", type=int, help="task id")

    sub.add_parser("clear", help="remove completed tasks")
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
        elif args.command == "list":
            tasks = manager.list()
            if not tasks:
                print("no tasks")
            for task in tasks:
                marker = "x" if task.done else " "
                print(f"[{marker}] #{task.id} {task.title}")
        elif args.command == "done":
            task = manager.complete(args.id)
            print(f"completed #{task.id}: {task.title}")
        elif args.command == "remove":
            manager.remove(args.id)
            print(f"removed #{args.id}")
        elif args.command == "clear":
            count = manager.clear_completed()
            print(f"cleared {count} completed task(s)")
    except TaskError as error:
        print(f"error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
