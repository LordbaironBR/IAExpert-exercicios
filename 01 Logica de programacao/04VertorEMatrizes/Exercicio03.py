'''
Leia duas matrizes A e B com as dimensões 3x3. Crie uma nova matriz C de
mesma dimensão que seja a soma de A + B. No final, imprimir a matriz C
'''

import numpy
import random

quantidade_vetor_a = int(input('quantidade_vetor_a: '))
vetor_a = numpy.empty((quantidade_vetor_a))
quantidade_vetor_b = quantidade_vetor_a
vetor_b = numpy.empty((quantidade_vetor_b))

for i in range(quantidade_vetor_a):
    vetor_a[i] = random.randint(0, 9)
    vetor_b[i] = vetor_a[i]**3

print(f'Vetor A:\n'
      f'{vetor_a}\n\n'
      f'Vetor B:\n'
      f'{vetor_b}')

