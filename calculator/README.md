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
