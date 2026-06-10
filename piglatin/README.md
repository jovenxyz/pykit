# piglatin

A tiny, dependency-free **Pig Latin** translator. The classic playful
word transform: move the leading consonant cluster to the end of the
word and tack on ``"ay"`` (``"hello" -> "ellohay"``); words that start
with a vowel just get ``"way"`` appended (``"egg" -> "eggway"``).

## Usage

```python
from piglatin import translate, translate_word

assert translate_word("hello") == "ellohay"
assert translate_word("string") == "ingstray"
assert translate_word("egg") == "eggway"
assert translate("Hello, World!") == "Ellohay, Orldway!"
```

``y`` is treated as a vowel except when it's the very first letter.
Capitalisation of the original first letter is preserved on the result.

## Tests

```bash
cd piglatin
pytest
```
