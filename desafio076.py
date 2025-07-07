# Criar tupla única com nomes de produtos e seus respectivos preços. No final mostrar uma listagem tabular.

productsList =  (
    "Arroz", 5.99,
    "Feijão", 4.49,
    "Macarrão", 3.8,
    "Leite", 4.79,
    "Café", 8.50,
    "Óleo", 6.29,
    "Açúcar", 3.10,
    "Farinha", 4.20,
    "Detergente", 2.50,
    "Sabonete", 1.99
    )

print('=' * 44)
print(('{:-^44}').format('    LISTA DE PRODUTOS    '))
print('=' * 44)

for v in range(0, len(productsList), 2):
    print(f'{productsList[v]:.<36}R${productsList[v + 1]:>6}')

