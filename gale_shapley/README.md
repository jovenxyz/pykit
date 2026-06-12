# gale_shapley

A tiny, dependency-free implementation of the **Gale-Shapley** stable
matching algorithm (proposer-optimal). Given two equal-sized groups and
their ranked preferences, find a matching with no blocking pair.

## Usage

```python
from gale_shapley import is_stable, stable_matching

applicants = {
    "Alice":   ["X", "Y", "Z"],
    "Bob":     ["Y", "X", "Z"],
    "Charlie": ["X", "Y", "Z"],
}
schools = {
    "X": ["Bob", "Alice", "Charlie"],
    "Y": ["Alice", "Bob", "Charlie"],
    "Z": ["Alice", "Bob", "Charlie"],
}

matching = stable_matching(applicants, schools)
assert is_stable(matching, applicants, schools)
```

The result maps each proposer to their assigned receiver. Proposers
achieve their best possible stable partner; receivers their worst.

## Tests

```bash
cd gale_shapley
pytest
```
