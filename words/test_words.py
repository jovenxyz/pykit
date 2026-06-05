import pytest

from words import DEFAULT_STOP_WORDS, count_words, tokenize, top_n


def test_tokenize_lowercases_and_strips_punctuation():
    assert tokenize("Hello, World! 1.5") == ["hello", "world", "1", "5"]


def test_tokenize_keeps_apostrophes():
    assert tokenize("don't can't") == ["don't", "can't"]


def test_count_words_excludes_stop_words():
    text = "The quick brown fox jumps over the lazy dog and the cat."
    counts = count_words(text)
    assert counts["the"] == 0
    assert counts["fox"] == 1
    assert counts["cat"] == 1


def test_count_words_custom_stop_set():
    counts = count_words("foo bar foo baz", stop_words={"baz"})
    assert counts == {"foo": 2, "bar": 1}


def test_count_words_no_stop_set():
    counts = count_words("the cat and the dog", stop_words=set())
    assert counts == {"the": 2, "cat": 1, "and": 1, "dog": 1}


def test_top_n_returns_most_common():
    text = "alpha beta alpha gamma alpha beta delta"
    assert top_n(text, 2) == [("alpha", 3), ("beta", 2)]


def test_top_n_handles_fewer_unique_words_than_n():
    result = top_n("alpha beta", 5)
    assert sorted(result) == [("alpha", 1), ("beta", 1)]


def test_top_n_negative_raises():
    with pytest.raises(ValueError):
        top_n("anything", -1)


def test_default_stop_words_contains_common_words():
    assert "the" in DEFAULT_STOP_WORDS
    assert "and" in DEFAULT_STOP_WORDS
