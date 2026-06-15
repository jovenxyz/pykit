"""Body mass index calculator with WHO categories."""
from __future__ import annotations


def bmi(weight_kg: float, height_m: float) -> float:
    """Return the body mass index (weight / height^2) in kg/m^2."""
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if height_m <= 0:
        raise ValueError("height must be positive")
    return weight_kg / (height_m ** 2)


def category(value: float) -> str:
    """Return the WHO BMI category for a given BMI value."""
    if value <= 0:
        raise ValueError("BMI must be positive")
    if value < 18.5:
        return "underweight"
    if value < 25:
        return "normal"
    if value < 30:
        return "overweight"
    if value < 35:
        return "obese class I"
    if value < 40:
        return "obese class II"
    return "obese class III"


def from_imperial(weight_lb: float, height_in: float) -> float:
    """Compute BMI from imperial units (pounds and inches)."""
    if weight_lb <= 0 or height_in <= 0:
        raise ValueError("weight and height must be positive")
    return (weight_lb * 703) / (height_in ** 2)
