# Continuação das Estruturas de Repetição - while com break
# Faça um programa que leia vários números inteiro e só pare quando digitar 999. Mostre quantidade de números e soma deles

print('Vamos somar! Obs.: 999 para a execução! ')

count = sum = 0

while True:
    n = int(input('Digite um número >>>>>>  '))
    if n == 999:
        break
    count += 1
    sum += n

print(f'A soma dos {count} números foi {sum}.')