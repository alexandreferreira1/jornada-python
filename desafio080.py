# Ler 5 números e cadastrar na lista já na ordem certa. Sem usar sort(). No final mostrar a lista ordenada
# Ex: Digite o valor // Valor adicionado na posição tal / início / final da lista

numbersList = []

for v in range(0,5):
    #Primeiro loop
    if v == 0:
        numbersList.append(int(input(f'Digite o {v + 1}º número: ')))
        print('Número inserido no final da lista.')
        # print(numbersList)
    #Segundo loop em diante
    elif v > 0:
        numberUser = (int(input(f'Digite o {v + 1}º número: ')))

        # Compara número digitado com os itens da lista
        for i in range(0,len(numbersList)):
            #Compara com cada número da lista
            if numberUser <= numbersList[i]:
                numbersList.insert(i, numberUser)
                print(f'Número inserido{' no início da lista,' if i == 0 else ''} na posição {i}."')
                # print(numbersList)
                break
            #Se o número for maior que todos da lista entra aqui
            elif i + 1 == len(numbersList):
                numbersList.append(numberUser)
                print('Número inserido no final da lista.')
                # print(numbersList)
                break

print()
print(f'Lista completa: {numbersList}')



