import random

import pytest

from skiplist import SkipList


def test_empty():
    sl = SkipList(rng=random.Random(0))
    assert len(sl) == 0
    assert 5 not in sl
    assert list(sl) == []


def test_insert_and_contains():
    sl = SkipList(rng=random.Random(0))
    assert sl.insert(5) is True
    assert sl.insert(2) is True
    assert sl.insert(8) is True
    assert 5 in sl
    assert 2 in sl
    assert 8 in sl
    assert 4 not in sl


def test_duplicate_insert_returns_false():
    sl = SkipList(rng=random.Random(0))
    sl.insert(5)
    assert sl.insert(5) is False
    assert len(sl) == 1


def test_iteration_is_sorted():
    values = [42, 7, 19, 3, 28, 11, 100, 0, 55]
    sl = SkipList(rng=random.Random(0))
    for v in values:
        sl.insert(v)
    assert list(sl) == sorted(values)


def test_remove():
    sl = SkipList(rng=random.Random(0))
    for v in [5, 2, 8, 3, 7]:
        sl.insert(v)
    assert sl.remove(3) is True
    assert 3 not in sl
    assert list(sl) == [2, 5, 7, 8]


def test_remove_missing_returns_false():
    sl = SkipList(rng=random.Random(0))
    sl.insert(5)
    assert sl.remove(99) is False
    assert len(sl) == 1


def test_len_tracks_inserts_and_removes():
    sl = SkipList(rng=random.Random(0))
    for v in range(10):
        sl.insert(v)
    assert len(sl) == 10
    sl.remove(5)
    assert len(sl) == 9


def test_invalid_constructor_args_raise():
    with pytest.raises(ValueError):
        SkipList(max_level=0)
    with pytest.raises(ValueError):
        SkipList(p=0)
    with pytest.raises(ValueError):
        SkipList(p=1)
