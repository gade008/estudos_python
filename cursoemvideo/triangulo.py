r1 = float(input('Seguimento: '))
r2 = float(input('Segundo segmento: '))
r3 =  float(input('Terceiro segmento: '))
print('-='*20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triangulo!')
else:
    print('Não forma um triangulo!')
print('-=' * 20)