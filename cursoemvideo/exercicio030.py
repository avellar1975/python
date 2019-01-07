
n = int(input('Digite um número inteiro: '))

r = n % 2

if (r == 0):
    print('O número digitado foi {}, ele é PAR'.format(n))
else:
    print('O número digitado foi {}, ele é IMPAR'.format(n))
