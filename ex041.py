idade = int(input('digite aqui a idade do nadador:'))
if idade <9:
    print('Sua categoria é mirim')
elif idade >9 and idade <=14:
    print('Sua categoria é infantil')
elif idade >14 and idade <=19:
    print ('Sua categoria é Júnior')
elif idade >19 and idade <25:
    print('sua categoria é Sênior')
else:
    print('Sua categoria é master!')