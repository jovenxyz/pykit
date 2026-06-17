import statistics as stdlib

import pytest

from stats import mean, median, percentile, quartiles, stdev, variance


def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3
    assert mean([2, 4]) == 3


def test_median_odd():
    assert median([1, 3, 2]) == 2


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_variance_and_stdev_match_stdlib():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    assert variance(data, sample=False) == pytest.approx(stdlib.pvariance(data))
    assert variance(data, sample=True) == pytest.approx(stdlib.variance(data))
    assert stdev(data, sample=True) == pytest.approx(stdlib.stdev(data))


def test_percentile_endpoints():
    data = [1, 2, 3, 4, 5]
    assert percentile(data, 0) == 1
    assert percentile(data, 100) == 5


def test_percentile_quartile_points():
    assert percentile([1, 2, 3, 4, 5], 25) == 2
    assert percentile([1, 2, 3, 4, 5], 50) == 3
    assert percentile([1, 2, 3, 4, 5], 75) == 4


def test_percentile_with_interpolation():
    # rank = 0.4 -> 1 + 0.4 * (2 - 1) = 1.4
    assert percentile([1, 2, 3, 4, 5], 10) == pytest.approx(1.4)


def test_quartiles():
    assert quartiles([1, 2, 3, 4, 5]) == (2, 3, 4)


def test_empty_raises():
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        percentile([], 50)


def test_variance_too_few_raises():
    with pytest.raises(ValueError):
        variance([1])              # sample needs >= 2


def test_percentile_invalid_range_raises():
    with pytest.raises(ValueError):
        percentile([1, 2, 3], -1)
    with pytest.raises(ValueError):
        percentile([1, 2, 3], 101)
