"""Parse and evaluate tabletop dice-notation expressions like ``"2d6+3"``."""
from __future__ import annotations

import random
import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

_DICE = re.compile(
    r"^\s*(\d+)?\s*d\s*(\d+)\s*(?:([+-])\s*(\d+))?\s*$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Dice:
    count: int
    sides: int
    modifier: int = 0


def parse(notation: str) -> Dice:
    """Parse ``"2d6+3"`` into a :class:`Dice`."""
    match = _DICE.match(notation)
    if not match:
        raise ValueError(f"invalid dice notation: {notation!r}")
    count_raw, sides_raw, sign, modifier_raw = match.groups()
    count = int(count_raw) if count_raw else 1
    sides = int(sides_raw)
    if count <= 0 or sides <= 0:
        raise ValueError(f"count and sides must be positive: {notation!r}")
    modifier = 0
    if modifier_raw is not None:
        modifier = int(modifier_raw) * (1 if sign == "+" else -1)
    return Dice(count=count, sides=sides, modifier=modifier)


def minimum(dice: Dice) -> int:
    """Lowest possible total (each die shows 1)."""
    return dice.count + dice.modifier


def maximum(dice: Dice) -> int:
    """Highest possible total (each die shows ``sides``)."""
    return dice.count * dice.sides + dice.modifier


def average(dice: Dice) -> float:
    """Expected value of a roll (uniform faces)."""
    return dice.count * (dice.sides + 1) / 2 + dice.modifier


def roll(dice: Dice, rng: Optional[random.Random] = None) -> Tuple[int, List[int]]:
    """Roll the dice and return ``(total, individual_rolls)``."""
    generator = rng if rng is not None else random
    rolls = [generator.randint(1, dice.sides) for _ in range(dice.count)]
    return sum(rolls) + dice.modifier, rolls
