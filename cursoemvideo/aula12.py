nome = str(input('Qual seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Enzo':
    print('Seu nome é bem popular!')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, {}!'.format(nome))
