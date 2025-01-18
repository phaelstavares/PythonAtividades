numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    n = int(input("Digite o valor do número: "))
    if n == 5:
        print("Número 5 encontrado, pode parar o loop")
        break
    print("Número não é 5.")

print("Loop encerrado.")