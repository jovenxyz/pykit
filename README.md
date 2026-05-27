# pytoolkit

A small, well-tested collection of classic **data structures** and **algorithms**
implemented in pure Python. Built as a learning reference and a place to practise
clean, tested code.

## Why

- Readable, dependency-free implementations.
- Every module is covered by `pytest`.
- A tidy `src/` layout that mirrors how real packages are shipped.

## Layout

```
src/pytoolkit/
  structures/   # Stack, Queue, LinkedList, BinarySearchTree, MinHeap
  algorithms/   # sorting, searching, graph traversal, dynamic programming
  strings/      # text helpers
  maths/        # number-theory helpers
tests/          # pytest suite mirroring the package layout
```

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
```
