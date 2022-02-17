a = int(input('digite um número:'))
b = int(input('digite um número:'))
c = int(input('digite um número:'))
menor = a
if b<a and b < c:
    menor = b
if c<b and c < a:
    menor = c
print('\n o menor número é:{}'.format(menor))
