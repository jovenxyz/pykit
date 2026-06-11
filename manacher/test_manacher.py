from manacher import all_palindrome_radii, longest_palindrome


def test_empty_string():
    assert longest_palindrome("") == ""


def test_single_character():
    assert longest_palindrome("a") == "a"


def test_full_palindrome():
    assert longest_palindrome("racecar") == "racecar"


def test_odd_length_inside():
    assert longest_palindrome("babad") in ("bab", "aba")


def test_even_length_inside():
    assert longest_palindrome("cbbd") == "bb"


def test_no_repeats_returns_single_character():
    result = longest_palindrome("abcdef")
    assert len(result) == 1
    assert result in "abcdef"


def test_long_example():
    text = "forgeeksskeegfor"
    assert longest_palindrome(text) == "geeksskeeg"


def test_palindrome_radii_length():
    text = "aba"
    assert len(all_palindrome_radii(text)) == 2 * len(text) + 1
