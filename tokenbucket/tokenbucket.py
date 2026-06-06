"""A simple token-bucket rate limiter."""
from __future__ import annotations

import time
from typing import Callable


class TokenBucket:
    """Allow up to ``capacity`` events that refill at ``rate`` per second."""

    def __init__(
        self,
        rate: float,
        capacity: float,
        *,
        time_func: Callable[[], float] = time.monotonic,
    ) -> None:
        if rate <= 0:
            raise ValueError("rate must be positive")
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._rate = rate
        self._capacity = capacity
        self._tokens = capacity
        self._time_func = time_func
        self._last = time_func()

    def _refill(self) -> None:
        now = self._time_func()
        elapsed = now - self._last
        if elapsed > 0:
            self._tokens = min(self._capacity, self._tokens + elapsed * self._rate)
            self._last = now

    def consume(self, tokens: float = 1) -> bool:
        """Try to remove ``tokens``; return ``True`` on success, else ``False``."""
        if tokens <= 0:
            raise ValueError("tokens must be positive")
        self._refill()
        if self._tokens >= tokens:
            self._tokens -= tokens
            return True
        return False

    def wait_time(self, tokens: float = 1) -> float:
        """Seconds until ``tokens`` would be available (0 if already)."""
        if tokens <= 0:
            raise ValueError("tokens must be positive")
        self._refill()
        deficit = tokens - self._tokens
        if deficit <= 0:
            return 0.0
        return deficit / self._rate

    @property
    def tokens(self) -> float:
        self._refill()
        return self._tokens
