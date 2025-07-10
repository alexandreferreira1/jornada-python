# Continuação das Funções - Parte 2
# Faça função ficha() que leia dois parâmetros opcionais: nome de jogador e quantos gols ele marcou.
# No final printar isso mesmo que não seja passado nenhum dado

def ficha(nome = '<desconhecido>', gols = '0'):
    print(f'O jogador {nome} fez {gols} gols.')


nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite quantos gols marcados: '))

# Convertendo para Número
if gols.isnumeric():
    gols = int(gols)

# Validação dos Dados
if nome == '' and gols == '':
    ficha()
elif nome == '':
    ficha(gols = gols)
elif gols == '':
    ficha(nome = nome)
else:
    ficha(nome, gols)