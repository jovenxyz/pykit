import pytest

from totient import (
    coprimes_up_to,
    gcd,
    is_coprime,
    totient,
    totient_sieve,
)


def test_totient_small_values():
    expected = {
        1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 2,
        7: 6, 8: 4, 9: 6, 10: 4, 11: 10, 12: 4,
        13: 12, 14: 6, 15: 8, 16: 8, 17: 16, 18: 6,
        19: 18, 20: 8,
    }
    for n, phi in expected.items():
        assert totient(n) == phi


def test_totient_prime():
    for p in (101, 1009, 99991):
        assert totient(p) == p - 1


def test_totient_prime_power():
    assert totient(2 ** 10) == 2 ** 10 - 2 ** 9
    assert totient(3 ** 5) == 3 ** 5 - 3 ** 4


def test_totient_invalid_raises():
    with pytest.raises(ValueError):
        totient(0)
    with pytest.raises(ValueError):
        totient(-3)


def test_totient_sieve_matches_function():
    sieve = totient_sieve(50)
    for n in range(1, 51):
        assert sieve[n] == totient(n)


def test_totient_sieve_invalid_raises():
    with pytest.raises(ValueError):
        totient_sieve(-1)


def test_is_coprime():
    assert is_coprime(8, 15)
    assert not is_coprime(8, 12)


def test_gcd_basic():
    assert gcd(0, 5) == 5
    assert gcd(12, 18) == 6
    assert gcd(-12, 18) == 6


def test_coprimes_up_to():
    assert list(coprimes_up_to(10)) == [1, 3, 7, 9]
    assert list(coprimes_up_to(12)) == [1, 5, 7, 11]


def test_coprime_count_matches_totient():
    for n in (10, 12, 25, 30):
        assert sum(1 for _ in coprimes_up_to(n)) == totient(n)
