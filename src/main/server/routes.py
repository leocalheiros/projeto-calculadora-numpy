from flask import request, jsonify
from src.controllers.first_calculator_controller import FirstCalculator
from src.controllers.second_calculator_controller import SecondCalculator
from src.controllers.third_calculator_controller import ThirdCalculator
from src.main.http_types.http_request import HttpRequest
from src.drivers.calculation_manager import CalculationManager
from .server import app

calculation_manager = CalculationManager()


@app.route("/calculate", methods=["POST"])
def calculator_function():
    request_data = request.json

    if 'calculator_type' not in request_data or 'values' not in request_data:
        return jsonify({'error': 'Campos obrigatórios ausentes'}, 400)

    calculator_type = request_data.get('calculator_type')
    values = request_data.get('values')

    if calculator_type == 'first':
        calculator = FirstCalculator(calculation_manager)
        calculator_name = 'First Calculator'
    elif calculator_type == 'second':
        calculator = SecondCalculator(calculation_manager)
        calculator_name = 'Second Calculator'
    elif calculator_type == 'third':
        calculator = ThirdCalculator(calculation_manager)
        calculator_name = 'Third Calculator'
    else:
        return jsonify({'error': 'Tipo de calculadora não suportado'}, 400)

    results = []
    for value in values:
        req = HttpRequest(
            header=request.headers,
            body={"value": value},
        )

        response = calculator.execute(req)

        result_dict = {
            "calculator": calculator_name,
            "inputs": [value],
            "status": response.status_code,
            "result": response.body
        }
        results.append(result_dict)

    return jsonify(results), 200
