"""Compute relative luminance and WCAG contrast ratios for sRGB colours."""
from __future__ import annotations

from typing import Tuple

RGB = Tuple[int, int, int]


def _channel(value: int) -> float:
    if not 0 <= value <= 255:
        raise ValueError(f"colour component out of range 0-255: {value}")
    fraction = value / 255
    if fraction <= 0.03928:
        return fraction / 12.92
    return ((fraction + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: RGB) -> float:
    """Return the WCAG relative luminance of an sRGB colour."""
    r, g, b = (_channel(component) for component in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a: RGB, b: RGB) -> float:
    """Return the WCAG contrast ratio between two sRGB colours."""
    lum_a = relative_luminance(a)
    lum_b = relative_luminance(b)
    lighter, darker = (lum_a, lum_b) if lum_a >= lum_b else (lum_b, lum_a)
    return (lighter + 0.05) / (darker + 0.05)


def passes_aa(a: RGB, b: RGB, *, large_text: bool = False) -> bool:
    """Return ``True`` if the contrast ratio meets WCAG 2.x AA."""
    threshold = 3.0 if large_text else 4.5
    return contrast_ratio(a, b) >= threshold


def passes_aaa(a: RGB, b: RGB, *, large_text: bool = False) -> bool:
    """Return ``True`` if the contrast ratio meets WCAG 2.x AAA."""
    threshold = 4.5 if large_text else 7.0
    return contrast_ratio(a, b) >= threshold
