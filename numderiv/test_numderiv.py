import math
import pytest
from numderiv import forward, backward, central, five_point, second, partial, gradient


def test_central_polynomial():
    f = lambda x: x ** 3
    assert math.isclose(central(f, 2.0), 12.0, abs_tol=1e-6)


def test_central_sin_is_cos():
    assert math.isclose(central(math.sin, 0.0), 1.0, abs_tol=1e-9)
    assert math.isclose(central(math.sin, math.pi / 2), 0.0, abs_tol=1e-9)


def test_forward_and_backward_agree_with_central_to_lower_precision():
    f = lambda x: x ** 2
    expected = 6.0  # d/dx x^2 at x=3
    assert math.isclose(forward(f, 3.0), expected, abs_tol=1e-3)
    assert math.isclose(backward(f, 3.0), expected, abs_tol=1e-3)
    assert math.isclose(central(f, 3.0), expected, abs_tol=1e-6)


def test_five_point_more_accurate_than_central():
    f = math.exp
    x = 1.0
    expected = math.exp(1.0)
    err_central = abs(central(f, x) - expected)
    err_five = abs(five_point(f, x) - expected)
    assert err_five <= err_central


def test_second_derivative_of_sin_is_minus_sin():
    assert math.isclose(second(math.sin, 1.0), -math.sin(1.0), abs_tol=1e-5)


def test_second_derivative_of_quadratic_is_constant():
    f = lambda x: 4 * x * x + 3 * x + 1
    assert math.isclose(second(f, 0.7), 8.0, abs_tol=1e-3)


def test_invalid_step_raises():
    with pytest.raises(ValueError):
        central(math.sin, 0.0, h=0)
    with pytest.raises(ValueError):
        forward(math.sin, 0.0, h=-1e-5)


def test_partial_derivative():
    f = lambda x, y: x * x * y + 3 * y
    assert math.isclose(partial(f, (2.0, 5.0), 0), 20.0, abs_tol=1e-5)
    assert math.isclose(partial(f, (2.0, 5.0), 1), 7.0, abs_tol=1e-5)


def test_partial_bad_index_raises():
    f = lambda x, y: x + y
    with pytest.raises(IndexError):
        partial(f, (1.0, 2.0), 5)


def test_gradient():
    f = lambda x, y, z: x * x + 2 * y + z ** 3
    g = gradient(f, (1.0, 0.0, 2.0))
    assert math.isclose(g[0], 2.0, abs_tol=1e-5)
    assert math.isclose(g[1], 2.0, abs_tol=1e-5)
    assert math.isclose(g[2], 12.0, abs_tol=1e-3)
