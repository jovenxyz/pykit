import pytest

from money import format_amount, parse_amount, round_half_up


def test_format_basic():
    assert format_amount(1234.5) == "$1,234.50"
    assert format_amount(0) == "$0.00"


def test_format_negative():
    assert format_amount(-1234.5) == "-$1,234.50"


def test_format_symbol_after():
    assert format_amount(1234.5, symbol="€", symbol_after=True) == "1,234.50 €"


def test_format_zero_decimals():
    assert format_amount(1234.6, decimals=0) == "$1,235"


def test_format_european_style():
    assert format_amount(
        1234.5,
        symbol="€",
        thousands=".",
        decimal_point=",",
        symbol_after=True,
    ) == "1.234,50 €"


def test_format_invalid_decimals_raises():
    with pytest.raises(ValueError):
        format_amount(100, decimals=-1)


def test_parse_basic():
    assert parse_amount("$1,234.50") == 1234.5
    assert parse_amount("-$1,234.50") == -1234.5
    assert parse_amount("1234.50 €") == 1234.5


def test_parse_european_style():
    assert parse_amount("1.234,50", thousands=".", decimal_point=",") == 1234.5


def test_parse_invalid_raises():
    with pytest.raises(ValueError):
        parse_amount("not a number")


def test_round_half_up_positive():
    assert round_half_up(0.5, 0) == 1
    assert round_half_up(1.5, 0) == 2
    assert round_half_up(2.5, 0) == 3
    assert round_half_up(2.4, 0) == 2
    assert round_half_up(0.125, 2) == 0.13


def test_round_half_up_negative():
    assert round_half_up(-0.5, 0) == -1
    assert round_half_up(-1.5, 0) == -2
    assert round_half_up(-2.4, 0) == -2


def test_round_half_up_invalid_raises():
    with pytest.raises(ValueError):
        round_half_up(1.0, -1)


def test_format_parse_round_trip():
    for amount in (0, 1234.5, -1.05, 1_000_000.99):
        assert parse_amount(format_amount(amount)) == amount
