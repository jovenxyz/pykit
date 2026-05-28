"""Task data model."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: str = field(default_factory=_now_iso)
