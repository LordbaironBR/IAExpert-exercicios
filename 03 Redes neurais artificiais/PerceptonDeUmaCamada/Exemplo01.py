# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

#Função da somatória
def formulaSomatoria(entradas, pesos):
    s = 0
    for i in range(len(entradas)):
        s += entradas[i] * pesos[i]
    return s

#função do StepFunction
def formulaStepFunction(somatoria):
    if somatoria >= 1:
        return 1
    return 0
    
    
somatoria = formulaSomatoria(entradas, pesos)
stepFunction = formulaStepFunction(somatoria)

if stepFunction >= 1:
    print(f'A somatoria das entradas é: {somatoria}\n e o StepFuntion é {stepFunction}.\n NEURÔNIO ATIVADO')
else:
    print(f'A somatoria das entradas é: {somatoria}\n e o StepFuntion é {stepFunction}.\n NEURÔNIO NÃO FOI ATIVADO')

 



