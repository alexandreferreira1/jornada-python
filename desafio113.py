# Início do tratamento de exceções
# Faça a função leiaInt e leiaFloat. Tratando os erros possíveis

def leiaInt():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except:
            print('\033[31mErro. Digite um número Inteiro válido.\033[m')
        else:
            return f'Você digitou o número {num}'

def leiaFloat():
    while True:
        try:
            entrada = input('Digite um número decimal: ')
            if '.' not in entrada:
                raise ValueError
            else:
                num = float(entrada)
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
        except:
            print('\033[31mErro. Digite um número Float válido.\033[m')
        else:
            return f'Você digitou o número {num}'

print(leiaInt())
print(leiaFloat())

