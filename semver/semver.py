"""Parse and compare semantic version strings.

Implements the rules from https://semver.org/spec/v2.0.0.html. Build metadata
is preserved on round-trip but ignored when ordering versions, per the spec.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional, Tuple

_SEMVER = re.compile(
    r"^(\d+)\.(\d+)\.(\d+)"
    r"(?:-([0-9A-Za-z.-]+))?"
    r"(?:\+([0-9A-Za-z.-]+))?$"
)


def _prerelease_key(prerelease: str) -> Tuple:
    parts = []
    for part in prerelease.split("."):
        if part.isdigit():
            parts.append((0, int(part)))
        else:
            parts.append((1, part))
    return tuple(parts)


@dataclass(frozen=True)
class Version:
    major: int
    minor: int
    patch: int
    prerelease: Optional[str] = None
    build: Optional[str] = None

    def __str__(self) -> str:
        core = f"{self.major}.{self.minor}.{self.patch}"
        if self.prerelease:
            core += f"-{self.prerelease}"
        if self.build:
            core += f"+{self.build}"
        return core

    def _order_key(self) -> Tuple:
        if self.prerelease is None:
            return (self.major, self.minor, self.patch, 1, ())
        return (
            self.major,
            self.minor,
            self.patch,
            0,
            _prerelease_key(self.prerelease),
        )

    def __lt__(self, other: "Version") -> bool:
        return self._order_key() < other._order_key()

    def __le__(self, other: "Version") -> bool:
        return self._order_key() <= other._order_key()

    def __gt__(self, other: "Version") -> bool:
        return self._order_key() > other._order_key()

    def __ge__(self, other: "Version") -> bool:
        return self._order_key() >= other._order_key()

    def bump_major(self) -> "Version":
        return Version(self.major + 1, 0, 0)

    def bump_minor(self) -> "Version":
        return Version(self.major, self.minor + 1, 0)

    def bump_patch(self) -> "Version":
        return Version(self.major, self.minor, self.patch + 1)


def parse(value: str) -> Version:
    """Parse a semantic-version string into a :class:`Version`."""
    match = _SEMVER.match(value.strip())
    if not match:
        raise ValueError(f"invalid semver: {value!r}")
    major, minor, patch, prerelease, build = match.groups()
    return Version(int(major), int(minor), int(patch), prerelease, build)
