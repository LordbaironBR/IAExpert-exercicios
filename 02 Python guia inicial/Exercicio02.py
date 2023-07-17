"""
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem.
Utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
Desta forma, será possível obter a distância percorrida com a fórmula:
DISTANCIA = TEMPO * VELOCIDADE.
Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a
fórmula: LITROS_USADOS = DISTANCIA / 12.
O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
"""

consumo_km = float(input("Consumo por KM: "))
tempo_viagem = float(input('tempo de viagem: '))
velocidade_media = float(input('velocidade media: '))
distancia_percorrida = tempo_viagem * velocidade_media
consumo_total = distancia_percorrida / consumo_km

print(f'O carro percorreu um total de {distancia_percorrida}KM\n'
      f'Gastandob um total de {consumo_total}l de combustivel.')





