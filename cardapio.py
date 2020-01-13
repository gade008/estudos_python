"""Esse exercicio foi desenvolvido para aprendizado somente, não é muito complexo e consegui realizar
sem conhecimento em Python, pode ser utilizado para explicação da lista, pois utiliza um exemplo real de cardapio.
Em adição, possui formatação de print e como utilizar no Python3!"""


# Variaveis
listalanches = []
listanumeros = []
erro = False
numeros = list(range(0, 9))
for numero in numeros:
    listanumeros.insert(0, str(numero))

# Mostrar o cardapio
print('Para sair do cardapio digite SAIR, para escolher um lanche digite o nome desejado!')
while True:
    erro = False
    lanche = str(input('Adicionar ou comer alimento do cardapio: ')).lower()
# Formatar a variavel
#  verifica se o usario digitou numeros, se verdadeiro não adiciona ao cardapio!
    for num in list(lanche):
        if num in listanumeros:
            print('Você digitou números, não é permitido no cardapio!')
            erro = True
            break
    # Verifica se o usuario quer sair com um break para o while, se a condição for falsa, irá executar o while normalmente!
    if erro == False:
        if lanche in 'sair':
            break
        # Condição para inserir lanche, verifica se o lanche digitado não existe no cardapio!
        if lanche.lower() not in listalanches:
            listalanches.insert(0, lanche.lower())
            listalanches.sort()
            if len(listalanches) > 0:
                print('-' * 20)
                print('\033[1;33m{:=^20}'.format('CARDAPIO:'))
                for comida in listalanches:
                    print(f'\033[1;35m{comida:=^20}', end='\n')
        # Condição para comer lanche, qualquer coisa digitada e que seja igual ao que tem no cardapio sera consumido!
        else:
            print(f'\033[1;31m Você pegou {lanche.upper()}, o lanche foi removido do cardapio!')
            listalanches.remove(lanche)
            print(f'\033[1;33m {"Agora o cardapio possui:":*^30}')
            for comida in listalanches:
                print(f'\033[1;35m{comida:=^20}')
        print('=' * 20)
