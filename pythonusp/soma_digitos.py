n = int(input('Digite um número: '))
s = total = 0
while n > 0:
    s = n % 10
    n //= 10
    total += s
print(total)