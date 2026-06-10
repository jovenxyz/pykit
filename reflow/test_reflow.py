import pytest

from reflow import fill, wrap


def test_short_text_one_line():
    assert wrap("hello world", 20) == ["hello world"]


def test_wraps_to_width():
    text = "the quick brown fox jumps over the lazy dog"
    lines = wrap(text, 20)
    assert all(len(line) <= 20 for line in lines)
    assert " ".join(lines) == text


def test_long_word_overflows():
    lines = wrap("a supercalifragilistic word", 10)
    assert "supercalifragilistic" in lines


def test_empty_text_returns_empty_list():
    assert wrap("", 10) == []
    assert wrap("   ", 10) == []


def test_collapses_whitespace():
    assert wrap("a    b\tc\nd", 20) == ["a b c d"]


def test_fill_joins_with_newlines():
    assert fill("hello world foo", 5) == "hello\nworld\nfoo"


def test_width_must_be_positive():
    with pytest.raises(ValueError):
        wrap("anything", 0)
    with pytest.raises(ValueError):
        wrap("anything", -1)


def test_single_word_fits():
    assert wrap("hi", 5) == ["hi"]
