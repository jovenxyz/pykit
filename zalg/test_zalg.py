import pytest

from zalg import find_all, z_array


def test_z_array_empty():
    assert z_array("") == []


def test_z_array_first_is_length():
    assert z_array("hello")[0] == 5


def test_z_array_known_example():
    # Classic textbook example.
    assert z_array("aabcaabxaaaz") == [12, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0]


def test_z_array_all_same():
    assert z_array("aaaa") == [4, 3, 2, 1]


def test_find_all_basic():
    assert find_all("hello world", "world") == [6]
    assert find_all("ababababab", "abab") == [0, 2, 4, 6]


def test_find_all_no_matches():
    assert find_all("hello", "x") == []


def test_find_all_empty_pattern():
    assert find_all("abc", "") == [0, 1, 2, 3]


def test_find_all_overlapping():
    assert find_all("AAAAAA", "AAAA") == [0, 1, 2]


def test_find_all_separator_collision_raises():
    with pytest.raises(ValueError):
        find_all("a\x00b", "a", sep="\x00")
