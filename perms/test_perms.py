import itertools

import pytest

from perms import combinations, permutations, power_set


def test_permutations_basic():
    assert list(permutations([1, 2, 3])) == [
        [1, 2, 3], [1, 3, 2], [2, 1, 3],
        [2, 3, 1], [3, 1, 2], [3, 2, 1],
    ]


def test_permutations_empty():
    assert list(permutations([])) == [[]]


def test_permutations_single():
    assert list(permutations(["x"])) == [["x"]]


def test_permutations_matches_itertools_for_small_sequences():
    items = ["a", "b", "c", "d"]
    mine = [tuple(p) for p in permutations(items)]
    builtin = list(itertools.permutations(items))
    assert mine == builtin


def test_combinations_basic():
    assert list(combinations([1, 2, 3, 4], 2)) == [
        [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4],
    ]


def test_combinations_zero():
    assert list(combinations([1, 2, 3], 0)) == [[]]


def test_combinations_full():
    assert list(combinations([1, 2, 3], 3)) == [[1, 2, 3]]


def test_combinations_too_large():
    assert list(combinations([1, 2], 5)) == []


def test_combinations_negative_raises():
    with pytest.raises(ValueError):
        list(combinations([1, 2, 3], -1))


def test_power_set_basic():
    assert list(power_set([1, 2, 3])) == [
        [], [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3],
    ]


def test_power_set_empty():
    assert list(power_set([])) == [[]]
