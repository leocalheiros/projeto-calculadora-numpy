import pytest
from src.controllers.first_calculator_controller import FirstCalculator
from src.drivers.calculation_manager import CalculationManager


def test_first_calculator_controller_success():
    calculation_manager = CalculationManager()

    first_calculator = FirstCalculator(calculation_manager)

    input_value = 12

    result = first_calculator.calculate(input_value)

    expected_result = 3.2

    assert result == pytest.approx(expected_result)
