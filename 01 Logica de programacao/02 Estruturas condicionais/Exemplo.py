m1 = float(input('Digite a nota m1: '))
m2 = float(input('Digite a nota M2: '))
m3 = float(input('Digite a nota M3: '))

media = (m1+m2+m3)/3

if media >= 6:
    print('Aluno aprovado')
elif media < 4:
    print('Aluno reprovado')
elif media >= 4 and media < 6:
    print(f'Aluno de recuperação \n'
          f'Resultado do exame de recuperação: ')
    exame = float(input())
    if exame >= 6:
        print('Aluno aprovado na recuperação')
    else:
        print('Aluno reprovado na recuperação')
