from damerau import distance


def test_identical():
    assert distance("", "") == 0
    assert distance("abc", "abc") == 0


def test_empty_strings():
    assert distance("", "abc") == 3
    assert distance("abc", "") == 3


def test_substitution():
    assert distance("abc", "axc") == 1


def test_insertion_and_deletion():
    assert distance("abc", "abcd") == 1
    assert distance("abcd", "abc") == 1


def test_transposition_counts_as_one():
    assert distance("ab", "ba") == 1
    assert distance("abc", "acb") == 1
    assert distance("teh", "the") == 1     # classic typo correction


def test_symmetric():
    assert distance("hello", "world") == distance("world", "hello")


def test_classic_examples():
    assert distance("kitten", "sitting") == 3
    assert distance("flaw", "lawn") == 2
