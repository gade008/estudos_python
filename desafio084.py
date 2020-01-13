cont = 'S'
pessoas = list()
dados = list()
pesada = list()
leves = list()
# Leitura dos dados
while 'S' in cont:
    dados.append(str(input('Nome: ')).lower().capitalize())
    dados.append(int(input('Peso: ')))
    cont = str(input('Deseja continuar? [S/N]'))
    pessoas.append(dados[:])
    dados.clear()
# analise dos dados
for p in pessoas:
    if p[1] <= 70:
        leves.append(p)
    else:
        pesada.append(p)
print(f'No total temos {len(pessoas)} pessoas, sendo {len(pesada)} pessoas acima do peso e {len(leves)} abaixo do peso!')
