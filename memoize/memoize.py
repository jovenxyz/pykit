"""Time-bounded memoization decorator."""
from __future__ import annotations

import functools
import time
from typing import Callable


def memoize(ttl: float, time_func: Callable[[], float] = time.monotonic):
    """Decorator that caches return values for ``ttl`` seconds.

    Each unique combination of positional and keyword arguments gets its
    own slot; expired entries are recomputed on the next call.

    Parameters
    ----------
    ttl:
        Time-to-live in seconds. Must be positive.
    time_func:
        Clock used to read the current time. Inject a fake for tests.
    """
    if ttl <= 0:
        raise ValueError("ttl must be positive")

    def decorator(func: Callable):
        cache: dict = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time_func()
            if key in cache:
                value, expires_at = cache[key]
                if now < expires_at:
                    return value
            value = func(*args, **kwargs)
            cache[key] = (value, now + ttl)
            return value

        def clear() -> None:
            cache.clear()

        wrapper.clear = clear  # type: ignore[attr-defined]
        return wrapper

    return decorator
