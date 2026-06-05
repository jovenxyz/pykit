# contrast

A tiny, dependency-free helper for **WCAG 2.x colour contrast**: compute the
relative luminance of an sRGB colour, the contrast ratio between two
colours, and AA / AAA pass-fail checks.

## Usage

```python
from contrast import contrast_ratio, passes_aa, passes_aaa, relative_luminance

assert contrast_ratio((0, 0, 0), (255, 255, 255)) == 21.0
assert passes_aa((0, 0, 0), (255, 255, 255))
assert not passes_aaa((0x77, 0x77, 0x77), (255, 255, 255))    # ~4.48
assert passes_aa((120, 120, 120), (255, 255, 255), large_text=True)
```

Colours are passed as ``(r, g, b)`` integer tuples in the 0-255 range.

## Tests

```bash
cd contrast
pytest
```
