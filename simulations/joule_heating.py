"""Joule heating estimators for resistive elements."""

from __future__ import annotations

from .common import require_non_negative


def joule_heating_power(current_a: float, resistance_ohm: float) -> float:
    """Compute resistive power as P = I^2 * R in watts."""
    require_non_negative(resistance_ohm, "resistance_ohm")
    return current_a**2 * resistance_ohm


def joule_heating_energy(current_a: float, resistance_ohm: float, time_s: float) -> float:
    """Compute joule heating energy as E = I^2 * R * t in joules."""
    require_non_negative(time_s, "time_s")
    return joule_heating_power(current_a=current_a, resistance_ohm=resistance_ohm) * time_s
