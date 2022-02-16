#preço da passagem
distancia = float(input('digite aqui a distância de sua viagem:'))
print('\n a distância de sua viagem é de {} km'.format(distancia))
if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('\n o preço da passagem é de {}R$'.format(preço))
