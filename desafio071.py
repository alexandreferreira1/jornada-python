# Simular um caixa eletrônico, perguntando o valor a ser sacado.
# Depois informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*60)
print('{:^60}'.format('  BEM VINDO AO BANCO 24 HORAS  '))
print('='*60)

print('Cédulas disponíveis: R$50, R$20, R$10 e R$1.')
value = int(input('Informe o valor que deseja sacar: R$'))

fiftyNotes = twentyNotes = tenNotes = oneNotes = 0

while True:
    # Quantidade de cédulas de 50
    if value >= 50:
        fiftyNotes = value // 50
        value = value - (50 * fiftyNotes)
        if value == 0:
            break
    # Quantidade de cédulas de 20
    elif value >= 20:
        twentyNotes = value // 20
        value = value - (20 * twentyNotes)
        if value == 0:
            break
    # Quantidade de cédulas de 10
    elif value >= 10:
        tenNotes = value // 10
        value = value - (10 * tenNotes)
        if value == 0:
            break
    # Quantidade de cédulas de 1
    elif value >= 1:
        oneNotes = value // 1
        value = value - (1 * oneNotes)
        if value == 0:
            break

print()
if fiftyNotes > 0:
    print(f'Cédulas de 50: {fiftyNotes}')
if twentyNotes > 0:
    print(f'Cédulas de 20: {twentyNotes}')
if tenNotes > 0:
    print(f'Cédulas de 10: {tenNotes}')
if oneNotes > 0:
    print(f'Cédulas de  1: {oneNotes}')
print('=' * 60)
print('Pedido Finalizado. Volte sempre ao Banco 24 Horas')

