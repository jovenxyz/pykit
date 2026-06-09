# wordle

A tiny, dependency-free helper that scores a guess against a target word
using **Wordle**'s rules: each letter is GREEN (correct position),
YELLOW (in word, wrong position), or GRAY (not in word). Duplicate letters
are handled exactly as in the official game.

## Usage

```python
from wordle import is_solved, score

assert score("RAINS", "ROBIN") == "G.YY."
assert score("AAB", "ABC") == "G.Y"          # 2nd 'A' is gray; only one in target
assert is_solved(score("apple", "apple"))
```

The score string is one character per guess letter: ``G`` for green,
``Y`` for yellow, ``.`` for gray. Comparison is case-insensitive.

## Tests

```bash
cd wordle
pytest
```
