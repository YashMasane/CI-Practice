import pytest
from app import calculate_bmi

def test_calculate_bmi_normal_case():
    """Test BMI calculation with normal inputs."""
    weight = 70  # in kilograms
    height = 1.75  # in meters
    expected_bmi = 22.86  # expected BMI
    assert calculate_bmi(weight, height) == expected_bmi

def test_calculate_bmi_zero_height():
    """Test BMI calculation when height is zero."""
    weight = 70
    height = 0
    with pytest.raises(ZeroDivisionError):
        calculate_bmi(weight, height)

def test_calculate_bmi_edge_case():
    """Test BMI calculation with edge values."""
    weight = 0  # no weight
    height = 1.75  # valid height
    expected_bmi = 0.0
    assert calculate_bmi(weight, height) == expected_bmi
