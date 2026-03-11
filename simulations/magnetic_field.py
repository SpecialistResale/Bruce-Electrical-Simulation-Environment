"""Magnetic field models for simple conductor geometries.

Assumptions:
- Long, straight conductor in free space.
- Quasi-static regime.
- Neglects proximity effects and ferromagnetic geometry.
"""

from __future__ import annotations

from .common import require_positive

MU_0 = 4e-7 * 3.141592653589793


def magnetic_field_straight_conductor(current_a: float, distance_m: float) -> float:
    """Compute magnetic flux density B (tesla) around a straight conductor.

    Formula: B = mu_0 * I / (2 * pi * r)

    Args:
        current_a: Current in amperes.
        distance_m: Radial distance from conductor center in meters.

    Returns:
        Magnetic flux density in tesla (T).
    """
    require_positive(distance_m, "distance_m")
    return MU_0 * current_a / (2 * 3.141592653589793 * distance_m)
