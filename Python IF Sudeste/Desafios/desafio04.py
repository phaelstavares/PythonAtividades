num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if(num1 > num2):
    print(f"O maior é o {num1}")
elif(num2 > num1):
    print(f"O maior é o {num2}")
else:
    print("Os dois são iguais.")