print ('LOJA DO RUAN')
preço = float(input('qual é o preço do produto?'))
print('''
[1] à vista em  dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opção = int(input('qual é a opção?:'))
if opção ==1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço*5/100)
elif opção == 3:
    total = preço
    parcela = total/2
    print('ficou o valor de 2x de {}R$'.format(parcela))
elif opção == 4:
    total = preço + (preço*20/100)
    totaldeparc = int(input('quantas parcelas?'))
    parcela = total/totaldeparc
    print('ficou {} vezes de {} R$'.format(totaldeparc, parcela))
print('o valor de {} R$ ficou no valor de {} R$:'.format(preço,total))

