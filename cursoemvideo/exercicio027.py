'''Exercício Python 027: Faça um programa que leia o nome completo 
de uma pessoa, mostrando em seguida o primeiro e o último nome 
separadamente.'''

nome = input('Digite seu nome completo: ').strip()
nome_completo = nome.split()

print('Seu primeiro nome é {}'.format(nome_completo[0]))
print('Seu último nome é {}'.format(nome_completo[len(nome_completo)-1]))


print('Muito prazer em te conhecer!')

