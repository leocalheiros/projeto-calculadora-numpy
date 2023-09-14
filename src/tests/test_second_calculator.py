import pytest
from src.controllers.second_calculator_controller import SecondCalculator
from src.drivers.calculation_manager import CalculationManager


@pytest.fixture
def second_calculator():
    calculation_manager = CalculationManager()
    return SecondCalculator(calculation_manager)


def test_second_calculator_success(second_calculator):
    input_values = [1, 2, 3, 4, 5]

    _, status = second_calculator.calculate(input_values)

    assert status == 'Sucesso'


def test_second_calculator_fail(second_calculator):
    input_values = [1, 1, 1, 1, 1]

    _, status = second_calculator.calculate(input_values)

    assert status == 'Falha'
