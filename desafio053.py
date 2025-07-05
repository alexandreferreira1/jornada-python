# Ler uma frase e dizer se ela é um palíndromo(frase igual de trás pra frente). Exemplo: APOS A SOPA. Obs.: Sem acentos

print()
print(f"{'Identificador de Palíndomo':=^62}")
word = input('Digite uma frase ou palavra para saber se ela é um palíndromo: ').strip().lower()

#Retirar espaços e inverter palavra
wordWithoutSpace = word.replace(' ', '')
invertedWord = ''

# Iterar a string
for v in range(len(wordWithoutSpace) - 1, -1, -1):
    invertedWord += wordWithoutSpace[v]

print()
print(f'A sua palavra ou frase invertida fica assim: {'\033[32m'}{invertedWord}{'\033[m'}.', end=' ')

if wordWithoutSpace == invertedWord:
    print('Então ela é um palíndromo!')
else:
    print('Não se enquadra nas condições.')


