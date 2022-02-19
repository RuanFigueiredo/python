print('Analisador de triângulos:')
r1 = float(input('segmento 1:'))
r2 = float(input('segmento 2:'))
r3 = float(input('segmento 3'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print ('\n os segmentos formam um triângulo')
else:
    print('\n os segmentos acima não formam um triângulo ')

