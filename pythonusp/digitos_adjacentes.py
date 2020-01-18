c = anterior = Q = quantidadeadj = 0
numeros = []
n = int(input('Digite um número inteiro: '))
numeros.append(n)
if n == 0:
    Q += 1
while n > 0:
    numeros.append(n % 10)
    n //= 10
    Q += 1
lista = [numeros[i:i+1] for i in range(Q+1)]
igual = False
listaiguais = list()
for n in lista:
    if c > 0 and anterior != 0 and n == anterior:
        igual = True
        if n not in listaiguais:
            listaiguais.append(n)
        quantidadeadj += 1
    else:
        anterior = n
        c += 1
lista.pop(0)
lista.reverse()
if Q > 1:
    print(f'sim' if igual
          else 'não')
else:
    print('não')
