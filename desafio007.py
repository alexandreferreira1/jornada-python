# Ler duas notas de um aluno e calcular a sua média

print('Olá professor. Seja bem vindo!')
n1 = float(input('Digite a primeira nota do seu aluno: '))
n2 = float(input('Muito bem! Agora digite a segunda nota dele: '))
print('{}'.format('='*30))
print('Um momento...')
print('{}'.format('='*30))
print('A média do seu aluno é: {:.1f}'.format((n1 + n2) / 2))