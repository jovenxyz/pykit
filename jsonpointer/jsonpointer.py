"""Look up values in nested dict/list structures via JSON Pointer (RFC 6901)."""
from __future__ import annotations

from typing import Any, List

_SENTINEL = object()


def parse_pointer(pointer: str) -> List[str]:
    """Parse a JSON Pointer string into its decoded reference tokens."""
    if pointer == "":
        return []
    if not pointer.startswith("/"):
        raise ValueError(f"pointer must start with '/' or be empty: {pointer!r}")
    tokens = pointer[1:].split("/")
    return [token.replace("~1", "/").replace("~0", "~") for token in tokens]


def resolve(document: Any, pointer: str, default: Any = _SENTINEL) -> Any:
    """Return the value referenced by ``pointer`` inside ``document``.

    If the pointer doesn't resolve, ``default`` is returned -- or
    ``KeyError`` is raised when no default was supplied.
    """
    current = document
    for token in parse_pointer(pointer):
        if isinstance(current, list):
            if not token.isdigit() or not 0 <= int(token) < len(current):
                return _miss(pointer, default)
            current = current[int(token)]
        elif isinstance(current, dict):
            if token not in current:
                return _miss(pointer, default)
            current = current[token]
        else:
            return _miss(pointer, default)
    return current


def _miss(pointer: str, default: Any) -> Any:
    if default is _SENTINEL:
        raise KeyError(pointer)
    return default
