import pytest

from fenwick import Fenwick


def test_construct_from_size_starts_zero():
    bit = Fenwick(5)
    assert bit.prefix_sum(5) == 0
    assert bit.range_sum(0, 5) == 0


def test_construct_from_values():
    bit = Fenwick([1, 2, 3, 4, 5])
    assert bit.prefix_sum(5) == 15
    assert bit.range_sum(1, 4) == 9
    assert bit.range_sum(2, 3) == 3


def test_add_updates_subsequent_queries():
    bit = Fenwick([1, 2, 3, 4, 5])
    bit.add(2, 7)            # values become [1, 2, 10, 4, 5]
    assert bit.range_sum(0, 5) == 22
    assert bit.range_sum(2, 3) == 10


def test_prefix_sum_empty_range():
    bit = Fenwick([1, 2, 3])
    assert bit.prefix_sum(0) == 0
    assert bit.range_sum(1, 1) == 0


def test_invalid_index_raises():
    bit = Fenwick([1, 2, 3])
    with pytest.raises(IndexError):
        bit.add(5, 1)
    with pytest.raises(IndexError):
        bit.add(-1, 1)


def test_invalid_range_raises():
    bit = Fenwick([1, 2, 3])
    with pytest.raises(IndexError):
        bit.range_sum(-1, 2)
    with pytest.raises(IndexError):
        bit.range_sum(0, 4)
    with pytest.raises(IndexError):
        bit.range_sum(2, 1)


def test_works_with_floats():
    bit = Fenwick([0.5, 1.5, 2.5])
    assert bit.range_sum(0, 3) == pytest.approx(4.5)


def test_len():
    assert len(Fenwick(7)) == 7
    assert len(Fenwick([1, 2, 3])) == 3


def test_negative_size_raises():
    with pytest.raises(ValueError):
        Fenwick(-1)
