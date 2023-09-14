from src.controllers.second_calculator_controller import SecondCalculator
from src.views.second_calculator_view import SecondCalculatorView
from src.drivers.calculation_manager import CalculationManager
from src.views.menu_view import MenuView


class SecondCalculatorConstructor:
    def __init__(self):
        self.calculation_manager = CalculationManager()
        self.second_calculator_controller = SecondCalculator(self.calculation_manager)
        self.second_calculator_view = SecondCalculatorView()
        self.menu_view = MenuView()

    def run(self):
        while True:
            self.second_calculator_view.display_menu()
            values = self.second_calculator_view.get_user_input()

            if not values or 0 in values:
                return

            result, status = self.second_calculator_controller.calculate(values)

            result_dict = {
                "calculator": "Segunda Calculadora",
                "inputs": values,
                "status": status,
                "result": result
            }

            self.menu_view.display_result(result_dict)
