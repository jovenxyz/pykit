"""FNV-1a non-cryptographic hash (32-bit, 64-bit and 128-bit variants)."""
from __future__ import annotations

_FNV32_OFFSET = 0x811C9DC5
_FNV32_PRIME = 0x01000193
_FNV32_MASK = 0xFFFFFFFF

_FNV64_OFFSET = 0xCBF29CE484222325
_FNV64_PRIME = 0x100000001B3
_FNV64_MASK = 0xFFFFFFFFFFFFFFFF

_FNV128_OFFSET = 0x6C62272E07BB014262B821756295C58D
_FNV128_PRIME = 0x0000000001000000000000000000013B
_FNV128_MASK = (1 << 128) - 1


def fnv1a_32(data: bytes) -> int:
    """32-bit FNV-1a hash of ``data``."""
    hash_value = _FNV32_OFFSET
    for byte in data:
        hash_value = ((hash_value ^ byte) * _FNV32_PRIME) & _FNV32_MASK
    return hash_value


def fnv1a_64(data: bytes) -> int:
    """64-bit FNV-1a hash of ``data``."""
    hash_value = _FNV64_OFFSET
    for byte in data:
        hash_value = ((hash_value ^ byte) * _FNV64_PRIME) & _FNV64_MASK
    return hash_value


def fnv1a_128(data: bytes) -> int:
    """128-bit FNV-1a hash of ``data``."""
    hash_value = _FNV128_OFFSET
    for byte in data:
        hash_value = ((hash_value ^ byte) * _FNV128_PRIME) & _FNV128_MASK
    return hash_value
