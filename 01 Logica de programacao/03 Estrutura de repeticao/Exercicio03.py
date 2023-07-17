"""
Escreva um algoritomo que lê 5 valores para a variavel A, um cada vez, e, e conta quantos destes valores são negativos. Após 
"""

import random

a = []
valores_positivos = []
valores_negativos = []
valor = int(input('Digite quantos valores irá conter na lista: '))

for i in range(valor):
    a.append(random.randint(-10, 10))

    if a[i] <0:
        valores_negativos.append(a[i])
    else:
        valores_positivos.append(a[i])

print(f'Os valores da lista são:\n'
      f'{a}\n\n'
      f'A lista possui {len(valores_positivos)} valores positivos:\n'
      f'{valores_positivos}\n\n'
      f'A lista possui {len(valores_negativos)} valores negativos:\n'
      f'{valores_negativos}')
