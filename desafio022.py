# Leia o nome completo e mostre nome em maiúsculas, minúsculas, contar quantidade de letras total e do primeiro nome.

nome = input('Digite seu nome completo: ').strip()

print(f'Maiúsculas: {nome.upper()}')
print(f'Minúsculas: {nome.lower()}')
# Pega o lenght no nome e subtrai a contagem de espaços
print(f'Quantidade de letras: {len(nome) - nome.count(' ')}')
# Encontra a posição do primeiro espaço, que coincide com a quantidade. Também da pra fazer com split e len
print(f'Letras do Primeiro Nome: {nome.find(' ')}')