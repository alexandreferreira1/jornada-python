def monetario(num):
    return f'R${num:.2f}'


def metade(num, conversao):
    if conversao == False:
        return num / 2
    else:
        return monetario(num / 2)


def dobro(num, conversao):
    if conversao == False:
        return num * 2
    else:
        return monetario(num * 2)


def aumentar(num, aumento, conversao):
    if conversao == False:
        return num + (num * aumento / 100)
    else:
        return monetario(num + (num * aumento / 100))


def diminuir(num, reducao, conversao):
    if conversao == False:
        return num - (num * reducao / 100)
    else:
        return monetario(num - (num * reducao / 100))

def resumo(valor, aumento, reducao):
    print('=' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('=' * 35)
    print(f'{"Preço Analisado: ":<26}{monetario(valor)}')
    print(f'{"Metade do preço: ":<26}{metade(valor, True)}')
    print(f'{"Dobro do preço: ":<26}{dobro(valor, True)}')
    print(f'{f"{aumento}% aumento no preço: ":<26}{aumentar(valor, aumento, True)}')
    print(f'{f"{reducao}% de redução no preço: ":<26}{diminuir(valor, reducao, True)}')