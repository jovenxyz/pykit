from pytoolkit.strings.text import is_anagram, is_palindrome, reverse_words


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")


def test_is_anagram():
    assert is_anagram("listen", "silent")
    assert not is_anagram("foo", "bar")


def test_reverse_words():
    assert reverse_words("hello world foo") == "foo world hello"
