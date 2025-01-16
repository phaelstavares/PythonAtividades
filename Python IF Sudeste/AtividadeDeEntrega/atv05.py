def calculadora():
    print("Bem-vindo à calculadora!")
    print("Escolha uma opção:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    if escolha not in ['1', '2', '3', '4']:
        print("Escolha inválida. Tente novamente.")
        return

    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
        return

    if escolha == '1':
        resultado = num1 + num2
        operacao = "soma"
    elif escolha == '2':
        resultado = num1 - num2
        operacao = "subtração"
    elif escolha == '3':
        resultado = num1 * num2
        operacao = "multiplicação"
    elif escolha == '4':
        if num2 == 0:
            print("Erro: divisão por zero não é permitida.")
            return
        resultado = num1 / num2
        operacao = "divisão"

    print(f"O resultado da {operacao} entre {num1} e {num2} é: {resultado}")

calculadora()