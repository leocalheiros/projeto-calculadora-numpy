import sys
from src.views.menu_view import MenuView


class ProcessHandler:
    def __init__(self):
        self.menu_view = MenuView()

    def start(self):
        while True:
            self.menu_view.display_menu()
            choice = self.menu_view.get_user_choice()

            if choice == 0:
                self.menu_view.display_goodbye()
                sys.exit()
