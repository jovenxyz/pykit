import pytest

from sheet import column_to_index, index_to_column


@pytest.mark.parametrize("column,index", [
    ("A", 1),
    ("B", 2),
    ("Z", 26),
    ("AA", 27),
    ("AB", 28),
    ("AZ", 52),
    ("BA", 53),
    ("ZZ", 702),
    ("AAA", 703),
])
def test_column_to_index(column, index):
    assert column_to_index(column) == index


@pytest.mark.parametrize("index,column", [
    (1, "A"),
    (26, "Z"),
    (27, "AA"),
    (52, "AZ"),
    (53, "BA"),
    (702, "ZZ"),
    (703, "AAA"),
])
def test_index_to_column(index, column):
    assert index_to_column(index) == column


def test_round_trip():
    for i in range(1, 1000):
        assert column_to_index(index_to_column(i)) == i


def test_case_insensitive():
    assert column_to_index("aa") == 27


def test_invalid_column_raises():
    with pytest.raises(ValueError):
        column_to_index("")
    with pytest.raises(ValueError):
        column_to_index("A1")
    with pytest.raises(ValueError):
        column_to_index("?")


def test_invalid_index_raises():
    with pytest.raises(ValueError):
        index_to_column(0)
    with pytest.raises(ValueError):
        index_to_column(-1)
