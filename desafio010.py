# Ler quanto dinheiro a pessoa tem na carteira e converter para dólar. Considere U$1,00 = R$3,27
import math

print('-------------------COMPRAS NO PARAGUAI----------------------')
print('Cuidado para não extrapolar a cota por pessoa de 250 dólares')
real = float(input('Quantos reais você tem na carteira ou na conta? R$'))
conversion = real / 3.27
casasDecimais = 2
fator = 10 ** casasDecimais

print('{}'.format('='*50))
print('Um momento... Realizando conversão...')

print('{}'.format('='*50))
print('Conversão exata:', conversion)
print('Você tem {} para gastar. Boas compras!'. format(math.floor(conversion * fator) / fator))