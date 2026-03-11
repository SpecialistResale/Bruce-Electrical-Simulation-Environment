"""Magnetic pressure approximation for field-dominated regions."""

from __future__ import annotations

from .common import require_non_negative


def magnetic_pressure(magnetic_flux_density_t: float) -> float:
    """Compute magnetic pressure p = B^2 / (2*mu_0) in pascals."""
    require_non_negative(magnetic_flux_density_t, "magnetic_flux_density_t")
    mu_0 = 4e-7 * 3.141592653589793
    return magnetic_flux_density_t**2 / (2 * mu_0)
