n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('A soma é {}\n o produto é {}\n a divisão é {:.2f}'.format(s,m,d), end= ' ')
print('A divisão inteira é {}\n com o resto {}\n a potência é {}'.format(di,e,r))
