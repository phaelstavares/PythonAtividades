nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if(idade >= 18):
    print(f"{nome} tem {idade} anos e está apto para tirar carteira.")
else:
    print(f"{nome} não está apto para tirar carteira.")