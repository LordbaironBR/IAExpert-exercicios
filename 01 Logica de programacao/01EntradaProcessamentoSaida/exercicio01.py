"""
 Ler uma temperatura em graus Celsius e apresentá-la  convertida em graus Fahrenheit.
  A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius

"""
c = float(input('Digite a temperatura em graus celsius: '))
formulaf = (9*c+160)/5

print(f'temperatura {c}cº -> {formulaf}fº')