# Início dos Dicionários
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde os resultados num dicionário.
# No final coloque em ordem sabendo que o primeiro lugar fica para o dado de maior número.

from random import randint

jogadas = {
            "jogador1": randint(1,6),
            "jogador2": randint(1,6),
            "jogador3": randint(1,6),
            "jogador4": randint(1,6),
          }

classicacao = sorted(jogadas.items(), key=lambda item: item[1], reverse=True)
print('=' * 60)
print('Jogadas Realizadas')
print(jogadas)
print('=' * 60)
print('Ranking dos Jogadores:')
c = 1
for jogador in classicacao:

    print(f'{c}º Lugar >> {jogador[0]} com dado {jogador[1]}')
    c += 1
