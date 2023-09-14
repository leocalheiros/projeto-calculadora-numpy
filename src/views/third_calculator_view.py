class ThirdCalculatorView:
    def display_menu(self):
        print("\nTerceira Calculadora:")
        print("Digite os valores separados por vírgula (0 para voltar):")

    def get_user_input(self):
        try:
            values = input("Valores: ")
            values = [float(val.strip()) for val in values.split(",")]
            return values
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir valores numéricos separados por vírgula.")
            return None
