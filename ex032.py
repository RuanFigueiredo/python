ano = int(input('qual o ano que deseja saber se é bissexto?'))
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 ==0:
    print('esse ano de {} é bissexto'.format(ano))
else:
    print("esse ano de {} não é bissexto".format(ano))
