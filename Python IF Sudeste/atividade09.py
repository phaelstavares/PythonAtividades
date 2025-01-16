numero = int(input("Digite um número pela semana (1 a 7): "))

if(numero == 1):
    print(f"{numero} é Domingo")
elif(numero == 2):
    print(f"{numero} é Segunda-feira")
elif(numero == 3):
    print(f"{numero} é Terça-feira")
elif(numero == 4):
    print(f"{numero} é Quarta-feira")
elif(numero == 5):
    print(f"{numero} é Quinta-feira")
elif(numero == 6):
    print(f"{numero} é Sexta-feira")
elif(numero == 7):
    print(f"{numero} é Sábado")
else:
    print("Número inválido")