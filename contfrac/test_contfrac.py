import math
from fractions import Fraction

import pytest

from contfrac import convergent, convergents, expand_rational, expand_real


def test_expand_rational_known_example():
    # 415/93 -> [4; 2, 6, 7] (Wikipedia example).
    assert expand_rational(415, 93) == [4, 2, 6, 7]


def test_expand_rational_integer():
    assert expand_rational(5, 1) == [5]


def test_expand_rational_negative():
    # -7/2 = -4 + 1/2 -> [-4, 2].
    assert expand_rational(-7, 2) == [-4, 2]


def test_expand_rational_zero():
    assert expand_rational(0, 1) == [0]


def test_expand_rational_denominator_zero_raises():
    with pytest.raises(ValueError):
        expand_rational(1, 0)


def test_expand_real_pi_initial_coefficients():
    # The continued fraction of pi starts [3, 7, 15, 1, 292, ...].
    coefficients = expand_real(math.pi, terms=5)
    assert coefficients[:4] == [3, 7, 15, 1]


def test_convergent_recovers_rational():
    coefficients = expand_rational(415, 93)
    assert convergent(coefficients) == Fraction(415, 93)


def test_convergents_include_classic_pi_approximation():
    approximations = convergents(expand_real(math.pi, terms=4))
    # 22/7 is the second convergent of pi.
    assert approximations[1] == Fraction(22, 7)


def test_convergent_empty_raises():
    with pytest.raises(ValueError):
        convergent([])


def test_expand_real_terminates_on_integer():
    assert expand_real(3.0, terms=5) == [3]


def test_expand_real_non_positive_terms_raises():
    with pytest.raises(ValueError):
        expand_real(1.5, terms=0)
