from random import sample
aluno1 = input('Digite o nome do(a) primeiro(a) aluno(a): ')
aluno2 = input('Digite o nome do(a) segundo(a) aluno(a): ')
aluno3 = input('Digite o nome do(a) terceiro(a) aluno(a): ')
aluno4 = input('Digite o nome do(a) quarto(a) aluno(a): ')
print(f'Ordem de apresentação do trabalho dos(as) alunos(as):{sample([aluno1,aluno2,aluno3,aluno4],k = 4)}')

