import math

import pytest

from vec2 import Vec2, distance, lerp


def test_addition_and_subtraction():
    a = Vec2(1, 2)
    b = Vec2(3, 4)
    assert a + b == Vec2(4, 6)
    assert b - a == Vec2(2, 2)


def test_scalar_multiplication():
    v = Vec2(1, 2)
    assert v * 3 == Vec2(3, 6)
    assert 3 * v == Vec2(3, 6)
    assert -v == Vec2(-1, -2)


def test_dot_and_cross():
    a = Vec2(1, 0)
    b = Vec2(0, 1)
    assert a.dot(b) == 0
    assert a.cross(b) == 1
    assert Vec2(3, 4).dot(Vec2(1, 2)) == 11


def test_length():
    assert Vec2(3, 4).length() == 5
    assert Vec2(3, 4).length_squared() == 25


def test_normalize():
    assert Vec2(3, 4).normalize().length() == pytest.approx(1.0)


def test_normalize_zero_raises():
    with pytest.raises(ValueError):
        Vec2(0, 0).normalize()


def test_rotate_90_degrees():
    v = Vec2(1, 0).rotate(math.pi / 2)
    assert v.x == pytest.approx(0.0, abs=1e-9)
    assert v.y == pytest.approx(1.0)


def test_angle():
    assert Vec2(1, 0).angle() == pytest.approx(0)
    assert Vec2(0, 1).angle() == pytest.approx(math.pi / 2)
    assert Vec2(-1, 0).angle() == pytest.approx(math.pi)


def test_distance():
    assert distance(Vec2(1, 1), Vec2(4, 5)) == 5


def test_lerp():
    assert lerp(Vec2(0, 0), Vec2(10, 20), 0.5) == Vec2(5, 10)
    assert lerp(Vec2(0, 0), Vec2(10, 20), 0) == Vec2(0, 0)
    assert lerp(Vec2(0, 0), Vec2(10, 20), 1) == Vec2(10, 20)
