preço = float(input('o preço do desodorante é em R$ : \n'))
desconto = preço - (preço*5/100)
print('o Desodorante que vale : {:.2f} R$, tem um descontasso de 5%, logo ele ficará no valor de {:.2f} R$'.format(preço, desconto))

