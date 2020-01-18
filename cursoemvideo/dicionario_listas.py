dados = {}
pessoas = []
soma = acimamedia = 0
while True:
    dados.clear
    dados['nome'] = str(input('Digite o nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: (M ou F) ')).upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F.')
        del dados['sexo']
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = input('Deseja continuar? (S/N)').upper()
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if resp in 'N':
        break
print('~='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
media = soma / len(pessoas)
print(f'A média de idade do grupo é de {media:.0f} anos')
print('As mulheres cadastradas foram:', end=' ')
for i in pessoas:
    if i['sexo'] in 'Ff':
        print(f'{i["nome"]}, ', end='')
print('')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p["nome"]} está acima da idade média do grupo, pois possui {p["idade"]} anos!')
        acimamedia += 1
print(f'No total temos {acimamedia} pessoas acima da média de idade!')


