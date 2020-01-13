resp = 'S'
maior = menor = total = n = 0
cont = 0
while resp in 'Ss' or cont < 2:
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    total += n
    if cont >= 2:
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
media = total / cont
print('Você digitou {} valor(es), sendo a média igual a {}'.format(cont, media), end='\n')
print('Sendo o maior número digitado {} e o menor número {}'.format(maior, menor))