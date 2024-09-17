num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
if num1 > num2:
    print("{} é maior que {} e a soma de ambos é {}".format(num1, num2, soma))
elif num1 < num2:
    print("{} é maior que {} e a soma de ambos é {}".format(num2, num1, soma))