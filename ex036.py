casa = float(input('qual o valor da casa?'))
salario = float(input('qual o valor do salário:'))
anos = int(input('em quantos anos será financiada a casa:'))
prestação = casa / (anos*12)
mínimo = salario * 30 / 100
print('\nA casa vale {:.2f} R$, e vai ser paga em {} anos'.format(casa, anos))
print('O valor da prestação da casa é de {:.2f} R$'.format(prestação))
if prestação <= mínimo:
    print('Financiamento APROVADO!')
else:
    print('Financiamento NEGADO!')
