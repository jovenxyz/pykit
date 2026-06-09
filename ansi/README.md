# ansi

A tiny, dependency-free helper to wrap text with **ANSI escape codes**
for terminal colours and styles. Includes the standard and bright 16-colour
palette plus the common styles (bold, dim, italic, underline, reverse,
strike, blink).

## Usage

```python
from ansi import colorize, strip_ansi

print(colorize("error", fg="red", style="bold"))
print(colorize("info",  fg="cyan"))
print(colorize("warn",  fg="black", bg="yellow"))

# Remove ANSI escapes -- useful for measuring lengths or asserting output:
assert strip_ansi(colorize("hi", fg="red")) == "hi"
```

Pass ``style=`` a single name or an iterable of names to combine effects.
Unknown colour or style names raise ``ValueError``.

## Tests

```bash
cd ansi
pytest
```
