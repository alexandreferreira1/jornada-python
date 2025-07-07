# Criar programa que leia o nome e preço de vários produtos, mostrando se deseja continuar.
# No final mostre o 1-total gasto, 2-Quantos produtos custam mais de 1.000, 3-Nome do produto mais barato.

print('='*60)
print('{:^60}'.format('  SUPERMERCADO DO POVO  '))
print('='*60)

sumProduct = productsOverThousand = count = 0

# Inicialização do produto mais barato
cheapestProductName = ''
cheapestProductValue = 0

while True:
    count += 1
    product = str(input('Digite o nome do produto: '))
    value = float(input('Digite o valor R$'))

    #Soma de produtos
    sumProduct += value

    #Produtos acima de mil
    if value > 1000:
        productsOverThousand += 1

    #Produto mais barato. Na primeira vez já armazena o primeiro produto
    if count == 1 or value < cheapestProductValue:
        cheapestProductName = product
        cheapestProductValue = value

    confirm = input('Deseja adicionar mais um produto? [S / N] ')
    if confirm in 'Nn':
        break

print()
print(f'Total gasto: R${sumProduct:.2f}')
print(f'Quantidade de produtos custando mais de R$1.000: {productsOverThousand} ')
print(f'O produto mais barato foi {cheapestProductName}')