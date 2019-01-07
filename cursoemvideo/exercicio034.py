
salario = float(input('Digite o seu salário: R$'))

if (salario > 1250):
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

print('Seu salário agora é de R$ {:.2f}'.format(aumento))
