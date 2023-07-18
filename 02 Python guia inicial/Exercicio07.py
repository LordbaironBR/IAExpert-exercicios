"""
Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista.
Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados
"""
import random

"""
lista1 = []
for i in range(5):
    lista1.append(random.randint(-10, 10))
print(sum(lista1))
"""

lista2 = []
soma = 0
for i in range(5):
    lista2.append(random.randint(-10, 10))
    soma += lista2[i]
print(soma)

