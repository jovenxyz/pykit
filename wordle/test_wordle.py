import pytest

from wordle import GRAY, GREEN, is_solved, score


def test_all_correct():
    assert score("apple", "apple") == GREEN * 5


def test_none_correct():
    assert score("xyz", "abc") == GRAY * 3


def test_mixed_greens_yellows_and_grays():
    # Target ROBIN, guess RAINS.
    # R vs R -> G
    # A vs O -> A is not in ROBIN -> .
    # I vs B -> I is in ROBIN (position 3) -> Y
    # N vs I -> N is in ROBIN (position 4) -> Y
    # S vs N -> S is not in ROBIN -> .
    assert score("RAINS", "ROBIN") == "G.YY."


def test_duplicate_letter_in_guess_with_single_in_target():
    # Guess AAB vs target ABC: first A is green, second A is gray, B is yellow.
    assert score("AAB", "ABC") == "G.Y"


def test_duplicate_letters_in_both():
    assert score("aaab", "baaa") == "YGGY"


def test_case_insensitive():
    assert score("Apple", "APPLE") == GREEN * 5


def test_length_mismatch_raises():
    with pytest.raises(ValueError):
        score("abc", "abcd")


def test_is_solved():
    assert is_solved("GGGGG")
    assert not is_solved("GGGGY")
    assert not is_solved("")
