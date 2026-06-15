import pytest

from asciitable import render


def test_basic_table():
    output = render(["name", "age"], [("alice", 30), ("bob", 25)])
    expected = (
        "+-------+-----+\n"
        "| name  | age |\n"
        "+-------+-----+\n"
        "| alice | 30  |\n"
        "| bob   | 25  |\n"
        "+-------+-----+"
    )
    assert output == expected


def test_right_alignment():
    output = render(["item", "price"], [("apple", 1.5)], align=["l", "r"])
    assert "|   1.5 |" in output


def test_center_alignment():
    output = render(["title"], [("x",)], align=["c"])
    # "x" centred in width 5 -> "  x  ", with surrounding spaces.
    assert "|   x   |" in output


def test_mismatched_row_length_raises():
    with pytest.raises(ValueError):
        render(["a", "b"], [("x",)])


def test_mismatched_align_length_raises():
    with pytest.raises(ValueError):
        render(["a", "b"], [], align=["l"])


def test_invalid_alignment_raises():
    with pytest.raises(ValueError):
        render(["a"], [], align=["x"])


def test_empty_rows():
    output = render(["x", "y"], [])
    lines = output.split("\n")
    assert len(lines) == 3
    assert lines[0] == lines[2]


def test_numeric_values_are_coerced():
    assert "| 42 |" in render(["n"], [(42,)])


def test_handles_long_cell():
    assert "this is wide" in render(["x"], [("this is wide",)])
