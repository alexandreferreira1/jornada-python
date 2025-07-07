# Ler 4 valores e guardar na tupla. Depois mostrar:
# A- Quantas vezes apareceu o número 9, B- Em que posição foi digitado o primeiro valor 3, C- Quais foram os números pares

numbers = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
           int(input('Digite o terceirovalor: ')), int(input('Digite o quarto valor: ')))

#A-Quantas vezes apareceu o número 9
if numbers.count(9) == 0:
    print('O número 9 não apareceu nenhuma vez')
elif numbers.count(9) == 1:
    print('O número 9 apareceu uma vez')
elif numbers.count(9) > 2:
    print(f'O número 9 apareceu {numbers.count(9)} vezes.')

#B-Em que posição foi digitado o primeiro valor 3
if 3 in numbers:
    if numbers.index(3) == 0:
        print(f'O primeiro número 3 está na posição {numbers.index(3) + 1}.')
    else:
        print(f'O primeiro número 3 está na {numbers.index(3) + 1}ª posição.')
else:
    print('Não foi digitado nenhum número 3')

#C-Quais foram os números pares
print('Os números pares foram: ', end='')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')
