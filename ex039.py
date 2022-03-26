#faça um  programa que leia o ano  de nascimento do cidadão e informe de acordo com sua idade , se ele ainda vai se alistar,
#ao serviço militar, se é a hora de ele se alistar, ou se já passou do tempo do alistamento, o programa é pra mostrar o tempo que falta,
#ou o que passou.
from datetime import date
nasc = int(input('ano de nascimento:'))
ano = date.today().year
idade = ano - nasc
print('nascido em {}, tem {} ano(s) em {}'.format(nasc, idade, ano))
if idade == 18:
    print('SE ALISTE IMEDIATAMENTE!!')
elif idade > 18:
    saldo = idade - 18
    print('já passou {} anos de seu tempo de alistamento'.format(saldo))
elif idade < 18:
    saldo = 18 - idade
    print('ainda falta(m) {} ano(s) pra seu alistamento.'.format(saldo))