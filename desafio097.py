# Início das Funções - parte 1
# Faça um programa que tenha uma função chamada escreva e receba como argumento uma mensagem com tamanho adaptável.
# Faça uma linha em cima e uma embaixo do texto utilizando "~" e faça com que ela acompanhe o tamanho do texto.

def escreva(msg):
    print(f'{"~~"}{"~" * len(msg)}{"~~"}')
    print(f'{msg:^{len(msg) + 4}}')
    print(f'{"~~"}{"~" * len(msg)}{"~~"}')


escreva('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum')