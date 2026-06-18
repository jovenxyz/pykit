import pytest

from hsl import hsl_to_rgb, hsv_to_rgb, rgb_to_hsl, rgb_to_hsv


def test_rgb_to_hsl_red():
    h, s, l = rgb_to_hsl((255, 0, 0))
    assert h == pytest.approx(0)
    assert s == pytest.approx(1.0)
    assert l == pytest.approx(0.5)


def test_rgb_to_hsl_white_and_black():
    assert rgb_to_hsl((255, 255, 255))[1:] == pytest.approx((0, 1.0))
    assert rgb_to_hsl((0, 0, 0)) == pytest.approx((0, 0, 0))


def test_rgb_hsl_round_trip():
    for rgb in ((255, 0, 0), (0, 128, 64), (200, 50, 100), (50, 50, 50)):
        assert hsl_to_rgb(rgb_to_hsl(rgb)) == rgb


def test_rgb_to_hsv_red():
    h, s, v = rgb_to_hsv((255, 0, 0))
    assert h == pytest.approx(0)
    assert s == pytest.approx(1.0)
    assert v == pytest.approx(1.0)


def test_rgb_hsv_round_trip():
    for rgb in ((255, 0, 0), (0, 128, 64), (200, 50, 100), (50, 50, 50)):
        assert hsv_to_rgb(rgb_to_hsv(rgb)) == rgb


def test_hue_for_pure_green():
    assert rgb_to_hsl((0, 255, 0))[0] == pytest.approx(120)
    assert rgb_to_hsv((0, 255, 0))[0] == pytest.approx(120)


def test_hue_for_pure_blue():
    assert rgb_to_hsl((0, 0, 255))[0] == pytest.approx(240)


def test_invalid_rgb_raises():
    with pytest.raises(ValueError):
        rgb_to_hsl((256, 0, 0))


def test_invalid_hsl_raises():
    with pytest.raises(ValueError):
        hsl_to_rgb((180, 1.5, 0.5))
    with pytest.raises(ValueError):
        hsl_to_rgb((180, 0.5, -0.1))


def test_invalid_hsv_raises():
    with pytest.raises(ValueError):
        hsv_to_rgb((180, 1.5, 0.5))
