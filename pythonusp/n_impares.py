n = int(input('Digite o valor de n: '))
i = r = 0

while i < n:
    if r % 2 != 0:
        print(r)
        i += 1
    r += 1
