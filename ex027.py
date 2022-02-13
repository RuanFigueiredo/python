n = str(input('digite um nome completo:')).strip()
nome = n.split()
print('\n Olá!, seu primeiro nome é: {}'.format(nome[0]))
print('\n Seu último nome é: {}'.format(nome[len(nome)-1]))


