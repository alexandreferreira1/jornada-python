# Ler três números e mostrar qual é o menor e o maior

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O menor número digitado é: {menor}')

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'E o maior número é: {maior}')