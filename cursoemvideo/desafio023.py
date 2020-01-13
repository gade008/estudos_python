n = int(input('Digite um número entre 0 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f""" 
Analisando Número: {n} ....
milhar: {m} 
centena: {c}
dezena: {d}
unidade: {u} """)
