import pytest

from simulations.lorentz_force import lorentz_force


def test_lorentz_force_at_90_degrees():
    force = lorentz_force(current_a=5.0, conductor_length_m=2.0, magnetic_flux_density_t=0.3, angle_deg=90)
    assert force == pytest.approx(3.0)


def test_lorentz_force_at_zero_angle():
    force = lorentz_force(current_a=5.0, conductor_length_m=2.0, magnetic_flux_density_t=0.3, angle_deg=0)
    assert force == pytest.approx(0.0)


def test_lorentz_force_rejects_negative_length():
    with pytest.raises(ValueError):
        lorentz_force(current_a=5.0, conductor_length_m=-1.0, magnetic_flux_density_t=0.3, angle_deg=90)
