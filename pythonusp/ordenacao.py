crescente = True
lista = []
for n in range(0, 3):
    numero = int(input(f'Digite o {n + 1}º número: '))
    lista.append(numero)
    if lista[n] < lista[n - 1]:
        crescente = False
print('crescente' if not True != crescente else 'não está em ordem crescente')
