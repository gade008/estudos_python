from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print('RANKING DOS JOGADORES')
posição = 1
for x in range(0, len(ranking)):
    if x == 0:
        print(f'{posição}º - {ranking[x][0]} com {ranking[x][1]} pontos.')
    elif ranking[x][1] == ranking[x - 1][1]:
        print(f'junto com o {ranking[x][0]} com {ranking[x][1]} pontos.')
    else:
        posição += 1
        print(f'{posição}º - {ranking[x][0]} com {ranking[x][1]} pontos.')

