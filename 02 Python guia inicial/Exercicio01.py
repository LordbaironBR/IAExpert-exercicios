#Ler 5 notas e informar a média

soma_das_notas = 0
quantidade_de_notas = int(input('quantidade_de_notas: '))
for i in range(quantidade_de_notas):
    nota = float(input('nota: '))
    soma_das_notas += nota
print(f'A média das notas é igual á:\n {soma_das_notas / quantidade_de_notas}')
    