import random

import numpy as np

quantidade_de_linha = int(input('quantidade_de_linha: '))
quantidade_de_coluna = int(input('quantidade_de_coluna '))
matriz = np.empty([quantidade_de_linha, quantidade_de_coluna])

for linha in range(quantidade_de_linha):
    for coluna in range(quantidade_de_coluna):
        #matriz[linha][coluna] = float(input(f'Digite o valor da linha {linha} e coluna {coluna}: '))
        matriz[linha][coluna] = float(random.randint(-100, 100))

print(f'\nA matriz ficou:\n'
      f'{matriz}')