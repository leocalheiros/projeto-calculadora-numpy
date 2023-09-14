class MenuView:
    def __init__(self):
        self.calculator_choices = ["Primeira Calculadora", "Segunda Calculadora", "Terceira Calculadora"]

    def display_menu(self):
        print("Bem-vindo ao Sistema de Calculadoras!")
        print("Escolha uma das opções abaixo:")
        for i, choice in enumerate(self.calculator_choices, start=1):
            print(f"{i}. {choice}")
        print("0. Sair")

    def get_user_choice(self):
        try:
            choice = int(input("Escolha a calculadora desejada (0 para sair): "))
            return choice
        except ValueError:
            print("Entrada inválida. Por favor, escolha uma opção válida.")
            return None

    def display_result(self, result_dict):
        print("\nResultado:")
        print(f"Calculadora: {result_dict['calculator']}")
        print(f"Entradas: {result_dict['inputs']}")
        print(f"Status: {result_dict['status']}")
        if 'result' in result_dict:
            print(f"Resultado: {result_dict['result']}")

    def display_goodbye(self):
        print("\nObrigado por usar o Sistema de Calculadoras. Até logo!")
