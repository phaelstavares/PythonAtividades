# Caso a nota informada seja menor que 7, mas simultaneamente maior ou igual a 4, então imprimir "Tem direito a exame de recuperação!"

nota = float(input("Digite a nota: "))

if(nota < 7 and nota >= 4):
    print("Tem direito a exame de recuperação!")