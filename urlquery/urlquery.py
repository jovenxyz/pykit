"""Parse and build URL query strings."""
from __future__ import annotations

from typing import Dict, List
from urllib.parse import quote, unquote


def parse_query(query: str) -> Dict[str, List[str]]:
    """Parse ``"a=1&b=2&a=3"`` into ``{"a": ["1", "3"], "b": ["2"]}``."""
    result: Dict[str, List[str]] = {}
    if not query:
        return result
    if query.startswith("?"):
        query = query[1:]
    for pair in query.split("&"):
        if not pair:
            continue
        if "=" in pair:
            key, _, value = pair.partition("=")
        else:
            key, value = pair, ""
        decoded_key = unquote(key.replace("+", " "))
        decoded_value = unquote(value.replace("+", " "))
        result.setdefault(decoded_key, []).append(decoded_value)
    return result


def build_query(params) -> str:
    """Build ``"a=1&b=2"`` from a dict or sequence of ``(key, value)`` pairs.

    Values may be strings or sequences of strings (repeated keys).
    """
    items = params.items() if hasattr(params, "items") else params
    parts: List[str] = []
    for key, value in items:
        encoded_key = quote(str(key), safe="")
        if isinstance(value, (list, tuple)):
            for entry in value:
                parts.append(f"{encoded_key}={quote(str(entry), safe='')}")
        else:
            parts.append(f"{encoded_key}={quote(str(value), safe='')}")
    return "&".join(parts)
