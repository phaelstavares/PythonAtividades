salario = int(input("Seu salário: "))
porcentagem = float(input("A porcentagem: "))

ajuste = (salario * (porcentagem / 100)) + salario

print(f"O novo salário com o ajuste de 25% é: \n {ajuste}")