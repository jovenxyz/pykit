"""Convert identifiers between snake_case, kebab-case, camelCase, PascalCase."""
from __future__ import annotations

import re
from typing import List

_CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
_SEPARATOR = re.compile(r"[\s_\-]+")


def _words(text: str) -> List[str]:
    text = _CAMEL_BOUNDARY.sub(" ", text)
    text = _SEPARATOR.sub(" ", text).strip()
    if not text:
        return []
    return [word.lower() for word in text.split(" ") if word]


def to_snake(text: str) -> str:
    return "_".join(_words(text))


def to_kebab(text: str) -> str:
    return "-".join(_words(text))


def to_camel(text: str) -> str:
    words = _words(text)
    if not words:
        return ""
    return words[0] + "".join(word.capitalize() for word in words[1:])


def to_pascal(text: str) -> str:
    return "".join(word.capitalize() for word in _words(text))
