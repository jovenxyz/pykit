"""Numerical differentiation via finite differences."""
from __future__ import annotations
from typing import Callable


def forward(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """Forward difference: O(h) error."""
    if h <= 0:
        raise ValueError("step h must be positive")
    return (f(x + h) - f(x)) / h


def backward(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """Backward difference: O(h) error."""
    if h <= 0:
        raise ValueError("step h must be positive")
    return (f(x) - f(x - h)) / h


def central(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """Central difference: O(h^2) error — generally the best default."""
    if h <= 0:
        raise ValueError("step h must be positive")
    return (f(x + h) - f(x - h)) / (2 * h)


def five_point(f: Callable[[float], float], x: float, h: float = 1e-4) -> float:
    """Five-point stencil: O(h^4) error."""
    if h <= 0:
        raise ValueError("step h must be positive")
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def second(f: Callable[[float], float], x: float, h: float = 1e-4) -> float:
    """Second derivative via central difference: O(h^2) error."""
    if h <= 0:
        raise ValueError("step h must be positive")
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


def partial(
    f: Callable[..., float],
    point: tuple[float, ...],
    index: int,
    h: float = 1e-5,
) -> float:
    """Partial derivative of a multivariate function via central difference."""
    if h <= 0:
        raise ValueError("step h must be positive")
    if not 0 <= index < len(point):
        raise IndexError("index out of range")
    plus = list(point)
    minus = list(point)
    plus[index] += h
    minus[index] -= h
    return (f(*plus) - f(*minus)) / (2 * h)


def gradient(
    f: Callable[..., float],
    point: tuple[float, ...],
    h: float = 1e-5,
) -> tuple[float, ...]:
    """Gradient vector of a scalar multivariate function."""
    return tuple(partial(f, point, i, h) for i in range(len(point)))
