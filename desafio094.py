# Leia nome, sexo e idade de várias pessoas, colocando cada pessoa em um dicionário e todos eles em uma lista.
# No final mostre: A-Total de cadastros, B-Média de idade do grupo, C-Pessoas com idade acima da média, D-Listar mulheres.

dados = []
mulheres = []
somaIdades = 0

while True:
    nome = str(input('Digite o nome: '))
    sexo = str(input('Digite o sexo: [M / F] >> '))
    idade = int(input('Digite a idade: '))

    dados.append({
        'nome': nome,
        'sexo': sexo,
        'idade': idade
    })

    resposta = input('Deseja continuar? [S / N] >> ')
    print('-' * 60)
    if resposta in 'Nn':
        break

# Buscar e Filtrar Dados
for v in range(0,len(dados)):
    # Apenas somar idades
    somaIdades += dados[v]['idade']

    # Listar mulheres
    if dados[v]['sexo'] in 'Ff':
        mulheres.append(dados[v]['nome'])

print(f'Total de Usuários Cadastrados: {len(dados)}')
print(f'Média de idade do grupo: {somaIdades / len(dados)}')
print(f'Lista de mulheres: {mulheres}')
print(f'Pessoas com idade acima da média:')
for v in range(0,len(dados)):
    if dados[v]['idade'] > somaIdades / len(dados):
        print(f'--{dados[v]['nome']} de {dados[v]['idade']} anos')

