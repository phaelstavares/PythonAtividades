base = float(input("Informe a base do retângulo: "))
altura = float(input("Informe a altura do retângulo: "))
op = int(input("Informe a operação (0 para perímetro, 1 para área): "))

if op == 0:
    perimetro = 2 * (base + altura)
    print(f"O perímetro do retângulo é: {perimetro}")
elif op == 1:
    area = base * altura
    print(f"A área do retângulo é: {area}")
else:
    print("Opção inválida.")