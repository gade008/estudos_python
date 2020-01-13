n = int(input('Digite um número: '))
if n % 4 == 0 and n % 100 == 0:
    print('Ano Bissexto!')
else:
    print('Ano comum!')