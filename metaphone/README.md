# metaphone

Pure-Python implementation of the Metaphone phonetic algorithm
(Lawrence Philips, 1990). Maps English words to a phonetic key so that
similarly-pronounced words collide.

## API

- `metaphone(word: str) -> str` — returns the phonetic code (uppercase, may include `0` for the *th* sound)

## Example

```python
from metaphone import metaphone

metaphone("knight")  # 'NFT'
metaphone("night")   # 'NFT'   (homophones match)
metaphone("phone")   # 'FN'
metaphone("Thompson")
```

## Notes

This is the original Metaphone, not Double Metaphone — it is short, fast,
and works well for English given names and common words.

## Test

```bash
python -m pytest
```
