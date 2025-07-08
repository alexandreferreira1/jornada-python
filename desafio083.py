# Ler uma expressão matemática que o usuário digitar com parenteses. Analisar se os parenteses estão abertos e fechados na ordem correta
from itertools import count

expression = input('Digite a expressão: ')
parentheses = []

for c in expression:
    if c in '()':
        parentheses.append(c)

if parentheses.count('(') == parentheses.count(')'):
    print('Expressão Válida')
else:
    print('Ops!!! Você digitou uma expressão inválida')



