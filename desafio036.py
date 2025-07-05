# Início das Condições Aninhadas
# Programa de aprovação de empréstimo: Perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('{}={}'.format('\033[33m', '\033[m') * 74)
print('Olá! Seja bem vindo ao programa de aprovação de Financiamento Residencial!')
print('{}={}'.format('\033[33m', '\033[m') * 74)

price = float(input('Qual o valor da casa a ser comprada? R$'))
wage = float(input('Qual o seu salário? R$'))
years = int(input('Pretende pagar a casa em quantos anos? '))

monthlyInstallment = price / (years * 12)
limitUserMonthly = wage * 30 / 100

if monthlyInstallment > limitUserMonthly:
    print('Sinto muito. Esse financiamento não pôde ser aprovado! Tente aumentar a quantidade de anos.')
else:
    print(f'Parabéns! Esse financiamento pode ser aprovado! Sua parcela vai ser de R${monthlyInstallment:.2f}. Procure o banco mais próximo.')