"""A tiny recursive-descent JSON parser."""
from __future__ import annotations

from typing import Any, Tuple


class JSONDecodeError(ValueError):
    """Raised on malformed JSON input."""


_ESCAPES = {
    '"': '"', "\\": "\\", "/": "/",
    "b": "\b", "f": "\f", "n": "\n", "r": "\r", "t": "\t",
}


def loads(text: str) -> Any:
    """Parse a JSON document and return the equivalent Python value."""
    value, position = _parse(text, _skip(text, 0))
    end = _skip(text, position)
    if end != len(text):
        raise JSONDecodeError(f"trailing data at position {end}")
    return value


def _skip(text: str, position: int) -> int:
    while position < len(text) and text[position] in " \t\r\n":
        position += 1
    return position


def _parse(text: str, position: int) -> Tuple[Any, int]:
    if position >= len(text):
        raise JSONDecodeError("unexpected end of input")
    char = text[position]
    if char == "{":
        return _parse_object(text, position)
    if char == "[":
        return _parse_array(text, position)
    if char == '"':
        return _parse_string(text, position)
    if char in ("t", "f"):
        return _parse_bool(text, position)
    if char == "n":
        return _parse_null(text, position)
    if char == "-" or char.isdigit():
        return _parse_number(text, position)
    raise JSONDecodeError(f"unexpected character {char!r} at position {position}")


def _parse_object(text: str, position: int) -> Tuple[dict, int]:
    position += 1                      # consume '{'
    position = _skip(text, position)
    result: dict = {}
    if position < len(text) and text[position] == "}":
        return result, position + 1
    while True:
        if position >= len(text) or text[position] != '"':
            raise JSONDecodeError(f"expected string key at position {position}")
        key, position = _parse_string(text, position)
        position = _skip(text, position)
        if position >= len(text) or text[position] != ":":
            raise JSONDecodeError(f"expected ':' at position {position}")
        position = _skip(text, position + 1)
        value, position = _parse(text, position)
        result[key] = value
        position = _skip(text, position)
        if position >= len(text):
            raise JSONDecodeError("unterminated object")
        if text[position] == ",":
            position = _skip(text, position + 1)
            continue
        if text[position] == "}":
            return result, position + 1
        raise JSONDecodeError(f"expected ',' or '}}' at position {position}")


def _parse_array(text: str, position: int) -> Tuple[list, int]:
    position += 1                      # consume '['
    position = _skip(text, position)
    items: list = []
    if position < len(text) and text[position] == "]":
        return items, position + 1
    while True:
        value, position = _parse(text, position)
        items.append(value)
        position = _skip(text, position)
        if position >= len(text):
            raise JSONDecodeError("unterminated array")
        if text[position] == ",":
            position = _skip(text, position + 1)
            continue
        if text[position] == "]":
            return items, position + 1
        raise JSONDecodeError(f"expected ',' or ']' at position {position}")


def _parse_string(text: str, position: int) -> Tuple[str, int]:
    position += 1                      # consume opening '"'
    chars = []
    while position < len(text):
        char = text[position]
        if char == '"':
            return "".join(chars), position + 1
        if char == "\\":
            position += 1
            if position >= len(text):
                raise JSONDecodeError("unterminated string escape")
            esc = text[position]
            if esc == "u":
                if position + 4 >= len(text):
                    raise JSONDecodeError("invalid unicode escape")
                hex_digits = text[position + 1:position + 5]
                try:
                    chars.append(chr(int(hex_digits, 16)))
                except ValueError as error:
                    raise JSONDecodeError(
                        f"invalid unicode escape: {hex_digits!r}"
                    ) from error
                position += 5
                continue
            if esc not in _ESCAPES:
                raise JSONDecodeError(f"invalid escape: \\{esc}")
            chars.append(_ESCAPES[esc])
            position += 1
            continue
        chars.append(char)
        position += 1
    raise JSONDecodeError("unterminated string")


def _parse_bool(text: str, position: int) -> Tuple[bool, int]:
    if text.startswith("true", position):
        return True, position + 4
    if text.startswith("false", position):
        return False, position + 5
    raise JSONDecodeError(f"invalid token at position {position}")


def _parse_null(text: str, position: int) -> Tuple[None, int]:
    if text.startswith("null", position):
        return None, position + 4
    raise JSONDecodeError(f"invalid token at position {position}")


def _parse_number(text: str, position: int) -> Tuple[Any, int]:
    start = position
    if text[position] == "-":
        position += 1
    while position < len(text) and text[position].isdigit():
        position += 1
    is_float = False
    if position < len(text) and text[position] == ".":
        is_float = True
        position += 1
        while position < len(text) and text[position].isdigit():
            position += 1
    if position < len(text) and text[position] in "eE":
        is_float = True
        position += 1
        if position < len(text) and text[position] in "+-":
            position += 1
        while position < len(text) and text[position].isdigit():
            position += 1
    raw = text[start:position]
    if not raw or raw == "-":
        raise JSONDecodeError(f"invalid number at position {start}")
    return (float(raw) if is_float else int(raw), position)
