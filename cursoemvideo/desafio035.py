vc = int(input('Valor da casa: '))
s = float(input('Seu Salário: '))
p = int(input('Parcelar em quantos anos: '))
vp = vc / p
if s > (100/30)*p:
    print('Emprestimo Bancário aprovado!')
else:
    print('Emprestimo Bancário reprovado!')