#Fase 07 – Operadores Aritméticos


#Desafio 005 ##################
n1 = int(input('Digite um número:'))

print('O antecessor do número {} é {}, e o sucessor é {}'.format(n1, n1-1, n1+1))

#Desafio 006 ##################
n2 = int(input('Digite um número:'))
print('O dobro do número {} é {}, seu triplo é {} e \n a raiz quadrada é {:.2f}'.format(n2, 2*n2, 3*n2, n2**(1/2)))


#Desafio 007 ##################
aluno = input('Digite o nome do aluno:')
n3 = float(input('Digite a primeira nota:'))
n4 = float(input('Digite a segunda nota:'))
print('A média das notas de {} é {:.2f}'.format(aluno, (n3+n4)/2))

#Desafio 008 ##################
m = float(input('Digite um valor em metros:'))
print('{:.2f} metros equivale a {:.2f} centímetros ou {:.2f} milímetros'.format(m, 100*m, 1000*m))

#Desafio 009 ##################
t = int(input('Escolha uma tabuada:'))
print('{}'.format('-'*15))
for x in range(1, 11):
    print('{} x {:2} = {:3}'.format(t, x, x*t))
print('{}'.format('-'*15))
    
#Desafio 010 ##################
r = float(input('Quanto você tem na carteira R$:'))

print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(r, r/3.27))

#Desafio 011 ##################
l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede:'))

print('A área da parede é {:.2f}m², serão necessárias {:.2f} litros de tinta '.format(l*a, (l*a)/2))


#Desafio 012 ##################
p = float(input('Digite o preço do produto: R$'))

print('O novo preço com 5% de desconto é R$ {:.2f}'.format(p*0.95))


#Desafio 013 ##################
s = float(input('Digite o salário do funcionário: R$'))

print('O novo salário é de R$ {:.2f}'.format(s*1.15))

#Desafio 014 ##################
'''
    Exercício Python 014: 
      Escreva um programa que converta uma temperatura digitando em graus
      Celsius e converta para graus Fahrenheit
'''
temp = float(input('Informe a temperatura em ºC: '))
print('A temperatura em Fahrenheit é {} Fº'.format(((9*temp)/5)+32))


#Desafio 015 ##################
'''
Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
km = float(input('Quantos km foram percorridos: '))
dias = int(input('Quantos dias foi alugado: '))
print('O preço a pagar pelo aluguel foi de {}'.
      format((60*dias)+(0.15*km)))
