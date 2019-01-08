# Desafio 028

from random import randint
import time

secreto = randint(0,5)

x = int(input('Digite um número inteiro de 0 a 5: '))

print('Processando ...')
time.sleep(3)

if(x == secreto):
    print('Você venceu!!!')
else:
    print('O número secreto era {}. Você perdeu!!!'.format(secreto))
