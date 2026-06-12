"""Knight's tour on an n x n chess board using Warnsdorff's heuristic."""
from __future__ import annotations

from typing import List, Optional, Tuple

Cell = Tuple[int, int]
_MOVES = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1),
]


def _in_bounds(x: int, y: int, n: int) -> bool:
    return 0 <= x < n and 0 <= y < n


def _degree(x: int, y: int, n: int, visited) -> int:
    count = 0
    for dx, dy in _MOVES:
        nx, ny = x + dx, y + dy
        if _in_bounds(nx, ny, n) and not visited[ny][nx]:
            count += 1
    return count


def find_tour(n: int, start: Cell = (0, 0)) -> Optional[List[Cell]]:
    """Return a knight's tour visiting every square exactly once.

    Uses Warnsdorff's rule (always step to the square with the fewest
    onward moves). Returns ``None`` if no tour was found.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    sx, sy = start
    if not _in_bounds(sx, sy, n):
        raise ValueError(f"start out of board for n={n}: {start}")
    visited = [[False] * n for _ in range(n)]
    visited[sy][sx] = True
    path: List[Cell] = [(sx, sy)]
    for _ in range(n * n - 1):
        x, y = path[-1]
        candidates = []
        for dx, dy in _MOVES:
            nx, ny = x + dx, y + dy
            if _in_bounds(nx, ny, n) and not visited[ny][nx]:
                candidates.append((_degree(nx, ny, n, visited), nx, ny))
        if not candidates:
            return None
        candidates.sort()
        _, nx, ny = candidates[0]
        visited[ny][nx] = True
        path.append((nx, ny))
    return path
