# Ler nome e duas notas de vários alunos e guarde tudo em uma lista composta. São 3 níveis de lista
# No final mostre o boletim com as médias e permita consultar a nota de cada aluno individualmente

reportCard = []
student = []
grades = []

c = 1
while True:
    print('=' * 30)
    print(f'{"ALUNO " + (str(c)):^30}')
    print('=' * 30)
    name = str(input('Digite o nome: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda: '))
    c += 1

    #Salvando dados individuais e repassando para boletim
    student.append(name)
    grades.append(nota1)
    grades.append(nota2)
    student.append(grades[:])
    reportCard.append(student[:])
    #Reset de aluno
    student.clear(); grades.clear()

    continuar = str(input('Deseja continuar? [S / N] >>> '))
    if continuar in 'Nn':
        break

#Formatação do Boletim
print()
print('=' * 34)
print(f'{"BOLETIM ESCOLAR":^34}')
print('=' * 34)
print(f'{"Nº":<4}', end='')
print(f'{"ALUNO":<25}', end='')
print(f'{"MÉDIA":>5}', end='')
print()

#Renderização das Notas
for i, student in enumerate(reportCard):
    print(f'{i + 1:<3} {student[0]:<25} {(student[1][0] + student[1][1]) / 2:>4}')

#Visualizar nota individual
while True:
    print('=' * 34)
    continuar = int(input('Digite o número do aluno que deseja\nvisualizar as notas ou digite 999 para sair: '))
    if continuar == 999:
        break
    else:
        print(f'\033[34mNotas de {reportCard[continuar - 1][0]}: {reportCard[continuar - 1][1]}\033[m')


