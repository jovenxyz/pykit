from horspool import find, find_all


def test_find_basic():
    assert find("hello world", "world") == 6
    assert find("hello world", "hello") == 0
    assert find("hello world", "missing") == -1


def test_find_empty_pattern():
    assert find("anything", "") == 0


def test_find_empty_text():
    assert find("", "x") == -1
    assert find("", "") == 0


def test_find_pattern_longer_than_text():
    assert find("hi", "hello") == -1


def test_find_at_end():
    assert find("abcdef", "ef") == 4


def test_find_all_basic():
    assert find_all("ababababab", "abab") == [0, 2, 4, 6]


def test_find_all_no_matches():
    assert find_all("hello", "x") == []


def test_find_all_overlapping_pattern():
    assert find_all("AAAAAA", "AAAA") == [0, 1, 2]


def test_classic_example():
    assert find("ABAAABCD", "ABC") == 4
