"""Encode and decode the bencode serialization format used by BitTorrent."""
from __future__ import annotations

from typing import Any, Tuple


class BencodeError(ValueError):
    """Raised when bencoded data cannot be parsed or encoded."""


def encode(value: Any) -> bytes:
    """Encode ``value`` as bencoded bytes.

    Supports ``int``, ``bytes``, ``str`` (UTF-8 encoded), ``list`` / ``tuple``
    and ``dict`` with ``str`` or ``bytes`` keys.
    """
    if isinstance(value, bool):
        # ``bool`` is a subclass of ``int`` -- reject explicitly to avoid surprises.
        raise BencodeError("bool is not bencodable")
    if isinstance(value, int):
        return f"i{value}e".encode("ascii")
    if isinstance(value, bytes):
        return f"{len(value)}:".encode("ascii") + value
    if isinstance(value, str):
        data = value.encode("utf-8")
        return f"{len(data)}:".encode("ascii") + data
    if isinstance(value, (list, tuple)):
        return b"l" + b"".join(encode(item) for item in value) + b"e"
    if isinstance(value, dict):
        parts = []
        for key in sorted(value):
            if not isinstance(key, (str, bytes)):
                raise BencodeError(f"dict keys must be str or bytes: {key!r}")
            parts.append(encode(key))
            parts.append(encode(value[key]))
        return b"d" + b"".join(parts) + b"e"
    raise BencodeError(f"unsupported type: {type(value).__name__}")


def decode(data: bytes) -> Any:
    """Decode bencoded ``data`` into a Python object."""
    value, position = _decode(data, 0)
    if position != len(data):
        raise BencodeError("trailing data after bencoded value")
    return value


def _decode(data: bytes, position: int) -> Tuple[Any, int]:
    if position >= len(data):
        raise BencodeError("unexpected end of data")
    prefix = data[position:position + 1]
    if prefix == b"i":
        end = data.index(b"e", position)
        return int(data[position + 1:end]), end + 1
    if prefix == b"l":
        position += 1
        items = []
        while data[position:position + 1] != b"e":
            item, position = _decode(data, position)
            items.append(item)
        return items, position + 1
    if prefix == b"d":
        position += 1
        result = {}
        while data[position:position + 1] != b"e":
            key, position = _decode(data, position)
            if not isinstance(key, bytes):
                raise BencodeError("dict keys must be byte strings")
            value, position = _decode(data, position)
            result[key] = value
        return result, position + 1
    if prefix.isdigit():
        colon = data.index(b":", position)
        length = int(data[position:colon])
        start = colon + 1
        end = start + length
        if end > len(data):
            raise BencodeError("string length exceeds available data")
        return data[start:end], end
    raise BencodeError(f"unexpected token at position {position}: {prefix!r}")
