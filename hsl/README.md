# hsl

A tiny, dependency-free helper to convert sRGB colours between **HSL**
(hue / saturation / lightness) and **HSV** (hue / saturation / value).

## Usage

```python
from hsl import hsl_to_rgb, hsv_to_rgb, rgb_to_hsl, rgb_to_hsv

# Pure red.
h, s, l = rgb_to_hsl((255, 0, 0))
assert (round(h), round(s, 1), round(l, 1)) == (0, 1.0, 0.5)

# HSL <-> RGB round-trip.
assert hsl_to_rgb(rgb_to_hsl((200, 50, 100))) == (200, 50, 100)

# HSV variant.
h, s, v = rgb_to_hsv((0, 255, 0))
assert (round(h), round(s, 1), round(v, 1)) == (120, 1.0, 1.0)
```

Hue is reported in degrees ``[0, 360)``; saturation / lightness / value
in ``[0, 1]``. RGB inputs are integers in ``[0, 255]``.

## Tests

```bash
cd hsl
pytest
```
