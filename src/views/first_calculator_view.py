class FirstCalculatorView:
    def display_menu(self):
        print("\nPrimeira Calculadora:")
        print("Digite o valor para o cálculo (0 para voltar):")

    def get_user_input(self):
        try:
            value = float(input("Valor: "))
            return value
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico.")
            return None
