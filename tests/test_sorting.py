import random

from pytoolkit.algorithms.sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
)

SORTS = (bubble_sort, insertion_sort, merge_sort, quick_sort)


def test_sorts_match_builtin():
    data = random.sample(range(100), 20)
    expected = sorted(data)
    for sort in SORTS:
        assert sort(data) == expected


def test_sorts_handle_empty():
    for sort in SORTS:
        assert sort([]) == []
