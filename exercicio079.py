lista = list()
resp = 'S'
while True:
    numero = int(input("Digite um valor: "))
    if numero not in lista:
        lista.insert(0, numero)
        resp = input('Deseja continuar? [S/N]').lower()
    else:
        print('Numero ja existe na lista! Não foi adicionado.')
    if resp in 'n':
        break
print('\033[1;31m-='*20)
lista.sort()
print(f'Você digitou os números {lista}')