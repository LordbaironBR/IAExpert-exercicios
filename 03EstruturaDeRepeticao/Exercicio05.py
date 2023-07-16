"""

Ler os valores: comprimento, largura e altura e apresentar o valor do volume de uma caixa retangular
Para o calculo da fórmula: VOLUME = COMPRIMENTO + LARGURA * ALTURA.

Ao final do calculo, perguntar ao usuario se deseja continuar o programa fazendo nova leitura.

"""

programa = bool(True)

while programa is True:
    comprimento = float(input('\nDigite o comprimento da caixa: '))
    largura = float(input('Digite a largura da caixa: '))
    altura = float(input('Digite a altura da caixa: '))
    volume = comprimento * largura * altura
    print(f'O volume da caixa é de {volume:.2f}m3\n')
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if continuar == 'S':
        programa = True
    elif continuar == 'N':
        programa = False
    else:
        print('Opção inválida. Tente novamente.')
        programa = False


