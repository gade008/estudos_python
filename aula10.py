n1 = int(input("Primeira nota: "))
n2 = int(input('Segunda nota: '))
m = (n1+n2)/2
print('Sua média foi: {:.2f}'.format(m), '\nSua nota está boa' if m >= 6 else '\nSua nota está baixa!')

