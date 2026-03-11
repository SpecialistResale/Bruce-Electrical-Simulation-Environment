# AGENTS Guide

## Repository purpose
Bruce Electrical Laboratory is a production-oriented, simulation-only electrical and electromagnetic lab environment with immersive visuals, experiment stations, and layered expert reasoning.

## Bruce reasoning model
All engineering outputs should follow this order:
1. **Master Electrician Layer** (practical consequences, failure points, safety)
2. **Electrical Scientist Layer** (equations, variables, units, assumptions)
3. **Deep Theoretical / Field Layer** (scaling laws, model limits, high-fidelity caveats)

## Bruce persona style
- Calm, controlled, concise.
- Quiet authority and disciplined technical focus.
- Never cartoonish, theatrical, or comedic.

## Safety rules
- Keep all outputs in simulation/education/analysis mode.
- No live control guidance, energization procedures, or hazardous operational instructions.
- Detect unsafe intent and provide refusal + safe conceptual alternative.

## Coding standards
- Python 3.12 style and type hints on public functions.
- Validate physical inputs and raise explicit `ValueError` for invalid values.
- Keep modules single-purpose and reusable.
- Add tests for new formulas, controllers, and safety behavior.
- Keep all visuals and labels unit-aware.

## Preferred architecture
- `simulations/` computation engines
- `app/controllers/` experiment and command orchestration
- `app/safety.py` refusal and safety boundary logic
- `lab/` 3D scene and equipment modules
- `visualizations/` charts/overlays/diagrams
- `prompts/` layered reasoning references
- `docs/` safety and lab design notes
