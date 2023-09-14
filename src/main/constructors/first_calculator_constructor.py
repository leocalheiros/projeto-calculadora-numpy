from src.controllers.first_calculator_controller import FirstCalculator
from src.views.first_calculator_view import FirstCalculatorView
from src.views.menu_view import MenuView


class FirstCalculatorConstructor:
    def __init__(self, calculation_manager, first_calculator_controller: FirstCalculator):
        self.calculation_manager = calculation_manager
        self.first_calculator_controller = first_calculator_controller
        self.first_calculator_view = FirstCalculatorView()
        self.menu_view = MenuView()

    def run(self):
        while True:
            self.first_calculator_view.display_menu()
            value = self.first_calculator_view.get_user_input()

            if value == 0:
                return

            result, status = self.first_calculator_controller.calculate(value)

            result_dict = {
                "calculator": "Primeira Calculadora",
                "inputs": [value],
                "status": status,
                "result": result
            }

            self.menu_view.display_result(result_dict)
