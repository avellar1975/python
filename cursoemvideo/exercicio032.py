
ano = int(input('Digite um ano: '))

bissexto = ano % 4

if (bissexto == 0):
    print('O ano de {} é um ano BISSEXTO'.format(ano))
else:
    print('O ano de {} não é um ano bissexto'.format(ano))
