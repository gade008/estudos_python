n = int(input('Digite um numero: '))
i = 1
q = 0
primo = False

while i <= n:
    if n % i == 0:
        q += 1
    i += 1
if q == 2:
    primo = True
print("primo" if primo else "não primo")

