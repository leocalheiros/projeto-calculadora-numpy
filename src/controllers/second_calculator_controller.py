from src.drivers.calculation_manager import CalculationManager


class SecondCalculator:
    def __init__(self, calculation_manager: CalculationManager) -> None:
        self.__calculation_manager = calculation_manager

    def calculate(self, values):
        powered_values = [(value * 11) ** 0.95 for value in values]

        std_deviation = self.__calculation_manager.std_deviation(powered_values)

        if std_deviation == 0:
            result = None
            status = "Falha"
        else:
            result = 1 / std_deviation
            status = "Sucesso"

        return result, status
