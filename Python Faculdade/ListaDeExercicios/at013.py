num = int(input("Digite um número para o fatorial: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
    print("{}! = {}".format(num, fatorial))