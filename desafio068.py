# Faça um jogo de par ou ímpar. Termina quando usuário perder e mostra quantas vitórias

from random import randint

print('='*60)
print('{:-^60}'.format('  PAR OU ÍMPAR  '))
print('='*60)

print('Vamos jogar!')
victories = 0

while True:
    # Validação de Input
    playerChoice = ' '
    playerNumber = 0
    while playerChoice not in 'PpIi':
        # [0] pega apenas a primeira letra
        playerChoice = str(input('Você escolhe: par ou impar? [P / I] '))[0]
    while playerNumber not in [1, 2, 3, 4, 5]:
        playerNumber = int(input('Agora escolha um número de 1 a 5: '))

    # Conversão da escolha do player para exibir no resultado
    playerChoice = 'PAR' if playerChoice in 'Pp' else 'IMPAR'

    # Sorteio de Número do CPU
    computerNumber = randint(1, 5)

    # Definindo se é par ou impar
    evenOdd = ''
    if (playerNumber + computerNumber) % 2 == 0:
        evenOdd = 'PAR'
    elif (playerNumber + computerNumber) % 2 == 1:
        evenOdd = 'IMPAR'

    # Resultado
    print()
    print(f'Você escolheu {playerChoice} e o número {playerNumber}. Eu escolhi o número {computerNumber}')
    print(f'Juntando os dois fica {playerNumber + computerNumber} que é {evenOdd}')
    print()

    if evenOdd == playerChoice:
        print('\033[34mVocê venceu!\033[m')
        print('Vamos de novo!')
        print()
        victories += 1
    elif evenOdd != playerChoice:
        break

print('\033[31mEu venci!\033[m')
print()
print(f'Fim de Jogo. Quantidade de vitórias que você teve: {victories}')

