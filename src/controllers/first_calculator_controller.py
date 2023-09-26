from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.drivers.calculation_manager import CalculationManager
from .interface.calculator_interface import ICalculator


class FirstCalculator(ICalculator):
    def __init__(self, calculation_manager: CalculationManager):
        self.__calculation_manager = calculation_manager

    def __calculate(self, value):
        part1 = self.__calculate_part1(value)
        part2 = self.__calculate_part2(value)
        part3 = self.__calculate_part3(value)

        result = self.__calculation_manager.average([part1, part2, part3])
        result = round(result, 1)

        status = "Sucesso"

        return {
            "status": status,
            "result": result
        }

    def __calculate_part1(self, value):
        part1 = value / 3
        part1 = (part1 / 4 + 7) ** 0.5 * 0.257
        return part1

    def __calculate_part2(self, value):
        part2 = value / 3
        part2 = (part2 ** 2.121) / 5 + 1
        return part2

    def __calculate_part3(self, value):
        return value / 3

    def execute(self, req: HttpRequest) -> HttpResponse:
        value = req.body.get('value')
        result_dict = self.__calculate(value)

        status = result_dict["status"]
        result = result_dict["result"]

        return HttpResponse(200, {
            "inputs": [value],
            "status": status,
            "result": result
        })
