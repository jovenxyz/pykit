# pluralize

A tiny, dependency-free English pluralizer covering the common cases:
regular suffixes, ``-y`` after a consonant, ``-f``/``-fe`` -> ``-ves``, a
small list of irregular words, and a few uncountables.

## Usage

```python
from pluralize import pluralize, quantity

assert pluralize("cat") == "cats"
assert pluralize("city") == "cities"
assert pluralize("child") == "children"
assert pluralize("fish") == "fish"      # uncountable

assert quantity(1, "cat") == "1 cat"
assert quantity(2, "cat") == "2 cats"
assert quantity(3, "child") == "3 children"
assert quantity(2, "cactus", "cacti") == "2 cacti"
```

English plurals are full of exceptions; this helper aims to cover everyday
cases. For unusual words (``chief``, ``roof``, ``cactus``, ...), pass an
explicit plural via ``quantity``.

## Tests

```bash
cd pluralize
pytest
```
