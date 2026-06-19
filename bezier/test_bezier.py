import pytest

from bezier import cubic, de_casteljau, quadratic, sample


def test_quadratic_endpoints():
    p0, p1, p2 = (0, 0), (5, 10), (10, 0)
    assert quadratic(p0, p1, p2, 0) == p0
    assert quadratic(p0, p1, p2, 1) == p2


def test_quadratic_midpoint():
    p0, p1, p2 = (0, 0), (10, 10), (20, 0)
    x, y = quadratic(p0, p1, p2, 0.5)
    assert x == pytest.approx(10)
    assert y == pytest.approx(5)


def test_cubic_endpoints():
    p0, p1, p2, p3 = (0, 0), (1, 2), (3, 2), (4, 0)
    assert cubic(p0, p1, p2, p3, 0) == p0
    assert cubic(p0, p1, p2, p3, 1) == p3


def test_cubic_midpoint():
    p0, p1, p2, p3 = (0, 0), (0, 10), (10, 10), (10, 0)
    x, y = cubic(p0, p1, p2, p3, 0.5)
    assert x == pytest.approx(5.0)
    assert y == pytest.approx(7.5)


def test_sample_length_and_endpoints():
    pts = sample([(0, 0), (5, 10), (10, 0)], steps=8)
    assert len(pts) == 9
    assert pts[0] == (0, 0)
    assert pts[-1] == (10, 0)


def test_sample_invalid_degree_raises():
    with pytest.raises(ValueError):
        sample([(0, 0), (1, 1)])
    with pytest.raises(ValueError):
        sample([(0, 0)])


def test_sample_invalid_steps_raises():
    with pytest.raises(ValueError):
        sample([(0, 0), (1, 1), (2, 2)], steps=0)


def test_de_casteljau_matches_quadratic_and_cubic():
    quad = [(0, 0), (5, 10), (10, 0)]
    cube = [(0, 0), (0, 10), (10, 10), (10, 0)]
    for t in (0.0, 0.25, 0.5, 0.75, 1.0):
        assert de_casteljau(quad, t) == pytest.approx(quadratic(*quad, t))
        assert de_casteljau(cube, t) == pytest.approx(cubic(*cube, t))


def test_invalid_t_raises():
    with pytest.raises(ValueError):
        quadratic((0, 0), (1, 1), (2, 0), -0.1)
    with pytest.raises(ValueError):
        cubic((0, 0), (1, 1), (2, 0), (3, 1), 1.5)
