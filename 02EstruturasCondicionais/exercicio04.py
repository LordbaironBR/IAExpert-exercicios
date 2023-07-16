"""
Leia 2 números reais e uma operação, e com isso imprima o resultado de acordo com a operação escolhida pelo usuario:
adição, subtração, multiplicação e divisão. Caso seja informado operação invalida, mostre.
"""
from random import randint


import random

n1 = float(randint(-100, 100))
n2 = float(randint(-100, 100))
operacao = str(input("Digite a operacao:"))

print('Os numeros sortiados para operacao são {} e {} o resultado da operação é: \n'.format(n1, n2))
if operacao == 'soma':
    print(n1 + n2)
elif operacao == 'subtração':
    print(n1 - n2)
elif operacao == 'multiplicação':
    print(n1 * n2)
elif operacao == 'divisão':
    print(n1 / n2)
else:
    print("Operacao invalida")
    