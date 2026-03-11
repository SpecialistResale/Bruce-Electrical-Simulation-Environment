import pytest

from simulations.inductive_energy import stored_inductive_energy
from simulations.inductive_voltage import induced_voltage


def test_stored_energy_basic():
    energy = stored_inductive_energy(inductance_h=0.2, current_a=10.0)
    assert energy == pytest.approx(10.0)


def test_induced_voltage_sign_follows_didt():
    voltage = induced_voltage(inductance_h=0.1, di_dt_a_per_s=-40.0)
    assert voltage == pytest.approx(-4.0)


def test_inductance_must_be_non_negative():
    with pytest.raises(ValueError):
        stored_inductive_energy(inductance_h=-0.1, current_a=1.0)
