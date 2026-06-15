import pytest

from modular import crt, extended_gcd, mod_inverse, mod_pow


def test_extended_gcd_basic():
    g, x, y = extended_gcd(30, 12)
    assert g == 6
    assert 30 * x + 12 * y == g


def test_extended_gcd_zero():
    assert extended_gcd(0, 5)[0] == 5
    assert extended_gcd(5, 0)[0] == 5


def test_mod_inverse_basic():
    assert mod_inverse(3, 11) == 4              # 3 * 4 = 12 = 11 + 1
    assert (mod_inverse(7, 26) * 7) % 26 == 1


def test_mod_inverse_no_inverse_raises():
    with pytest.raises(ValueError):
        mod_inverse(6, 9)                       # gcd(6, 9) = 3


def test_mod_inverse_invalid_modulus_raises():
    with pytest.raises(ValueError):
        mod_inverse(3, 0)


def test_mod_pow_basic():
    assert mod_pow(3, 7, 13) == pow(3, 7, 13)


def test_mod_pow_large_exponent():
    assert mod_pow(2, 10000, 1009) == pow(2, 10000, 1009)


def test_mod_pow_negative_exponent_uses_inverse():
    # 3^-1 mod 11 = 4, so 3^-3 = 4^3 mod 11 = 64 mod 11 = 9.
    assert mod_pow(3, -3, 11) == 9


def test_crt_classic_example():
    assert crt([2, 3, 2], [3, 5, 7]) == 23


def test_crt_two_congruences():
    assert crt([1, 2], [4, 5]) == 17


def test_crt_non_coprime_raises():
    with pytest.raises(ValueError):
        crt([1, 2], [4, 6])
