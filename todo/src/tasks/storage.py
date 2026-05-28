"""Persist tasks to a JSON file."""
from __future__ import annotations

import json
from pathlib import Path
from typing import List

from tasks.models import Task


def load_tasks(path: Path) -> List[Task]:
    if not path.exists():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [Task.from_dict(item) for item in raw]


def save_tasks(path: Path, tasks: List[Task]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [task.to_dict() for task in tasks]
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
