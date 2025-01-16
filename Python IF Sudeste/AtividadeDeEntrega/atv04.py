num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if(num1 == num2):
    resultado = num1 * num2
    print(f"A multiplicação entre os dois números é: {resultado}")
elif(num1 > num2):
    resultado = num1 - num2
    print(f"A subtração do primeiro pelo segundo é: {resultado}")
else:
    resultado = num1 + num2
    print(f"A soma entre os dois números é: {resultado}")