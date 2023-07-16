"""

Leia um numero e se ele estiver entre 1 e 9 o valor é invalido, for menor que 1 e maior que 9 está dentro da margem aceita.

"""

import random

n = int(random.randint(-25, 25))

if n < 1 or n > 9:
    print(f'{n} é Valor Valido')
else:
    print(f'{n} é Valor invalido')
        