import pytest

from regression import correlation, fit


def test_exact_line():
    xs = [1, 2, 3, 4]
    ys = [3, 5, 7, 9]            # y = 2x + 1
    line = fit(xs, ys)
    assert line.slope == pytest.approx(2.0)
    assert line.intercept == pytest.approx(1.0)
    assert line.r_squared == pytest.approx(1.0)


def test_predict():
    line = fit([0, 1], [1, 3])
    assert line.predict(2) == pytest.approx(5.0)


def test_noisy_data():
    xs = [1, 2, 3, 4, 5]
    ys = [2.1, 3.9, 6.1, 8.0, 10.1]
    line = fit(xs, ys)
    assert line.slope == pytest.approx(2.0, abs=0.1)
    assert line.r_squared > 0.99


def test_perfect_negative_slope():
    line = fit([0, 1, 2, 3], [10, 8, 6, 4])
    assert line.slope == pytest.approx(-2.0)
    assert line.intercept == pytest.approx(10.0)


def test_correlation_positive():
    assert correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) == pytest.approx(1.0)


def test_correlation_negative():
    assert correlation([1, 2, 3, 4], [4, 3, 2, 1]) == pytest.approx(-1.0)


def test_correlation_no_relationship():
    assert correlation([-2, -1, 1, 2], [4, 1, 1, 4]) == pytest.approx(0.0, abs=1e-12)


def test_mismatched_lengths_raise():
    with pytest.raises(ValueError):
        fit([1, 2], [1])
    with pytest.raises(ValueError):
        correlation([1], [1, 2])


def test_too_few_points_raises():
    with pytest.raises(ValueError):
        fit([1], [1])
    with pytest.raises(ValueError):
        correlation([1], [1])


def test_zero_variance_raises():
    with pytest.raises(ValueError):
        fit([5, 5, 5], [1, 2, 3])
    with pytest.raises(ValueError):
        correlation([5, 5, 5], [1, 2, 3])
