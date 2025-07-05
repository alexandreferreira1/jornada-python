# Ler preço de um produto e mostrar novo preço com 5% de desconto

print('-------------------DESCONTO NO SEU PRODUTO----------------------')
print('Será que ta valendo a pena comprar? Vamos descobrir!')
valor = float(input('Qual o valor do produto que você quer comprar? '))
desconto = valor * 5 / 100
precoFinal = valor - desconto

print('{}'.format('='*50))
print('Um momento...')
print('{}'.format('='*50))

print(f'Você pagará R${precoFinal:.2f}, aplicando 5% de desconto')
