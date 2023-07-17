#Leia um número inteiro e informe se ele é positivo ou negativo (considere zero como positivo)
import random

n = int(random.randint(-100,100))

if n < 0 or n > 0:
    if n < 0:
        print(f'O número {n} é negativo')
    elif n > 0:
        print(f'O número {n} é positivo')
else:
    print(f'O numero {n} é neutro')