import pytest

from hilbert import d_to_xy, xy_to_d


def test_round_trip_small_grid():
    order = 3
    n = 1 << order
    for y in range(n):
        for x in range(n):
            assert d_to_xy(order, xy_to_d(order, x, y)) == (x, y)


def test_indices_cover_grid():
    order = 3
    n = 1 << order
    indices = {xy_to_d(order, x, y) for x in range(n) for y in range(n)}
    assert indices == set(range(n * n))


def test_known_first_order():
    # Order 1: 2x2 grid. Hilbert order: (0,0)->0, (0,1)->1, (1,1)->2, (1,0)->3.
    assert xy_to_d(1, 0, 0) == 0
    assert xy_to_d(1, 0, 1) == 1
    assert xy_to_d(1, 1, 1) == 2
    assert xy_to_d(1, 1, 0) == 3


def test_locality_preserved_for_consecutive_indices():
    order = 4
    n = 1 << order
    for d in range(n * n - 1):
        a = d_to_xy(order, d)
        b = d_to_xy(order, d + 1)
        assert abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def test_out_of_range_coordinates_raise():
    with pytest.raises(ValueError):
        xy_to_d(2, 4, 0)
    with pytest.raises(ValueError):
        xy_to_d(2, 0, 4)


def test_out_of_range_index_raises():
    with pytest.raises(ValueError):
        d_to_xy(2, 16)
