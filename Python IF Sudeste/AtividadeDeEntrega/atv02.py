num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if(num1 > num2 and num1 > num3 and num1 != num2 and num1 != num3):
    print("Condição satisfeita")
else:
    print("Erro")