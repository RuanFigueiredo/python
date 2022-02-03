from random import shuffle
a1 = input('\ndigite o primeiro aluno:')
a2 = input('\ndigite o segundo aluno:')
a3 = input('\ndigite o terceiro aluno:')
a4 = input('\ndigite o quarto aluno:')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('\nos alunos em ordem são:')
print(lista)


