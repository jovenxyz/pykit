import pytest

from histo import bar_chart, histogram


def test_bar_chart_simple():
    output = bar_chart({"alpha": 10, "beta": 5, "gamma": 1}, width=10)
    lines = output.split("\n")
    assert len(lines) == 3
    assert lines[0].startswith("alpha")
    assert "##########" in lines[0]
    assert "#####" in lines[1]
    assert "#" in lines[2]


def test_bar_chart_empty_data():
    assert bar_chart({}) == ""


def test_bar_chart_zero_values():
    output = bar_chart({"a": 0, "b": 0})
    lines = output.split("\n")
    assert len(lines) == 2
    assert "#" not in output


def test_bar_chart_sort_desc():
    output = bar_chart({"a": 1, "b": 3, "c": 2}, sort="desc")
    lines = output.split("\n")
    assert lines[0].startswith("b")
    assert lines[1].startswith("c")
    assert lines[2].startswith("a")


def test_bar_chart_sort_asc():
    output = bar_chart({"a": 1, "b": 3, "c": 2}, sort="asc")
    labels = [line.split(" ")[0] for line in output.split("\n")]
    assert labels == ["a", "c", "b"]


def test_bar_chart_invalid_args_raise():
    with pytest.raises(ValueError):
        bar_chart({"a": 1}, width=0)
    with pytest.raises(ValueError):
        bar_chart({"a": 1}, sort="random")


def test_histogram_basic():
    output = histogram([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], bins=4)
    assert output != ""
    assert len(output.split("\n")) == 4


def test_histogram_empty_input():
    assert histogram([]) == ""


def test_histogram_uniform_values():
    assert histogram([5, 5, 5], bins=4) != ""


def test_histogram_invalid_bins_raise():
    with pytest.raises(ValueError):
        histogram([1, 2, 3], bins=0)
