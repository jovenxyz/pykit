"""A retry decorator with exponential backoff."""
from __future__ import annotations

import functools
import random
import time
from typing import Callable, Tuple, Type


def retry(
    *,
    attempts: int = 3,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    delay: float = 0.0,
    backoff: float = 2.0,
    jitter: float = 0.0,
    sleep: Callable[[float], None] = time.sleep,
):
    """Decorator that retries a function on ``exceptions`` with backoff.

    Parameters
    ----------
    attempts:
        Total number of attempts (must be >= 1).
    exceptions:
        Exception types that should trigger a retry.
    delay:
        Initial delay between attempts in seconds.
    backoff:
        Multiplier applied to ``delay`` after each failed attempt.
    jitter:
        Maximum random fraction added/subtracted from each delay
        (``0.0`` to disable).
    sleep:
        Function called to wait. Inject a fake for tests.
    """
    if attempts < 1:
        raise ValueError("attempts must be >= 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == attempts:
                        raise
                    wait = current_delay
                    if jitter:
                        wait += random.uniform(-jitter, jitter) * current_delay
                    if wait > 0:
                        sleep(wait)
                    current_delay *= backoff
            raise RuntimeError("retry exhausted")  # unreachable

        return wrapper

    return decorator
