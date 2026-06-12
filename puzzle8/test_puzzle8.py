import pytest

from puzzle8 import GOAL, is_solvable, manhattan, solve


def test_manhattan_zero_for_goal():
    assert manhattan(GOAL) == 0


def test_manhattan_basic():
    state = (1, 2, 3, 4, 5, 6, 7, 0, 8)    # blank and 8 swapped
    assert manhattan(state) == 1


def test_solve_goal_state():
    assert solve(GOAL) == [GOAL]


def test_solve_one_move():
    state = (1, 2, 3, 4, 5, 6, 7, 0, 8)
    path = solve(state)
    assert path is not None
    assert path[0] == state
    assert path[-1] == GOAL
    assert len(path) == 2


def test_solve_classic_two_moves():
    state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    path = solve(state)
    assert path is not None
    assert path[-1] == GOAL
    assert len(path) == 3


def test_solve_unsolvable_returns_none():
    # Swap two tiles -> odd inversion parity -> unsolvable.
    state = (2, 1, 3, 4, 5, 6, 7, 8, 0)
    assert solve(state) is None


def test_is_solvable():
    assert is_solvable(GOAL)
    assert is_solvable((1, 2, 3, 4, 5, 6, 0, 7, 8))
    assert not is_solvable((2, 1, 3, 4, 5, 6, 7, 8, 0))


def test_invalid_state_raises():
    with pytest.raises(ValueError):
        solve((1, 2, 3))
    with pytest.raises(ValueError):
        solve((1, 1, 2, 3, 4, 5, 6, 7, 8))
