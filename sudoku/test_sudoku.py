import pytest

from sudoku import is_complete, is_valid


VALID_SOLVED = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

PARTIAL_VALID = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def test_solved_board_is_valid_and_complete():
    assert is_valid(VALID_SOLVED)
    assert is_complete(VALID_SOLVED)


def test_partial_board_is_valid_but_not_complete():
    assert is_valid(PARTIAL_VALID)
    assert not is_complete(PARTIAL_VALID)


def test_row_conflict_is_invalid():
    board = [row[:] for row in VALID_SOLVED]
    board[0][0], board[0][1] = 5, 5
    assert not is_valid(board)


def test_column_conflict_is_invalid():
    board = [row[:] for row in PARTIAL_VALID]
    board[0][0] = 6      # column 0 already has a 6 at row 1
    assert not is_valid(board)


def test_box_conflict_is_invalid():
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 5
    board[1][1] = 5      # same 3x3 box
    assert not is_valid(board)


def test_value_out_of_range_is_invalid():
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 10
    assert not is_valid(board)


def test_wrong_size_raises():
    with pytest.raises(ValueError):
        is_valid([[0] * 9 for _ in range(8)])
    with pytest.raises(ValueError):
        is_valid([[0] * 8 for _ in range(9)])


def test_empty_grid_is_valid_but_not_complete():
    empty = [[0] * 9 for _ in range(9)]
    assert is_valid(empty)
    assert not is_complete(empty)
