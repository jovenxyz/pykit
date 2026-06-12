"""N-queens solver: count and enumerate non-attacking placements."""
from __future__ import annotations

from typing import Iterator, List


def count_solutions(n: int) -> int:
    """Return the number of distinct ways to place ``n`` non-attacking queens."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    total = 0
    full = (1 << n) - 1

    def _solve(cols: int, diag1: int, diag2: int) -> None:
        nonlocal total
        if cols == full:
            total += 1
            return
        free = full & ~(cols | diag1 | diag2)
        while free:
            bit = free & -free
            free ^= bit
            _solve(cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1)

    _solve(0, 0, 0)
    return total


def solutions(n: int) -> Iterator[List[int]]:
    """Yield each solution as a list ``placement[row] = column``."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        yield []
        return
    placement = [0] * n
    full = (1 << n) - 1

    def _solve(row: int, cols: int, diag1: int, diag2: int) -> Iterator[List[int]]:
        if row == n:
            yield placement.copy()
            return
        free = full & ~(cols | diag1 | diag2)
        while free:
            bit = free & -free
            free ^= bit
            placement[row] = bit.bit_length() - 1
            yield from _solve(row + 1, cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1)

    yield from _solve(0, 0, 0, 0)


def first_solution(n: int) -> List[int]:
    """Return any one valid placement; raise ``ValueError`` if none exists."""
    try:
        return next(solutions(n))
    except StopIteration as error:
        raise ValueError(f"no solution for n={n}") from error
