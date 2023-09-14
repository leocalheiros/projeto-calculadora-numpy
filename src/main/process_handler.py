import sys
from src.views.menu_view import MenuView
from src.drivers.calculation_manager import CalculationManager
from src.controllers.first_calculator_controller import FirstCalculator
from src.main.constructors.first_calculator_constructor import FirstCalculatorConstructor
from src.main.constructors.second_calculator_constructor import SecondCalculatorConstructor
from src.main.constructors.third_calculator_constructor import ThirdCalculatorConstructor


class ProcessHandler:
    def __init__(self):
        self.menu_view = MenuView()

    def start(self):
        calculation_manager = CalculationManager()
        first_calculator_controller = FirstCalculator(calculation_manager)
        first_calculator_constructor = FirstCalculatorConstructor(calculation_manager, first_calculator_controller)

        second_calculator_constructor = SecondCalculatorConstructor()

        third_calculator_constructor = ThirdCalculatorConstructor()
        while True:
            self.menu_view.display_menu()
            choice = self.menu_view.get_user_choice()

            if choice == 1:
                first_calculator_constructor.run()

            elif choice == 2:
                second_calculator_constructor.run()

            elif choice == 3:
                third_calculator_constructor.run()

            elif choice == 0:
                self.menu_view.display_goodbye()
                sys.exit()
