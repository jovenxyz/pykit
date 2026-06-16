import pytest

from segtree import SegmentTree


def test_query_basic_sum():
    st = SegmentTree([1, 2, 3, 4, 5])
    assert st.query(0, 5) == 15
    assert st.query(1, 4) == 9
    assert st.query(2, 3) == 3
    assert st.query(0, 0) == 0


def test_update_changes_subsequent_queries():
    st = SegmentTree([1, 2, 3, 4, 5])
    st.update(2, 10)
    assert st.query(0, 5) == 1 + 2 + 10 + 4 + 5
    assert st.query(2, 3) == 10


def test_indexed_access():
    st = SegmentTree([1, 2, 3])
    assert st[0] == 1
    st[1] = 20
    assert st[1] == 20
    assert st.query(0, 3) == 1 + 20 + 3


def test_invalid_range_raises():
    st = SegmentTree([1, 2, 3])
    with pytest.raises(IndexError):
        st.query(-1, 2)
    with pytest.raises(IndexError):
        st.query(0, 4)
    with pytest.raises(IndexError):
        st.query(2, 1)


def test_invalid_index_raises():
    st = SegmentTree([1, 2, 3])
    with pytest.raises(IndexError):
        st.update(5, 0)
    with pytest.raises(IndexError):
        st[-1]


def test_single_element():
    st = SegmentTree([42])
    assert st.query(0, 1) == 42
    st.update(0, 100)
    assert st.query(0, 1) == 100


def test_works_with_floats():
    st = SegmentTree([0.5, 1.5, 2.5])
    assert st.query(0, 3) == pytest.approx(4.5)


def test_len():
    assert len(SegmentTree([1, 2, 3, 4])) == 4
