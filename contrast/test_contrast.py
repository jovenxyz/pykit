import pytest

from contrast import contrast_ratio, passes_aa, passes_aaa, relative_luminance


def test_luminance_extremes():
    assert relative_luminance((0, 0, 0)) == 0.0
    assert relative_luminance((255, 255, 255)) == pytest.approx(1.0)


def test_contrast_ratio_black_white_is_21():
    assert contrast_ratio((0, 0, 0), (255, 255, 255)) == pytest.approx(21.0)


def test_contrast_ratio_is_symmetric():
    a = contrast_ratio((30, 30, 30), (200, 200, 200))
    b = contrast_ratio((200, 200, 200), (30, 30, 30))
    assert a == pytest.approx(b)


def test_known_grey_on_white():
    # WCAG example: #777777 on white is approximately 4.48 (just below AA).
    ratio = contrast_ratio((0x77, 0x77, 0x77), (255, 255, 255))
    assert ratio == pytest.approx(4.48, abs=0.02)


def test_passes_aa_normal_text():
    assert passes_aa((0, 0, 0), (255, 255, 255))
    assert not passes_aa((180, 180, 180), (255, 255, 255))


def test_passes_aa_large_text_uses_lower_threshold():
    # Grey 120 on white is ~4.4: below normal AA but above the 3.0 large-text AA.
    assert passes_aa((120, 120, 120), (255, 255, 255), large_text=True)
    assert not passes_aa((120, 120, 120), (255, 255, 255))


def test_passes_aaa_normal_text():
    assert passes_aaa((0, 0, 0), (255, 255, 255))
    # #666666 on white is ~5.74: passes AA but not AAA for normal text.
    assert passes_aa((0x66, 0x66, 0x66), (255, 255, 255))
    assert not passes_aaa((0x66, 0x66, 0x66), (255, 255, 255))


def test_invalid_component_raises():
    with pytest.raises(ValueError):
        relative_luminance((256, 0, 0))
    with pytest.raises(ValueError):
        contrast_ratio((-1, 0, 0), (0, 0, 0))
