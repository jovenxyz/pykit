from caesar import caesar, rot13


def test_caesar_basic():
    assert caesar("abc", 1) == "bcd"
    assert caesar("xyz", 3) == "abc"
    assert caesar("Hello, World!", 5) == "Mjqqt, Btwqi!"


def test_caesar_preserves_non_letters():
    assert caesar("123 ?!", 10) == "123 ?!"


def test_caesar_negative_shift():
    assert caesar("bcd", -1) == "abc"
    assert caesar("abc", -3) == "xyz"


def test_caesar_large_shift_wraps():
    assert caesar("abc", 27) == "bcd"
    assert caesar("abc", 52) == "abc"


def test_caesar_round_trip():
    text = "The quick brown fox jumps over the lazy dog!"
    assert caesar(caesar(text, 7), -7) == text


def test_rot13_is_self_inverse():
    text = "Hello, World!"
    assert rot13(rot13(text)) == text


def test_rot13_known_value():
    assert rot13("Hello, World!") == "Uryyb, Jbeyq!"
