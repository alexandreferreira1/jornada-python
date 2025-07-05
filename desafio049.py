# Tabuada de um número escolhido pelo usuário

n = int(input('Digite o número da tabuada que deseja estudar agora: '))

for v in range(0,11):
    print(f'{n} x {v:^2} = {n * v}')