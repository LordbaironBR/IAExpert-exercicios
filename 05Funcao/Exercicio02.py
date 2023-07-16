"""

Ler uma temperatura em graus Celsius e apresentá-la  convertida em graus Fahrenheit. A fórmula de conversão é:
F = (9 * C + 160) / 5
Na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius• Função para ler os valores
• Função para fazer o cálculo
• Função para mostrar o resultado

"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    print(f'Fahrenheit: {fahrenheit}')

def fahrenheit_to_celsius(fahrenheit):
    celsius = 5/9 * (fahrenheit - 32)
    print(f'Celsius: {celsius}')

escolha = int(input(f'Qual gostaria de descobrir?\n'
                f'Fahrenheit (1)\n'
                f'Celsius (2)\n'))

if escolha == 1:
    fahrenheit = float(input('fahrenheit: '))
    fahrenheit_to_celsius(fahrenheit)
else:
    celsius = float(input('celsius: '))
    celsius_to_fahrenheit(celsius)
