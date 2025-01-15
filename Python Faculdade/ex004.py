nota = float(input("Digite a nota: "))
if nota == 7:
    print("No limite!")
elif nota > 7:
    print("Aprovado")
else: 
    if nota >= 5 and nota < 7:
        print("Exame especial")
    else:
        print("Reprovado")