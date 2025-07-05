# Início das Estruturas de Repetição - for
# Faça uma contagem regressiva de 10 segundo para o estouro de fogos. Utilizar emoji

import emoji
import time

# Apenas texto
print('{}=-={}'.format('\033[32m','\033[m') * 33)
print(f"{'\033[0;42m'}{'PREPARE-SE PARA A GRANDE QUEIMA DE FOGOS!!!':^99}{'\033[m'}")
print('{}=-={}'.format('\033[32m','\033[m') * 33)

time.sleep(1.5)

print()

#Contagem Regressiva
for v in range(10,0,-1):
    print(f'{v}...', end='      ')
    time.sleep(1)

#Limpar console pulando 50 linhas
print("\n" * 50)

#Print dos Fogos
print(emoji.emojize(':fireworks:' * 45, language='alias'))
print('{}=-={}'.format('\033[35m','\033[m') * 33)
print('{}=-={}'.format('\033[45m','\033[m') * 33)
print("\n" * 2)
time.sleep(2)

print(emoji.emojize(':fireworks:' * 45, language='alias'))
print('{}=-={}'.format('\033[36m','\033[m') * 33)
print('{}=-={}'.format('\033[46m','\033[m') * 33)
print("\n" * 3)
time.sleep(2)

print(emoji.emojize(':fireworks:' * 45, language='alias'))
print('{}=-={}'.format('\033[33m','\033[m') * 33)
print('{}=-={}'.format('\033[43m','\033[m') * 33)
print("\n" * 3)
time.sleep(2)