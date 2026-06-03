import pytest

from intervals import intersect, length, merge


def test_merge_overlapping():
    assert merge([(1, 3), (2, 5), (7, 9)]) == [(1, 5), (7, 9)]


def test_merge_adjacent_intervals_coalesce():
    assert merge([(1, 3), (4, 6)]) == [(1, 6)]


def test_merge_disjoint_intervals():
    assert merge([(1, 2), (5, 6), (10, 11)]) == [(1, 2), (5, 6), (10, 11)]


def test_merge_unsorted_input():
    assert merge([(7, 9), (1, 3), (2, 5)]) == [(1, 5), (7, 9)]


def test_merge_empty():
    assert merge([]) == []


def test_merge_invalid_interval_raises():
    with pytest.raises(ValueError):
        merge([(5, 3)])


def test_intersect_overlap():
    assert intersect((1, 5), (3, 7)) == (3, 5)


def test_intersect_touching_inclusive():
    assert intersect((1, 5), (5, 7)) == (5, 5)


def test_intersect_disjoint_returns_none():
    assert intersect((1, 2), (3, 4)) is None


def test_length():
    assert length([(1, 3), (5, 6)]) == 5     # 3 + 2
    assert length([(1, 3), (2, 5)]) == 5     # merged to (1, 5)
    assert length([]) == 0
