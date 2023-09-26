from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from src.drivers.calculation_manager import CalculationManager
from .interface.calculator_interface import ICalculator


class ThirdCalculator(ICalculator):
    def __init__(self, calculation_manager: CalculationManager):
        self.__calculation_manager = calculation_manager

    def __calculate(self, values):
        variance = self.__calculate_variance(values)
        std_deviation = self.__calculate_std_deviation(values)

        status, result = self.__calculate_status(variance, std_deviation)

        return status, result

    def execute(self, req: HttpRequest) -> HttpResponse:
        values = req.body.get('values', [])
        status, result = self.__calculate(values)

        return HttpResponse(200, {
            "inputs": values,
            "status": status,
            "result": result
        })

    def __calculate_variance(self, values):
        return self.__calculation_manager.variance(values)

    def __calculate_std_deviation(self, values):
        return self.__calculation_manager.std_deviation(values)

    def __calculate_status(self, variance, std_deviation):
        if variance > std_deviation:
            status = "Sucesso"
            result = f"Variance: {variance}, Std Deviation: {std_deviation}"
        else:
            status = "Falha"
            result = None

        return status, result
