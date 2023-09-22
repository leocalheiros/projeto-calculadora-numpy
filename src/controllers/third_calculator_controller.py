from src.drivers.calculation_manager import CalculationManager
from .interface.calculator_interface import ICalculator


class ThirdCalculator(ICalculator):
    def __init__(self, calculation_manager: CalculationManager):
        self.__calculation_manager = calculation_manager

    def calculate(self, values):
        variance = self.__calculation_manager.variance(values)
        std_deviation = self.__calculation_manager.std_deviation(values)

        if variance > std_deviation:
            status = "Sucesso"
            result = f"Variance: {variance}, Std Deviation: {std_deviation}"
        else:
            status = "Falha"
            result = None

        return status, result
