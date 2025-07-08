# Ler 5 números e cadastrar na lista já na ordem certa. Sem usar sort(). No final mostrar a lista ordenada
# Ex: Digite o valor // Valor adicionado na posição tal / início / final da lista

numbersList = []

for v in range(0,5):
    number = int(input(f'Digite o {v + 1}º número: '))

    if v == 0 or number > numbersList[-1]:
        numbersList.append(number)
        print('Número inserido no final da lista.')
        print(numbersList)
    else:
        # Compara número digitado com os itens da lista
        for i in range(0,len(numbersList)):
            #Compara com cada número da lista
            if number <= numbersList[i]:
                numbersList.insert(i, number)
                print(f'Número inserido{' no início da lista,' if i == 0 else ''} na posição {i}."')
                print(numbersList)
                break

print()
print(f'Lista completa: {numbersList}')



