# Início das Tuplas
# Preencha uma tupla de 0 a 20 e o usuário vai escolher um número e irá mostrar ele por extenso.

numbers = (
            "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
            "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
            )

while True:
    userChoice = int(input('Escolha um número de 0 a 20: '))
    if 0 <= userChoice <= 20:
        print('Você escolheu o número \033[34m{}\033[m'.format(numbers[userChoice]))
        print()
        resposta = input('Deseja continuar? [S / N] ')

    if resposta in 'Nn':
        break





