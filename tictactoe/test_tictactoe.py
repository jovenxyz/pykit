import pytest

from tictactoe import (
    EMPTY, O, X, available_moves, best_move, empty_board, is_draw, play, winner,
)


def test_empty_board_has_no_winner():
    board = empty_board()
    assert winner(board) is None
    assert not is_draw(board)


def test_play_places_marker():
    board = play(empty_board(), (1, 1), X)
    assert board[1][1] == X
    assert board[0][0] == EMPTY


def test_play_does_not_mutate_input():
    original = empty_board()
    play(original, (0, 0), X)
    assert original[0][0] == EMPTY


def test_play_rejects_taken_square():
    board = play(empty_board(), (0, 0), X)
    with pytest.raises(ValueError):
        play(board, (0, 0), O)


def test_row_win():
    board = empty_board()
    for c in range(3):
        board = play(board, (0, c), X)
    assert winner(board) == X


def test_column_win():
    board = empty_board()
    for r in range(3):
        board = play(board, (r, 1), O)
    assert winner(board) == O


def test_diagonal_win():
    board = empty_board()
    for i in range(3):
        board = play(board, (i, i), X)
    assert winner(board) == X


def test_draw():
    # X | O | X
    # X | O | O
    # O | X | X
    moves = [
        ((0, 0), X), ((0, 1), O), ((0, 2), X),
        ((1, 0), X), ((1, 1), O), ((1, 2), O),
        ((2, 0), O), ((2, 1), X), ((2, 2), X),
    ]
    board = empty_board()
    for move, player in moves:
        board = play(board, move, player)
    assert winner(board) is None
    assert is_draw(board)


def test_available_moves_shrinks():
    board = empty_board()
    assert len(available_moves(board)) == 9
    board = play(board, (0, 0), X)
    assert (0, 0) not in available_moves(board)
    assert len(available_moves(board)) == 8


def test_best_move_blocks_immediate_loss():
    board = empty_board()
    board = play(board, (0, 0), X)
    board = play(board, (0, 1), X)
    assert best_move(board, O) == (0, 2)


def test_best_move_takes_immediate_win():
    board = empty_board()
    board = play(board, (0, 0), X)
    board = play(board, (0, 1), X)
    assert best_move(board, X) == (0, 2)


def test_best_move_invalid_player_raises():
    with pytest.raises(ValueError):
        best_move(empty_board(), "Q")
