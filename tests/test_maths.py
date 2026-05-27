from pytoolkit.maths.number_theory import (
    factorial,
    gcd,
    lcm,
    sieve_of_eratosthenes,
)


def test_gcd_lcm():
    assert gcd(12, 18) == 6
    assert lcm(4, 6) == 12


def test_factorial():
    assert factorial(5) == 120


def test_sieve():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
