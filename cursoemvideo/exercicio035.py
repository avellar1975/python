
r1 = float(input('Digite o tamanho da reta 1: '))

r2 = float(input('Digite o tamanho da reta 2: '))

r3 = float(input('Digite o tamanho da reta 3: '))

if (r1 > r2 and r1 > r3):
    print('{} é a maior reta'.format(r1))
    m = r1
    if(m < r2 + r3):
        print('As retas podem formar um triângulo')
    else:
        print('Não dá para formar um triângulo')
if (r2 > r1 and r2 > r3):
    print('{} é o maior reta'.format(r2))
    m = r2
    if(m < r1 + r3):
        print('As retas podem formar um triângulo')
    else:
        print('Não dá para formar um triângulo')
if (r3 > r1 and r3 > r1):    
    print('{} é o maior reta'.format(r3))
    m = r3
    if(m < r1 + r2):
        print('As retas podem formar um triângulo')
    else:
        print('Não dá para formar um triângulo')
    
