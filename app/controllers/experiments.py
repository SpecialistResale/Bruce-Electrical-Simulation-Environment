"""Experiment controllers that bind UI inputs to simulation engines."""

from __future__ import annotations

from dataclasses import dataclass

from simulations.inductive_energy import stored_inductive_energy
from simulations.inductive_voltage import induced_voltage
from simulations.joule_heating import joule_heating_energy, joule_heating_power
from simulations.lorentz_force import lorentz_force
from simulations.magnetic_field import magnetic_field_straight_conductor
from simulations.magnetic_pressure import magnetic_pressure
from simulations.skin_effect import skin_depth


@dataclass
class ExperimentResult:
    name: str
    value: float
    unit: str
    equation: str
    assumptions: str
    safety_note: str


def run_experiment(experiment_name: str, params: dict[str, float]) -> ExperimentResult:
    safety_note = "Simulation-only output. Do not use for live switching, hardware control, or energization procedures."

    if experiment_name == "Magnetic field around a straight conductor":
        value = magnetic_field_straight_conductor(params["current_a"], params["distance_m"])
        return ExperimentResult(experiment_name, value, "T", "B = μ0I/(2πr)", "Long straight conductor; free-space approximation.", safety_note)

    if experiment_name == "Lorentz force on conductor":
        value = lorentz_force(params["current_a"], params["length_m"], params["b_t"], params["angle_deg"])
        return ExperimentResult(experiment_name, value, "N", "F = BILsinθ", "Uniform field and static orientation.", safety_note)

    if experiment_name == "Inductive energy storage":
        value = stored_inductive_energy(params["inductance_h"], params["current_a"])
        return ExperimentResult(experiment_name, value, "J", "E = 1/2 LI²", "Linear lumped inductance.", safety_note)

    if experiment_name == "Inductive voltage / field collapse":
        value = induced_voltage(params["inductance_h"], params["di_dt_a_per_s"])
        return ExperimentResult(experiment_name, value, "V", "V = L dI/dt", "Linear inductor and simplified transient.", safety_note)

    if experiment_name == "Skin depth / frequency behavior":
        value = skin_depth(params["resistivity_ohm_m"], params["relative_permeability"], params["frequency_hz"])
        return ExperimentResult(experiment_name, value, "m", "δ = √(2ρ/(ωμ))", "Good-conductor sinusoidal approximation.", safety_note)

    if experiment_name == "Joule heating":
        value = joule_heating_energy(params["current_a"], params["resistance_ohm"], params["time_s"])
        return ExperimentResult(experiment_name, value, "J", "E = I²Rt", "Constant current and resistance.", safety_note)

    if experiment_name == "Magnetic pressure / busbar force approximation":
        value = magnetic_pressure(params["b_t"])
        return ExperimentResult(experiment_name, value, "Pa", "p = B²/(2μ0)", "Field-dominant isotropic estimate.", safety_note)

    raise ValueError(f"Unsupported experiment: {experiment_name}")


def run_joule_power(params: dict[str, float]) -> float:
    return joule_heating_power(params["current_a"], params["resistance_ohm"])
