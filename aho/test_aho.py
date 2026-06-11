import pytest

from aho import AhoCorasick


def test_single_pattern():
    ac = AhoCorasick(["abc"])
    assert sorted(ac.find("ababcabc")) == [(2, "abc"), (5, "abc")]


def test_classic_wikipedia_example():
    ac = AhoCorasick(["he", "she", "his", "hers"])
    matches = sorted(ac.find("ushers"))
    assert (1, "she") in matches
    assert (2, "he") in matches
    assert (2, "hers") in matches


def test_no_matches():
    ac = AhoCorasick(["xyz"])
    assert ac.find("abcdef") == []


def test_overlapping_patterns():
    ac = AhoCorasick(["aa"])
    assert sorted(ac.find("aaaa")) == [(0, "aa"), (1, "aa"), (2, "aa")]


def test_one_pattern_is_substring_of_another():
    ac = AhoCorasick(["a", "ab", "bc"])
    matches = sorted(ac.find("abcab"))
    assert matches == sorted([
        (0, "a"), (0, "ab"), (1, "bc"),
        (3, "a"), (3, "ab"),
    ])


def test_empty_pattern_raises():
    with pytest.raises(ValueError):
        AhoCorasick([""])


def test_empty_text():
    ac = AhoCorasick(["abc"])
    assert ac.find("") == []


def test_patterns_property():
    ac = AhoCorasick(["one", "two", "three"])
    assert ac.patterns == ["one", "two", "three"]
