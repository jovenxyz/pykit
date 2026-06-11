# medianstream

A tiny, dependency-free **streaming median** -- track the median of a
number stream in O(log n) per push using the classic two-heap technique.

## Usage

```python
from medianstream import StreamingMedian

sm = StreamingMedian()
for v in (3, 1, 4, 1, 5, 9, 2, 6):
    sm.push(v)
    print(sm.median())
```

For an even count the median is the average of the two middle values.

## Tests

```bash
cd medianstream
pytest
```
