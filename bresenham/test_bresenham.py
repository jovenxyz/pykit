import pytest

from bresenham import circle, line


def test_horizontal_line():
    assert line(0, 0, 4, 0) == [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]


def test_vertical_line():
    assert line(0, 0, 0, 3) == [(0, 0), (0, 1), (0, 2), (0, 3)]


def test_diagonal_line():
    assert line(0, 0, 3, 3) == [(0, 0), (1, 1), (2, 2), (3, 3)]


def test_negative_direction():
    assert line(3, 3, 0, 0) == [(3, 3), (2, 2), (1, 1), (0, 0)]


def test_single_point():
    assert line(2, 5, 2, 5) == [(2, 5)]


def test_steep_line_is_8_connected():
    pts = line(0, 0, 2, 5)
    assert pts[0] == (0, 0)
    assert pts[-1] == (2, 5)
    for a, b in zip(pts, pts[1:]):
        assert abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1


def test_circle_radius_zero():
    assert circle(5, 5, 0) == [(5, 5)]


def test_circle_radius_one():
    pts = set(circle(0, 0, 1))
    expected = {(1, 0), (0, 1), (-1, 0), (0, -1)}
    assert expected <= pts


def test_circle_radius_three_close_to_circle():
    pts = set(circle(0, 0, 3))
    for x, y in pts:
        d2 = x * x + y * y
        assert 4 <= d2 <= 13
    assert (3, 0) in pts
    assert (0, 3) in pts


def test_circle_negative_radius_raises():
    with pytest.raises(ValueError):
        circle(0, 0, -1)


def test_circle_symmetric():
    pts = set(circle(0, 0, 5))
    for x, y in list(pts):
        assert (-x, -y) in pts
        assert (-x, y) in pts
        assert (y, x) in pts
