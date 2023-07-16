notas = []
contador = 1
qtdnotas = int(input('Quantas notas irá comparar? '))

while contador <= qtdnotas:
    notas.append(float(input(f'Digite a nota nº {contador} ')))
    contador += 1

print(f'\nAs notas são:\n'
      f'{notas}\n\n'
      f'e a média das notas é:\n'
      f'{sum(notas) / len(notas)}')