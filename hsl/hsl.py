"""Convert sRGB colours to and from HSL and HSV."""
from __future__ import annotations

from typing import Tuple

RGB = Tuple[int, int, int]
HSL = Tuple[float, float, float]
HSV = Tuple[float, float, float]


def _check_rgb(rgb: RGB) -> None:
    for c in rgb:
        if not 0 <= c <= 255:
            raise ValueError(f"colour component out of range 0-255: {c}")


def rgb_to_hsl(rgb: RGB) -> HSL:
    """Convert RGB to ``(hue°, saturation, lightness)``."""
    _check_rgb(rgb)
    r, g, b = (c / 255 for c in rgb)
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    chroma = cmax - cmin
    lightness = (cmax + cmin) / 2
    if chroma == 0:
        return 0.0, 0.0, lightness
    if lightness in (0, 1):
        saturation = 0.0
    else:
        saturation = chroma / (1 - abs(2 * lightness - 1))
    if cmax == r:
        hue = 60 * (((g - b) / chroma) % 6)
    elif cmax == g:
        hue = 60 * ((b - r) / chroma + 2)
    else:
        hue = 60 * ((r - g) / chroma + 4)
    return hue, saturation, lightness


def hsl_to_rgb(hsl: HSL) -> RGB:
    """Convert ``(hue°, saturation, lightness)`` back to RGB."""
    h, s, lightness = hsl
    if not 0 <= s <= 1:
        raise ValueError(f"saturation must be in [0, 1]: {s}")
    if not 0 <= lightness <= 1:
        raise ValueError(f"lightness must be in [0, 1]: {lightness}")
    h = h % 360
    c = (1 - abs(2 * lightness - 1)) * s
    h_prime = h / 60
    x = c * (1 - abs(h_prime % 2 - 1))
    r1, g1, b1 = _slice(h_prime, c, x)
    m = lightness - c / 2
    return _scale(r1, g1, b1, m)


def rgb_to_hsv(rgb: RGB) -> HSV:
    """Convert RGB to ``(hue°, saturation, value)``."""
    _check_rgb(rgb)
    r, g, b = (c / 255 for c in rgb)
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    chroma = cmax - cmin
    value = cmax
    saturation = 0.0 if cmax == 0 else chroma / cmax
    if chroma == 0:
        hue = 0.0
    elif cmax == r:
        hue = 60 * (((g - b) / chroma) % 6)
    elif cmax == g:
        hue = 60 * ((b - r) / chroma + 2)
    else:
        hue = 60 * ((r - g) / chroma + 4)
    return hue, saturation, value


def hsv_to_rgb(hsv: HSV) -> RGB:
    """Convert ``(hue°, saturation, value)`` back to RGB."""
    h, s, v = hsv
    if not 0 <= s <= 1:
        raise ValueError(f"saturation must be in [0, 1]: {s}")
    if not 0 <= v <= 1:
        raise ValueError(f"value must be in [0, 1]: {v}")
    h = h % 360
    c = v * s
    h_prime = h / 60
    x = c * (1 - abs(h_prime % 2 - 1))
    r1, g1, b1 = _slice(h_prime, c, x)
    m = v - c
    return _scale(r1, g1, b1, m)


def _slice(h_prime: float, c: float, x: float) -> Tuple[float, float, float]:
    if h_prime < 1:
        return c, x, 0.0
    if h_prime < 2:
        return x, c, 0.0
    if h_prime < 3:
        return 0.0, c, x
    if h_prime < 4:
        return 0.0, x, c
    if h_prime < 5:
        return x, 0.0, c
    return c, 0.0, x


def _scale(r: float, g: float, b: float, m: float) -> RGB:
    return (
        round((r + m) * 255),
        round((g + m) * 255),
        round((b + m) * 255),
    )
