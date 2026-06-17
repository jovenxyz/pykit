import pytest

from convex_hull import convex_hull, polygon_area


def test_single_point():
    assert convex_hull([(1, 2)]) == [(1, 2)]


def test_two_points():
    assert convex_hull([(0, 0), (1, 1)]) == [(0, 0), (1, 1)]


def test_square_returns_all_corners():
    pts = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert sorted(convex_hull(pts)) == sorted(pts)


def test_interior_points_excluded():
    pts = [(0, 0), (4, 0), (4, 4), (0, 4), (1, 1), (2, 2), (3, 1)]
    hull = convex_hull(pts)
    assert (1, 1) not in hull
    assert (2, 2) not in hull
    assert (3, 1) not in hull
    assert sorted(hull) == [(0, 0), (0, 4), (4, 0), (4, 4)]


def test_collinear_points_excluded():
    pts = [(0, 0), (1, 0), (2, 0), (1, 1)]
    hull = convex_hull(pts)
    assert (1, 0) not in hull


def test_duplicate_points():
    pts = [(0, 0), (1, 0), (1, 0), (0, 1), (1, 1)]
    assert sorted(convex_hull(pts)) == sorted([(0, 0), (1, 0), (1, 1), (0, 1)])


def test_polygon_area_square():
    assert polygon_area([(0, 0), (1, 0), (1, 1), (0, 1)]) == pytest.approx(1.0)


def test_polygon_area_triangle():
    assert polygon_area([(0, 0), (4, 0), (0, 3)]) == pytest.approx(6.0)


def test_polygon_area_clockwise_is_negative():
    assert polygon_area([(0, 0), (0, 1), (1, 1), (1, 0)]) == pytest.approx(-1.0)


def test_empty_input():
    assert convex_hull([]) == []
