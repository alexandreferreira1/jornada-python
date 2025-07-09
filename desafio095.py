# Leia nome e gols de jogadores de futebol e mostre uma tabela de quantos gols cada um fez no total.
# Depois pergunte se quer ver dados de um jogador específico e mostre quantos gols ele fez em cada jogo.

tabela = []
jogador = {}

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    gols = []
    for v in range(0, partidas):
        gols.append(int(input(f'Quantos gols fez na partida {v + 1} >>> ')))

    jogador['gols'] = gols
    tabela.append(jogador.copy())

    resposta = input('Deseja continuar? [S / N] >> ')
    print('-' * 60)
    if resposta in 'Nn':
        break

print()
print(tabela)
print()

#Formatação da Tabela
print()
print('=' * 48)
print(f'{"TABELA DE JOGOS":^34}')
print('=' * 48)
print(f'{"Nº":<3}', end='')
print(f'{"JOGADOR":<20}', end='')
print(f'{"GOLS":<20}', end='')
print(f'{"TOTAL":>5}', end='')
print()

c = 1
for jogador in tabela:
    print(f"{c:<3}{jogador['nome']:<20}{str(jogador['gols']):<20}{sum(jogador['gols']):>5}")
    c += 1

print('=' * 48)

#Visualizar levantamento individual
while True:
    continuar = int(input('Mostrar dados de qual Nº de jogador? (999 para sair) >>> '))
    if continuar == 999:
        break
    else:
        print(f"--------- Levantamento do jogador {str(tabela[continuar - 1]['nome']).upper()}")
        for v in range(0,len(tabela[continuar - 1]['gols'])):
            print(f'\033[34mNo jogo {v + 1} fez {tabela[continuar - 1]['gols'][v]} gol(s)\033[m')
    print('=' * 48)