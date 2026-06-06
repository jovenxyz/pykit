import pytest

from tokenbucket import TokenBucket


def test_starts_full():
    clock = [0.0]
    bucket = TokenBucket(rate=10, capacity=5, time_func=lambda: clock[0])
    assert bucket.tokens == 5


def test_consume_within_capacity():
    clock = [0.0]
    bucket = TokenBucket(rate=10, capacity=5, time_func=lambda: clock[0])
    for _ in range(5):
        assert bucket.consume() is True
    assert bucket.consume() is False


def test_refill_over_time():
    clock = [0.0]
    bucket = TokenBucket(rate=2, capacity=5, time_func=lambda: clock[0])
    for _ in range(5):
        bucket.consume()
    assert bucket.consume() is False
    clock[0] = 1.0           # one second elapsed -> +2 tokens
    assert bucket.consume() is True
    assert bucket.consume() is True
    assert bucket.consume() is False


def test_capacity_caps_refill():
    clock = [0.0]
    bucket = TokenBucket(rate=1, capacity=3, time_func=lambda: clock[0])
    bucket.consume()
    bucket.consume()
    clock[0] = 100.0         # plenty of time, but capped at capacity
    assert bucket.tokens == 3


def test_wait_time_zero_when_available():
    clock = [0.0]
    bucket = TokenBucket(rate=1, capacity=5, time_func=lambda: clock[0])
    assert bucket.wait_time(3) == 0.0


def test_wait_time_when_empty():
    clock = [0.0]
    bucket = TokenBucket(rate=2, capacity=2, time_func=lambda: clock[0])
    bucket.consume()
    bucket.consume()
    # Need 1 more token at 2/sec -> 0.5 s wait.
    assert bucket.wait_time(1) == pytest.approx(0.5)


def test_invalid_rate_or_capacity_raises():
    with pytest.raises(ValueError):
        TokenBucket(rate=0, capacity=5)
    with pytest.raises(ValueError):
        TokenBucket(rate=1, capacity=0)


def test_consume_non_positive_raises():
    clock = [0.0]
    bucket = TokenBucket(rate=1, capacity=5, time_func=lambda: clock[0])
    with pytest.raises(ValueError):
        bucket.consume(0)
