num = int(input("Digite um número: "))

f = 1
for i in range(num, 1, -1):
    f = f * i
    print(i)
print("o resultado do fatorial do", num, "é", f)