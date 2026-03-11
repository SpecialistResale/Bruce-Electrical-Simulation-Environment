# Bruce Electrical Simulator v1 File Inventory

This repository was expanded from a README-only baseline to include the first runnable simulation environment.

## Top-level files added
- `.gitignore`
- `AGENTS.md`
- `pytest.ini`
- `requirements.txt`
- `streamlit_app.py`

## Application files added
- `app/__init__.py`
- `app/main.py`
- `app/explanations.py`
- `app/safety.py`
- `app/controllers/__init__.py`
- `app/controllers/experiments.py`
- `app/controllers/voice.py`
- `app/state/__init__.py`

## Simulation engine files added
- `simulations/__init__.py`
- `simulations/common.py`
- `simulations/magnetic_field.py`
- `simulations/lorentz_force.py`
- `simulations/inductive_energy.py`
- `simulations/inductive_voltage.py`
- `simulations/skin_effect.py`
- `simulations/joule_heating.py`
- `simulations/magnetic_pressure.py`

## Laboratory and visualization files added
- `lab/__init__.py`
- `lab/scene/__init__.py`
- `lab/scene/lab_scene.py`
- `lab/equipment/__init__.py`
- `lab/experiments/__init__.py`
- `lab/ui/__init__.py`
- `lab/voice/__init__.py`
- `visualizations/__init__.py`
- `visualizations/plotting.py`
- `visualizations/charts/__init__.py`
- `visualizations/diagrams/__init__.py`
- `visualizations/overlays/__init__.py`

## Prompt and documentation files added
- `prompts/electrician_layered_prompt.md`
- `docs/safety_rules.md`
- `docs/engineering_notes.md`
- `docs/lab_design_brief.md`

## Test files added
- `tests/test_magnetic_field.py`
- `tests/test_lorentz_force.py`
- `tests/test_inductive_energy.py`
- `tests/test_skin_effect.py`
- `tests/test_experiment_controller.py`
- `tests/test_voice_controller.py`
- `tests/test_safety.py`
