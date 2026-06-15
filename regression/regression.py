"""Least-squares linear regression and Pearson correlation."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class LinearFit:
    slope: float
    intercept: float
    r_squared: float

    def predict(self, x: float) -> float:
        return self.slope * x + self.intercept


def fit(xs: Sequence[float], ys: Sequence[float]) -> LinearFit:
    """Fit ``y = slope * x + intercept`` to the points by least squares."""
    if len(xs) != len(ys):
        raise ValueError("xs and ys must be the same length")
    if len(xs) < 2:
        raise ValueError("need at least two points")
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    sxx = sum((x - mean_x) ** 2 for x in xs)
    sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    if sxx == 0:
        raise ValueError("xs has zero variance; line is undefined")
    slope = sxy / sxx
    intercept = mean_y - slope * mean_x
    ss_total = sum((y - mean_y) ** 2 for y in ys)
    if ss_total == 0:
        r_squared = 1.0
    else:
        ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys))
        r_squared = 1 - ss_res / ss_total
    return LinearFit(slope=slope, intercept=intercept, r_squared=r_squared)


def correlation(xs: Sequence[float], ys: Sequence[float]) -> float:
    """Return the Pearson correlation coefficient of ``xs`` and ``ys``."""
    if len(xs) != len(ys):
        raise ValueError("xs and ys must be the same length")
    if len(xs) < 2:
        raise ValueError("need at least two points")
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    sxx = sum((x - mean_x) ** 2 for x in xs)
    syy = sum((y - mean_y) ** 2 for y in ys)
    sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    if sxx == 0 or syy == 0:
        raise ValueError("one of the series has zero variance")
    return sxy / (sxx ** 0.5 * syy ** 0.5)
