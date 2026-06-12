import pytest

from knight import find_tour


def test_tour_length_matches_board():
    for n in (5, 6, 7, 8):
        tour = find_tour(n)
        assert tour is not None
        assert len(tour) == n * n


def test_tour_visits_every_square_once():
    tour = find_tour(8)
    assert tour is not None
    assert len(set(tour)) == 8 * 8


def test_each_step_is_a_knight_move():
    tour = find_tour(8)
    assert tour is not None
    for (x1, y1), (x2, y2) in zip(tour, tour[1:]):
        assert {abs(x2 - x1), abs(y2 - y1)} == {1, 2}


def test_starts_at_given_cell():
    tour = find_tour(8, start=(3, 4))
    assert tour is not None
    assert tour[0] == (3, 4)


def test_no_tour_for_tiny_boards():
    # No knight's tour exists on 2x2, 3x3 or 4x4.
    assert find_tour(2) is None
    assert find_tour(3) is None
    assert find_tour(4) is None


def test_one_by_one_is_trivial():
    assert find_tour(1) == [(0, 0)]


def test_invalid_args_raise():
    with pytest.raises(ValueError):
        find_tour(0)
    with pytest.raises(ValueError):
        find_tour(8, start=(10, 0))
