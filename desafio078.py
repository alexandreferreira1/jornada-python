# Início das Listas - Parte 1
# Ler 5 valores e colocar em uma lista. Depois mostrar o maior e o menor valor e suas posições na lista.
# Se o número for repetido, mostrar todas as posições dele

numbers = []

for v in range(0,5):
    numbers.append(int(input(f'Digite o valor da posição {v + 1}:  ')))

print()
print(numbers)
print()

nMax = max(numbers)
nMin = min(numbers)

#Maior número
print(f'O MAIOR valor é {nMax} e sua posição na lista é: ', end='')
for i, value in enumerate(numbers):
    if value == nMax:
        print(i + 1, end='.. ')

print()

#Menor número
print(f'O menor é {nMin} e sua posição é: ', end='')
for i, value in enumerate(numbers):
    if value == nMin:
        print(i + 1, end='.. ')

print()



