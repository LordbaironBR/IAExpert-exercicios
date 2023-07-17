"""

Crie uma função que imprima a palavra PROGRAMAÇÃO 10 vezes

"""

#Forma simples
"""
def programacao(palavra):
    print(palavra)

for i in range(10):
    programacao("PROGRAMAÇÃO")
"""

#Forma mais complexa
def programacao(quantidade_de_vezes, palavra):
    for i in range(quantidade_de_vezes):
        print(palavra)

programacao(10, 'PROGRAMAÇÃO')