"""Pluralize English nouns with a small set of common rules."""
from __future__ import annotations

from typing import Optional

_UNCOUNTABLE = {
    "deer", "fish", "sheep", "series", "species", "moose",
    "aircraft", "data", "equipment", "information", "rice", "money",
}

_IRREGULAR = {
    "man": "men", "woman": "women", "child": "children",
    "tooth": "teeth", "foot": "feet", "mouse": "mice",
    "person": "people", "goose": "geese", "ox": "oxen",
}


def _apply_case(original: str, replacement: str) -> str:
    if original.isupper():
        return replacement.upper()
    if original[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def pluralize(word: str, count: int = 2) -> str:
    """Return the plural form of ``word`` when ``count`` is not 1."""
    if count == 1:
        return word
    lower = word.lower()
    if lower in _UNCOUNTABLE:
        return word
    if lower in _IRREGULAR:
        return _apply_case(word, _IRREGULAR[lower])
    if any(lower.endswith(suffix) for suffix in ("s", "x", "z", "ch", "sh")):
        return word + "es"
    if len(lower) >= 2 and lower.endswith("y") and lower[-2] not in "aeiou":
        return word[:-1] + "ies"
    if lower.endswith("fe"):
        return word[:-2] + "ves"
    if lower.endswith("f"):
        return word[:-1] + "ves"
    return word + "s"


def quantity(count: int, singular: str, plural: Optional[str] = None) -> str:
    """Return ``"1 cat"`` / ``"2 cats"`` for a count and singular noun."""
    word = singular if count == 1 else (plural or pluralize(singular, count))
    return f"{count} {word}"
