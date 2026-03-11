# Bruce Electrical Laboratory

Bruce Electrical Laboratory is a safe, interactive, and immersive simulation environment for electrical and electromagnetic learning, analysis, and experimentation.

It is designed as a serious engineering lab experience: 3D scene navigation, experiment stations, live plots, layered expert interpretation, and voice-command-ready control flow.

## What this system is
- A simulation-first electrical laboratory.
- A learning and analytical environment.
- A modular platform for extending Bruce's layered electrical intelligence.

## What this system is not
- Not live hardware control.
- Not energization procedure guidance.
- Not a substitute for licensed field execution.

## Features
- 3D laboratory scene (browser-based Three.js render embedded in Streamlit).
- Experiment stations for:
  - Magnetic field around a conductor
  - Lorentz force
  - Inductive energy storage
  - Inductive voltage / field collapse
  - Skin depth behavior
  - Joule heating (power + energy)
  - Magnetic pressure approximation
- Real-time parameter controls and engineering charts.
- Layered explanations:
  1. Practical (Master Electrician)
  2. Scientific (Electrical Scientist)
  3. Deep Theory (Field interpretation)
- Voice/text command parsing pipeline (e.g., update current, distance, frequency, angle).
- Safety boundary checks with refusal handling for unsafe operational requests.

## Run locally
1. Create a Python 3.12 virtual environment.
2. Install dependencies.
3. Launch the application.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Test
```bash
pytest -q
python -m compileall simulations app visualizations lab tests
```

## Voice interaction notes
- In this baseline repository, command parsing and safe command routing are implemented and tested.
- Browser microphone capture / TTS integrations are designed to use Web Speech APIs in deployment environments.

## Repository layout
- `app/` application entrypoint, controllers, safety, and layered explanations
- `lab/` 3D lab scene and future equipment/experiment visual modules
- `simulations/` validated electrical simulation formulas
- `visualizations/` plotting helpers and future overlays/diagrams
- `tests/` unit tests for formulas, controllers, and safety logic
- `prompts/` layered Bruce reasoning prompt assets
- `docs/` safety and engineering notes

## Safety boundary
Bruce Electrical Laboratory must remain simulation-only and educational/analytical.
Unsafe real-world operational requests are refused and redirected to conceptual simulation-safe explanations.

## Cloud environment install troubleshooting
If dependency installation fails with proxy/network errors (for example when downloading `streamlit`), the simulation modules and tests can still be validated locally:

```bash
source .venv/bin/activate
pytest -q
```

When network access is restored, rerun:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
