import random

import pytest

from karatsuba import karatsuba


def test_small_numbers():
    assert karatsuba(0, 0) == 0
    assert karatsuba(1234, 5678) == 1234 * 5678
    assert karatsuba(7, 9) == 63


def test_negative_factors():
    assert karatsuba(-1234, 5678) == -1234 * 5678
    assert karatsuba(1234, -5678) == -1234 * 5678
    assert karatsuba(-1234, -5678) == 1234 * 5678


def test_one_factor_zero():
    assert karatsuba(0, 12345) == 0
    assert karatsuba(98765, 0) == 0


def test_large_numbers_match_builtin():
    rng = random.Random(0)
    for _ in range(20):
        a = rng.randint(10 ** 50, 10 ** 100)
        b = rng.randint(10 ** 50, 10 ** 100)
        assert karatsuba(a, b) == a * b


def test_very_large_numbers():
    a = (1 << 1024) + 12345
    b = (1 << 1024) - 67890
    assert karatsuba(a, b) == a * b


def test_invalid_cutoff_raises():
    with pytest.raises(ValueError):
        karatsuba(2, 3, cutoff=0)


def test_low_cutoff_still_correct():
    # Force every multiplication to recurse.
    assert karatsuba(123456789, 987654321, cutoff=2) == 123456789 * 987654321
