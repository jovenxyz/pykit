# markov

A tiny, dependency-free **Markov-chain text generator**. Train on any
sequence of tokens (characters, words, anything hashable) and sample new
sequences from it.

## Usage

```python
import random

from markov import MarkovChain

chain = MarkovChain(order=2)
chain.train("the quick brown fox jumps over the lazy dog".split())

print(" ".join(chain.generate(10, rng=random.Random(0))))
```

The ``order`` controls how many previous tokens condition each next pick.
Pass ``rng=`` to make generation deterministic in tests.

## Tests

```bash
cd markov
pytest
```
