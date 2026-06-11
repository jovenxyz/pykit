import random
import statistics

import pytest

from medianstream import StreamingMedian


def test_empty_median_raises():
    with pytest.raises(ValueError):
        StreamingMedian().median()


def test_single_value():
    sm = StreamingMedian()
    sm.push(5)
    assert sm.median() == 5


def test_odd_count_median():
    sm = StreamingMedian()
    for v in [1, 3, 5, 7, 9]:
        sm.push(v)
    assert sm.median() == 5


def test_even_count_median():
    sm = StreamingMedian()
    for v in [1, 2, 3, 4]:
        sm.push(v)
    assert sm.median() == 2.5


def test_handles_unsorted_input():
    sm = StreamingMedian()
    for v in [9, 1, 7, 3, 5]:
        sm.push(v)
    assert sm.median() == 5


def test_running_median_matches_statistics():
    rng = random.Random(0)
    values = [rng.randint(-100, 100) for _ in range(200)]
    sm = StreamingMedian()
    for i, v in enumerate(values, 1):
        sm.push(v)
        assert sm.median() == pytest.approx(statistics.median(values[:i]))


def test_handles_duplicates():
    sm = StreamingMedian()
    for _ in range(5):
        sm.push(7)
    assert sm.median() == 7


def test_len_tracks_pushes():
    sm = StreamingMedian()
    assert len(sm) == 0
    sm.push(1)
    sm.push(2)
    assert len(sm) == 2
