"""

Ler os valores de comprimento, largura e altura e apresentar o valor do volume de uma caixa retangular.
Utilize para o cálculo a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA

"""

comprimento = float(input('Comprimento: '))
largura = float(input('Largura: '))
altura = float(input('Altura: '))
volume = comprimento * largura * altura

print(f'\n Uma caixa possui as seguintes medidas:\n'
      f'Comprimento: {comprimento}m\n'
      f' Largura: {largura}m\n'
      f'Altura: {altura}m\n\n'
      f'Seu volume é igual á: {volume}m³')