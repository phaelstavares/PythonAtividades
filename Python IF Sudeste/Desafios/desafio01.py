# Caso atenda a condição da da nota 7 e frequência maior ou igual a 70%, então imprima "Aprovado(a)", na tela"

nota = float(input("Digite a nota: "))
frequencia = int(input("Digite a frequência em %: "))

if(nota >= 7 and frequencia >= 70):
    print("Aprovado(a)")