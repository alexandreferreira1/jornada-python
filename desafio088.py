# Faça um programa que crie palpites para Mega Sena. Perguntar no início quantos conjuntos de palpites serão gerados.
# Cada conjunto vai ter 6 número sorteados de 1 a 60 sem repetir. Cada conjunto vai estar dentro de uma lista composta

from random import randint
from time import sleep

list = []
guess = []

print('=' * 40)
print(f'{"Jogo da MEGA SENA":^40}')
print('=' * 40)

numberGuesses = int(input('Quantos palpites deseja gerar? '))

c = 0
while c < numberGuesses:
    for v in range(0,6):
        number = randint(1,60)
        if number in guess:
            number = randint(1, 60)
        if number not in guess:
            guess.append(number)
    #Ordena os números
    guess.sort()
    #Coloca números sorteados na lista
    list.append(guess[:])
    # Reseta palpites
    guess.clear()

    c += 1

print('{:-^40}'.format('Sorteando Jogos'))

for i, guessGame in enumerate(list):
    sleep(0.6)
    print(f'Jogo {i + 1}: {guessGame}')

print()
print(f'\033[34m{"Boa sorte!":^40}')