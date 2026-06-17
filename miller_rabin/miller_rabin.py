"""Miller-Rabin probabilistic primality test."""
from __future__ import annotations

import random
from typing import Optional

# This witness set is deterministic for all n < 3.317 * 10**24.
_DETERMINISTIC_WITNESSES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(
    n: int,
    *,
    rounds: int = 12,
    rng: Optional[random.Random] = None,
) -> bool:
    """Return ``True`` if ``n`` is (probably) prime."""
    if n < 2:
        return False
    for small in _DETERMINISTIC_WITNESSES:
        if n == small:
            return True
        if n % small == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    if n < 3_317_044_064_679_887_385_961_981:
        witnesses = _DETERMINISTIC_WITNESSES
    else:
        generator = rng if rng is not None else random
        witnesses = [generator.randrange(2, n - 1) for _ in range(rounds)]
    for a in witnesses:
        if not _check(a, d, s, n):
            return False
    return True


def _check(a: int, d: int, s: int, n: int) -> bool:
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return True
    return False


def next_prime(n: int) -> int:
    """Return the smallest prime strictly greater than ``n``."""
    if n < 2:
        return 2
    candidate = n + 1
    if candidate % 2 == 0 and candidate != 2:
        candidate += 1
    while not is_prime(candidate):
        candidate += 2
    return candidate
