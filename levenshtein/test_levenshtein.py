import math

from levenshtein import distance, ratio


def test_distance_identical():
    assert distance("", "") == 0
    assert distance("abc", "abc") == 0


def test_distance_empty():
    assert distance("", "abc") == 3
    assert distance("abc", "") == 3


def test_distance_classic_examples():
    assert distance("kitten", "sitting") == 3
    assert distance("flaw", "lawn") == 2
    assert distance("intention", "execution") == 5


def test_distance_is_symmetric():
    assert distance("hello", "world") == distance("world", "hello")


def test_ratio_full_match_and_no_match():
    assert ratio("", "") == 1.0
    assert ratio("abc", "abc") == 1.0
    assert ratio("abc", "xyz") == 0.0


def test_ratio_partial_match():
    # kitten vs sitting: 3 edits over length 7 -> 4/7 ~ 0.571
    assert math.isclose(ratio("kitten", "sitting"), 1 - 3 / 7)
