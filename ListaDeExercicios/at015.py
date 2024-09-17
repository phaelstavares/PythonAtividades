def multiplicar(vetor):
    resultado = 1
    for num in vetor:
        resultado *= num
    return resultado

vetor = []
for i in range(5):
    numero = int(input(f"Digite o número {i+1}: "))
    vetor.append(numero)

soma = sum(vetor)
multiplicacao = multiplicar(vetor)

print("\nNúmeros digitados:", vetor)
print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)