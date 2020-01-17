from math import trunc
aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['média'] = float(input('Digite a média: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

