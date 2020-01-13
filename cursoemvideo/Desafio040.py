'''from time import sleep
for c in range(10, -1, -1):
    print('Falta {} segundos para os fogos!'.format(c))
    sleep(1)'''

#Desafio 047
'''
for p in range(1, 50+1):
    if p % 2 == 0:
        print(p)
'''

#Desafio 048
'''
for n in range (1, 500+1):
    if n % 3 == 0 and n % 2 != 0:
        print(n)
'''

#Desafio 050
'''
s = 0
for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print('A soma total é igual a: ', s)
'''

#Desafio 051
'''
t = float(input('Digite o primeiro termo: '))
n =  int(input('Digite a posição do termo: '))
r = float(input('Digite a razão: '))
i = t + (n-1)*r
print('O valor é igual a', int(i))
'''

#Desafio 052
'''
n = int(input('Digite um número: '))
i = 0
tot = 0
for i in range(i < n, n + 1):
    if n % i == 0:
        print('\033[34m', end= '')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
print('\nO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('\033[32m número é primo!')
else:
    print('\033[31m O número não é primo!')
'''

#Desafio 053
'''
maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[33m O maior peso lido foi de {} Kg \n\033[31m O menor peso lido foi de {} Kg'.format(maior, menor))
'''

#Desafio 56

from time import sleep

velho = 0
total = 0
totidade = 0
hvelho = ''
for i in range(1, 5):
    print('-'*5, '{}ª pessoa: '.format(i), '-'*5)
    nome = str(input('Digite o nome: '))
    idade =  int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo:'))
    totidade += idade
    if 'M' in sexo:
        if i == 1:
            hvelho = nome
            velho = idade
        else:
            if idade > velho:
                hvelho = nome
                velho = idade
    if 'F' in sexo:
        if idade < 20:
            total += 1
media = totidade / 4
print('\033[33mUm momento enquanto analiso os resultados...')
sleep(3)
print('\033[31mResultado da analise: \nA média de idade é de: {} anos\nO homem mais velho é o Sr.{}\nNo total {} mulhere(s) tem menos de 20 anos! '.format(media,hvelho,total))
