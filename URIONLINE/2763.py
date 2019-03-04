while True:
    try:
                
        a,b,c = input().split('.')
        c,d = c.split('-')
        cpf = a+b+c
        dig = d
        b1 = int(dig[0])
        b2 = int(dig[1])
        soma1 =  soma2 = 0
        [int(i) for i in str(cpf)]

        for z in range(9):
            a = int(cpf[z])*(z+1)
            soma1+=a

        resto1 = soma1 % 11
        if(resto1 == 10):
            resto1 = 0

        for w in range(9):
            a = int(cpf[w])*(9-w)
            soma2+=a

        resto2 = soma2 % 11
        if(resto2 == 10):
            resto2 = 0
            
        if (b1 == resto1 and b2 == resto2):
            print('CPF valido')
        else:
            print('CPF invalido')
    except:
        break
