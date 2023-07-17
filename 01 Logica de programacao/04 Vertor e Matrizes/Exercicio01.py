"""

Leia um vetor A de 10 elementos inteiros e um valor individual X.
A seguir, imprimir os indices do vetor A em que aparece um valor igual a X

"""
import random
import numpy

quantidade_de_variavel = int(input('Quantas variaveis térá no vetor: '))
vetor = numpy.empty(quantidade_de_variavel)
valor = int(input('Digie o valor a ser procurado dentro do vetor: '))
valor_achado = int(0)

for a in range(quantidade_de_variavel):
    vetor[a] = random.randint(0, 5)
for b in range(quantidade_de_variavel):
    if vetor[b] == valor:
        print(f'{vetor[b]} Valor encontrado')
        valor_achado += 1
    else:
        print(f'{vetor[b]} Valor não encontrado')
print(f'O valor {valor} Foi encontrado {valor_achado} vezes.')