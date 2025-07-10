# Crie a função notas() que recebe várias notas de alunos (*num), depois retorne um dicionário contendo:
# Quantidade de notas, Maior nota, Menor nota, Média da turma, Situação(opcional): de RUIM a ÓTIMA.
# Adicione docstrings

def notas(*n, sit = False):
    """
    Soma várias notas de um aluno. (*n)
    sit é opcional.
    Se True, mostra a situação atual do aluno.
    """
    soma = media = 0
    situacao = ''

    for valor in n:
        soma += valor

    media = soma / len(n)

    if media < 6:
        situacao = 'RUIM'
    elif 6 <= media <= 7:
        situacao = 'RAZOÁVEL'
    elif media > 7:
        situacao = 'RAZOÁVEL'

    resultado = {
        'total de notas': soma,
        'maior nota': max(n),
        'menor nota': min(n),
        'média': media,
    }

    if sit == True:
        resultado['situação'] = situacao

    return resultado

boletim = notas(5, 7, 6, 8, sit=True)
print(boletim)

# help(notas)