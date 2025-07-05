# Ler um ano qualquer e mostrar se é bissexto

num = int(input('Digite o ano: '))

doisUltimos = num // 1 % 100

if doisUltimos != 00 and num % 4 == 0 or doisUltimos == 0 and num % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')