n = int(input('Digite um número: '))

print('A tabuada do número {} é: '.format(n))
for c in range(0,11):
    print("{} x {} = {}".format(n, c, (n*c)))

