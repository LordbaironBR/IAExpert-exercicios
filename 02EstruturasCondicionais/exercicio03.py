"""

Leia a idade do usuário e classifique-o em:
Criança – 0 a 12 anos
Adolescente – 13 a 17 anos
Adulto – acima de 18 anos (se o usuário digitar um número negativo, mostrar a mensagem que a idade
é inválida)

"""
import random

idade = int(random.randint(0,65))

if idade < 0:
    print('Idade inválida')
elif idade <= 12:
    print(f'{idade} é idade de: Criança')
elif idade <= 17:
    print(f'{idade} é idade de: Adolecente')
elif idade >= 18:
    print(f'{idade} é idade de: Adulto')
