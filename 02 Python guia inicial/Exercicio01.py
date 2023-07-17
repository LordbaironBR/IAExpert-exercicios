#Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

n1 = int(input('Numero 1:'))
n2 = int(input('Numero 2:'))
operacao = str(input(f'Qual operacao deseja realizas?\n'
                     f'Adicao; Subtracao; Multicacao e divisao:'))

if operacao == 'Soma':
    print(f'Soma de {n1} e {n2} resulta em: {n1+n2}')
elif operacao == 'Subtracao':
    print(f'Subtracao de {n1} e {n2} resulta em: {n1-n2}')
elif operacao == 'Multiplicacao':
    print(f'Multiplicacao entre {n1} e {n2} resulta em: {n1*n2}')
elif operacao == 'Divisao':
    print(f'Divisao de {n1} e {n2} resulta em {n1/n2}')

