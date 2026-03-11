import pytest

from simulations.skin_effect import skin_depth


def test_skin_depth_for_copper_60hz():
    delta = skin_depth(resistivity_ohm_m=1.68e-8, relative_permeability=1.0, frequency_hz=60.0)
    assert delta == pytest.approx(0.00843, rel=0.02)


def test_skin_depth_rejects_invalid_frequency():
    with pytest.raises(ValueError):
        skin_depth(resistivity_ohm_m=1.68e-8, relative_permeability=1.0, frequency_hz=0.0)
