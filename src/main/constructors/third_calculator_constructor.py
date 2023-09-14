from src.controllers.third_calculator_controller import ThirdCalculator
from src.views.third_calculator_view import ThirdCalculatorView
from src.drivers.calculation_manager import CalculationManager
from src.views.menu_view import MenuView


class ThirdCalculatorConstructor:
    def __init__(self):
        self.calculation_manager = CalculationManager()
        self.third_calculator_controller = ThirdCalculator(self.calculation_manager)
        self.third_calculator_view = ThirdCalculatorView()
        self.menu_view = MenuView()

    def run(self):
        while True:
            self.third_calculator_view.display_menu()
            values = self.third_calculator_view.get_user_input()

            if not values or 0 in values:
                return

            status, result = self.third_calculator_controller.calculate(values)

            result_dict = {
                "calculator": "Terceira Calculadora",
                "inputs": values,
                "status": status,
                "result": result,
            }

            self.menu_view.display_result(result_dict)
