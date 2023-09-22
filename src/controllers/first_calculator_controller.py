from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.drivers.calculation_manager import CalculationManager
from .interface.calculator_interface import ICalculator


class FirstCalculator(ICalculator):
    def __init__(self, calculation_manager: CalculationManager):
        self.__calculation_manager = calculation_manager

    def __calculate(self, value):
        part1 = value / 3
        part2 = value / 3
        part3 = value / 3

        part1 = (part1 / 4 + 7) ** 0.5 * 0.257

        part2 = (part2 ** 2.121) / 5 + 1

        result = self.__calculation_manager.average([part1, part2, part3])
        result = round(result, 1)

        status = "Sucesso"

        return {
            "status": status,
            "result": result
        }

    def execute(self, req: HttpRequest) -> HttpResponse:
        value = req.body.get('value')
        result_dict = self.__calculate(value)

        status = result_dict["status"]
        result = result_dict["result"]

        return HttpResponse(200, {
            "calculator": "First Calculator",
            "inputs": [value],
            "status": status,
            "result": result
        })
