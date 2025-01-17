contador = 0
while True:
    num = int(input("Insira um número: "))
    if(num == 0):
        break
    if(num > 0):
        contador += 1
print("Quantidade de valores positivos:", contador)