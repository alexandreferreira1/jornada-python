# # Continuação das Estruturas de Repetição - while sem break
# Faça uma validação de dados. Ele pede sexo M ou F. Caso a pessoa digite algo além disso, o programa pede novamente. Acertado, então finaliza.

sexUser = input('Olá. Informe o seu sexo: [M/F] ')

while sexUser not in 'MmFf':
        sexUser = input('Dados inválidos. Tente novamente: [M/F] ')

if sexUser in ('Mm'):
        print('Sexo masculino registrado com sucesso.')
else:
        print('Sexo feminino registrado com sucesso.')