class SecondCalculatorView:
    def display_menu(self):
        print("\nSegunda Calculadora:")
        print("Digite os valores separados por vírgula (Deixe o espaço em branco pra voltar):")

    def get_user_input(self):
        try:
            input_str = input("Valores: ")
            values = [float(val.strip()) for val in input_str.split(",")]
            return values
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir valores numéricos separados por vírgula.")
            return None
