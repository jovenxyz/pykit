# bmi

A tiny, dependency-free helper for **Body Mass Index** calculations and
the WHO category lookup, in metric or imperial units.

## Usage

```python
from bmi import bmi, category, from_imperial

assert round(bmi(70, 1.75), 1) == 22.9
assert category(22.9) == "normal"

# Imperial:
assert round(from_imperial(154, 69), 1) == 22.7
```

WHO category thresholds: ``< 18.5`` underweight; ``18.5-24.9`` normal;
``25-29.9`` overweight; ``30+`` obese (classes I, II, III at 30 / 35 /
40).

## Tests

```bash
cd bmi
pytest
```
