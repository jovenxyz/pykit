import pytest

from ansi import COLORS, STYLES, colorize, strip_ansi


def test_no_args_returns_plain_text():
    assert colorize("hello") == "hello"


def test_foreground_colour():
    assert colorize("hello", fg="red") == "\x1b[31mhello\x1b[0m"


def test_background_colour():
    assert colorize("hello", bg="blue") == "\x1b[44mhello\x1b[0m"


def test_single_style():
    assert colorize("hello", style="bold") == "\x1b[1mhello\x1b[0m"


def test_combination():
    out = colorize("hello", fg="green", bg="black", style=["bold", "underline"])
    assert out == "\x1b[1;4;32;40mhello\x1b[0m"


def test_bright_colour():
    assert colorize("hello", fg="bright_cyan") == "\x1b[96mhello\x1b[0m"


def test_unknown_colour_raises():
    with pytest.raises(ValueError):
        colorize("x", fg="puce")


def test_unknown_style_raises():
    with pytest.raises(ValueError):
        colorize("x", style="wibble")


def test_strip_ansi_removes_escapes():
    coloured = colorize("hello", fg="red", style="bold")
    assert strip_ansi(coloured) == "hello"
    assert strip_ansi("plain") == "plain"


def test_palettes_exposed():
    assert "red" in COLORS
    assert "bold" in STYLES
