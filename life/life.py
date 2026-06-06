"""Conway's Game of Life on an unbounded grid."""
from __future__ import annotations

from typing import Dict, FrozenSet, Iterable, Set, Tuple

Cell = Tuple[int, int]


def step(live: Iterable[Cell]) -> FrozenSet[Cell]:
    """Advance the board one generation.

    The board is represented as the set of live ``(x, y)`` cells, so the
    playing field is effectively infinite.
    """
    live_set: Set[Cell] = set(live)
    neighbour_counts: Dict[Cell, int] = {}
    for x, y in live_set:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                key = (x + dx, y + dy)
                neighbour_counts[key] = neighbour_counts.get(key, 0) + 1
    return frozenset(
        cell
        for cell, count in neighbour_counts.items()
        if count == 3 or (count == 2 and cell in live_set)
    )


def run(live: Iterable[Cell], generations: int) -> FrozenSet[Cell]:
    """Step the board ``generations`` times."""
    if generations < 0:
        raise ValueError("generations must be non-negative")
    state = frozenset(live)
    for _ in range(generations):
        state = step(state)
    return state
