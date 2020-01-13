from math import sqrt, floor
import random
num = int(input('Digite um número:'))
num1 = random.expovariate(1/5)
r = sqrt(num)
print('A raiz quadrade de {} é igual a {:.2f}'.format(num, floor(r)))