"""In-memory task manager backed by JSON storage."""
from __future__ import annotations

from pathlib import Path
from typing import List

from tasks.errors import TaskNotFoundError
from tasks.models import Task
from tasks.storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self, path: Path) -> None:
        self._path = Path(path)
        self._tasks: List[Task] = load_tasks(self._path)

    def _next_id(self) -> int:
        return max((task.id for task in self._tasks), default=0) + 1

    def _save(self) -> None:
        save_tasks(self._path, self._tasks)

    def add(self, title: str) -> Task:
        task = Task(id=self._next_id(), title=title)
        self._tasks.append(task)
        self._save()
        return task

    def list(self) -> List[Task]:
        return list(self._tasks)
