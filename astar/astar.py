"""A* pathfinding on a 2D grid."""
from __future__ import annotations

import heapq
import math
from typing import Callable, Dict, List, Optional, Sequence, Set, Tuple

Cell = Tuple[int, int]


def manhattan(a: Cell, b: Cell) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean(a: Cell, b: Cell) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def find_path(
    grid: Sequence[Sequence[int]],
    start: Cell,
    goal: Cell,
    *,
    heuristic: Callable[[Cell, Cell], float] = manhattan,
    diagonal: bool = False,
) -> Optional[List[Cell]]:
    """Return the shortest path from ``start`` to ``goal`` or ``None``.

    ``grid`` is a sequence of rows; cells with truthy values are obstacles.
    Coordinates are ``(x, y)`` with ``y`` indexing rows.
    """
    if not grid or not grid[0]:
        return None
    height, width = len(grid), len(grid[0])
    if not _in_bounds(start, width, height) or not _in_bounds(goal, width, height):
        return None
    if grid[start[1]][start[0]] or grid[goal[1]][goal[0]]:
        return None
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if diagonal:
        moves += [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    open_set: List[Tuple[float, int, Cell]] = [(0.0, 0, start)]
    counter = 1
    came_from: Dict[Cell, Cell] = {}
    g_score: Dict[Cell, float] = {start: 0.0}
    closed: Set[Cell] = set()

    while open_set:
        _, _, current = heapq.heappop(open_set)
        if current == goal:
            return _reconstruct(came_from, current)
        if current in closed:
            continue
        closed.add(current)
        cx, cy = current
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if grid[ny][nx]:
                continue
            step = math.hypot(dx, dy)        # 1 for cardinal, sqrt(2) for diagonal
            tentative = g_score[current] + step
            neighbour = (nx, ny)
            if tentative < g_score.get(neighbour, math.inf):
                g_score[neighbour] = tentative
                came_from[neighbour] = current
                f = tentative + heuristic(neighbour, goal)
                heapq.heappush(open_set, (f, counter, neighbour))
                counter += 1
    return None


def _in_bounds(cell: Cell, width: int, height: int) -> bool:
    x, y = cell
    return 0 <= x < width and 0 <= y < height


def _reconstruct(came_from: Dict[Cell, Cell], current: Cell) -> List[Cell]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
