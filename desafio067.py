# Mostre a tabuada do número escolhido e pare apenas quando o usuário quiser ou se o número for negativo

while True:
    n = int(input('Digite o número da tabuada que deseja estudar agora: '))
    if n < 0:
        break

    # Renderiza tabuada
    for v in range(0,11):
        print(f'{n} x {v:^2} = {n * v}')

    print()
    resposta = input('Deseja continuar? [S / N] ')
    print()
    if resposta in 'Nn':
        break
