'''''
lista = list(range(0, 5))
lista[4] = 4
lista.append(5)
lista.insert(4, 6)
lista.sort(reverse=True)
lista.pop(0)

print(lista)
print(f'Essa lista possui {len(lista)} elementos!')
'''''
valores = list()
for cont in range(0,5):
    valores.append((int(input('Digite um valor:'))))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')