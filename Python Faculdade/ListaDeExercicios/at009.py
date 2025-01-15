num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é {}".format(num1))
elif num2 > num1:
    print("O maior número é {}".format(num2))
else:
    print("Os dois números são iguais")
