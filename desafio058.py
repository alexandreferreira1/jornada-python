# Faça um jogo de adivinhação de número de 0 a 10, mostrando quantas tentativas foram feitas

import random

#Gerar número
computer = random.randint(0, 10)
print('Olá! Eu escolhi um número de 0 a 10')
print('Vamos jogar. Tente Adivinhar')
print()

thatsRight = False
trying = 0

while not thatsRight:
    if trying > 0:
        print('Tente novamente')
    player = int(input('Escolha um número de 0 a 10: '))
    if player == computer:
        thatsRight = True
    elif player < computer:
        print()
        print('Errou. É um número maior.', end=' ')
    elif player > computer:
        print()
        print('Errou. É um número menor.', end=' ')

    trying += 1

print()
print(f'Aeeee! O número a ser adivinhado era {computer}')
print(f'Você acertou depois de {trying} tentativa(s)')


