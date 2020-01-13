#desafio022
nome = str(input('Digite seu nome:'))
nom = nome.split()
print(f"""Seu nome é: {nome.upper()}
\n ou {nome.lower()} 
\n tem no total  {nome.count('')} letras
\n sendo que o primeiro nome tem {(nom[1]).count('')} letras""")