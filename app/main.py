"""Bruce Electrical Laboratory: immersive simulation-first interface."""

from __future__ import annotations

import numpy as np
import streamlit as st
import streamlit.components.v1 as components

from app.controllers.experiments import run_experiment, run_joule_power
from app.controllers.voice import parse_voice_command
from app.explanations import layered_explanation
from app.safety import is_unsafe_request, safe_refusal_message
from lab.scene.lab_scene import build_lab_scene_html
from simulations.inductive_energy import stored_inductive_energy
from simulations.inductive_voltage import induced_voltage
from simulations.joule_heating import joule_heating_energy
from simulations.lorentz_force import lorentz_force
from simulations.magnetic_field import magnetic_field_straight_conductor
from simulations.magnetic_pressure import magnetic_pressure
from simulations.skin_effect import skin_depth
from visualizations.plotting import line_plot

st.set_page_config(page_title="Bruce Electrical Laboratory", layout="wide")
st.title("Bruce Electrical Laboratory")
st.caption("Safe, immersive simulation lab for electrical and electromagnetic analysis.")

if "current_a" not in st.session_state:
    st.session_state.current_a = 120.0
if "distance_m" not in st.session_state:
    st.session_state.distance_m = 0.05
if "frequency_hz" not in st.session_state:
    st.session_state.frequency_hz = 60.0
if "angle_deg" not in st.session_state:
    st.session_state.angle_deg = 90.0

lab_tab, experiment_tab, bruce_tab = st.tabs(["3D Laboratory", "Experiment Stations", "Bruce Voice & Analysis"])

with lab_tab:
    st.subheader("Immersive laboratory scene")
    st.write("Rotate and inspect benches, racks, instrument panels, and cable routing.")
    components.html(build_lab_scene_html(), height=540)

