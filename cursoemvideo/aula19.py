estado = dict()
brasil = []
for c in range(0, 2):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print('v', end=' ')
    print()



