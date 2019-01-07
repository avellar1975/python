
d = float(input('Qual a distância da sua viagem? '))

if (d<=200.0):
    p = 0.5 * d
    print('Sua passagem custa R$ {:.2f}'.format(p))
else:
    p = 0.45 * d
    print('Sua passagem custa R$ {:.2f}'.format(p))
