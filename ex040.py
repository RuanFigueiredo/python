nota1 = float(input('primeira nota'))
nota2 = float(input('segunda nota'))
média = (nota1 + nota2)/2
print('Juntando a nota {} e a nota {} a média do aluno ficou de {}'.format(nota1, nota2, média))
if média >7:
    print('aluno aprovado')
elif média <5:
    print('aluno reprovado')
else:
    print('aluno em recuperação')
