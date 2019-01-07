# Desafio 028

import random

n = random.random()
secreto = int(n * 100 % 6)

x = int(input('Digite um número inteiro de 0 a 5: '))

if(x == secreto):
    print('Você venceu!!!')
else:
    print('O número secreto era {}. Você perdeu!!!'.format(secreto))
    
    

