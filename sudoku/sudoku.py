"""Validate a 9x9 Sudoku board (partially filled or complete)."""
from __future__ import annotations

from typing import Sequence

Board = Sequence[Sequence[int]]


def _check_dimensions(board: Board) -> None:
    if len(board) != 9 or any(len(row) != 9 for row in board):
        raise ValueError("board must be 9x9")


def is_valid(board: Board) -> bool:
    """Return ``True`` if the board has no rule conflicts.

    Empty cells are encoded as ``0`` and are ignored. Other values must be
    integers in ``1..9``.
    """
    _check_dimensions(board)
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == 0:
                continue
            if not 1 <= value <= 9:
                return False
            box = (r // 3) * 3 + c // 3
            if value in rows[r] or value in cols[c] or value in boxes[box]:
                return False
            rows[r].add(value)
            cols[c].add(value)
            boxes[box].add(value)
    return True


def is_complete(board: Board) -> bool:
    """Return ``True`` if the board is fully filled (no zeros) and valid."""
    _check_dimensions(board)
    if any(0 in row for row in board):
        return False
    return is_valid(board)
