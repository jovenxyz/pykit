from kmp import build_failure, find, find_all


def test_build_failure_examples():
    assert build_failure("ABCDABD") == [0, 0, 0, 0, 1, 2, 0]
    assert build_failure("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert build_failure("AAAA") == [0, 1, 2, 3]


def test_find_basic():
    assert find("hello world", "world") == 6
    assert find("hello world", "hello") == 0
    assert find("hello world", "missing") == -1


def test_find_empty_pattern():
    assert find("anything", "") == 0


def test_find_empty_text():
    assert find("", "x") == -1
    assert find("", "") == 0


def test_find_at_end():
    assert find("abcdef", "ef") == 4


def test_find_all_basic():
    assert find_all("ababababab", "abab") == [0, 2, 4, 6]


def test_find_all_no_matches():
    assert find_all("hello", "x") == []


def test_find_all_overlapping_pattern():
    # "AAAA" inside "AAAAAA" overlaps at positions 0, 1, 2.
    assert find_all("AAAAAA", "AAAA") == [0, 1, 2]


def test_works_on_arbitrary_strings():
    assert find("abracadabra", "cad") == 4
