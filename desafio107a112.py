# Modulos e Pacotes
#107- Crie um módulo chamado moeda.py que tenha funções aumentar, diminuir, dobro e metade. Digite o preço. Depois imprima:
#     metade do preço, o dobro, aumentando 10% e reduzindo 15%.
#108- Crie uma função adicional chamada monetario() que consiga mostrar os valores formatados para monetário
#109- Modifique as funções para que aceitem um argumento a mais, informando se o valor vai ser formatado.Porém as
#     funções não vão mais dentro de monetario. Chamamos as funções como no início, mas passando True.
#110- Adicione uma função resumo no módulo moeda.py para imprimir as informações sem precisar digitar tudo manualmente. Em resumo
#     passamos 3 argumentos, o valor e as duas porcentagens. Agora é possível definir as porcentagens. Faça uma tabela dos dados
#111- Crie um pacote chamado utilidades que tenha dois módulos, moeda e dados. Transfira tudo para lá.
#112- No módulo dados, crie uma função leiaDinheiro que receba um input e faça a validação para aceitar apenas dados monetários
#     e também faça a conversão de dolar para real..


from utilidades.dados.leiaDinheiro import leiaDinheiro
from utilidades.moeda import moeda


valor = leiaDinheiro('Digite o preço: R$')
moeda.resumo(valor, aumento=80, reducao=30)