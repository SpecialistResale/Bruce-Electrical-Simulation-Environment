"""Skin effect approximation in good conductors."""

from __future__ import annotations

import math

from .common import require_positive


def skin_depth(resistivity_ohm_m: float, relative_permeability: float, frequency_hz: float) -> float:
    """Approximate skin depth in meters.

    Formula: delta = sqrt(2 * rho / (omega * mu))
    where mu = mu_0 * mu_r and omega = 2*pi*f.
    """
    require_positive(resistivity_ohm_m, "resistivity_ohm_m")
    require_positive(relative_permeability, "relative_permeability")
    require_positive(frequency_hz, "frequency_hz")
    mu_0 = 4e-7 * math.pi
    omega = 2 * math.pi * frequency_hz
    mu = mu_0 * relative_permeability
    return math.sqrt((2 * resistivity_ohm_m) / (omega * mu))
