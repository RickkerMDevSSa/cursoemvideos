# Analisador texto

nome = str (input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome ejm maiuscula é {}'.format(nome.upper())) # MAIUSCULA
print('Seu nome ejm maiuscula é {}'.format(nome.lower())) # MINUSCULA
print('Seu nome ejm maiuscula é {}'.format(len(nome)- nome.count(' ')))


# By Rickker