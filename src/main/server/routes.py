from flask import request, jsonify
from src.controllers.first_calculator_controller import FirstCalculator
from src.controllers.second_calculator_controller import SecondCalculator
from src.controllers.third_calculator_controller import ThirdCalculator
from src.main.http_types.http_request import HttpRequest
from src.main.adapter.request_adapter import request_adapter
from src.drivers.calculation_manager import CalculationManager
from .server import app

calculation_manager = CalculationManager()


@app.route("/calculate/first", methods=["POST"])
def calculate_first():
    request_data = request.json

    if 'values' not in request_data:
        return jsonify({'error': 'Campo "values" ausente'}, 400)

    values = request_data.get('values')

    results = []

    for value in values:
        req = HttpRequest(
            header=request.headers,
            body={"value": value},
        )

        calculator = FirstCalculator(calculation_manager)
        response = request_adapter(req, calculator)

        result_dict = {
            "calculator": "First Calculator",
            "inputs": [value],
            "status": response.status_code,
            "result": response.body
        }

        results.append(result_dict)

    return jsonify(results), 200


@app.route("/calculate/second", methods=["POST"])
def calculate_second():
    request_data = request.json

    if 'values' not in request_data:
        return jsonify({'error': 'Campo "values" ausente'}, 400)

    values = request_data.get('values')

    calculator = SecondCalculator(calculation_manager)
    calculator_name = 'Second Calculator'

    req = HttpRequest(
        header=request.headers,
        body={"values": values},
    )

    response = request_adapter(req, calculator)

    result_dict = {
        "calculator": calculator_name,
        "inputs": values,
        "status": response.status_code,
        "result": response.body
    }

    return jsonify(result_dict), 200


@app.route("/calculate/third", methods=["POST"])
def calculate_third():
    request_data = request.json

    if 'values' not in request_data:
        return jsonify({'error': 'Campo "values" ausente'}, 400)

    values = request_data.get('values')

    calculator = ThirdCalculator(calculation_manager)
    calculator_name = 'Third Calculator'

    req = HttpRequest(
        header=request.headers,
        body={"values": values},
    )

    response = request_adapter(req, calculator)

    result_dict = {
        "calculator": calculator_name,
        "inputs": values,
        "status": response.status_code,
        "result": response.body
    }

    return jsonify(result_dict), 200
