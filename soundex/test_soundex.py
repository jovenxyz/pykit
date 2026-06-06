import pytest

from soundex import soundex


@pytest.mark.parametrize("name,code", [
    ("Robert", "R163"),
    ("Rupert", "R163"),
    ("Rubin", "R150"),
    ("Ashcraft", "A261"),
    ("Tymczak", "T522"),
    ("Pfister", "P236"),
    ("Honeyman", "H555"),
    ("Smith", "S530"),
])
def test_classic_examples(name, code):
    assert soundex(name) == code


def test_case_insensitive():
    assert soundex("robert") == soundex("ROBERT") == "R163"


def test_ignores_non_alpha_characters():
    assert soundex("O'Brien") == soundex("OBrien")


def test_empty_input_returns_zeros():
    assert soundex("") == "0000"
    assert soundex("123") == "0000"


def test_short_name_is_padded():
    assert soundex("Lee") == "L000"
