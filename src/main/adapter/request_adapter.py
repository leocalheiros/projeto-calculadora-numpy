from src.controllers.interface.calculator_interface import ICalculator
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest


def request_adapter(request: HttpRequest, calculator: ICalculator) -> HttpResponse:
    http_response = calculator.execute(request)
    return http_response
