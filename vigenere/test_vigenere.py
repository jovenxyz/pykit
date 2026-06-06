import pytest

from vigenere import decrypt, encrypt


def test_classic_wikipedia_example():
    # Plaintext ATTACKATDAWN with key LEMON -> LXFOPVEFRNHR.
    assert encrypt("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"


def test_round_trip():
    text = "The quick brown fox jumps over the lazy dog."
    assert decrypt(encrypt(text, "KEY"), "KEY") == text


def test_non_letters_pass_through():
    assert encrypt("Hello, World!", "ABC") == "Hfnlp, Yosnd!"


def test_preserves_case():
    assert encrypt("aA", "B") == "bB"


def test_decrypt_classic_example():
    assert decrypt("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"


def test_empty_or_punctuation_key_raises():
    with pytest.raises(ValueError):
        encrypt("abc", "")
    with pytest.raises(ValueError):
        encrypt("abc", "!!!")


def test_short_key_repeats_across_text():
    # Key "AB" gives shifts 0, 1, 0, 1, ...
    assert encrypt("ABCDEFGHIJKL", "AB") == "ACCEEGGIIKKM"
