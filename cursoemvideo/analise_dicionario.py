def notas(*n, sit=False):
    """
    -> Função para anlisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, inidicando se mostra a situação
    :return: dicionario com varias informações sobre a situação das notas
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif ['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
