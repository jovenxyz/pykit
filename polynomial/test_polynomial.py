import pytest

from polynomial import degree, derivative, evaluate, newton_root


def test_evaluate_constant():
    assert evaluate([7], 5) == 7


def test_evaluate_linear():
    # 2 + 3x at x=4 -> 14
    assert evaluate([2, 3], 4) == 14


def test_evaluate_quadratic():
    # 1 + 2x + 3x^2 at x=2 -> 1 + 4 + 12 = 17
    assert evaluate([1, 2, 3], 2) == 17


def test_evaluate_empty_polynomial():
    assert evaluate([], 5) == 0.0


def test_evaluate_at_zero_returns_constant_term():
    assert evaluate([5, 2, 3], 0) == 5


def test_derivative_of_constant_is_zero():
    assert derivative([42]) == [0.0]
    assert derivative([]) == [0.0]


def test_derivative_basic():
    # d/dx (1 + 2x + 3x^2) = 2 + 6x
    assert derivative([1, 2, 3]) == [2, 6]


def test_degree():
    assert degree([1, 2, 3]) == 2
    assert degree([1, 2, 3, 0]) == 2
    assert degree([0, 0, 0]) == 0


def test_newton_root_finds_simple_root():
    # x^2 - 4 -> roots at +/-2.
    assert newton_root([-4, 0, 1], initial=1.5) == pytest.approx(2, abs=1e-9)


def test_newton_root_finds_negative_root():
    assert newton_root([-4, 0, 1], initial=-1.5) == pytest.approx(-2, abs=1e-9)


def test_newton_root_no_convergence_raises():
    # x^2 + 1 has no real roots; Newton wanders.
    with pytest.raises(ValueError):
        newton_root([1, 0, 1], initial=0.5, max_iterations=20)
