"""String utility helpers."""
from __future__ import annotations

import re

_NON_ALNUM = re.compile(r"[^a-z0-9]")
_WHITESPACE = re.compile(r"\s")


def is_palindrome(text: str) -> bool:
    cleaned = _NON_ALNUM.sub("", text.lower())
    return cleaned == cleaned[::-1]


def is_anagram(first: str, second: str) -> bool:
    def _key(value: str) -> list:
        return sorted(_WHITESPACE.sub("", value.lower()))

    return _key(first) == _key(second)


def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))
