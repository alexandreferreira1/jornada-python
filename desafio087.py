# Fazer uma matriz 3x3 com os números digitado pelo usuário. No final, mostrar a matriz e:
# A- Soma de todos os valores pares digitados, B- Soma dos valores da terceira coluna. C- Maior número da segunda linha

# Solução da Aula
matriz = [[0,0,0], [0,0,0], [0,0,0]]
somaPares = 0
# Gerar Matriz
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

# Imprimir Matriz
print('=' * 25)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end="")

        #Soma todos os valores pares
        if matriz[linha][coluna] % 2 == 0:
         somaPares += matriz[linha][coluna]
    print()

# # Exibição
print('=' * 25)
print(f'A soma de todos os valores pares digitados é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'Maior número da segunda linha: {max(matriz[1])}')







# matrix = []
# numberMatrix = []
# sumEvenNumbers = 0
#
# #Gerar Matriz
# for v in range(0,9):
#     number = int(input(f'Digite o número a ser inserido na posição {v} >>> '))
#     numberMatrix.append(number)
#
#     #Soma dos Pares
#     if number % 2 == 0:
#         sumEvenNumbers += number
#
#     if v in (2,5,8):
#         matrix.append(numberMatrix[:])
#         numberMatrix.clear()
#
# # Renderização da Matriz
# print('=' * 30)
# print(f'[ {matrix[0][0]:^3} ][ {matrix[0][1]:^3} ][ {matrix[0][2]:^3} ]')
# print(f'[ {matrix[1][0]:^3} ][ {matrix[1][1]:^3} ][ {matrix[1][2]:^3} ]')
# print(f'[ {matrix[2][0]:^3} ][ {matrix[2][1]:^3} ][ {matrix[2][2]:^3} ]')
# print('=' * 30)
#
# # Exibição
# print(f'A soma de todos os valores pares digitados é: {sumEvenNumbers}')
# print(f'A soma dos valores da terceira coluna é: {matrix[0][2] + matrix[1][2] + matrix[2][2]}')
# print(f'Maior número da segunda linha: {max(matrix[1])}')