import pytest

from spark import sparkline


def test_empty_returns_empty():
    assert sparkline([]) == ""


def test_uses_eight_distinct_levels():
    # Equally-spaced values 0..7 hit each of the eight glyphs.
    assert len(set(sparkline(list(range(8))))) == 8


def test_min_and_max_endpoints():
    result = sparkline([0, 1, 2, 3, 4, 5, 6, 7])
    assert result[0] == "▁"      # lowest glyph
    assert result[-1] == "█"     # highest glyph


def test_flat_input_uses_lowest_bar():
    assert sparkline([5, 5, 5, 5]) == "▁" * 4


def test_explicit_min_and_max():
    result = sparkline([0, 50, 100], minimum=0, maximum=100)
    assert result[0] == "▁"
    assert result[-1] == "█"
    assert result[1] not in {"▁", "█"}


def test_values_above_max_clamp_to_highest():
    assert sparkline([0, 50, 200], minimum=0, maximum=100)[-1] == "█"


def test_invalid_range_raises():
    with pytest.raises(ValueError):
        sparkline([1, 2, 3], minimum=10, maximum=0)


def test_length_matches_input():
    assert len(sparkline(list(range(20)))) == 20
