"""Count word frequencies and surface the most common words."""
from __future__ import annotations

import re
from collections import Counter
from typing import Iterable, List, Set, Tuple

_WORD = re.compile(r"[A-Za-z0-9']+")

# A handful of common English stop words.
DEFAULT_STOP_WORDS = frozenset({
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on",
    "for", "with", "is", "are", "was", "were", "be", "been", "being",
    "by", "at", "as", "this", "that", "these", "those", "it", "its",
    "i", "you", "he", "she", "we", "they", "them", "his", "her", "our",
    "their", "from", "not", "no", "do", "does", "did", "have", "has", "had",
})


def tokenize(text: str) -> List[str]:
    """Split ``text`` into lowercased word tokens."""
    return [match.lower() for match in _WORD.findall(text)]


def count_words(
    text: str,
    stop_words: Iterable[str] = DEFAULT_STOP_WORDS,
) -> Counter:
    """Return a :class:`Counter` of words in ``text`` (excluding stop words)."""
    stop: Set[str] = set(stop_words)
    return Counter(token for token in tokenize(text) if token not in stop)


def top_n(
    text: str,
    n: int,
    stop_words: Iterable[str] = DEFAULT_STOP_WORDS,
) -> List[Tuple[str, int]]:
    """Return the ``n`` most-common ``(word, count)`` pairs in ``text``."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return count_words(text, stop_words=stop_words).most_common(n)
