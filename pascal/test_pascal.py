import math

import pytest

from pascal import binomial, row, triangle


def test_row_basic():
    assert row(0) == [1]
    assert row(1) == [1, 1]
    assert row(2) == [1, 2, 1]
    assert row(3) == [1, 3, 3, 1]
    assert row(4) == [1, 4, 6, 4, 1]
    assert row(5) == [1, 5, 10, 10, 5, 1]


def test_triangle_basic():
    assert triangle(0) == []
    assert triangle(4) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]


def test_binomial_known_values():
    assert binomial(5, 0) == 1
    assert binomial(5, 5) == 1
    assert binomial(5, 2) == 10
    assert binomial(10, 3) == 120
    assert binomial(20, 10) == 184756


def test_binomial_k_too_large_returns_zero():
    assert binomial(3, 5) == 0


def test_binomial_matches_math_comb():
    for n in range(15):
        for k in range(n + 1):
            assert binomial(n, k) == math.comb(n, k)


def test_negative_args_raise():
    with pytest.raises(ValueError):
        row(-1)
    with pytest.raises(ValueError):
        triangle(-1)
    with pytest.raises(ValueError):
        binomial(-1, 0)
    with pytest.raises(ValueError):
        binomial(5, -1)


def test_row_n_matches_binomial():
    for n in range(10):
        assert row(n) == [binomial(n, k) for k in range(n + 1)]
