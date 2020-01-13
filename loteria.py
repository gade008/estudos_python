from random import randint
from time import sleep
n = randint(0, 5)
print('Tente advinhar o número que o computador escolheu!')
sleep(3)
print('Dica: O número é maior que 3' if n > 3 else 'Dica: O número é menor ou igual a 3', )
escolha = int(input('Escolha um número entre 0 e 5: '))
print(f'Você escolheu o mesmo número que o computador! O número {n}' if n == escolha
      else f'Você escolheu {escolha} e o computador escolheu {n}')
