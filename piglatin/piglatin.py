"""Translate English text to Pig Latin."""
from __future__ import annotations

import re

_VOWELS = set("aeiouAEIOU")
_WORD = re.compile(r"[A-Za-z]+")


def translate_word(word: str) -> str:
    """Return the Pig Latin form of a single word.

    Rules:

    - Words starting with a vowel get ``"way"`` appended
      (``"egg"`` -> ``"eggway"``).
    - Words starting with consonants have the leading consonant cluster
      moved to the end and ``"ay"`` appended
      (``"hello"`` -> ``"ellohay"``, ``"string"`` -> ``"ingstray"``).
    - ``"y"`` is treated as a vowel except in the leading position.
    - Capitalisation of the original first letter is preserved on the
      first letter of the result.
    """
    if not word:
        return word
    leading = 0
    while leading < len(word) and word[leading].lower() not in _VOWELS:
        if leading > 0 and word[leading].lower() == "y":
            break
        leading += 1
    if leading == 0:
        result = word + "way"
    elif leading == len(word):
        result = word + "ay"
    else:
        result = word[leading:] + word[:leading] + "ay"
    if word[0].isupper():
        return result[0].upper() + result[1:].lower()
    return result.lower()


def translate(text: str) -> str:
    """Translate every English word in ``text`` to Pig Latin."""
    return _WORD.sub(lambda m: translate_word(m.group(0)), text)
