from random import randint
from time import sleep
computador = randint(0, 4)
print('começou o jogo de adivinhação,  adivinhe de 0 a 4...')
jogador = int(input('qual foi o número?'))
print('PROCESSANDO...')
sleep(4)
if jogador == computador:
    print('\n ai sim, parabéns, adivinhou o número')
else:
    print('\n errou, infelizmente você não conseguiu adivinhar o número, eu pensei no número {} e não no {}'
          .format(computador, jogador))
