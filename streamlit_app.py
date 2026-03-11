"""Bruce Electrical Simulator v1 Streamlit entrypoint.

Simulation-only, educational laboratory interface.
"""

from __future__ import annotations

import numpy as np
import streamlit as st

from app.explanations import layered_explanation
from app.safety import safe_refusal_message
from simulations.inductive_energy import stored_inductive_energy
from simulations.inductive_voltage import induced_voltage
from simulations.lorentz_force import lorentz_force
from simulations.magnetic_field import magnetic_field_straight_conductor
from simulations.skin_effect import skin_depth
from visualizations.plotting import line_plot


st.set_page_config(page_title="Bruce Electrical Simulator", layout="wide")
st.title("Bruce Electrical Simulator")
st.caption("Simulation-only electrical laboratory for learning, analysis, and safe experimentation.")

st.sidebar.header("Experiment selector")
experiment = st.sidebar.selectbox(
    "Choose simulation",
    [
        "Magnetic field around straight conductor",
        "Lorentz force on conductor",
        "Inductive energy storage",
        "Inductive voltage from dI/dt",
        "Skin depth approximation",
    ],
)

result_value: float
result_unit: str
result_equation: str
assumptions: str

if experiment == "Magnetic field around straight conductor":
    current_a = st.number_input("Current I (A)", value=100.0)
    distance_m = st.number_input("Distance r (m)", value=0.05, min_value=1e-6)

    result_value = magnetic_field_straight_conductor(current_a, distance_m)
    result_unit = "T"
    result_equation = "B = μ₀I / (2πr)"
    assumptions = "Long straight conductor, free-space permeability, quasi-static approximation."

    r_values = np.linspace(0.001, max(0.2, distance_m * 3), 160)
    b_values = [magnetic_field_straight_conductor(current_a, r) for r in r_values]
    st.pyplot(line_plot(r_values, b_values, "Magnetic field vs distance", "Distance (m)", "B (T)"))

elif experiment == "Lorentz force on conductor":
    current_a = st.number_input("Current I (A)", value=100.0)
    length_m = st.number_input("Conductor length L (m)", value=0.5, min_value=0.0)
    magnetic_flux_density_t = st.number_input("Magnetic field B (T)", value=0.2, min_value=0.0)
    angle_deg = st.slider("Angle θ (deg)", min_value=0, max_value=180, value=90)

    result_value = lorentz_force(current_a, length_m, magnetic_flux_density_t, angle_deg)
    result_unit = "N"
    result_equation = "F = BIL sin(θ)"
    assumptions = "Uniform magnetic field and straight conductor segment in-field."

    i_values = np.linspace(0, max(200.0, current_a * 2), 160)
    force_values = [lorentz_force(i, length_m, magnetic_flux_density_t, angle_deg) for i in i_values]
    st.pyplot(line_plot(i_values, force_values, "Lorentz force vs current", "Current (A)", "Force (N)"))

elif experiment == "Inductive energy storage":
    inductance_h = st.number_input("Inductance L (H)", value=0.01, min_value=0.0)
    current_a = st.number_input("Current I (A)", value=100.0)

    result_value = stored_inductive_energy(inductance_h, current_a)
    result_unit = "J"
    result_equation = "E = 1/2 LI²"
    assumptions = "Lumped inductor, linear inductance, no saturation."

    i_values = np.linspace(0, max(150.0, current_a * 1.5), 160)
    energy_values = [stored_inductive_energy(inductance_h, i) for i in i_values]
    st.pyplot(line_plot(i_values, energy_values, "Stored energy vs current", "Current (A)", "Energy (J)"))

elif experiment == "Inductive voltage from dI/dt":
    inductance_h = st.number_input("Inductance L (H)", value=0.01, min_value=0.0)
    di_dt_a_per_s = st.number_input("Current change rate dI/dt (A/s)", value=1000.0)

    result_value = induced_voltage(inductance_h, di_dt_a_per_s)
    result_unit = "V"
    result_equation = "V = L(dI/dt)"
    assumptions = "Lumped inductor model, constant L over the operating region."

    didt_values = np.linspace(-2000, 2000, 160)
    voltage_values = [induced_voltage(inductance_h, x) for x in didt_values]
    st.pyplot(line_plot(didt_values, voltage_values, "Induced voltage vs dI/dt", "dI/dt (A/s)", "Voltage (V)"))

else:
    resistivity_ohm_m = st.number_input("Resistivity ρ (Ω·m)", value=1.68e-8, format="%.3e")
    relative_permeability = st.number_input("Relative permeability μr", value=1.0, min_value=1e-4)
    frequency_hz = st.number_input("Frequency f (Hz)", value=60.0, min_value=1e-6)

    result_value = skin_depth(resistivity_ohm_m, relative_permeability, frequency_hz)
    result_unit = "m"
    result_equation = "δ = √(2ρ / ωμ)"
    assumptions = "Good-conductor approximation and sinusoidal steady-state excitation."

    f_values = np.logspace(1, 6, 160)
    depth_values = [skin_depth(resistivity_ohm_m, relative_permeability, f) for f in f_values]
    st.pyplot(line_plot(f_values, depth_values, "Skin depth vs frequency", "Frequency (Hz)", "Skin depth (m)"))

st.metric("Computed result", f"{result_value:.6e} {result_unit}")

layers = layered_explanation(
    result_summary=f"Computed result = {result_value:.3e} {result_unit}",
    equation=result_equation,
    assumptions=assumptions,
    deep_note="Nonlinear materials, geometric edge effects, thermal coupling, and transients can require FEM-based multiphysics solvers.",
)

st.markdown("### Layered explanation")
for layer_name in ["Practical layer", "Scientific layer", "Deep theory layer", "Safety boundary"]:
    with st.expander(layer_name, expanded=layer_name == "Practical layer"):
        st.write(layers[layer_name])

st.info(safe_refusal_message())
