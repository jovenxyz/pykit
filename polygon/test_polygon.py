import pytest

from polygon import bounding_box, point_in_polygon, signed_area


SQUARE = [(0, 0), (4, 0), (4, 4), (0, 4)]

L_SHAPE = [
    (0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4),
]


def test_inside_square():
    assert point_in_polygon((2, 2), SQUARE)


def test_outside_square():
    assert not point_in_polygon((-1, 2), SQUARE)
    assert not point_in_polygon((5, 2), SQUARE)
    assert not point_in_polygon((2, -1), SQUARE)
    assert not point_in_polygon((2, 5), SQUARE)


def test_l_shape_concave_region_excluded():
    # The missing corner of the L is excluded.
    assert not point_in_polygon((3, 3), L_SHAPE)
    assert point_in_polygon((1, 3), L_SHAPE)


def test_bounding_box():
    assert bounding_box(SQUARE) == ((0, 0), (4, 4))


def test_signed_area():
    assert signed_area(SQUARE) == pytest.approx(16.0)
    assert signed_area(L_SHAPE) == pytest.approx(12.0)


def test_signed_area_clockwise_is_negative():
    assert signed_area(list(reversed(SQUARE))) == pytest.approx(-16.0)


def test_too_few_vertices_raises():
    with pytest.raises(ValueError):
        point_in_polygon((0, 0), [(0, 0), (1, 1)])


def test_empty_bounding_box_raises():
    with pytest.raises(ValueError):
        bounding_box([])
