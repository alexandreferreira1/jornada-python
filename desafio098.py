# Criar programa que tenha função contador() e receba inicio, fim e passo, realizando a contagem.
# Faça contagem de 1 a 10 passo 1, 10 a 1 passo 2 e uma personalizada

from time import sleep

print('-=' * 40)
def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
    if inicio > fim:
        for v in range(inicio, fim - 1, passo * -1):
            print(f'{v}', end=' ')
            sleep(0.3)
    else:
        for v in range(inicio, fim + 1, passo):
            print(f'{v}', end=' ')
            sleep(0.3)
    print()
    print('-=' * 40)


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez!')
inicioInput = int(input('Início: '))
fimInput = int(input('Fim: '))
passoInput = int(input('Passo: '))

contador(inicioInput, fimInput, passoInput)