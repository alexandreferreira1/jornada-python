# Sortear 5 números e guardar numa tupla. Depois mostrar qual é menor e maior

from random import randint

numbers = (randint(0,100), randint(0,100), randint(0,100), randint(0,100))

# Solução com for
# greater = less = count = 0
#
# for n in numbers:
#     # Maior número
#     if n > greater:
#         greater = n
#     # Menor número
#     if count == 0:
#         less = n
#         count += 1
#     if n < less:
#         less = n

print()
print(f'Os números sorteados foram {numbers}')
print()
print(f'O MAIOR número foi {max(numbers)}')
print(f'O menor número foi {min(numbers)}')