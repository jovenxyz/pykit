"""Group words by their anagram class."""
from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, List


def signature(word: str, case_insensitive: bool = True) -> str:
    """Return a canonical key shared by all anagrams of ``word``."""
    text = word.casefold() if case_insensitive else word
    return "".join(sorted(text))


def group_anagrams(
    words: Iterable[str],
    case_insensitive: bool = True,
) -> List[List[str]]:
    """Group ``words`` into lists of anagrams.

    Within each group, words appear in their original order. The groups
    themselves are returned in the order each anagram class is first seen.
    """
    buckets: Dict[str, List[str]] = defaultdict(list)
    order: List[str] = []
    for word in words:
        key = signature(word, case_insensitive)
        if key not in buckets:
            order.append(key)
        buckets[key].append(word)
    return [buckets[key] for key in order]


def are_anagrams(a: str, b: str, case_insensitive: bool = True) -> bool:
    """Return ``True`` if ``a`` and ``b`` are anagrams of each other."""
    return signature(a, case_insensitive) == signature(b, case_insensitive)
