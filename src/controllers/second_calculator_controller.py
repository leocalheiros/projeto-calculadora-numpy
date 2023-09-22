from src.drivers.calculation_manager import CalculationManager
from .interface.calculator_interface import ICalculator
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest


class SecondCalculator(ICalculator):
    def __init__(self, calculation_manager: CalculationManager) -> None:
        self.__calculation_manager = calculation_manager

    def __calculate(self, values):
        print(f"Received values: {values}")

        powered_values = []

        if not isinstance(values, list):
            values = [values]

        for value in values:
            if value is not None:
                powered_value = (value * 11) ** 0.95
                print(f"Powered value: {powered_value}")
                powered_values.append(powered_value)

        if not powered_values:
            result = None
            status = "Falha"
        else:
            std_deviation = self.__calculation_manager.std_deviation(powered_values)
            if std_deviation == 0:
                result = None
                status = "Falha"
                print('Estou dando erro aqui')
                print(powered_values)
            else:
                result = 1 / std_deviation
                status = "Sucesso"
            print(f"Result: {result}, Status: {status}")

        return {
            "status": status,
            "result": result
        }

    def execute(self, req: HttpRequest) -> HttpResponse:
        values = req.body.get('value')
        result_dict = self.__calculate(values)

        status = result_dict["status"]
        result = result_dict["result"]

        return HttpResponse(200, {
            "calculator": "Second Calculator",
            "inputs": [values],
            "status": status,
            "result": result
        })

