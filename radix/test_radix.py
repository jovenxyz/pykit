import random

import pytest

from radix import counting_sort, radix_sort


def test_radix_sort_basic():
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [
        2, 24, 45, 66, 75, 90, 170, 802,
    ]


def test_radix_sort_with_negatives():
    assert radix_sort([3, -1, 4, -1, 5, -9, 2, 6]) == [
        -9, -1, -1, 2, 3, 4, 5, 6,
    ]


def test_radix_sort_empty():
    assert radix_sort([]) == []


def test_radix_sort_single():
    assert radix_sort([42]) == [42]


def test_radix_sort_already_sorted():
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_radix_sort_matches_builtin():
    rng = random.Random(0)
    data = [rng.randint(-1000, 1000) for _ in range(200)]
    assert radix_sort(data) == sorted(data)


def test_invalid_base_raises():
    with pytest.raises(ValueError):
        radix_sort([1, 2, 3], base=1)


def test_counting_sort_basic():
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]


def test_counting_sort_empty():
    assert counting_sort([]) == []


def test_counting_sort_rejects_negative():
    with pytest.raises(ValueError):
        counting_sort([1, -2, 3])
