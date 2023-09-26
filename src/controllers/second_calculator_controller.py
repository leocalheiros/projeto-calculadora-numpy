from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.drivers.calculation_manager import CalculationManager
from .interface.calculator_interface import ICalculator


class SecondCalculator(ICalculator):
    def __init__(self, calculation_manager: CalculationManager) -> None:
        self.__calculation_manager = calculation_manager

    def __calculate(self, values):
        powered_values = [(value * 11) ** 0.95 for value in values]
        return powered_values

    def __calculate_std_deviation(self, powered_values):
        std_deviation = self.__calculation_manager.std_deviation(powered_values)
        return std_deviation

    def __calculate_result(self, std_deviation):
        if std_deviation == 0:
            result = None
            status = "Falha"
        else:
            result = 1 / std_deviation
            status = "Sucesso"
        return result, status

    def execute(self, req: HttpRequest) -> HttpResponse:
        values = req.body.get('values', [])

        powered_values = self.__calculate(values)
        std_deviation = self.__calculate_std_deviation(powered_values)
        result, status = self.__calculate_result(std_deviation)

        return HttpResponse(200, {
            "inputs": values,
            "status": status,
            "result": result
        })
