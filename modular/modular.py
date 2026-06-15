"""Modular arithmetic helpers: extended Euclidean, inverse, exponentiation, CRT."""
from __future__ import annotations

from typing import Sequence, Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Return ``(g, x, y)`` such that ``g = gcd(a, b)`` and ``a*x + b*y = g``."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def mod_inverse(a: int, m: int) -> int:
    """Return the modular multiplicative inverse of ``a`` mod ``m``."""
    if m <= 0:
        raise ValueError("modulus must be positive")
    g, x, _ = extended_gcd(a % m, m)
    if g != 1:
        raise ValueError(f"no inverse: gcd({a}, {m}) = {g}")
    return x % m


def mod_pow(base: int, exponent: int, modulus: int) -> int:
    """Return ``(base ** exponent) mod modulus`` using fast exponentiation."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if exponent < 0:
        base = mod_inverse(base, modulus)
        exponent = -exponent
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1
    return result


def crt(remainders: Sequence[int], moduli: Sequence[int]) -> int:
    """Solve ``x = remainders[i] (mod moduli[i])`` for pairwise-coprime moduli."""
    if len(remainders) != len(moduli):
        raise ValueError("remainders and moduli must be the same length")
    if not remainders:
        raise ValueError("at least one congruence is required")
    total_modulus = 1
    for m in moduli:
        if m <= 0:
            raise ValueError("moduli must be positive")
        total_modulus *= m
    x = 0
    for r, m in zip(remainders, moduli):
        other = total_modulus // m
        try:
            inverse = mod_inverse(other, m)
        except ValueError as error:
            raise ValueError("moduli must be pairwise coprime") from error
        x = (x + r * other * inverse) % total_modulus
    return x
