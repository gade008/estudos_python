from math import sqrt

x1 = int(input('Digite a coordenada x do ponto 1: '))
y1 = int(input('Digite a coordenada y do ponto 1: '))
x2 = int(input('Digite a coordenada x do ponto 2: '))
y2 = int(input('Digite a coordenada y do ponto 2: '))

distancia = sqrt(((x1 - x2)**2)+((y1 - y2)**2))

if distancia < 10:
    print('perto')
else:
    print('longe')
