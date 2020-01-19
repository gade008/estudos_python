from time import sleep

def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('~='*30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2)
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += c
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= c
    print('FIM!')
    print('~='*30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar a contagem!')
inic = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inic, fim, passo)
