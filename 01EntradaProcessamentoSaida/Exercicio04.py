'''
Leia as informações de um consórcio, tal como o número total de prestações,
a quantidade total de prestações pagas e o valor de cada prestação.
Calcule e mostre na tela o total pago pelo consorciado e o saldo devedor.
'''

numero_prestacoes_total = int(input('Numero de prestacoes: '))
numero_prestacoes_pagas = int(input('Numero de pagas: '))
valor_prestacoes_unico = float(input('Valor de cada prestacoes: '))
pagamento_total = numero_prestacoes_pagas * valor_prestacoes_unico
saldo_devedor = (numero_prestacoes_total * valor_prestacoes_unico) - (pagamento_total)
print(f'A prestacao possui um total de {numero_prestacoes_total} parcelas.\n'
      f'O valor unitario de cada parcela e: R${valor_prestacoes_unico}\n'
      f'O senhor ja realizou o pagamento de {numero_prestacoes_pagas} parcelas. Totalizando R${pagamento_total}.\n'
      f'Para concluir o pagamento total do consorcio, falta um total de R${saldo_devedor}')


