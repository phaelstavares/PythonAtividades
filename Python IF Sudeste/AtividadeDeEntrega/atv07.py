trabalho_lab = float(input("Digite a nota do Trabalho de Laboratório (0-10): "))
avaliacao_semestral = float(input("Digite a nota da Avaliação Semestral (0-10): "))
exame_final = float(input("Digite a nota do Exame Final (0-10): "))

peso_lab = 2
peso_avaliacao = 3
peso_exame = 5

media_ponderada = (
    (trabalho_lab * peso_lab) +
    (avaliacao_semestral * peso_avaliacao) +
    (exame_final * peso_exame)
) / (peso_lab + peso_avaliacao + peso_exame)

if 8.0 <= media_ponderada <= 10.0:
    conceito = "A"
elif 7.0 <= media_ponderada < 8.0:
    conceito = "B"
elif 6.0 <= media_ponderada < 7.0:
    conceito = "C"
elif 5.0 <= media_ponderada < 6.0:
    conceito = "D"
else:
    conceito = "E"

print(f"\nMédia Ponderada: {media_ponderada:.2f}")
print(f"Conceito Final: {conceito}")