def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')


def metade(num, conversao):
    if conversao == False:
        return num / 2
    else:
        valorMetade = num / 2
        return moeda(valorMetade)


def dobro(num, conversao):
    if conversao == False:
        return num * 2
    else:
        valorDobro = num * 2
        return moeda(valorDobro)


def aumentar(num, aumento, conversao):
    if conversao == False:
        return num + (num * aumento / 100)
    else:
        valorAumento = num + (num * aumento / 100)
        return moeda(valorAumento)


def diminuir(num, reducao, conversao):
    if conversao == False:
        return num - (num * reducao / 100)
    else:
        valorReducao = num - (num * reducao / 100)
        return moeda(valorReducao)

def resumo(valor, aumento = 10, reducao = 15):
    print('=' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('=' * 35)
    print(f'{"Preço Analisado: ":<26}{moeda(valor)}')
    print(f'{"Metade do preço: ":<26}{metade(valor, True)}')
    print(f'{"Dobro do preço: ":<26}{dobro(valor, True)}')
    print(f'{f"{aumento}% aumento no preço: ":<26}{aumentar(valor, aumento, True)}')
    print(f'{f"{reducao}% de redução no preço: ":<26}{diminuir(valor, reducao, True)}')