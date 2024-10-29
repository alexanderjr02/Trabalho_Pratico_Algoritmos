# Trabalho Prático: Calculadora Refatorada

# Função de adição
def adicao(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função principal da calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        return adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        return subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        return multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        return divisao(num1, num2)
    else:
        return "Operação inválida"

# Variável de controle para saída
saida = ''

# Laço principal para execução da calculadora
while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, / ou o nome da operação): ")
        
        # Calculando o resultado
        resultado = calculadora(num1, num2, operacao)
        print("Resultado da operação:", resultado)
        
        # Verificando se o usuário deseja continuar
        saida = input("Deseja continuar? (S/N): ")
    except ValueError:
        print("Por favor, insira números válidos.")
