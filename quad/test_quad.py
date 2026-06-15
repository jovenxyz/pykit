import math

import pytest

from quad import simpson, trapezoidal


def test_trapezoidal_linear_exact():
    # f(x) = 2x + 1; integral 0..3 = 12.
    assert trapezoidal(lambda x: 2 * x + 1, 0, 3, n=10) == pytest.approx(12.0, abs=1e-9)


def test_trapezoidal_sin():
    # integral of sin from 0 to pi = 2.
    assert trapezoidal(math.sin, 0, math.pi, n=10000) == pytest.approx(2.0, abs=1e-4)


def test_simpson_polynomial_exact():
    # Simpson is exact for polynomials of degree <= 3.
    assert simpson(lambda x: x ** 3, 0, 1, n=2) == pytest.approx(0.25, abs=1e-12)


def test_simpson_sin_high_accuracy():
    assert simpson(math.sin, 0, math.pi, n=100) == pytest.approx(2.0, abs=1e-6)


def test_equal_limits_returns_zero():
    assert trapezoidal(lambda x: x, 1, 1) == 0.0
    assert simpson(lambda x: x, 1, 1) == 0.0


def test_negative_or_zero_n_raises():
    with pytest.raises(ValueError):
        trapezoidal(lambda x: x, 0, 1, n=0)
    with pytest.raises(ValueError):
        simpson(lambda x: x, 0, 1, n=0)


def test_simpson_requires_even_n():
    with pytest.raises(ValueError):
        simpson(lambda x: x, 0, 1, n=3)


def test_reversed_limits_flips_sign():
    forward = trapezoidal(math.sin, 0, math.pi, n=1000)
    reverse = trapezoidal(math.sin, math.pi, 0, n=1000)
    assert forward == pytest.approx(-reverse, abs=1e-6)
