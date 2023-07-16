"""

Lê 2 notas e informe as médias. Se o valor digitado for menor do que 0 (zero) ou maior do que 10 (dez).
O úsuario deve digitar a nota novamente

"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

while  ((nota1 + nota2) / 2) < 0 or  10 < ((nota1 + nota2) / 2):
    print('Valor inválido, tente novamente')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    
print(f'A média é {((nota1 + nota2) / 2)}')