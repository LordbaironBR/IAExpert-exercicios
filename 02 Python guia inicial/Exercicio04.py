"""
Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3;
passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
– Se a média for maior ou igual 0.0 e menor ou igual 4.0, o aluno está reprovado
– Se a média for maior que 4.0 e menor do que 6.0, o aluno pegou exame
– Se a média for maior ou igual a 6.0, o aluno está aprovado
– Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
Bom trabalho,
"""

loop = bool(True)

while loop:
    m1 = float(input("Nota 1: "))
    m2 = float(input("Nota 2:"))
    m3 = float(input("Nota 3"))
    media = (m1 + m2 + m3) / 3
    if media >= 0 and media <= 4:
        print('Aluno Reprovado')
        loop = False
    elif media > 4 and media < 6:
        print('Aluno de recuperacao')
        loop = False
    elif media > 6 and media <= 10:
        print('Aluno Aprovado')
        loop = False
    else:
        print('Nota invalida')
