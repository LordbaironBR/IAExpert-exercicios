"""
Ler 5 notas e informar a média
"""
quantidade_notas = int(input('quantidade_notas: '))
soma = float(0)
for i in range(quantidade_notas):
    nota = int(input(f'Digite a nota {i+1}: '))
    soma += nota
print(f'A media das notas:\n'
      f'{soma / i}')

