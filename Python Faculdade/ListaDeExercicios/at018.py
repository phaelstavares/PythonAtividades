def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não permitida."
    return a / b

def calculadora():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    
    operacao = input("Escolha a operação (+, -, *, /): ")
    
    if operacao == '+':
        resultado = adicionar(a, b)
    elif operacao == '-':
        resultado = subtrair(a, b)
    elif operacao == '*':
        resultado = multiplicar(a, b)
    elif operacao == '/':
        resultado = dividir(a, b)
    else:
        print("Operação inválida.")
        return

    print(f"O resultado da operação {operacao} é: {resultado}")

calculadora()