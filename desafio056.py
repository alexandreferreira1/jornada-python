# Ler nome, idade e sexo de 4 pessoas e mostrar:
# 1- Média de idade do grupo, 2- O nome do homem mais velho, 3- Quantas mulheres tem menos de 20 anos

sumAge = 0
olderManName = 0
olderManAge = 0
womanUnderTwelve = 0

for v in range(1,5):
    print(f'----------{v}ª Pessoa----------')
    name = input(f'Digite o nome da {v}ª pessoa: ')
    age = int(input(f'Idade da {v}ª pessoa: '))
    sex = (input(f'Informe o sexo da {v}ª pessoa (M / F): '))

    # Média das idades
    sumAge += age

    # Nome do homem mais velho
    if sex in 'Mm' and v == 1:
        olderManName = name
        olderManAge = age
    if sex in 'Mm' and age > olderManAge:
        olderManName = name
        olderManAge = age

    # Mulheres Abaixo de 20 anos
    if age < 20 and sex in 'Ff':
        womanUnderTwelve += 1

print()
print('A média de idade do grupo é: {}'.format(sumAge / 4))
print(f'O homem mais velho tem {olderManAge} anos e se chama {olderManName}')
print('Mulheres abaixo de 20 anos: {}'.format(womanUnderTwelve))







# # =============================SOLUÇÃO ARRAYS===========================================
# person = []
# age = []
# sex = []
#
# # Captura de dados
# for v in range(0,4):
#     print()
#     person.append(input(f'Digite o nome da {v + 1}ª pessoa: '))
#     age.append(int(input(f'Digite a idade da {v + 1}ª pessoa: ')))
#
#     sexValue = int(input(f'Informe o sexo da {v + 1}ª pessoa\n1- Masculino.\n2- Feminino\nDigite o número e aperte Enter: '))
#     if sexValue == 1:
#         sexValue = 'masculino'
#     elif sexValue == 2:
#         sexValue = 'feminino'
#     sex.append(sexValue)
#
# print()
# # print(person)
# # print(age)
# # print(sex)
# print()
#
# # Verificação do homem mais velho
# olderMan = None
# menArray = []
# menAgeArray = []
#
# if 'masculino' in sex:
#     for v in range(0, 4):
#         if sex[v] == 'masculino':
#             menArray.append(person[v])
#             menAgeArray.append(age[v])
#
#     for v in range(1, len(menArray)):
#         if age[v] > age[v - 1]:
#             olderMan = v
#     print(f'O homem mais velho é: {menArray[olderMan]}')
# else:
#     print('Nenhum homem foi informado.')
#
#
# # Verificação da média de idade do grupo
# ageSum = 0
# for v in range(0,4):
#     ageSum += age[v]
# averageAge = ageSum / 4
# print(f'A média de idade do grupo é: {averageAge:.1f}')
#
# # Verificação de mulheres abaixo de 20 anos
# womanUnderTwelve = 0
# for v in range(0,4):
#     if age[v] < 20 and sex[v] == 'feminino':
#         womanUnderTwelve += 1
# print(f'Mulheres abaixo de 20 anos: {womanUnderTwelve}')

