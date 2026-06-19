import math

import pytest

from vec3 import Vec3, angle_between, distance, lerp


def test_addition_and_subtraction():
    a = Vec3(1, 2, 3)
    b = Vec3(4, 5, 6)
    assert a + b == Vec3(5, 7, 9)
    assert b - a == Vec3(3, 3, 3)


def test_scalar_multiplication():
    v = Vec3(1, 2, 3)
    assert v * 2 == Vec3(2, 4, 6)
    assert 2 * v == Vec3(2, 4, 6)
    assert -v == Vec3(-1, -2, -3)


def test_dot():
    assert Vec3(1, 2, 3).dot(Vec3(4, 5, 6)) == 32       # 4 + 10 + 18
    assert Vec3(1, 0, 0).dot(Vec3(0, 1, 0)) == 0


def test_cross_unit_vectors():
    assert Vec3(1, 0, 0).cross(Vec3(0, 1, 0)) == Vec3(0, 0, 1)   # i x j = k
    assert Vec3(0, 1, 0).cross(Vec3(0, 0, 1)) == Vec3(1, 0, 0)   # j x k = i


def test_length():
    assert Vec3(2, 3, 6).length() == 7
    assert Vec3(2, 3, 6).length_squared() == 49


def test_normalize():
    assert Vec3(2, 3, 6).normalize().length() == pytest.approx(1.0)


def test_normalize_zero_raises():
    with pytest.raises(ValueError):
        Vec3(0, 0, 0).normalize()


def test_distance():
    assert distance(Vec3(0, 0, 0), Vec3(2, 3, 6)) == 7


def test_lerp():
    assert lerp(Vec3(0, 0, 0), Vec3(10, 20, 30), 0.5) == Vec3(5, 10, 15)


def test_angle_between_perpendicular():
    assert angle_between(Vec3(1, 0, 0), Vec3(0, 1, 0)) == pytest.approx(math.pi / 2)


def test_angle_between_parallel():
    assert angle_between(Vec3(1, 0, 0), Vec3(2, 0, 0)) == pytest.approx(0.0)


def test_angle_between_anti_parallel():
    assert angle_between(Vec3(1, 0, 0), Vec3(-1, 0, 0)) == pytest.approx(math.pi)


def test_angle_between_zero_raises():
    with pytest.raises(ValueError):
        angle_between(Vec3(0, 0, 0), Vec3(1, 0, 0))
