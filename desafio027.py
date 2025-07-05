# Ler nome completo e mostrar primeiro e último nome separadamente

nome = input('Nome completo: ').strip()
nomeSeparado = nome.split()

print(f'Primeiro nome: {nomeSeparado[0]}')
print(f'Último nome: {nomeSeparado[-1]}')

# Também pode ser feito assim:
print(f'Último nome: {nomeSeparado[len(nome)-1]}')
