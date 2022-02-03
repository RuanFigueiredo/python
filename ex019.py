from random import choice
n1 = input('\njogador 1:')
n2 = input('\njogador 2:')
n3 = input('\njogador 3:')
n4 = input('\njogador 4:')
lista_de_jogadores = [n1, n2, n3, n4]
escolhido = choice(lista_de_jogadores)
print('o jogador escolhido foi: {}, do corinthians'.format(escolhido))
