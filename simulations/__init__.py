"""Core electrical simulation modules for Bruce Electrical Laboratory."""

from .inductive_energy import stored_inductive_energy
from .inductive_voltage import induced_voltage
from .joule_heating import joule_heating_energy, joule_heating_power
from .lorentz_force import lorentz_force
from .magnetic_field import magnetic_field_straight_conductor
from .magnetic_pressure import magnetic_pressure
from .skin_effect import skin_depth

__all__ = [
    "magnetic_field_straight_conductor",
    "lorentz_force",
    "stored_inductive_energy",
    "induced_voltage",
    "skin_depth",
    "joule_heating_power",
    "joule_heating_energy",
    "magnetic_pressure",
]
