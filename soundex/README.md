# soundex

A tiny, dependency-free implementation of the **American Soundex**
phonetic algorithm. Encode names by their sound so similar-sounding names
share a code -- ``"Robert"`` and ``"Rupert"`` both become ``"R163"``.

## Usage

```python
from soundex import soundex

assert soundex("Robert") == "R163"
assert soundex("Rupert") == "R163"
assert soundex("Ashcraft") == "A261"
assert soundex("Honeyman") == "H555"
```

The first letter is preserved; ``H`` and ``W`` are transparent; vowels and
``Y`` act as separators; runs of the same digit collapse to one. Codes are
padded with zeros to four characters.

## Tests

```bash
cd soundex
pytest
```
