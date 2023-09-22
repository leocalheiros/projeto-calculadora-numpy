from flask import request as FlaskRequest
from src.controllers.interface.calculator_interface import ICalculator
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest


def request_adapter(request: FlaskRequest, calculator: ICalculator) -> HttpResponse:
    req = HttpRequest(
        header=request.headers,
        body=request.json,
        query_params=dict(request.args),
        path_params=request.view_args,
        url=request.full_path,
        ipv4=request.remote_addr,
    )
    http_response = calculator.calculate(req)
    return http_response
