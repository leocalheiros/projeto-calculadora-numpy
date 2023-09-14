from src.drivers.calculation_manager import CalculationManager


class FirstCalculator:
    def __init__(self, calculation_manager: CalculationManager):
        self.__calculation_manager = calculation_manager

    def calculate(self, value):
        part1 = value / 3
        part2 = value / 3
        part3 = value / 3

        part1 = (part1 / 4 + 7) ** 0.5 * 0.257

        part2 = (part2 ** 2.121) / 5 + 1

        result = self.__calculation_manager.average([part1, part2, part3])
        result = round(result, 1)

        status = "Sucesso"

        return result, status
