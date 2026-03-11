"""Induced voltage helper module for transient current change simulations."""

from __future__ import annotations

from .common import require_non_negative


def induced_voltage(inductance_h: float, di_dt_a_per_s: float) -> float:
    """Compute induced voltage from changing current.

    Formula: V = L * dI/dt
    Returns volts (V).
    """
    require_non_negative(inductance_h, "inductance_h")
    return inductance_h * di_dt_a_per_s
