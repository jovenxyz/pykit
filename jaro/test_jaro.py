import pytest

from jaro import jaro_similarity, jaro_winkler_similarity


def test_identical_strings():
    assert jaro_similarity("hello", "hello") == 1.0
    assert jaro_winkler_similarity("hello", "hello") == 1.0


def test_empty_strings():
    assert jaro_similarity("", "") == 1.0
    assert jaro_similarity("abc", "") == 0.0
    assert jaro_similarity("", "abc") == 0.0


def test_jaro_known_values():
    assert jaro_similarity("MARTHA", "MARHTA") == pytest.approx(0.9444, abs=0.001)
    assert jaro_similarity("DIXON", "DICKSONX") == pytest.approx(0.7666, abs=0.001)
    assert jaro_similarity("CRATE", "TRACE") == pytest.approx(0.7333, abs=0.001)


def test_jaro_winkler_adds_prefix_bonus():
    assert jaro_winkler_similarity("MARTHA", "MARHTA") == pytest.approx(0.9611, abs=0.001)
    assert jaro_winkler_similarity("DIXON", "DICKSONX") == pytest.approx(0.8133, abs=0.001)


def test_jaro_winkler_at_least_jaro():
    for a, b in (("foo", "bar"), ("hello", "help"), ("abc", "xyz")):
        assert jaro_winkler_similarity(a, b) >= jaro_similarity(a, b)


def test_invalid_prefix_scale_raises():
    with pytest.raises(ValueError):
        jaro_winkler_similarity("a", "b", prefix_scale=0.5)
    with pytest.raises(ValueError):
        jaro_winkler_similarity("a", "b", prefix_scale=-0.1)
