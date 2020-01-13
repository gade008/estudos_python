while True:
    n = int(input('Você quer mostrar a tabuada de qual valor? (Digite 0 para finalizar) '))
    if n == 0:
        print('Programa parado, volte sempre!')
        break
    print('~' * 20)

    for i in range(1, 11):
        r = i * n

        print(f'{n} X {i} = {r}')
    print('-' * 20)
