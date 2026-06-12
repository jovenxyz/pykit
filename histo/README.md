# histo

A tiny, dependency-free helper for **ASCII bar charts and histograms**.
Render labelled data as simple horizontal bars, or bucket a sequence of
numbers into a histogram in one call.

## Usage

```python
from histo import bar_chart, histogram

print(bar_chart({"alpha": 10, "beta": 5, "gamma": 1}, width=20))
# alpha | #################### 10
# beta  | ########## 5
# gamma | ## 1

print(histogram([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], bins=4))
```

Pass ``sort="asc"`` or ``"desc"`` to reorder rows by value, and tune
``width`` (max bar length) or the ``bar`` character.

## Tests

```bash
cd histo
pytest
```
