frase = input('Digite a frase:').strip().lower()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('Ela aparece na ultima posição {}'.format(frase.rfind('a')+1))