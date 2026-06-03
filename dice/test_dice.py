import random

import pytest

from dice import Dice, average, maximum, minimum, parse, roll


def test_parse_basic():
    assert parse("2d6+3") == Dice(count=2, sides=6, modifier=3)


def test_parse_implicit_count():
    assert parse("d20") == Dice(count=1, sides=20, modifier=0)


def test_parse_negative_modifier():
    assert parse("3d4-2") == Dice(count=3, sides=4, modifier=-2)


def test_parse_case_and_spaces():
    assert parse(" 2 D 6 + 3 ") == Dice(count=2, sides=6, modifier=3)


def test_parse_invalid_raises():
    for bad in ("", "2x6", "d", "0d6", "2d0", "abc"):
        with pytest.raises(ValueError):
            parse(bad)


def test_minimum_maximum_average():
    d = parse("2d6+3")
    assert minimum(d) == 5        # 2*1 + 3
    assert maximum(d) == 15       # 2*6 + 3
    assert average(d) == 10.0     # 2*3.5 + 3


def test_roll_in_range_and_components():
    d = parse("3d6+1")
    rng = random.Random(42)
    for _ in range(50):
        total, rolls = roll(d, rng)
        assert len(rolls) == 3
        assert all(1 <= r <= 6 for r in rolls)
        assert total == sum(rolls) + 1
        assert minimum(d) <= total <= maximum(d)
