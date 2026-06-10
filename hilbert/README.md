# hilbert

A tiny, dependency-free helper that converts between ``(x, y)`` grid
coordinates and **Hilbert-curve indices**. The Hilbert curve is a
space-filling curve that preserves locality -- points close in 1-D index
space stay close in 2-D coordinate space.

## Usage

```python
from hilbert import d_to_xy, xy_to_d

order = 4                               # 16 x 16 grid
d = xy_to_d(order, 5, 7)                # encode (5, 7) as a Hilbert index
assert d_to_xy(order, d) == (5, 7)      # round-trip
```

Coordinates run over the ``2**order`` by ``2**order`` grid; indices run
over ``range(4**order)``.

## Tests

```bash
cd hilbert
pytest
```
