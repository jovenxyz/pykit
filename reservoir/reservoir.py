"""Reservoir sampling: uniform random sample from a stream of unknown size."""
from __future__ import annotations

import random
from typing import Iterable, List, Optional, TypeVar

T = TypeVar("T")


def sample(
    stream: Iterable[T],
    k: int,
    rng: Optional[random.Random] = None,
) -> List[T]:
    """Return a uniform random sample of ``k`` items from ``stream``.

    Uses Algorithm R: a single pass, O(k) memory. Every item in the stream
    has equal probability of appearing in the result, regardless of how
    many items the stream produces.
    """
    if k < 0:
        raise ValueError("k must be non-negative")
    if k == 0:
        return []
    generator = rng if rng is not None else random
    reservoir: List[T] = []
    for index, item in enumerate(stream):
        if index < k:
            reservoir.append(item)
        else:
            replace = generator.randint(0, index)
            if replace < k:
                reservoir[replace] = item
    return reservoir
