# Entrada de dados
a = int(input('Digite o valor de ax²: '))
b = int(input('Digite o valor de bx: '))
c = int(input('Digite o valor de c: '))

# Calcula o delta e raiz do delta, vertices e a coordenada do vertice
delta = (b**2) - (4 * a * c)

x1 = ((-1 * b) - pow(delta, 1 / 2)) / (2 * a)
x2 = ((-1 * b) + pow(delta, 1 / 2)) / (2 * a)
lista = []

# Mostra o resultado para o usuario
if delta < 0:
    print(f'esta equação não possui raízes reais')
else:
    lista = [x1, x2]
    lista.sort()
    print(f'as raízes da equação são {x1} e {x2}' if x1 != x2 else f'a raiz desta equação é {x1}')
