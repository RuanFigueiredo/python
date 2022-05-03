peso = float(input('qual é  peso:(kg) '))
altura = float(input('qual é a altura '))
imc = peso / (altura **2)
print(' o imc do cidadão ou da cidadã é:'.format(imc))
if imc < 18.5:
    print('está abaixo do peso')
elif 18.5 <= imc < 25:
    print('parabéns, peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso!')
elif 30 <= imc < 40:
    print('cuidado, obesidade!')
elif imc >40:
    print('OBESIDADE MÓRBIDA')