with experiment_tab:
    station = st.sidebar.selectbox(
        "Experiment station",
        [
            "Magnetic field around a straight conductor",
            "Lorentz force on conductor",
            "Inductive energy storage",
            "Inductive voltage / field collapse",
            "Skin depth / frequency behavior",
            "Joule heating",
            "Magnetic pressure / busbar force approximation",
        ],
    )

    params: dict[str, float] = {}

    if station == "Magnetic field around a straight conductor":
        params["current_a"] = st.number_input("Current I (A)", value=st.session_state.current_a)
        params["distance_m"] = st.number_input("Distance r (m)", value=st.session_state.distance_m, min_value=1e-6)
        st.session_state.current_a = params["current_a"]
        st.session_state.distance_m = params["distance_m"]

    elif station == "Lorentz force on conductor":
        params["current_a"] = st.number_input("Current I (A)", value=st.session_state.current_a)
        params["length_m"] = st.number_input("Conductor length L (m)", value=0.5, min_value=0.0)
        params["b_t"] = st.number_input("Magnetic flux density B (T)", value=0.2, min_value=0.0)
        params["angle_deg"] = st.slider("Angle θ (deg)", 0, 180, int(st.session_state.angle_deg))
        st.session_state.current_a = params["current_a"]
        st.session_state.angle_deg = params["angle_deg"]

    elif station == "Inductive energy storage":
        params["inductance_h"] = st.number_input("Inductance L (H)", value=0.02, min_value=0.0)
        params["current_a"] = st.number_input("Current I (A)", value=st.session_state.current_a)
        st.session_state.current_a = params["current_a"]

    elif station == "Inductive voltage / field collapse":
        params["inductance_h"] = st.number_input("Inductance L (H)", value=0.02, min_value=0.0)
        params["di_dt_a_per_s"] = st.number_input("dI/dt (A/s)", value=100.0)

    elif station == "Skin depth / frequency behavior":
        params["resistivity_ohm_m"] = st.number_input("Resistivity ρ (Ω·m)", value=1.68e-8, format="%.3e")
        params["relative_permeability"] = st.number_input("Relative permeability μr", value=1.0, min_value=1e-4)
        params["frequency_hz"] = st.number_input("Frequency f (Hz)", value=st.session_state.frequency_hz, min_value=1e-4)
        st.session_state.frequency_hz = params["frequency_hz"]

    elif station == "Joule heating":
        params["current_a"] = st.number_input("Current I (A)", value=st.session_state.current_a)
        params["resistance_ohm"] = st.number_input("Resistance R (Ω)", value=0.5, min_value=0.0)
        params["time_s"] = st.number_input("Time t (s)", value=10.0, min_value=0.0)
        st.session_state.current_a = params["current_a"]

    else:
        params["b_t"] = st.number_input("Magnetic flux density B (T)", value=0.5, min_value=0.0)

    result = run_experiment(station, params)
    st.metric(f"{result.name} result", f"{result.value:.6e} {result.unit}")

    st.markdown("### Assumptions")
    st.table({"Equation": [result.equation], "Assumptions": [result.assumptions], "Safety": [result.safety_note]})

    if station == "Magnetic field around a straight conductor":
        r_vals = np.linspace(0.005, max(params["distance_m"] * 3, 0.06), 160)
        y_vals = [magnetic_field_straight_conductor(params["current_a"], x) for x in r_vals]
        st.pyplot(line_plot(r_vals, y_vals, "Magnetic field vs distance", "Distance (m)", "B (T)"))
    elif station == "Lorentz force on conductor":
        i_vals = np.linspace(0, max(params["current_a"] * 2, 10), 160)
        y_vals = [lorentz_force(x, params["length_m"], params["b_t"], params["angle_deg"]) for x in i_vals]
        st.pyplot(line_plot(i_vals, y_vals, "Lorentz force vs current", "Current (A)", "Force (N)"))
    elif station == "Inductive energy storage":
        i_vals = np.linspace(0, max(params["current_a"] * 1.5, 1), 160)
        y_vals = [stored_inductive_energy(params["inductance_h"], x) for x in i_vals]
        st.pyplot(line_plot(i_vals, y_vals, "Stored energy vs current", "Current (A)", "Energy (J)"))
    elif station == "Inductive voltage / field collapse":
        didt = np.linspace(-500, 500, 160)
        y_vals = [induced_voltage(params["inductance_h"], x) for x in didt]
        st.pyplot(line_plot(didt, y_vals, "Induced voltage vs dI/dt", "dI/dt (A/s)", "Voltage (V)"))
    elif station == "Skin depth / frequency behavior":
        f_vals = np.logspace(1, 6, 160)
        y_vals = [skin_depth(params["resistivity_ohm_m"], params["relative_permeability"], x) for x in f_vals]
        st.pyplot(line_plot(f_vals, y_vals, "Skin depth vs frequency", "Frequency (Hz)", "Skin depth (m)"))
    elif station == "Joule heating":
        t_vals = np.linspace(0, max(params["time_s"] * 2, 1), 160)
        y_vals = [joule_heating_energy(params["current_a"], params["resistance_ohm"], x) for x in t_vals]
        st.pyplot(line_plot(t_vals, y_vals, "Joule heating vs time", "Time (s)", "Energy (J)"))
        st.metric("Power dissipation", f"{run_joule_power(params):.6e} W")
    else:
        b_vals = np.linspace(0, max(params["b_t"] * 2, 1), 160)
        y_vals = [magnetic_pressure(x) for x in b_vals]
        st.pyplot(line_plot(b_vals, y_vals, "Magnetic pressure vs field", "B (T)", "Pressure (Pa)"))

    explanation = layered_explanation(
        result_summary=f"Computed result: {result.value:.3e} {result.unit}.",
        equation=result.equation,
        assumptions=result.assumptions,
        deep_note="For geometry-rich systems, nonlinear material behavior and distributed transients require FEM-grade or multiphysics modeling.",
    )
    st.markdown("### Layered Bruce explanation")
    for k, v in explanation.items():
        with st.expander(k, expanded=k == "Practical layer"):
            st.write(v)

with bruce_tab:
    st.subheader("Bruce conversation and voice command bridge")
    st.write("Use text or voice transcript to modify simulation state. Example: 'increase current to 800' or 'distance to 10 mm'.")

    user_prompt = st.text_area("Message or voice transcript", placeholder="Bruce, increase current to 800 amps.")
    if st.button("Process request"):
        if is_unsafe_request(user_prompt):
            st.error(safe_refusal_message())
        else:
            parsed = parse_voice_command(user_prompt)
            st.json(parsed)
            if parsed.get("intent") == "update_parameters":
                if "current_a" in parsed:
                    st.session_state.current_a = float(parsed["current_a"])
                if "distance_m" in parsed:
                    st.session_state.distance_m = float(parsed["distance_m"])
                if "frequency_hz" in parsed:
                    st.session_state.frequency_hz = float(parsed["frequency_hz"])
                if "angle_deg" in parsed:
                    st.session_state.angle_deg = float(parsed["angle_deg"])
                st.success("Simulation parameters updated from voice/text command.")

    st.markdown("#### Browser voice I/O implementation note")
    st.info(
        "Microphone capture and TTS are integrated through browser APIs in deployment environments. "
        "In this repository baseline, command parsing and response pipeline are implemented and testable in simulation mode."
    )
