"""Score a Wordle-style guess against a target word."""
from __future__ import annotations

from typing import List, Optional

GREEN = "G"
YELLOW = "Y"
GRAY = "."


def score(guess: str, target: str) -> str:
    """Return a length-``len(guess)`` string of ``G``/``Y``/``.`` per letter.

    Duplicate letters are handled exactly as in the official game: each
    target letter can only be consumed by one guess position.
    """
    if len(guess) != len(target):
        raise ValueError("guess and target must be the same length")
    guess = guess.lower()
    target = target.lower()
    result: List[str] = [GRAY] * len(guess)
    target_chars: List[Optional[str]] = list(target)
    # First pass: mark greens and consume those target letters.
    for i, char in enumerate(guess):
        if target_chars[i] == char:
            result[i] = GREEN
            target_chars[i] = None
    # Second pass: mark yellows, each from a distinct remaining target letter.
    for i, char in enumerate(guess):
        if result[i] == GREEN:
            continue
        if char in target_chars:
            result[i] = YELLOW
            target_chars[target_chars.index(char)] = None
    return "".join(result)


def is_solved(score_string: str) -> bool:
    """Return ``True`` if every letter in ``score_string`` is GREEN."""
    return bool(score_string) and all(ch == GREEN for ch in score_string)
