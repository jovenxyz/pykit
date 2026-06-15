"""A tiny regex engine supporting . * + ? ^ $."""
from __future__ import annotations


def match(pattern: str, text: str) -> bool:
    """Return ``True`` if ``pattern`` matches anywhere in ``text``.

    ``^`` anchors at the start, ``$`` at the end.
    """
    if pattern.startswith("^"):
        return _match_here(pattern[1:], text)
    for i in range(len(text) + 1):
        if _match_here(pattern, text[i:]):
            return True
    return False


def _match_here(pattern: str, text: str) -> bool:
    if not pattern:
        return True
    if pattern == "$":
        return text == ""
    if len(pattern) >= 2 and pattern[1] in "*+?":
        return _match_quantifier(pattern[0], pattern[1], pattern[2:], text)
    if text and _match_char(pattern[0], text[0]):
        return _match_here(pattern[1:], text[1:])
    return False


def _match_quantifier(c: str, q: str, rest: str, text: str) -> bool:
    if q == "*":
        return _match_star(c, rest, text)
    if q == "+":
        if not text or not _match_char(c, text[0]):
            return False
        return _match_star(c, rest, text[1:])
    # ``?``
    if text and _match_char(c, text[0]):
        if _match_here(rest, text[1:]):
            return True
    return _match_here(rest, text)


def _match_star(c: str, rest: str, text: str) -> bool:
    # Greedy match with backtracking.
    i = 0
    while i < len(text) and _match_char(c, text[i]):
        i += 1
    while i >= 0:
        if _match_here(rest, text[i:]):
            return True
        i -= 1
    return False


def _match_char(pattern_char: str, text_char: str) -> bool:
    return pattern_char == "." or pattern_char == text_char
