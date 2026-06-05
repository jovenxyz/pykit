"""A tiny character/word Markov-chain text generator."""
from __future__ import annotations

import random
from collections import defaultdict
from typing import Dict, List, Optional, Sequence, Tuple


class MarkovChain:
    """Train on token sequences and sample new ones from the chain."""

    def __init__(self, order: int = 2) -> None:
        if order < 1:
            raise ValueError("order must be >= 1")
        self._order = order
        self._transitions: Dict[Tuple, List[str]] = defaultdict(list)
        self._starts: List[Tuple] = []

    def train(self, tokens: Sequence[str]) -> None:
        """Update the chain with a sequence of tokens."""
        if len(tokens) <= self._order:
            return
        self._starts.append(tuple(tokens[: self._order]))
        for i in range(len(tokens) - self._order):
            state = tuple(tokens[i : i + self._order])
            self._transitions[state].append(tokens[i + self._order])

    def generate(
        self,
        length: int,
        rng: Optional[random.Random] = None,
    ) -> List[str]:
        """Sample up to ``length`` tokens from the trained chain."""
        if not self._starts:
            raise RuntimeError("chain has no training data")
        generator = rng if rng is not None else random
        state = generator.choice(self._starts)
        result = list(state)
        while len(result) < length:
            options = self._transitions.get(state)
            if not options:
                break
            result.append(generator.choice(options))
            state = tuple(result[-self._order:])
        return result[:length]

    @property
    def order(self) -> int:
        return self._order

    @property
    def starts(self) -> List[Tuple]:
        return list(self._starts)
