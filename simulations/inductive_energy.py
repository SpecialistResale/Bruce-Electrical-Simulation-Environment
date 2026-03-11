"""Inductive energy formulas for lumped models."""

from __future__ import annotations

from .common import require_non_negative


def stored_inductive_energy(inductance_h: float, current_a: float) -> float:
    """Compute energy stored in an inductor.

    Formula: E = 1/2 * L * I^2
    Returns joules (J).
    """
    require_non_negative(inductance_h, "inductance_h")
    return 0.5 * inductance_h * current_a**2
