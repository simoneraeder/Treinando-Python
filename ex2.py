# Classe Calculadora com tratamento de exceções
class Calculadora:
    def adicao(self, x, y):
        try:
            return x + y
        except TypeError:
            return "Erro: Tipos de dados inválidos para adição."

    def subtracao(self, x, y):
        try:
            return x - y
        except TypeError:
            return "Erro: Tipos de dados inválidos para subtração."

    def multiplicacao(self, x, y):
        try:
            return x * y
        except TypeError:
            return "Erro: Tipos de dados inválidos para multiplicação."

    def divisao(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Erro: Divisão por zero."
        except TypeError:
            return "Erro: Tipos de dados inválidos para divisão."

# Testando as implementações
calculadora = Calculadora()

print(calculadora.adicao(5, 3))       # Saída: 8
print(calculadora.subtracao(5, 3))    # Saída: 2
print(calculadora.multiplicacao(5, 3))# Saída: 15
print(calculadora.divisao(5, 0))      # Saída: Erro: Divisão por zero.
print(calculadora.divisao(5, 'a'))    # Saída: Erro: Tipos de dados inválidos para divisão.
