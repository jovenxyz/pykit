"""Wrap text with ANSI escape codes for terminal colours and styles."""
from __future__ import annotations

import re
from typing import Iterable, Optional, Union

RESET = "\x1b[0m"

_COLORS = {
    "black": 30, "red": 31, "green": 32, "yellow": 33,
    "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
    "bright_black": 90, "bright_red": 91, "bright_green": 92,
    "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
    "bright_cyan": 96, "bright_white": 97,
}

_STYLES = {
    "bold": 1, "dim": 2, "italic": 3, "underline": 4,
    "blink": 5, "reverse": 7, "strike": 9,
}

COLORS = tuple(sorted(_COLORS))
STYLES = tuple(sorted(_STYLES))

_ANSI = re.compile(r"\x1b\[[0-9;]*m")


def colorize(
    text: str,
    fg: Optional[str] = None,
    bg: Optional[str] = None,
    style: Union[str, Iterable[str], None] = None,
) -> str:
    """Wrap ``text`` in ANSI escape codes for the requested colour/style.

    ``fg``/``bg`` accept any colour name in :data:`COLORS`. ``style`` is a
    single style name or an iterable of styles from :data:`STYLES`.
    """
    codes = []
    if style is not None:
        names = [style] if isinstance(style, str) else list(style)
        for name in names:
            if name not in _STYLES:
                raise ValueError(f"unknown style: {name!r}")
            codes.append(str(_STYLES[name]))
    if fg is not None:
        if fg not in _COLORS:
            raise ValueError(f"unknown foreground colour: {fg!r}")
        codes.append(str(_COLORS[fg]))
    if bg is not None:
        if bg not in _COLORS:
            raise ValueError(f"unknown background colour: {bg!r}")
        codes.append(str(_COLORS[bg] + 10))
    if not codes:
        return text
    return f"\x1b[{';'.join(codes)}m{text}{RESET}"


def strip_ansi(text: str) -> str:
    """Remove all ANSI escape sequences from ``text``."""
    return _ANSI.sub("", text)
