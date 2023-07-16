"""

Leia dois números inteiros e informe qual deles é o maior. Se os números forem iguais,
mostrar esta informação na tela

"""
import random

n1 = int(random.randint(-10, 10))
n2 = int(random.randint(-10, 10))

print(f'Os numeros sorteados são {n1} e {n2}')
if n1 != n2:
    if n1 > n2:
        print(f'O numero {n1} é maior')
    elif n2 > n1:
        print(f'O numero {n2} é maior')
else:
    print(f'Os numeros são iguais')

