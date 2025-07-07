# Criar tupla com várias palavras sem acento e mostrar em cada uma quais as suas vogais

words = ("maca", "livro", "python", "janela", "sol")

for word in words:
    print()
    print(f'A palavra {word.upper()} tem as seguintes vogais: ', end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')

print()

