#Início das Estruturas Condicionais
# Ler velocidade e se ultrapassar 80km/h, multar em R$7 a cada KM acima do limite

velocidade = int(input('Qual a velocidade captada? '))

if velocidade > 80:
    excedente = velocidade - 80
    multa = excedente * 7
    print(f'Ops! Você foi multado em {multa}')
else:
    print('Parabéns. Você estava dentro dos limites de velocidade')

