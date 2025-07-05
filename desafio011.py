# Ler largura e altura de uma parede em metros e calular tinta necessária. Cada litro de tinta pinta 2m²

print('-------------------CALCULO PARA PINTURA----------------------')
n1 = float(input('Qual a Altura da parede a ser pintada? '))
n2 = float(input('E a Largura? '))

area = n1 * n2

print('{}'.format('='*50))

print('Um momento...')

print('{}'.format('='*50))

print(f'A sua parede tem {area}m². Você precisará de {area / 2} litros de tinta.')
