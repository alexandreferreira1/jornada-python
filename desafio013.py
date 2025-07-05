#Ler salário e mostrar com % de aumento

print('-------------------DESCUBRA SEU NOVO SALÁRIO----------------------')
salario = input('Qual o seu salário atual? (Ex.: 10.500,53) R$')
salarioFormatado = float(salario.replace('.', '').replace(',', '.'))

porcentagem = input('Qual vai ser a porcentagem do seu aumento? ')
porcentagemConvertida = float(porcentagem.replace('%', '').replace(',', '.'))
aumento = salarioFormatado * porcentagemConvertida / 100

novoSalario = salarioFormatado + aumento

#Strings estéticas
print('{}'.format('='*50))
print('Um momento...')
print('{}'.format('='*50))
#Fim das Strings estéticas

print(f'Seu novo salário vai ser de {novoSalario:.2f}, Parabéns!')
