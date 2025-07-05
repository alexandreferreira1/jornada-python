# Faça o computador jogar Jokenpô com você

import random
import sys
import time

# Apenas texto
print('{}=-={}'.format('\033[33m','\033[m') * 19)
print(f"{'\033[0;43m'}{'JOKENPÔ':^57}{'\033[m'}")
print('{}=-={}'.format('\033[33m','\033[m') * 19)

game = ['pedra', 'papel', 'tesoura']

print('Vamos jogar jokenpô!!!')
print('Escolha entre: \n1- Pedra \n2- Papel \n3- Tesoura')

computer = random.choice(game)

userInput = int(input('Digite o número de sua escolha e pressione Enter: '))
user = game[userInput - 1]

if userInput not in (1, 2, 3):
    print()
    print('{}Você digitou uma opção inválida. Tente de novo'.format('\033[31m'))
    sys.exit()

time.sleep(1)
print()
print('=' * 57)
print('JÓ...')
time.sleep(2)
print('KEN...')
time.sleep(2)
print('PÔ')
time.sleep(0.3)
print('=' * 57)
print()
print()
print()

print(f'\033[34mEu escolhi: {computer}\033[m')
print(f'\033[32mVocê escolheu: {user}\033[m')
print()

if computer == user:
    print('Ops!!! Deu empate. Vamos de novo!')
if computer == 'pedra' and user == 'papel':
    print('Você ganhou! Parabéns!')
elif computer == 'pedra' and user == 'tesoura':
    print('Eu ganhei!')
elif computer == 'papel' and user == 'pedra':
    print('Eu ganhei!')
elif computer == 'papel' and user == 'tesoura':
    print('Você ganhou! Parabéns!')
elif computer == 'tesoura' and user == 'pedra':
    print('Você ganhou! Parabéns!')
elif computer == 'tesoura' and user == 'papel':
    print('Eu ganhei!')

print()










