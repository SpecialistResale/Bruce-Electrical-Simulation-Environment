import pytest

from simulations.magnetic_field import magnetic_field_straight_conductor


def test_magnetic_field_nominal_case():
    result = magnetic_field_straight_conductor(current_a=10.0, distance_m=0.1)
    assert result == pytest.approx(2e-5, rel=1e-6)


def test_magnetic_field_invalid_distance():
    with pytest.raises(ValueError):
        magnetic_field_straight_conductor(current_a=5.0, distance_m=0.0)
