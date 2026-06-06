import random
from collections import Counter

import pytest

from reservoir import sample


def test_returns_empty_when_k_is_zero():
    assert sample(range(10), 0) == []


def test_returns_all_items_when_stream_smaller_than_k():
    result = sample([1, 2, 3], 10)
    assert sorted(result) == [1, 2, 3]


def test_sample_size_when_stream_larger_than_k():
    result = sample(range(100), 5)
    assert len(result) == 5
    assert set(result) <= set(range(100))


def test_deterministic_with_seeded_rng():
    a = sample(range(1000), 10, rng=random.Random(42))
    b = sample(range(1000), 10, rng=random.Random(42))
    assert a == b


def test_works_on_generators():
    def stream():
        yield from range(50)

    result = sample(stream(), 5, rng=random.Random(1))
    assert len(result) == 5
    assert set(result) <= set(range(50))


def test_uniformity_is_roughly_balanced():
    # Sampling 5 of 10 -> each item should land in the result ~half the time.
    counts: Counter = Counter()
    rng = random.Random(0)
    trials = 5000
    for _ in range(trials):
        counts.update(sample(range(10), 5, rng=rng))
    # Expected ~2500 per item; allow a generous +/-15 percentage points.
    for item in range(10):
        assert 0.4 * trials < counts[item] < 0.6 * trials


def test_negative_k_raises():
    with pytest.raises(ValueError):
        sample(range(10), -1)
