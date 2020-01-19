def area():
    print('~='*30)
    print('Controle de Terreno')
    l = float(input('Largura do terreno (m): '))
    c = float(input('Comprimento do terreno (m): '))
    total = l * c
    print(f'A área do terreno {l}x{c} é igual a {total}m²')


area()
