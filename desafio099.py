# Faça uma função chamada maior e receba vários parâmetros com números inteiros. No final mostrar o maior número.

def maior(*num):
    print(f'O maior número passado como argumento é {max(num)}')


maior(7, 5, 9, 8, 15, 1, 5)