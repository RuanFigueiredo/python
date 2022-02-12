frase = str(input('digite alguma frase:')).strip()
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A letra "a" aparece primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra "a" aparece na última vez na posição {}'.format(frase.rfind('a')+1))
