#aumento de salario
salariodofuncionário = int(input('digite o salário: R$'))
if salariodofuncionário <= 2000:
    novosalario = salariodofuncionário + (salariodofuncionário*20/100)
if salariodofuncionário > 2000:
    novosalario = salariodofuncionário + (salariodofuncionário*10/100)
print('o novo salário do funcionário é : {:.2f} R$'.format(novosalario))

