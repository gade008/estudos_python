jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Partidas que jogou: '))
jogador['gols'] = list()

for i in range(jogador['partidas']):
    gols = int(input(f'Quantos gols na {i+1}ª partida:'))
    jogador['gols'].append(gols)
    jogador['total'] = sum(jogador['gols'])

print('~='*20)
print(jogador)
print('-='*20)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas!')
for k in range(jogador['partidas']):
    print(f' => Na {k+1}ª partida fez {jogador["gols"][k]} gols ')
print(f'Sendo um total de {jogador["total"]} gols na carreira.')
