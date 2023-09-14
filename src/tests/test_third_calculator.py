from src.controllers.third_calculator_controller import ThirdCalculator
from src.drivers.calculation_manager import CalculationManager


def test_third_calculator_is_not_none():
    calculation_manager = CalculationManager()
    third_calculator = ThirdCalculator(calculation_manager)

    input_values = [1, 2, 3, 4, 5]

    result = third_calculator.calculate(input_values)

    assert result is not None


def test_third_calculator_expected_result_sucesso():
    calculation_manager = CalculationManager()
    third_calculator = ThirdCalculator(calculation_manager)

    input_values = [1, 2, 3, 4, 5]

    result, _ = third_calculator.calculate(input_values)

    expected_result = 'Sucesso'

    assert result == expected_result


def test_third_calculator_expected_result_falha():
    calculation_manager = CalculationManager()
    third_calculator = ThirdCalculator(calculation_manager)

    input_values = [1, 2, 3]

    result, _ = third_calculator.calculate(input_values)

    # Substitua por um valor que você acha apropriado para um teste de falha
    expected_result = 'Falha'

    assert result == expected_result
