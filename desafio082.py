# Ler vários números e colocar numa lista. Depois criar uma lista extra para valores pares e outra para ímpares.
# Faça com um loop que apenas lê os dados primeiro. No final exibir as 3 listas.

numbers = evenNumbers = oddNumbers = []

while True:
    numbers.append(int(input(f'Digite um número: ')))
    print('Número adicionado')

    while True:
        response = input('Deseja continuar? [S / N] ')
        if response not in 'SsNn':
            print('Opção Inválida. Tente novamente!')
        else:
            break

    if response in 'Nn':
        break

print()
print(f'Números digitados: {numbers}')
print()

for n in numbers:
    if n % 2 == 0:
        evenNumbers.append(n)
    else:
        oddNumbers.append(n)

print(f'Números pares filtrados: {evenNumbers}')
print(f'Números ímpares filtrados: {oddNumbers}')