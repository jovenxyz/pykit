import math
import pytest
from quaternion import Quaternion, from_axis_angle, rotate_vector


def approx_q(a, b, tol=1e-9):
    return (
        math.isclose(a.w, b.w, abs_tol=tol)
        and math.isclose(a.x, b.x, abs_tol=tol)
        and math.isclose(a.y, b.y, abs_tol=tol)
        and math.isclose(a.z, b.z, abs_tol=tol)
    )


def test_add_sub():
    a = Quaternion(1, 2, 3, 4)
    b = Quaternion(5, 6, 7, 8)
    assert a + b == Quaternion(6, 8, 10, 12)
    assert b - a == Quaternion(4, 4, 4, 4)


def test_scalar_mul():
    q = Quaternion(1, 2, 3, 4)
    assert q * 2 == Quaternion(2, 4, 6, 8)
    assert 3 * q == Quaternion(3, 6, 9, 12)


def test_hamilton_product_ij_equals_k():
    i = Quaternion(0, 1, 0, 0)
    j = Quaternion(0, 0, 1, 0)
    k = Quaternion(0, 0, 0, 1)
    assert i * j == k
    assert j * k == i
    assert k * i == j


def test_hamilton_product_i_squared_minus_one():
    i = Quaternion(0, 1, 0, 0)
    assert i * i == Quaternion(-1, 0, 0, 0)


def test_conjugate_and_norm():
    q = Quaternion(1, 2, 3, 4)
    assert q.conjugate() == Quaternion(1, -2, -3, -4)
    assert q.norm_squared() == 30
    assert math.isclose(q.norm(), math.sqrt(30))


def test_normalize():
    q = Quaternion(0, 3, 0, 4).normalize()
    assert math.isclose(q.norm(), 1.0)


def test_normalize_zero_raises():
    with pytest.raises(ValueError):
        Quaternion(0, 0, 0, 0).normalize()


def test_inverse_times_self_is_identity():
    q = Quaternion(1, 2, 3, 4)
    r = q * q.inverse()
    assert approx_q(r, Quaternion(1, 0, 0, 0))


def test_inverse_of_zero_raises():
    with pytest.raises(ValueError):
        Quaternion(0, 0, 0, 0).inverse()


def test_from_axis_angle_identity():
    q = from_axis_angle((0, 0, 1), 0)
    assert approx_q(q, Quaternion(1, 0, 0, 0))


def test_rotate_vector_90_about_z():
    q = from_axis_angle((0, 0, 1), math.pi / 2)
    x, y, z = rotate_vector(q, (1, 0, 0))
    assert math.isclose(x, 0, abs_tol=1e-9)
    assert math.isclose(y, 1, abs_tol=1e-9)
    assert math.isclose(z, 0, abs_tol=1e-9)


def test_rotate_vector_180_about_y():
    q = from_axis_angle((0, 1, 0), math.pi)
    x, y, z = rotate_vector(q, (1, 0, 0))
    assert math.isclose(x, -1, abs_tol=1e-9)
    assert math.isclose(y, 0, abs_tol=1e-9)
    assert math.isclose(z, 0, abs_tol=1e-9)


def test_from_axis_angle_zero_axis_raises():
    with pytest.raises(ValueError):
        from_axis_angle((0, 0, 0), 1.0)
