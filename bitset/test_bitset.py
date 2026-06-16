import pytest

from bitset import BitSet


def test_initial_empty():
    bs = BitSet(16)
    assert bs.count() == 0
    assert list(bs) == []


def test_set_and_get():
    bs = BitSet(8)
    bs.set(3)
    assert bs.get(3)
    assert not bs.get(0)
    assert bs.count() == 1


def test_clear_and_toggle():
    bs = BitSet(8)
    bs.set(3)
    bs.clear(3)
    assert not bs.get(3)
    bs.toggle(5)
    assert bs.get(5)
    bs.toggle(5)
    assert not bs.get(5)


def test_iteration_yields_set_bits():
    bs = BitSet(16)
    for i in (1, 4, 9, 15):
        bs.set(i)
    assert list(bs) == [1, 4, 9, 15]


def test_union_intersect_difference():
    a = BitSet(8)
    b = BitSet(8)
    for i in (1, 2, 3):
        a.set(i)
    for i in (2, 3, 4):
        b.set(i)
    assert list(a.union(b)) == [1, 2, 3, 4]
    assert list(a.intersect(b)) == [2, 3]
    assert list(a.difference(b)) == [1]


def test_size_mismatch_raises():
    with pytest.raises(ValueError):
        BitSet(4).union(BitSet(8))


def test_out_of_range_raises():
    bs = BitSet(4)
    with pytest.raises(IndexError):
        bs.set(4)
    with pytest.raises(IndexError):
        bs.get(-1)


def test_dict_style_access():
    bs = BitSet(8)
    bs[3] = True
    assert bs[3]
    assert 3 in bs
    assert 5 not in bs


def test_len_and_count():
    bs = BitSet(16)
    for i in (1, 5, 9):
        bs.set(i)
    assert len(bs) == 3
    assert bs.count() == 3


def test_equality():
    a = BitSet(8)
    b = BitSet(8)
    a.set(2)
    b.set(2)
    assert a == b
    b.set(3)
    assert a != b
