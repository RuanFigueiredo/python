r1 = float(input('primeiro segmento do triângulo:'))
r2 = float(input('segundo segmento do triângulo:'))
r3 = float(input('terceiro segmento do triângulo:'))
if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1 + r2:
    print('eis aqui um triângulo')
    if r1 == r2 == r3:
        print('o triângulo é equilátero')
    elif r1 != r2 !=r3!= r1:
        print('triângulo é escaleno!')
    else:
        print('triângulo é iscóceles')
else:
    print('esses segmentos não formam um triângulo')