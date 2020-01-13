import math
ang = int(input('Digite o angulo:'))
rad = math.radians(ang)
cos = math.cos(rad)
tang = math.tan(rad)
sen = math.sin(rad)
print('O seno do angulo de {}º é igual a: {:.2f}'.format(ang, sen))
print('O cosseno do angulo de {}º é igual a: {:.2f}'.format(ang, cos))
print('A tangente do angulo de {}º é igual a : {:.2f}'.format(ang, tang))