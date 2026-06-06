# jaro

A tiny, dependency-free implementation of **Jaro** and **Jaro-Winkler**
string similarity -- a character-based measure that emphasises matches
near the start of the string. Often used for record linkage and fuzzy
name matching.

## Usage

```python
from jaro import jaro_similarity, jaro_winkler_similarity

assert round(jaro_similarity("MARTHA", "MARHTA"), 4) == 0.9444
assert round(jaro_winkler_similarity("MARTHA", "MARHTA"), 4) == 0.9611
assert round(jaro_similarity("DIXON", "DICKSONX"), 4) == 0.7666
```

Both return a value in ``[0.0, 1.0]``. Tune ``prefix_scale`` (default
``0.1``, max ``0.25``) and ``max_prefix`` (default ``4``) to weight the
shared prefix more or less aggressively.

## Tests

```bash
cd jaro
pytest
```
