# Entrada de dados
a = int(input('Digite o valor de ax²: '))
b = int(input('Digite o valor de bx: '))
c = int(input('Digite o valor de c: '))

# Calcula o delta e raiz do delta, vertices e a coordenada do vertice
delta = (b**2) - (4 * a * c)

x1 = ((-1 * b) - pow(delta, 1 / 2)) / (2 * a)
x2 = ((-1 * b) + pow(delta, 1 / 2)) / (2 * a)

Xv = (-1*b)/(2*a)
Yv = (-1*(pow(delta, 1/2)))/(4*a)

# Mostra o resultado para o usuario
print('-'*20, 'Resultado', '-'*20)
print(f'\033[34m Δ = {delta}')
print(f'\033[33m Raizes: \n X¹= {x1} \n X²= {x2}' if x1 != x2 else f'\033[33m Á única raiz é {x1}')
print(f'\033[35m Coordernadas do vertice: \n Xv= {Xv} \n Yv= {Yv}' if Xv != Yv
      else f'\033[33m As coordenadas do vertice é igual a {Xv}')
