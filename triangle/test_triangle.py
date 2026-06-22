import math
import pytest
from triangle import (
    is_triangle,
    perimeter,
    area,
    classify_by_sides,
    classify_by_angles,
    angles,
    centroid,
    area_from_points,
    Point,
)


def test_is_triangle_valid():
    assert is_triangle(3, 4, 5)
    assert is_triangle(1, 1, 1)


def test_is_triangle_invalid():
    assert not is_triangle(1, 2, 3)
    assert not is_triangle(0, 1, 1)
    assert not is_triangle(-1, 2, 2)


def test_perimeter():
    assert perimeter(3, 4, 5) == 12
    with pytest.raises(ValueError):
        perimeter(1, 2, 3)


def test_area_right_triangle():
    assert math.isclose(area(3, 4, 5), 6.0)


def test_area_equilateral():
    assert math.isclose(area(2, 2, 2), math.sqrt(3))


def test_area_invalid_raises():
    with pytest.raises(ValueError):
        area(1, 2, 3)


def test_classify_by_sides():
    assert classify_by_sides(2, 2, 2) == "equilateral"
    assert classify_by_sides(2, 2, 3) == "isosceles"
    assert classify_by_sides(3, 4, 5) == "scalene"


def test_classify_by_angles():
    assert classify_by_angles(3, 4, 5) == "right"
    assert classify_by_angles(2, 2, 2) == "acute"
    assert classify_by_angles(3, 4, 6) == "obtuse"


def test_angles_sum_to_pi():
    A, B, C = angles(3, 4, 5)
    assert math.isclose(A + B + C, math.pi, abs_tol=1e-9)


def test_angles_right_triangle():
    A, B, C = angles(3, 4, 5)
    assert math.isclose(C, math.pi / 2, abs_tol=1e-9)


def test_centroid():
    c = centroid(Point(0, 0), Point(6, 0), Point(0, 9))
    assert math.isclose(c.x, 2.0)
    assert math.isclose(c.y, 3.0)


def test_area_from_points_shoelace():
    a = area_from_points(Point(0, 0), Point(4, 0), Point(0, 3))
    assert math.isclose(a, 6.0)


def test_area_from_points_colinear_is_zero():
    a = area_from_points(Point(0, 0), Point(1, 1), Point(2, 2))
    assert math.isclose(a, 0.0)
