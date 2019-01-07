

veloc = float(input('Digite a velocidade do carro: '))

if (veloc > 80.0):
    print('Você foi multado')
    multa = (veloc - 80)*7
    print('Sua multa foi de R$ {:.2f}, por transitar a {} km/h'.
    format(multa, veloc))
