import pytest

from app.controllers.experiments import run_experiment


def test_experiment_controller_magnetic_field():
    result = run_experiment(
        "Magnetic field around a straight conductor",
        {"current_a": 10.0, "distance_m": 0.1},
    )
    assert result.unit == "T"
    assert result.value == pytest.approx(2e-5, rel=1e-6)


def test_experiment_controller_unknown_experiment_raises():
    with pytest.raises(ValueError):
        run_experiment("Unknown", {})
