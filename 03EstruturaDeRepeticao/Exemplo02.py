"""
Enquanto o valor for invalido, continue rodando a nota.
"""

nota = float(0)
while nota < 6:
    nota = float(input('Digite a nota: '))
    if nota < 6:
        print(f'A nota {nota} está abaixo do permitido.')
    else:
        print(f'A nota {nota} está acima do permitido.')