import math
import pytest
from mat2 import Mat2, identity, rotation, scale


def approx_m(m1: Mat2, m2: Mat2, tol: float = 1e-9) -> bool:
    return (
        math.isclose(m1.a, m2.a, abs_tol=tol)
        and math.isclose(m1.b, m2.b, abs_tol=tol)
        and math.isclose(m1.c, m2.c, abs_tol=tol)
        and math.isclose(m1.d, m2.d, abs_tol=tol)
    )


def test_add_sub():
    a = Mat2(1, 2, 3, 4)
    b = Mat2(5, 6, 7, 8)
    assert a + b == Mat2(6, 8, 10, 12)
    assert b - a == Mat2(4, 4, 4, 4)


def test_scalar_mul():
    m = Mat2(1, 2, 3, 4)
    assert m * 2 == Mat2(2, 4, 6, 8)
    assert 3 * m == Mat2(3, 6, 9, 12)


def test_matrix_mul():
    a = Mat2(1, 2, 3, 4)
    b = Mat2(5, 6, 7, 8)
    # [[1,2],[3,4]] * [[5,6],[7,8]] = [[19,22],[43,50]]
    assert a * b == Mat2(19, 22, 43, 50)


def test_identity_is_identity():
    m = Mat2(1, 2, 3, 4)
    i = identity()
    assert m * i == m
    assert i * m == m


def test_apply_vector():
    m = Mat2(1, 2, 3, 4)
    assert m.apply((1, 1)) == (3, 7)


def test_transpose():
    assert Mat2(1, 2, 3, 4).transpose() == Mat2(1, 3, 2, 4)


def test_det_and_trace():
    m = Mat2(1, 2, 3, 4)
    assert m.det() == -2
    assert m.trace() == 5


def test_inverse_times_self_is_identity():
    m = Mat2(4, 7, 2, 6)
    assert approx_m(m * m.inverse(), identity())
    assert approx_m(m.inverse() * m, identity())


def test_singular_inverse_raises():
    with pytest.raises(ValueError):
        Mat2(1, 2, 2, 4).inverse()


def test_rotation_90_takes_x_to_y():
    r = rotation(math.pi / 2)
    x, y = r.apply((1, 0))
    assert math.isclose(x, 0, abs_tol=1e-9)
    assert math.isclose(y, 1, abs_tol=1e-9)


def test_rotation_is_orthogonal():
    r = rotation(0.7)
    assert approx_m(r * r.transpose(), identity())


def test_scale_uniform_and_anisotropic():
    assert scale(2).apply((3, 4)) == (6, 8)
    assert scale(2, 3).apply((1, 1)) == (2, 3)


def test_real_eigenvalues_of_diagonal():
    m = Mat2(3, 0, 0, 5)
    eigs = sorted(m.eigenvalues(), key=lambda z: z.real if isinstance(z, complex) else z)
    assert eigs == [3, 5]


def test_complex_eigenvalues_of_rotation():
    r = rotation(math.pi / 2)
    eigs = r.eigenvalues()
    assert all(isinstance(e, complex) for e in eigs)
    # rotation by 90° has eigenvalues ±i
    imags = sorted(e.imag for e in eigs)
    assert math.isclose(imags[0], -1, abs_tol=1e-9)
    assert math.isclose(imags[1], 1, abs_tol=1e-9)
