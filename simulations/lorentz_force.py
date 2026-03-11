"""Lorentz force model for a straight conductor segment in a magnetic field."""

from __future__ import annotations

import math

from .common import require_non_negative


def lorentz_force(
    current_a: float,
    conductor_length_m: float,
    magnetic_flux_density_t: float,
    angle_deg: float,
) -> float:
    """Compute force magnitude on a current-carrying conductor.

    Formula: F = B * I * L * sin(theta)

    Args:
        current_a: Current in amperes.
        conductor_length_m: Effective conductor length in field (m).
        magnetic_flux_density_t: Magnetic flux density in tesla.
        angle_deg: Angle between conductor current direction and field vector.

    Returns:
        Force magnitude in newtons.
    """
    require_non_negative(conductor_length_m, "conductor_length_m")
    require_non_negative(magnetic_flux_density_t, "magnetic_flux_density_t")
    theta = math.radians(angle_deg)
    return abs(magnetic_flux_density_t * current_a * conductor_length_m * math.sin(theta))
