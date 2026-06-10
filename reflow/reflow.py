"""Word-wrap text to a maximum line width."""
from __future__ import annotations

from typing import List


def wrap(text: str, width: int) -> List[str]:
    """Break ``text`` into lines no longer than ``width`` characters.

    Runs of whitespace (including tabs and newlines) collapse to a single
    space. Words longer than ``width`` are emitted on their own line as-is.
    """
    if width <= 0:
        raise ValueError("width must be positive")
    words = text.split()
    if not words:
        return []
    lines: List[str] = []
    current = words[0]
    for word in words[1:]:
        if len(current) + 1 + len(word) <= width:
            current += " " + word
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def fill(text: str, width: int) -> str:
    """Like :func:`wrap` but return a single string joined by ``\\n``."""
    return "\n".join(wrap(text, width))
