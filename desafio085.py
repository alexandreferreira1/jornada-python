# Continuação das Listas - Parte 2
# Ler 7 valores numéricos e cadastrá-los numa lista única. Já organizar número quando for digitado.
# Vai ser uma lista com duas listas dentro, de pares e ímpares. No final mostrar pares e ímpares em ordem crescente

list = [[], []]

for v in range(0,7):
    number = int(input(f'Digite o {v + 1}º número inteiro: '))

    if number % 2 == 0:
        list[0].append(number)
    else:
        list[1].append(number)

print(f'Pares: {sorted(list[0])}')
print(f'Ímpares {sorted(list[1])}')
