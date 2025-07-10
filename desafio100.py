# Faça um programa que tenha uma lista chamada números. Faça duas funções chamadas sorteia() e somaPar().
# A primeira vai sortear 5 números e vai colocá-los dentro da lista. A segunda vai mostrar a soma entre os valores pares sorteados.

from random import randint

numeros = []

def somaPar(valores):
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    print(f'A soma entre os números pares gerados foi {soma}')

def sorteia():
    for v in range(0,5):
        numeros.append(randint(1,20))

    print()
    print(numeros)


sorteia()
somaPar(numeros)


