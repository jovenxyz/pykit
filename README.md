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

## Usage

```python
from pytoolkit import Stack, BinarySearchTree
from pytoolkit.algorithms.sorting import merge_sort

stack = Stack()
stack.push(1)
stack.push(2)
assert stack.pop() == 2

tree = BinarySearchTree()
for key in (5, 3, 8, 1):
    tree.insert(key)
assert tree.inorder() == [1, 3, 5, 8]

assert merge_sort([3, 1, 2]) == [1, 2, 3]
```
