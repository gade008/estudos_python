cinquenta = 0
vinte = 0
dez = 0
um = 0
print('~'*20)
print('{:^20}'.format('Banco GCC'))
print('Abaixo as opções disponiveis para realizar em sua conta!')
print('~'*20)
saldo = 1000
print('Sua conta possui um saldo de  R${}'.format(saldo))
while True:
    print('\033[1;32m-'*20)
    print(' Sacar \n Depositar \n Saldo \n Sair')
    print('\033[1;32m-'*20)
    opção = str(input('Oque deseja fazer? ')).lower()
    if 'sacar' in opção:
        saque = int(input('Digite o valor para sacar: '))
        if saque <= saldo:
            saldo -= saque
            valor = saque
            while saque > 0:
                if saque % 50 == 0:
                    saque -= 50
                    cinquenta += 1
                elif saque % 20 == 0:
                    saque -= 20
                    vinte += 1
                elif saque % 10 == 0:
                    saque -= 10
                    dez += 1
                elif saque % 1 == 0:
                    saque -= 1
                    um += 1
            print('Total de cédulas:', end='\n')
            if cinquenta > 0: print(f'{cinquenta} cédulas de cinquenta reais', end='\n')
            if vinte > 0: print(f'{vinte} cédulas de vinte reais', end='\n')
            if dez > 0: print(f'{dez} cédulas de dez reais', end='\n')
            if um > 0: print(f'{um} cédulas de um real', end='\n')
            print(f'Com um saque de R${valor}, seu saldo agora é de R${saldo}')
        else:
            print('\033[1;31mErro! Saldo insuficiente.')
    elif 'depositar' in opção:
        deposito = int(input('Digite o valor para depositar: '))
        saldo += deposito
        print(f'Após o deposito de {deposito}, seu saldo agora é de R${saldo}')
    elif 'saldo' in opção:
        print(f'Seu saldo é de R${saldo}')
    elif 'sair' in opção:
        break
    else:
        print('Não entendi, por favor verifique se a opção que digitou corresponde ao menu abaixo:')
print('\033[1;32m='*20)
print('\033[1;97mObrigado por utilizar o Banco GCC, volte sempre!')

