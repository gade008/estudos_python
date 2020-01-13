pessoas = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Digite seu nome: ')).lower().capitalize())
    dados.append(int(input('Digite sua idade: ')))
    pessoas.append(dados[:])
    # Importante não esquecer o [:] pois ele cria uma copia da entrada de dados
    dados.clear()
for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1
print(f'No total temos {totmen} menor(es) de idade e {totmai} pessoa(s) maior(es) de idade!')
