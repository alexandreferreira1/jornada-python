def leiaDinheiro(string):
    while True:
        valor = str(input(string)).strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO: "{valor}" não é um valor válido!\033[m')
        else:
            return float(valor.replace(",", "."))
            break

for i in range(5):
    print(i)