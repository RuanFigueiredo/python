# radar eletrônico da federal
velocidade = float(input('olá motorista, sua velocidade foi:'))
if velocidade <=90:
    print('\nestá indo bem, vá em frente')
else:
    print('MULTADO!')
    multa = (velocidade-90)*7
    print('\nvocê passou do limite de velocidade! deve pagar {:.2f}R$'.format(multa))
print('\ndirija com segurança')
