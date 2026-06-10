"""Tic-tac-toe board with a perfect-play negamax AI."""
from __future__ import annotations

from typing import List, Optional, Tuple

EMPTY = "."
X = "X"
O = "O"

Board = List[List[str]]
Move = Tuple[int, int]

_WIN_LINES = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


def empty_board() -> Board:
    return [[EMPTY] * 3 for _ in range(3)]


def winner(board: Board) -> Optional[str]:
    """Return ``X``/``O`` if either has won, else ``None``."""
    for a, b, c in _WIN_LINES:
        v = board[a[0]][a[1]]
        if v != EMPTY and v == board[b[0]][b[1]] == board[c[0]][c[1]]:
            return v
    return None


def is_draw(board: Board) -> bool:
    return winner(board) is None and all(
        cell != EMPTY for row in board for cell in row
    )


def available_moves(board: Board) -> List[Move]:
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]


def play(board: Board, move: Move, player: str) -> Board:
    """Return a new board with ``player`` placed at ``move``."""
    if player not in (X, O):
        raise ValueError(f"player must be 'X' or 'O', got {player!r}")
    r, c = move
    if board[r][c] != EMPTY:
        raise ValueError(f"square ({r}, {c}) is already taken")
    new = [row[:] for row in board]
    new[r][c] = player
    return new


def best_move(board: Board, player: str) -> Move:
    """Return the move that minimax considers best for ``player``."""
    if player not in (X, O):
        raise ValueError(f"player must be 'X' or 'O', got {player!r}")
    moves = available_moves(board)
    if not moves:
        raise ValueError("no moves available")
    opponent = O if player == X else X
    best_score = -2
    chosen: Optional[Move] = None
    for move in moves:
        score = -_negamax(play(board, move, player), opponent)
        if score > best_score:
            best_score = score
            chosen = move
    assert chosen is not None
    return chosen


def _negamax(board: Board, player: str) -> int:
    if winner(board) is not None:
        # The previous mover already won, so ``player`` has lost.
        return -1
    if is_draw(board):
        return 0
    opponent = O if player == X else X
    best = -2
    for move in available_moves(board):
        score = -_negamax(play(board, move, player), opponent)
        if score > best:
            best = score
    return best
