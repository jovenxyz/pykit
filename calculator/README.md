# calc

A tiny, dependency-free **arithmetic expression calculator** for the command
line, built around a hand-written tokenizer and a recursive-descent parser.

It supports `+`, `-`, `*`, `/`, `%`, `**`, parentheses, unary signs and decimals.

## Install (editable)

```bash
cd calculator
pip install -e .
```

## Development

```bash
cd calculator
pip install pytest
pytest
```

## Grammar

```
expr  := term (("+" | "-") term)*
term  := power (("*" | "/" | "%") power)*
power := unary ("**" power)?       # right associative
unary := ("+" | "-") unary | atom
atom  := NUMBER | "(" expr ")"
```

## Usage

```bash
$ calc "2 + 3 * 4"
14
$ calc "2 ** 10"
1024
```

Run without an argument for an interactive REPL:

```bash
$ calc
calc REPL - type 'quit' to exit
> (1 + 2) * 3
9
> quit
```

From Python:

```python
from calc import evaluate

assert evaluate("2 ** 3 ** 2") == 512
```
