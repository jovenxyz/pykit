import pytest

from gale_shapley import is_stable, stable_matching


CLASSIC_PROPOSERS = {
    "Alice":   ["X", "Y", "Z"],
    "Bob":     ["Y", "X", "Z"],
    "Charlie": ["X", "Y", "Z"],
}
CLASSIC_RECEIVERS = {
    "X": ["Bob", "Alice", "Charlie"],
    "Y": ["Alice", "Bob", "Charlie"],
    "Z": ["Alice", "Bob", "Charlie"],
}


def test_returns_complete_matching():
    matching = stable_matching(CLASSIC_PROPOSERS, CLASSIC_RECEIVERS)
    assert set(matching) == set(CLASSIC_PROPOSERS)
    assert set(matching.values()) == set(CLASSIC_RECEIVERS)


def test_matching_is_stable():
    matching = stable_matching(CLASSIC_PROPOSERS, CLASSIC_RECEIVERS)
    assert is_stable(matching, CLASSIC_PROPOSERS, CLASSIC_RECEIVERS)


def test_top_choice_when_possible():
    proposers = {"A": ["X", "Y"], "B": ["Y", "X"]}
    receivers = {"X": ["A", "B"], "Y": ["B", "A"]}
    assert stable_matching(proposers, receivers) == {"A": "X", "B": "Y"}


def test_mismatched_set_sizes_raise():
    with pytest.raises(ValueError):
        stable_matching({"A": ["X"]}, {"X": ["A"], "Y": ["A"]})


def test_incomplete_preferences_raise():
    with pytest.raises(ValueError):
        stable_matching(
            {"A": ["X"], "B": ["X", "Y"]},
            {"X": ["A", "B"], "Y": ["A", "B"]},
        )


def test_detects_unstable_matching():
    bad = {"Alice": "Z", "Bob": "Y", "Charlie": "X"}
    assert not is_stable(bad, CLASSIC_PROPOSERS, CLASSIC_RECEIVERS)


def test_single_pair():
    assert stable_matching({"A": ["X"]}, {"X": ["A"]}) == {"A": "X"}
