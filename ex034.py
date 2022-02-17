#aumento de salario
salariodofuncionário = int(input('digite o salário: R$'))
if salariodofuncionário <= 2000:
    novosalario = salariodofuncionário + (salariodofuncionário*20/100)
if salariodofuncionário > 2000:
    novosalario = salariodofuncionário + (salariodofuncionário*10/100)
print(' O  salário do funcionário era : {:.2f} R$ e agora é: {}R$'.format(salariodofuncionário, novosalario))

