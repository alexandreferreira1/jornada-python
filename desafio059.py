# Crie um programa que leia dois valores e mostre o menu na tela:
# [1] Somar, [2] Multiplicar, [3] Maior número, [4] Novos números, [5] Sair

print()

option = 4

print('Olá. Seja bem vindo!')

while option != 5:
    if option == 4:
        print()
        print('Digite dois valores a serem trabalhados')
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))

    print(f'{"Menu de Opções":=^40}')
    option = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior Número\n[4] Novos Números\n[5] Sair\nDigite a sua escolha: '))
    if option not in [1,2,3,4,5]:
        print()
        print('Opção Inválida. Tente Novamente')

    if option == 1:
        print()
        print(f'A soma é: {n1 + n2}')
        print()
    elif option == 2:
        print()
        print(f'A multiplicação é {n1 * n2}')
        print()
    elif option == 3:
        print()
        if n1 > n2:
            print((f'O maior número é {n1}'))
        else:
            print((f'O maior número é {n2}'))
        print()
