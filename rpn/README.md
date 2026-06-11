# rpn

A tiny, dependency-free **Reverse Polish Notation** (postfix) evaluator,
plus a shunting-yard **infix-to-RPN** converter.

## Usage

```python
from rpn import evaluate, infix_to_rpn

# Pure RPN:
assert evaluate("3 4 + 5 *") == 35
assert evaluate("2 3 2 ** **") == 512        # right-associative power

# Convert from infix:
assert infix_to_rpn("(3 + 4) * 5") == "3 4 + 5 *"
assert evaluate(infix_to_rpn("10 - 2 * 3")) == 4
```

Supports ``+ - * / % **``, parentheses, and integer/float literals.
Right-associative ``**`` and standard precedence are handled by the
shunting-yard algorithm.

## Tests

```bash
cd rpn
pytest
```
