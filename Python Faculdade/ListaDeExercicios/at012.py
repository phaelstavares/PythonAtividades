letra = str(input("Digite uma letra: "))
if letra in "aeiou":
    print("É uma vogal")
elif letra.isalpha():
    print("É uma consoante")
else:
    print("Inválido")