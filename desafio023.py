# Ler numero entre 0 e 9999 e mostrar dígitos separados. Ex.: 1834. Tem 4 unidades, 3 dezenas, 8 centenas e 1 milhar

num = int(input('Número de 0 a 9999: '))

unid = num // 1 % 10
dezen = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10

print(f'Unidade: {unid}')
print(f'Dezena: {dezen}')
print(f'Centena: {cent}')
print(f'Milhar: {mil}')
