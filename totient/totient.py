"""Euler's totient function and related number-theoretic helpers."""
from __future__ import annotations

from typing import Iterator, List


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def is_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def totient(n: int) -> int:
    """Return the count of integers in ``[1, n]`` coprime to ``n``."""
    if n <= 0:
        raise ValueError("n must be positive")
    result = n
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def totient_sieve(limit: int) -> List[int]:
    """Return ``phi(0), phi(1), ..., phi(limit)`` precomputed at once."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:                  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    return phi


def coprimes_up_to(n: int) -> Iterator[int]:
    """Yield every integer in ``[1, n)`` coprime to ``n``."""
    if n <= 0:
        raise ValueError("n must be positive")
    for k in range(1, n):
        if gcd(k, n) == 1:
            yield k
