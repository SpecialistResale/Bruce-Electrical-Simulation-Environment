"""Shared helpers for validation and engineering assumptions."""

from __future__ import annotations


def require_positive(value: float, name: str) -> None:
    """Raise ValueError if value is not strictly positive."""
    if value <= 0:
        raise ValueError(f"{name} must be > 0. Received: {value}")


def require_non_negative(value: float, name: str) -> None:
    """Raise ValueError if value is negative."""
    if value < 0:
        raise ValueError(f"{name} must be >= 0. Received: {value}")
