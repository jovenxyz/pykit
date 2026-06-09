"""Generate random perfect mazes via iterative depth-first search."""
from __future__ import annotations

import random
from typing import Dict, List, Optional

Cell = Dict[str, bool]
Grid = List[List[Cell]]

_OPPOSITE = {"N": "S", "S": "N", "E": "W", "W": "E"}
_DELTAS = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def generate(
    width: int,
    height: int,
    rng: Optional[random.Random] = None,
) -> Grid:
    """Return a perfect maze as a 2D list of cell dicts.

    Each cell is ``{"N": bool, "E": bool, "S": bool, "W": bool}`` where
    ``True`` means the wall is intact. A perfect maze has exactly one path
    between any pair of cells.
    """
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    generator = rng if rng is not None else random
    grid: Grid = [
        [{"N": True, "E": True, "S": True, "W": True} for _ in range(width)]
        for _ in range(height)
    ]
    visited = [[False] * width for _ in range(height)]
    _carve(0, 0, grid, visited, width, height, generator)
    return grid


def _carve(
    start_x: int,
    start_y: int,
    grid: Grid,
    visited: List[List[bool]],
    width: int,
    height: int,
    generator,
) -> None:
    stack = [(start_x, start_y)]
    visited[start_y][start_x] = True
    while stack:
        x, y = stack[-1]
        directions = ["N", "E", "S", "W"]
        generator.shuffle(directions)
        for direction in directions:
            dx, dy = _DELTAS[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
                grid[y][x][direction] = False
                grid[ny][nx][_OPPOSITE[direction]] = False
                visited[ny][nx] = True
                stack.append((nx, ny))
                break
        else:
            stack.pop()


def render(grid: Grid) -> str:
    """Render the maze as ASCII art (three columns wide per cell)."""
    height = len(grid)
    width = len(grid[0]) if grid else 0
    lines: List[str] = ["+" + "---+" * width]
    for y in range(height):
        row_top = "|"
        row_bottom = "+"
        for x in range(width):
            row_top += "   "
            row_top += " " if not grid[y][x]["E"] else "|"
            row_bottom += "---" if grid[y][x]["S"] else "   "
            row_bottom += "+"
        lines.append(row_top)
        lines.append(row_bottom)
    return "\n".join(lines)
